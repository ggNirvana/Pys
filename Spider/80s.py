'''
请求多了之后会验证cookie
cookie不对就不能完成跳转
捕获返回的JS代码破解
计算一次就够
'''
from urllib import request,parse
import re
import xlwt

finalUrl = ''

def getSort(html):
    p1 = re.compile('<div class="s_block1">.*</div>',re.DOTALL)
    p2 = re.compile('<a.*?</a>',re.DOTALL)
    p3 = re.compile('>[\u4E00 -\u9FA5].*<')
    p4 = re.compile('  [\u4E00 -\u9FA5].* ')
    tsort = re.findall(p1, html)
    try:
        tsort = re.findall(p2,tsort[0])
        sort = re.findall(p4,tsort[1])[0].replace(' ','')+re.findall(p3,tsort[2])[0].replace('>','').replace('<','')
        return sort
    except BaseException :
        return None

def getHtml(url):
    headers = {
        'cache-control': 'max-age=0',
        'cookie': "__cm_warden_uid=7091182325c13ded55c87bf0c4f70081cookie;__cm_warden_upi=MTIyLjIyOC4xODguMTA5",
        'upgrade-insecure-requests': 1,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    }

    try:
        rsp = request.Request(url=url, headers=headers)
        html = request.urlopen(rsp)
        global finalUrl
        finalUrl = html.geturl()
        html = html.read().decode()
        return html
    except BaseException:
        return None

def getResult(html):
    thunList=[]
    p1 = re.compile(r'thunder://.*?["] thunderr|magnet:.*?["] thunderr')
    tthunList = re.findall(p1,html)
    for i in range(tthunList.__sizeof__()):
        try:
            thun = tthunList.__getitem__(i).replace('" thunderr','')
            thunList.append(thun)
        except BaseException:
            pass
    return thunList

def getName(html):
    p1 = re.compile('<h1 class="font14w">.*</h1>')
    name = re.findall(p1,html)
    name = name[0].replace('<h1 class="font14w">','').replace('</h1>','')
    print(name)
    return name

if __name__ == '__main__':

    book =xlwt.Workbook('result.xlsx')
    sheet = book.add_sheet('sheet1')
    sheet.write(0, 0, '名称')
    sheet.write(0, 1, '连接')
    sheet.write(0, 2, '分类')
    sheet.col(0).width = 4000
    sheet.col(1).width = 20000
    row = 1
    for i in range(7777,23000):
        if(i==7789):
            continue
        print(i.__str__() + 'isdoing...')
        try:
            url = 'https://www.80s.tw/ju/'+i.__str__()

            html=getHtml(url)
            if html==None:
                continue
            thunlist=getResult(html)
            sort = getSort(html)
            name = getName(html)
            for j in range(thunlist.__len__()):
                sheet.write(row, 0, name)
                sheet.write(row, 2, sort)
                sheet.write(row, 1, thunlist.__getitem__(j))
                print(name + '   ' + thunlist.__getitem__(j))
                row = row + 1
        except Exception as e:
            url = 'https://www.80s.tw/ju/' + i.__str__()
            html = getHtml(url)
            print(html)
            print(e)
        book.save(filename_or_stream='result.xls')



