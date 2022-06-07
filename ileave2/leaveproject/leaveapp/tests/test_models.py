from django.contrib.auth.models import User
from leaveapp.models import Leave, Leave_Type_Create, Leave_Department_Create
import pytest

@pytest.mark.django_db
def test_leave_type_create():
    leave = Leave_Type_Create.objects.create(
        leave_type_name = "test",
        leave_amount = 30
        )
    assert leave.leave_type_name == "test"
    assert leave.leave_amount == 30

@pytest.mark.django_db
def test_leave_department_create():
    leave = Leave_Department_Create.objects.create(
        leave_department_name = "test"
    )
    assert leave.leave_department_name == "test"
