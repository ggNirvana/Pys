from urllib import request,parse


req = request.Request('http://0.0.0.0:8000/mainApp')
data={
    'username':'admin'
}
data = parse.urlencode(data).encode()
rsp = request.urlopen(req,data=data)
