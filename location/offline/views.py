from django.shortcuts import render
from django.http import HttpResponse
from login.models import userInf
# Create your views here.


def setOff(request):
    if request.method=='GET':
        return render(request,'offline.html')
    else:
        username = request.POST.get('username','')
        try:
            obj = userInf.objects.get(username=username)

            if obj.isOnline==False:
                return HttpResponse('offline!!!')
            obj.isOnline=False
            obj.save()
            return HttpResponse(obj.username+' has been offline!!!')
        except BaseException:

            return HttpResponse('failed!!!')