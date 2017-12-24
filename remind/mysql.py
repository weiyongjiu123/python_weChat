import pymysql
from data import username,password,dbName,host

cursor = ''
db = ''
def setCursor():
    global cursor,db
    if cursor == '':
        db = pymysql.connect(host, username, password, dbName)
        cursor = db.cursor()
        cursor.execute('set names utf8')
    try:
        db.ping()
    except:
        db.connection()
# 查询
def mysql_query(sql):
    setCursor()
    sql = sql.encode("utf-8").decode("latin1")
    if cursor.execute(sql):
        return cursor.fetchall()
    else:
        return 0
# 增删改
def mysql_exec(sql):
    setCursor()
    sql = sql.encode("utf-8").decode("latin1")
    res = cursor.execute(sql)
    db.commit()
    return res