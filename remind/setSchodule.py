from mysql import mysql_query,mysql_exec
from sys import path
import json
import re

week = 1
day = 1

def index():
    updateTime()
    if week > 17:           # 周数不能大于17
        return
    res = getSchedule()
    for value in res:
        setSchedule(value)
def getSchedule():
    return mysql_query("select id,schedule from users where subscribe=1 and login=1 ")

def updateTime():
    global week,day
    timePath = path[0]+'/time.json'
    with open(timePath,'r',encoding='utf-8') as fr:
        timeDic = json.load(fr)
        fr.close()
    week = timeDic['week']
    day = timeDic['day']
    if day >=7:
        newWeek = week + 1
        newDay = 1
    else:
        newDay = day + 1
        newWeek = week

    timeDic = {
        'week':newWeek,
        'day':newDay
    }
    with open(timePath,'w') as fw:
        json.dump(timeDic,fw)
        fw.close()

def setSchedule(value):
    id = value[0]
    schedule = json.loads(value[1].encode("latin1").decode("utf-8"))
    todayAllSch = schedule[str(week)][str(day)]
    todaySch = {}       # 今天的课程
    for i in range(1,9):
        which = str(i)
        if todayAllSch[which]['classroom']:
            if not re.match(r'^ZX[\S\s]*$',todayAllSch[which]['classroom']):
                todaySch[which] = {
                    'classroom':todayAllSch[which]['classroom'],
                    'subject':todayAllSch[which]['subject']
                }
    mysql_exec("update users set todaySchedule='%s' where id=%d" % (json.dumps(todaySch,ensure_ascii=False),id))     # 将今天课保存起来
