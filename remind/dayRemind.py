import userDao
from weChat import sendTemMsg
from data import todayRemindContentTemId,todayRemindTitleTemId
from common import getContent,timeQue,json


def index():
    res = userDao.getDayRemind()
    for value in res:
        sendSchoduleToUser(value)

def sendSchoduleToUser(userMsg):
    openId = userMsg[0]
    if not userMsg[1]:
        return
    todaySchedule = json.loads(userMsg[1].encode("latin1").decode("utf-8"))
    if len(todaySchedule) == 0:
        return
    data = {
        'count':{
            'value':len(todaySchedule)
        }
    }
    content = getContent(data,openId,todayRemindTitleTemId)
    sendTemMsg(content)         # 发送当日提醒的头部信息
    for i in range(1,9):
        which = str(i)
        if which in todaySchedule.keys():
            data = {
                'courses':{
                    'value':todaySchedule[which]['subject']
                },
                'time':{
                    'value':timeQue[i-1]
                },
                'classroom':{
                    'value':todaySchedule[which]['classroom']
                }
            }
            content = getContent(data, openId, todayRemindContentTemId)
            sendTemMsg(content)
