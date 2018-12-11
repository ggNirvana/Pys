
from urllib import request


def test():
    rsp = request.Request("http://0.0.0.0:8000/registe")
    req = request.urlopen(rsp)
    print(req.read().decode())

test()