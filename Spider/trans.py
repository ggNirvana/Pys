import urllib
import json

url = 'http://fanyi.baidu.com/sug'
res = urllib.request.urlopen(url)

data={
    'kw': 'girl',
}
data = urllib.parse.urlencode(data).encode()

rsp = urllib.request.urlopen(url,data)
json_data = rsp.read().decode()
json_data = json.loads(json_data)
print(json_data)

list=json_data['data']
for d in list:
    k,v=d
    print(d)
    print(v)