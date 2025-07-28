from django.shortcuts import render,redirect # type: ignore
from .forms import *
from .models import *

def HomePage(request):

    return render(request, 'index.html')

def Addpage(request):
   
   context={
       'employee_form':Employee_Form()
   }

   if request.method == 'POST':
       
       employee_form=Employee_Form(request.POST)

       if employee_form.is_valid():
           
           employee_form.save()

   return render(request, 'add_emp.html',context)

def Viewpage(request):

    context={
        "all_employees":Employee.objects.all()
    }

    return render(request, 'view_emp.html',context)


def Editpage(request):

    context={
        "all_employees":Employee.objects.all()
    }

    return render(request, 'edit_emp.html',context)

def DeleteEmployee(request , id):

    selected_employee=Employee.objects.get(employee_id = id)

    selected_employee.delete()

    return redirect('/employeehub/edit/')

def UpdateEmployee(request ,id):

    selected_employee=Employee.objects.get(employee_id=id)

    context={
        'employee_form':Employee_Form(instance=selected_employee)
    }

    if request.method =="POST":

        employee_form=Employee_Form(request.POST,instance=selected_employee)

        if employee_form.is_valid():

            employee_form.save()

            return redirect('/employeehub/edit/')

    return render(request, 'add_emp.html',context)


