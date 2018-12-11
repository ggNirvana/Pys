import requests
import re
from bs4 import BeautifulSoup
import re
while(1):
    print("**************************************************************************************************************\n")
    id=input("输入车牌：")
    newsurl='https://m.zhongziso.com/list/'+id+'/1'
    res=requests.get(newsurl)
    res.encoding ='utf-8'
    soup=BeautifulSoup(res.text,"html.parser")
    nameList = []
    magnetList = []
    thunderList = []
    for x in soup.select('.list-group'):
        p1=re.compile(r'[>](.*?)[<]',re.S)
        name=str(x.select('.text-success'))
        name=str(re.findall(p1,name)).replace("'","").replace(",","").replace(" ","")
        nameList.append(name)


    for x in soup.select('.down'):
        magnet = x.select('a')[0]['href']
        thunder = x.select('a')[1]['href']
        magnetList.append(magnet)
        thunderList.append(thunder)

    print("***********************************************搜索结果*******************************************************\n")
    for i in range(0,len(nameList)):
        print(nameList[i])
        print("磁力链接："+magnetList[i])
        print("迅雷链接："+thunderList[i])



