import userDao

def setDayRemindOpen(openId):
    res = userDao.setDayRemind(openId,1)
    if res:
        return '当日提醒已开启'
    else:
        return '当日提醒已经开启，请勿重复开启'

def setDayRemindClose(openId):
    res = userDao.setDayRemind(openId,0)
    if res:
        return '当日提醒已关闭'
    else:
        return '当日提醒已经关闭，请勿重复关闭'

def setBeforeRemindOpen(openId):
    res =userDao.setBeforeRemind(openId,1)
    if res:
        return '课前提醒已开启'
    else:
        return '课前提醒已经开启，请勿重复开启'
def setBeforeRemindClose(openId):
    res = userDao.setBeforeRemind(openId,0)
    if res:
        return '课前提醒已关闭'
    else:
        return '课前提醒已经关闭，请勿重复关闭'
def getRemindStatus(openId):
    res = userDao.getRemindStatus(openId)
    content = '当日提醒状态：'
    if res[0] == 1:
        content += '开启，'
    else:
        content += '关闭，'
    content += '课前提醒状态：'
    if res[1] == 1:
        content += '开启'
    else:
        content += '关闭'
    return content

def getSchedule(openId):
    return '请发送“s:第几周”，如“s:13”就可以获取第13周的课表'

eventType = {
    'setDayRemindOpen':setDayRemindOpen,
    'setDayRemindClose':setDayRemindClose,
    'setBeforeRemindOpen':setBeforeRemindOpen,
    'setBeforeRemindClose':setBeforeRemindClose,
    'getRemindStatus':getRemindStatus,
    'getSchedule':getSchedule
}