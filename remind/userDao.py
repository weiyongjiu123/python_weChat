from mysql import mysql_exec,mysql_query

def getAllUserMsg(sql):
    return mysql_query(sql)

def getDayRemind():
    return  getAllUserMsg("select openId,todaySchedule from users where subscribe=1 and login=1 and dayRemind=1")

def getBeforeRemind():
    return  getAllUserMsg("select openId,todaySchedule from users where subscribe=1 and login=1 and beforeRemind=1")
