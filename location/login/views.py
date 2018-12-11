from django.shortcuts import render
from django.http import HttpResponse
from login.models import userInf

# Create your views here.


def isValide(request):
    if request.method=='GET':
        return render(request,'login.html')
    else:
        username=request.POST.get('username','')
        password=request.POST.get('password','')


        try:
            result = userInf.objects.get(username=username)
            if password==result.password:
                return HttpResponse('Login Successfully!!!'+result.name)
            else:
                return HttpResponse('Not Match!!!')

        except BaseException :

            return HttpResponse("User doesn't exists!!!")

