from django.shortcuts import render
import json
from django.http import HttpResponse
from login.models import userInf
from mainApp.models import mainInf
from django.http import FileResponse

# Create your views here.
def sendLocation(request):

    if request.method=='GET':
        return render(request,'mainApp.html')

    else:
        username=request.POST.get('username','')
        longi = request.POST.get('longi','')
        lati = request.POST.get('lati','')

        try:
            item = mainInf.objects.get(username=username)
            item.longi = longi
            item.lati = lati
            item.save()

            user = userInf.objects.get(username=username)
            user.isOnline = True
            user.save()

            return HttpResponse('Location updated!!!')
        except  Exception:
            try:
                item = userInf.objects.get(username=username)
                name = item.username
                item.isOnline = True
                item.save()
                mainInf.objects.create(username=username,longi=longi,lati=lati,name=name)
                return HttpResponse('Created userInf!!!')
            except Exception:
                return HttpResponse('Server Failed!!!')

def getLocation(request):

    try:

        list = userInf.objects.filter(isOnline=True)
        result=[]
        tmp = {}
        onlineList = list.values()
        count = 0
        for item in onlineList:
            username = item["username"]
            obj = mainInf.objects.get(username=username)
            user = userInf.objects.get(username=username)

            longi = obj.longi
            lati = obj.lati
            name = user.name

            tmp['username']=username
            tmp['longi']=longi
            tmp['lati']=lati
            tmp['name']=name

            result.append(tmp)

            tmp={}

            count=count+1

        if count==0:
            print(result)
            return HttpResponse('Nobody is Online!!!')

        return HttpResponse(json.dumps(result), content_type="application/json")

    except Exception:
        print(Exception.__doc__)
        pass

def dload(request):

    file = open('/tmp/location.v1.apk', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="location.v1.apk"'
    return response

