from django import forms
from .models import Leave, Leave_Type_Create, Leave_Department_Create

class LeaveForm(forms.ModelForm):

    class Meta:

        model = Leave

        fields = '__all__'

        exclude = ('user', 'updated', 'created', 'status',)

class Leave_Type_Create_Form(forms.ModelForm):

    class Meta:

        model = Leave_Type_Create

        fields = '__all__'

class Leave_Department_Create_Form(forms.ModelForm):

    class Meta:

        model = Leave_Department_Create

        fields = '__all__'

