import json


import requests

import re
import urllib3

requests.packages.urllib3.disable_warnings()
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)

pro={
    "http":"http://127.0.0.1:8888",
     "https":"http://127.0.0.1:8888"
     }
s=requests.Session()
#登录
mndlurl="http://mall.health-100.cn/mnMall/user/login"
mndheader={"Content-Type":"application/json"}
bodydata={"verificationcode":"","telenumber":"15979276985","password":"a1394512032","sign":"82cc2ceaa98d6154af30f6031c634740"}
d=json.dumps(bodydata)
#print(d)
resp=s.post(mndlurl,data=d,headers=mndheader,verify=False)#,proxies=pro)

#print(resp.content)

reg1='token": "(.*?)"'
token11=re.findall(reg1,resp.text)
print(token11[0])
tjdzurl='http://mall.health-100.cn/mnMall/address/addAddress'
tjdzheader={"Content-Type":"application/json"}
tjbodydata={"token":token11[0],"uid":"0748b14a-b699-4e01-ac29-b57ef0bf8740","receiver":"愉快","receiverphone":"13555656565","province":"河北省","city":"秦皇岛市","customize":"嘻嘻嘻","ifdefault":"","sign":"c0cbf444165d83d672d2559911a913d5"}
ee=json.dumps(tjbodydata)
print(ee)
tjpesp=s.post(tjdzurl,data=ee,headers=tjdzheader,verify=False)
print(tjpesp.text)

