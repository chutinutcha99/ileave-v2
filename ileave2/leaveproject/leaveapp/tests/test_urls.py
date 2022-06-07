from django.urls import reverse, resolve

def test_home_url():
    url = reverse('home')
    assert resolve(url).view_name == "home"

def test_leave_url():
    url = reverse('leaveapp:leave')
    assert resolve(url).view_name == "leaveapp:leave"

def test_approve_url():
    url = reverse('leaveapp:approve')
    assert resolve(url).view_name == "leaveapp:approve"

def test_pending_url():
    url = reverse('leaveapp:pending')
    assert resolve(url).view_name == "leaveapp:pending"

def test_reject_url():
    url = reverse('leaveapp:reject')
    assert resolve(url).view_name == "leaveapp:reject"

def test_leave_type_create_url():
    url = reverse('leaveapp:leave_type_create')
    assert resolve(url).view_name == "leaveapp:leave_type_create"

def test_leave_type_list_url():
    url = reverse('leaveapp:leave_type_list')
    assert resolve(url).view_name == "leaveapp:leave_type_list"

def test_leave_department_create_url():
    url = reverse('leaveapp:leave_department_create')
    assert resolve(url).view_name == "leaveapp:leave_department_create"

def test_leave_department_list_url():
    url = reverse('leaveapp:leave_department_list')
    assert resolve(url).view_name == "leaveapp:leave_department_list"

def test_list_leave_url():
    url = reverse('leaveapp:list_leave')
    assert resolve(url).view_name == "leaveapp:list_leave"

def test_statistic_url():
    url = reverse('leaveapp:statistic')
    assert resolve(url).view_name == "leaveapp:statistic"

