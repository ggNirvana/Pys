import pytesseract
from PIL import Image
from urllib import request,parse
from io import BytesIO
from http import cookiejar
import re


cookie = cookiejar.CookieJar()
cookie_handler = request.HTTPCookieProcessor(cookie)
http_handler = request.HTTPHandler()
https_handler = request.HTTPSHandler()
opener = request.build_opener(http_handler,https_handler,cookie_handler)


data = {
    'useValidateCode': 1,
    'isremenberme': 1,
    'ip':'',
    '_eventId': 'submit',
    'username': '16211134120',
    'password': 'woshi.123456',
    'rememberUser': 'true',
    'rememberMe': 'true',
    'losetime': 30
}

urlcode = 'http://rz.wzu.edu.cn/zfca/captcha.htm'
urlLog = 'http://spoc.wzu.edu.cn/oauth/toMoocAuth.mooc'
urlDefault = 'http://spoc.wzu.edu.cn/portal/myCourseIndex/1.mooc'

head = {
    'Accept':'image/gif, image/jpeg, image/pjpeg, application/x-ms-application, application/xaml+xml, application/x-ms-xbap, */*',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN',
    'Connection': 'keep-alive',
    'Host':'spoc.wzu.edu.cn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}

def getAction(html):
    p = re.compile('action=".*?"')
    action = re.findall(p,html)[0].replace('action=','').replace('"','')
    return 'http://rz.wzu.edu.cn'+action

def Login(data,action):

    data = parse.urlencode(data).encode()
    req = request.Request(action,data=data,headers=head)
    headers = opener.open(req).headers
    print(headers)
    req = request.Request(urlDefault,headers=head)



    opener.open(req)
    for i in cookie:
        print(i)

def getCode():
    req = request.Request(urlcode,headers=head)
    rsp = opener.open(req).read()
    image = Image.open(BytesIO(rsp))
    text = pytesseract.image_to_string(image=image)
    print(text)
    return text


def getLt(html):
    p = re.compile('name="lt" value=".*"')
    lt = re.findall(p,html)[0].replace('name="lt" value="','').replace('"','')
    return lt


code = getCode()
req = request.Request(urlLog,headers=head)
html = opener.open(req).read().decode('gbk')

lt = getLt(html)
data.update({'lt': lt})
data.update({'j_captcha_response': code})
action = getAction(html)
Login(data,action)
print(action)
print(cookie)


# http://218.75.27.182:8080/sso.auth?tn=1538098725201&ru=http%3A%2F%2Fspoc.wzu.edu.cn%2Foauth%2FmoocAuth.mooc