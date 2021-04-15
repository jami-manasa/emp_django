from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import EmployeeForm,AssetsForm
from .models import Employee,table

# Create your views here.


def employee_list(request):
    context = {'employee_list': Employee.objects.all()}
    return render(request, "data/employee_list.html", context)

def assets_list(request):
    context = {'assets_list': table.objects.all()}
    return render(request, "data/employee_assets.html", context)


def employee_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, "data/employee_form.html", {'form': form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST,instance= employee)
        if form.is_valid():
            form.save()
        return redirect('/employeelist')


def employee_delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employeelist')

# def employee_assets(request,id):


def assets_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = AssetsForm()
        else:
            assets = table.objects.get(pk=id)
            form = AssetsForm(instance=assets)
        return render(request, "data/employee_aform.html", {'form': form})
    else:
        if id == 0:
            form =AssetsForm(request.POST)
        else:
            assets = table.objects.get(pk=id)
            form = AssetsForm(request.POST,instance= assets)
        if form.is_valid():
            form.save()
        return redirect('/assetslist')
# def show(request):
#     showall=table.objects.all()
#     return render(request,"data/employee_aform.html.",{'data':showall})


def assets_delete(request,id):
    a = table.objects.get(pk=id)
    a.delete()
    return redirect('/assetslist')