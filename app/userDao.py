from mysql import mysql_query,mysql_exec

def isHasUser(openId):
     return mysql_query("select id from users where openId = '%s' limit 1" % openId)

def addUser(openId):
    return mysql_exec("insert into users(openId,subscribe,login,dayRemind,beforeRemind) values('%s',1,0,1,1)" % openId)

def setUnSubscribe(openId):
    return mysql_exec("update users set subscribe=0 where openId='%s'" % openId)

def setDayRemind(openId,status):
    return mysql_exec("update users set dayRemind = %s where openId='%s'" % (status,openId))

def setBeforeRemind(openId,status):
    return mysql_exec("update users set beforeRemind = %s where openId='%s'" % (status,openId))

def getRemindStatus(openId):
    res = mysql_query("select dayRemind,beforeRemind from users where openId='%s' limit 1" % openId)
    return res[0]

def getOneWeekSchedule(openId):
    return mysql_query("select schedule from users where openId = '%s'" % openId)

def isHasLogin(openId):
    return  mysql_query("select openId from users where openId = '%s' and login=1 limit 1" % openId)

def updateLogin(openId,schedule):
    return mysql_exec("update users set login=1,schedule='%s' where openId='%s'" % (schedule,openId) )