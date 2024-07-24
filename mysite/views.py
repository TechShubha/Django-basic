from employees.models import Employee
from django.shortcuts import render


def index(request):
  employees = Employee.objects.all()
  context={'employees' : employees,}
  return render(request, 'index.html',context)