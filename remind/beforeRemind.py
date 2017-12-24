import userDao
from common import getContent,timeQue,json
from weChat import sendTemMsg
from data import beforeRemindTemId

which = '1'
def index(w):
    global which
    which = w
    res = userDao.getBeforeRemind()
    for value in res:
        sendBeforeRemind(value)

def sendBeforeRemind(userMsg):
    openId = userMsg[0]
    todaySchedule = json.loads(userMsg[1].encode('latin1').decode('utf-8'))
    if which in todaySchedule.keys():
        data = {
            'courses':{
                'value':todaySchedule[which]['subject']
            },
            'time':{
                'value':timeQue[int(which)]
            },
            'classroom':{
                'value':todaySchedule[which]['classroom']
            }
        }
        content = getContent(data,openId,beforeRemindTemId)
        sendTemMsg(content)

