from django.shortcuts import render, HttpResponse
from .models import Employee, Role, Department
from datetime import datetime
from django.db.models import Q
from .form import FeedbackForm
# Create your views here.


def index(request):
    return render(request, 'index.html')


def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request, 'all_emp.html', context)


def add_emp(request):
    if request.method == 'POST':
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        dept = int(request.POST['dept'])
        role = int(request.POST['role'])
        new_emp = Employee(first_name=fname, last_name=lname, salary=salary, bonus=bonus,
        phone=phone, dept_id=dept, role_id=role, hire_date=datetime.now())
        new_emp.save()
        return HttpResponse("Employee Added.")
    elif request.method == 'GET':
        return render(request, 'add_emp.html')
    else:
        return HttpResponse("Else and handled, Employee not Added.")


def remove_emp(request, emp_id = 0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Removed successfully")
        except:
            return HttpResponse("please enter valid emp_id")

    emps = Employee.objects.all()
    context = {
        'emps': emps            
    }
    return render(request, 'remove_emp.html', context)
    
def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']

        emps = Employee.objects.all()

        if name:
            emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))

        if dept:
            emps = emps.filter(Q(dept__name__icontains = dept))

        if role:
            emps = emps.filter(Q(role__name__icontains = role))
            
        context = {
            'emps': emps            
        }
        return render(request,'all_emp.html', context)

    elif request.method == 'GET':
        return render(request,'filter_emp.html')
    else:
        return HttpResponse("Else is not handled, Employee not filtered.")
def feedback_emp(request):
    if request.method=='post':
        form=FeedbackForm(request.post)
        if form.is_valid():
            form.save()
            print("data saved")
        else:
            return render(request, 'feedback_emp.html',{'form':form})
    else:
        form=FeedbackForm()
        return render(request,"feedback_emp.html",{'form':form})
    

 
    