from django.shortcuts import render, redirect
from .models import *
import datetime
from django.contrib import messages
# Create your views here.


def home(request):
    user = request.user
    if user.is_authenticated:
        incomplete = tasks.objects.filter(user=user,date=datetime.date.today(),check=False)
        complete = tasks.objects.filter(user=user,date=datetime.date.today(),check=True)
        count = tasks.objects.filter(user=user,date=datetime.date.today()).count()
        if request.method == "POST":
            check = request.POST['check']
            id = request.POST['taskid']
            obj = tasks.objects.get(id=id)
            obj.check = check
            obj.save()
            messages.success(request, "Task Updated")
        parms = {
            "incomplete":incomplete,
            "complete":complete,
            "countz":count,
        }
        return render(request,'index.html',parms)
    else:
        return redirect('account_login')

def about(request):
    return render(request,'about.html')

def history(request):
    user = request.user
    if user.is_authenticated:
        obj = tasks.objects.filter(user=user,date__lt=datetime.date.today())
        parms = {
            "tasks":obj,
            "countz":obj.count(),
        }
        return render(request,'history.html',parms)
    else:
        return redirect('account_login')

def addtask(request):
    user = request.user
    if user.is_authenticated:
        count = tasks.objects.filter(user=user,date=datetime.date.today()).count()
        if request.method == "POST":
            if 'normal' in request.POST:
                name= request.POST['name']
                desc = request.POST['desc']
                obj = tasks.objects.filter(user=user,title__iexact=name)
                if obj.count() != 0:
                    messages.error(request,"This Task Already Exist!")
                else:
                    tasks.objects.create(title=name,desc=desc,user=user,check=False)
                    messages.success(request,"Task Created!")
            if 'yesterday' in request.POST:
                ob = tasks.objects.filter(user=user,date__lt=datetime.date.today())[0]
                getdate = ob.date
                obj = tasks.objects.filter(user=user,date=getdate)
                if obj is not None:
                    for i in obj:
                        tasks.objects.create(user=user,title=i.title,desc=i.desc,check=False)
                    messages.success(request,"Tasks Added!")
                else:
                    messages.error(request,'No Previous Task Present')
        parms = {
            "countz":count,
        }
        return render(request,'addtask.html',parms)
    else:
        return redirect('account_login')

def profile(request):
    return render(request,'account/Profile.html')
