import userDao
import json
from data import scheduleTemId
from  weChat import sendTemMsg,get

classroom = [
    'oneCla',
    'twoCla',
    'threeCla',
    'fourCla',
    'fiveCla',
    'sixCla',
    'sevenCla',
    'eightCla'
]
subject =[
    'oneCou',
    'twoCou',
    'threeCou',
    'fourCou',
    'fiveCou',
    'sixCou',
    'sevenCou',
    'eightCou'
]

dayQue = [
    '一',
    '二',
    '三',
    '四',
    '五',
    '六',
    '日'
]
def getOneWeekSchedule(openId,week):
    schedule = userDao.getOneWeekSchedule(openId)
    schedule = schedule[0][0].encode("latin1").decode("utf-8")
    scheduleDic = json.loads(schedule)
    return scheduleDic[week]
def sendOneWeekToUser(dic,openId,week):
    content = {
        'touser': openId,
        'template_id': scheduleTemId
    }
    for day in range(1,8):
        data = {
            'week':{
                'value':week
            },
            'day':{
                'value':dayQue[day-1]
            }
        }
        for i in range(1,9):
            dayStr = str(day)
            which = str(i)
            if dic[dayStr][which]['classroom']:
                data[classroom[i-1]] ={
                    'value': dic[dayStr][which]['classroom']
                }
                data[subject[i-1]] = {
                    'value': dic[dayStr][which]['subject']
                }
        content['data'] = data
        res = sendTemMsg(json.dumps(content).encode(encoding='utf-8'))

def doLogin(openId,number,password):
    isHasLogin = userDao.isHasLogin(openId)
    if isHasLogin == 0:
        url = "https://smallsi.com:9503/?number="+number+"&password="+password+"&type=schedule"
        res = json.loads(get(url))
        schedule = json.dumps(res['content'],ensure_ascii=False)
        if res['error'] == 0:
            updateRes = userDao.updateLogin(openId=openId,schedule=schedule)
            if updateRes:
                return '登陆成功'
            else:
                return '登陆失败，请重试'
        else:
            return '登陆失败，请检查学号和密码是否正确'
    else:
         return '你已经登陆过了'
