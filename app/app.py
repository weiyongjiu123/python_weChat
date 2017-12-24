import xml.etree.ElementTree as Etree
from tools import sendTextToMsg
from weChat import sendWelCome
import userDao
from doEvent import eventType
import re
import doText

replyContent = 'success'
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    if environ['REQUEST_METHOD'] == 'GET':
        if environ['QUERY_STRING'] != '':
            params = environ['QUERY_STRING'].split('&')
            getParam = {}
            if(params):
                for key in params:
                    split = key.split('=')
                    getParam[split[0]] = split[1]
                    # print(split)
        return [bytes(getParam['echostr'], encoding="utf8")]
    elif environ['REQUEST_METHOD'] == 'POST':
        try:
            request_body_size = int(environ.get('CONTENT_LENGTH', 0))
        except (ValueError):
            request_body_size = 0
        request_body = environ['wsgi.input'].read(request_body_size)
        xml = str(request_body, encoding = "utf-8")
        dataTree = Etree.fromstring(xml)
        str_value = dataTree.find("MsgType").text
        __replyMsgType[str_value](dataTree)
        return [bytes(replyContent, encoding = "utf8")]

def reply(dataTree,content):
    global replyContent
    replyContent = sendTextToMsg(dataTree=dataTree, content=content)

def replyNull():
    global replyContent
    replyContent = 'success'

def replyTextMsg(dataTree):
    text = dataTree.find('Content').text
    openId = dataTree.find('FromUserName').text
    matchObj = re.match(r'^s:(\d*)$', text)
    if matchObj:
        week = matchObj.group(1)
        oneWeekDic = doText.getOneWeekSchedule(openId=openId,week=week)
        doText.sendOneWeekToUser(dic=oneWeekDic,openId=openId,week=week)
        replyNull()     # 不回复信息
        return
    loginMatch = re.match(r'^login:(\d{10})_([\S]*$)',text)
    if loginMatch:          # 登陆
        number = loginMatch.group(1)
        password = loginMatch.group(2)
        doTextRes = doText.doLogin(openId=openId,number=number,password=password)
        reply(dataTree, doTextRes)
        return
    content = '你发送消息的类型是'+dataTree.find('MsgType').text+'，内容为：'+dataTree.find('Content').text
    reply(dataTree,content)

def replyImageMsg(dataTree):
    content = '你发送消息的类型是'+dataTree.find('MsgType').text+'，图片链接为：' \
                                                        ''+dataTree.find('PicUrl').text+ '，图片消息媒体id：'+dataTree.find('MediaId').text
    reply(dataTree, content)

def replyVoiceMsg(dataTree):
    content = '你发送消息的类型是' + dataTree.find('MsgType').text + '，语音消息媒体id：' \
                                                            ''+dataTree.find('MediaId').text+'，语音格式：'+dataTree.find('Format').text
    reply(dataTree, content)

def replyVideoMsg(dataTree):
    content = '你发送消息的类型是' + dataTree.find('MsgType').text + '，语音消息媒体id：' \
                                                            '' +  dataTree.find('MediaId').text + '，视频消息缩略图的媒体id'+dataTree.find('ThumbMediaId').text
    reply(dataTree, content)

def replyLocationMsg(dataTree):
    content = '你发送消息的类型是' + dataTree.find('MsgType').text + '，维度：'  + dataTree.find('Location_X').text + '，经度：'+ dataTree.find('Location_Y').text + '，地图缩放大小：'+dataTree.find('Scale').text + '，地理位置信息：'+ dataTree.find('Label').text
    reply(dataTree, content)

def replyEventMsg(dataTree):
    openId = dataTree.find('FromUserName').text
    if dataTree.find('Event').text == 'CLICK':
        doEventRes = eventType[dataTree.find('EventKey').text](openId)
        reply(dataTree, doEventRes)
    elif dataTree.find('Event').text == 'subscribe':
        sendWelCome(openId)
        res = userDao.isHasUser(openId)
        if res:
            pass
        else:
            addRes = userDao.addUser(openId)
    elif dataTree.find('Event').text == 'unsubscribe':
            setRes = userDao.setUnSubscribe(openId)

def replyLinkMsg(dataTree):
    content = '你发送消息的类型是' + dataTree.find('MsgType').text + '，消息标题：' \
                                                            ''+dataTree.find('Title').text +'，消息描述：'+dataTree.find('Description').text + '，消息链接：'+dataTree.find('Url').text
    reply(dataTree, content)
__replyMsgType = {
    'text':replyTextMsg,
    'image':replyImageMsg,
    'voice':replyVoiceMsg,
    'video':replyVideoMsg,
    'location':replyLocationMsg,
    'event':replyEventMsg,
    'link':replyLinkMsg
}
