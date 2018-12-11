from urllib import request


request = request.urlopen("https://baidu.com")
data = {

}
print(request.read().decode())


