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


urlcode = 'http://rz.wzu.edu.cn/zfca/captcha.htm'
urlLog = 'http://rz.wzu.edu.cn/zfca/login'
urlDefault= 'http://portal.wzu.edu.cn/portal.do?caUserName=16211134120'
data = {
    'useValidateCode': 1,
    'isremenberme': 1,
    'ip':'',
    '_eventId': 'submit',
    'username': '16211134117',
    'password': '19980309xbj',
    'rememberUser': 'true',
    'rememberMe': 'true',
    'losetime': 30
}

head ={
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'rz.wzu.edu.cn',
    'Origin': 'http://rz.wzu.edu.cn',
    'Referer': 'http://rz.wzu.edu.cn/zfca/login',
    'Upgrade-Insecure-Requests': 1,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',


}

'''
验证码获取和识别
'''

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


def Login(data,urlLog):
    code = getCode()
    req = request.Request(urlLog, headers=head)
    rsp = opener.open(req)
    html = rsp.read().decode('GBK')
    lt = getLt(html)
    data.update({'lt': lt})
    data.update({'j_captcha_response': code})
    data = parse.urlencode(data).encode()
    req = request.Request(urlLog, data=data, headers=head)
    opener.open(req)
    return opener

def getMainPage():
    for c in cookie:
        print(c)
    req = request.Request(urlDefault, headers=head)
    rsp = opener.open(req)
    html = rsp.read().decode('gbk')
    p = re.compile('<div id="140186609476925696" class="urlportlet_140627552087873573_140186609476925696" >')
    result = re.findall(p,html)

    if result.__len__() !=0:
        print('登陆成功')
    else:
        print('登陆失败')


if __name__ ==  '__main__':

    Login(data,urlLog)
    getMainPage()





