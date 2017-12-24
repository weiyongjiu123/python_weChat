from urllib import parse,request
from data import appID,appSecret
import time
import json

access_token = ''
access_tokenTime = 0

def getAccessToken():
    global  access_token,access_tokenTime
    url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid='+appID+'&secret='+appSecret
    dic = post(url=url)
    access_token = dic['access_token']
    access_tokenTime = dic['expires_in'] + int(time.time())
# setAccessToken()
def setAccessToken():
    if int(time.time()) > access_tokenTime:
        getAccessToken()


def sendTemMsg(content):
    setAccessToken()
    url = 'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token='+access_token
    return post(url=url,content=content)

def sendWelCome(toUserOpenId):
    content = {
        'touser':toUserOpenId,
        'template_id':'j3nXKTJJzf_Xt-5Jutusvr8g4ICAs6L2BPeyYmdB_ro'
    }
    content = json.dumps(content).encode(encoding='utf-8')
    resDic = sendTemMsg(content)
    return resDic

def post(url,content=''):
    req = request.Request(url=url)
    if content == '':
        res = request.urlopen(req)
    else:
        res = request.urlopen(req,data=content)
    jsonStr = str(res.read(), encoding='utf-8')
    dic = json.loads(jsonStr)
    return dic

