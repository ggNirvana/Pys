from django.shortcuts import render
from django.http import HttpResponse
from login.models import userInf
# Create your views here.


def addUser(request):
    if request.method=='GET':
        return render(request,'registe.html')

    else:
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        name = request.POST.get('name','')
        userInf.objects.create(username=username,password=password,name=name)
        return HttpResponse('Registe successfully!!!')

