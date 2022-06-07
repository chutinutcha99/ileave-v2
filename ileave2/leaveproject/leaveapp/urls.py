from django.urls import path
from . import views

app_name = 'leaveapp'

urlpatterns = [

    path('leave/', views.leave, name='leave'),
    path('approve/', views.approve, name='approve'),
    path('pending/', views.pending, name='pending'),
    path('reject/', views.reject, name='reject'),
    path('statistic/', views.statistic, name='statistic'),
    path('leave_type_create/', views.leave_type_create, name='leave_type_create'),
    path('leave_type_list/', views.leave_type_list, name='leave_type_list'),
    path('leave_department_create/', views.leave_department_create, name='leave_department_create'),
    path('leave_department_list/', views.leave_department_list, name='leave_department_list'),
    path('list_leave/', views.list_leave, name='list_leave'),
    path('approve_leave_form/<int:id>/<int:approve>/', views.approve_leave_form, name='approve_leave_form'),
    path('leave_type_edit/<int:id>/', views.leave_type_edit, name='leave_type_edit'),
    path('leave_department_edit/<int:id>/', views.leave_department_edit, name='leave_department_edit'),
    path('leave_type_delete/<int:id>/', views.deleteType, name='leave_type_delete'),
    path('leave_department_delete/<int:id>/', views.deleteDepartment, name='leave_department_delete')



]
