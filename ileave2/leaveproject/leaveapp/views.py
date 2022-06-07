from django.shortcuts import redirect, render
from .forms import Leave_Department_Create_Form, Leave_Type_Create_Form, LeaveForm
from leaveapp.models import Leave, Leave_Type_Create, Leave_Department_Create
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Q, Sum, Count, F, Max
from django.contrib.auth.models import User

# Create your views here.
def ChangeActions(user):
    if user.groups.filter(Q(name = 'HR') | Q(name = 'Supervisor')).exists():
        return True
    return False

@login_required
def home(request):
    members = User.objects.count()
    pending_count = Leave.objects.filter(status='รออนุมัติ').count()
    approve_count = Leave.objects.filter(status='อนุมัติ').count()
    rejects_count = Leave.objects.filter(status='ไม่อนุมัติ').count()

    context = {
        'members': members,
        'pending_count': pending_count,
        'approve_count': approve_count,
        'rejects_count': rejects_count
        
        }
    return render(request, 'leaveapp/home.html', context)

@login_required
def leave(request):
    if request.method == 'POST':
        form = LeaveForm(request.POST, request.FILES)
        if form.is_valid():
            leaveapp = form.save(commit=False)
            leaveapp.user = request.user
            leaveapp.save()
            return redirect('leaveapp:list_leave')
        else:
            print('Error :', form.errors)
    else:
        form = LeaveForm()
    return render(request, 'leaveapp/leave.html', {'form': form})

@login_required
def approve(request):
    result_approve = Leave.objects.filter(status='อนุมัติ', user = request.user)

    context = {'result_approve': result_approve}
    return render(request, 'leaveapp/approve.html', context)

@login_required
def pending(request):
    result_pending = Leave.objects.filter(status='รออนุมัติ', user = request.user)

    context = {'result_pending': result_pending}
    return render(request, 'leaveapp/pending.html', context)

@login_required
def reject(request):
    result_reject = Leave.objects.filter(status='ไม่อนุมัติ', user = request.user)

    context = {'result_reject': result_reject}
    return render(request, 'leaveapp/reject.html', context)

@login_required
def leave_type_create(request):
    if request.method == 'POST':
        form = Leave_Type_Create_Form(request.POST)
        if form.is_valid():
            leaveapp = form.save(commit=False)
            leaveapp.user = request.user
            leaveapp.save()
            return redirect('leaveapp:leave_type_list')
        else:
            print('Error :', form.errors)
    else:
        form = Leave_Type_Create_Form()
    return render(request, 'leaveapp/leave_type_create.html', {'form' : form})

@login_required
def leave_type_list(request):
    type_list = Leave_Type_Create.objects.all()

    context = {'type_list': type_list}
    return render(request, 'leaveapp/leave_type_list.html', context)

@login_required
def leave_department_create(request):
    if request.method == 'POST':
        form = Leave_Department_Create_Form(request.POST)
        if form.is_valid():
            leaveapp = form.save(commit=False)
            leaveapp.user = request.user
            leaveapp.save()
            return redirect('leaveapp:leave_department_list')
        else:
            print('Error :', form.errors)
    else:
        form = Leave_Department_Create_Form()
    return render(request, 'leaveapp/leave_department_create.html', {'form': form})

@login_required
def leave_department_list(request):
    department_list = Leave_Department_Create.objects.all()

    context = {'department_list': department_list}
    return render(request, 'leaveapp/leave_department_list.html', context)

@login_required
@user_passes_test(ChangeActions, login_url='/')
def list_leave(request):
    approve_leave = Leave.objects.filter(status='รออนุมัติ')

    context = {'approve_leave': approve_leave}
    return render(request, 'leaveapp/list_leave.html', context)

@login_required
def approve_leave_form(request, id, approve = 1):
    approve_leave = Leave.objects.get(id = id)
    print(approve_leave)
    if approve == 0:
        approve_leave.status = 'ไม่อนุมัติ'
        approve_leave.save()
        return redirect('/leaveapp/reject/')
    elif approve == 1:
        approve_leave.status = 'อนุมัติ'
        approve_leave.save()
        return redirect('/leaveapp/approve/')

@login_required
def statistic(request):
    result = Leave.objects.filter(user = request.user).annotate(
                                    LeaveType = F('leave_type_name__leave_type_name')
                                ).values(
                                    'user',
                                    'emp_id',
                                    'LeaveType' 
                                ).annotate(
                                    LeaveDay = Sum('leave_amount'),
                                    MaxLeaveDay = Max('leave_type_name__leave_amount')
                                ).annotate(RemainingLeaveDays = 
                                    F('MaxLeaveDay') - F('LeaveDay')
                                )
                                
    context = {'result': result}                           
    return render(request, 'leaveapp/statistic.html', context)

@login_required
def leave_type_edit(request, id):
    type_edit = Leave_Type_Create.objects.get(id=id)
    form = Leave_Type_Create_Form(instance=type_edit)

    if request.method == 'POST':
        form = Leave_Type_Create_Form(request.POST, instance=type_edit)
        if form.is_valid():
            form.save()
            return redirect('leaveapp:leave_type_list')

    context = {'form': form}
    return render(request, 'leaveapp/leave_type_edit.html', context)

@login_required
def leave_department_edit(request, id):
    department_edit = Leave_Department_Create.objects.get(id=id)
    form = Leave_Department_Create_Form(instance=department_edit)

    if request.method == 'POST':
        form = Leave_Department_Create_Form(request.POST, instance=department_edit)
        if form.is_valid():
            form.save()
            return redirect('leaveapp:leave_department_list')
    
    context = {'form': form}
    return render(request, 'leaveapp/leave_department_edit.html', context)

@login_required
def deleteType(request, id):
    delete_type = Leave_Type_Create.objects.get(id = id)
    if request.method == 'POST':

        delete_type.delete()
        return redirect('leaveapp:leave_type_list')
        
    return render(request, 'leaveapp/leave_type_delete.html')

@login_required
def deleteDepartment(request, id):
    delete_department = Leave_Department_Create.objects.get(id=id)
    if request.method == 'POST':

        delete_department.delete()
        return redirect('leaveapp:leave_department_list')
    
    return render(request, 'leaveapp/leave_department_delete.html')

    
