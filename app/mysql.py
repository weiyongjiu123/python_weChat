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

# def addUser(openId):
#     return mysql_exec(openId)
# res = msyql_query('select * from user where id=1')
# result = cursor.fetchall()
# mysql_exec("insert into users(openId,subscribe,login,dayRemind,beforeRemind) values('%s','1','0','1','1')" % '333')
# print(res[0][1].encode("latin1").decode("utf-8"))
# res = mysql_exec('insert into users(openId,subscribe) values("234234",1)')
# res = mysql_exec("update users set subscribe=0 where openId='%s'" % 'ojuLjv4-rfCQcSVEx7pPnGeAIvas')
# print(res)

# print(result)
# if 0:
#     print(11)
# else:
#     print(22)
# sql = 'insert into `user`(username) values("哈哈")'.encode("utf-8").decode("latin1")

# try:
#     cursor.execute(sql)
#     db.commit()
# except:
#     db.rollback()
# cursor.execute("SELECT VERSION()")
# data = cursor.fetchone()
# db.close()
# print(data)