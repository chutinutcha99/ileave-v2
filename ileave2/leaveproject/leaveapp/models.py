import datetime
from django.db import models
from django.contrib.auth.models import User
import numpy as np

STATUSES_CHOICES = (
    ('PENDING', 'รออนุมัติ'),
    ('APPROVE', 'อนุมัติ'),
    ('REJECT', 'ไม่อนุมัติ'),
)

class Leave_Type_Create(models.Model):
    leave_type_name = models.CharField(verbose_name="ประเภทการลา", max_length=200)
    leave_amount = models.PositiveIntegerField(verbose_name="จำนวนวันลา")

    class Meta:
        db_table = "leaveapp_leave_type_create"
    
    def __str__(self):
        return self.leave_type_name

class Leave_Department_Create(models.Model):
    leave_department_name = models.CharField(verbose_name="ชื่อแผนก", max_length=200)

    class Meta:
        db_table = "leaveapp_leave_department_create"

    def __str__(self):
        return self.leave_department_name


class Leave(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    emp_id = models.IntegerField(verbose_name="รหัสพนักงาน")
    leave_type_name = models.ForeignKey(Leave_Type_Create, on_delete=models.CASCADE, verbose_name="ประเภทการลา")
    leave_department_name = models.ForeignKey(Leave_Department_Create, on_delete=models.CASCADE, verbose_name="แผนก")
    leave_reason = models.CharField(max_length=200, verbose_name="เหตุผลการลา")
    start_date = models.DateField(default=datetime.date.today, verbose_name="ตั้งแต่วันที่")
    end_date = models.DateField(default=datetime.date.today, verbose_name="ถึงวันที่")
    leave_amount = models.IntegerField(verbose_name="จำนวนวันลา")
    upload = models.FileField(upload_to='file_uploads')
    leave_contact = models.CharField(max_length=200, verbose_name="การติดต่อระหว่างลา")
    status = models.CharField(max_length=200, choices=STATUSES_CHOICES, default='รออนุมัติ')
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        db_table = "leaveapp_leave"

    def days_leave(self):
        start_date = self.start_date
        end_date = self.end_date

        return np.busday_count(start_date, end_date) + 1

    def __str__(self):
        return self.user.first_name  + ' - ' + str(self.start_date)
    


