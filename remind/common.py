import json

def getContent(data,openId,temId):
   return json.dumps({
        'touser': openId,
        'template_id': temId,
        'data':data
    }).encode('utf-8')

timeQue = [
    '09：00~10：20',
    '10：40~12:00',
    '12：30~13：50',
    '14：00~15：20',
    '15：30~16：50',
    '17：00~18：20',
    '19：00~20：20',
    '20：00~21：50'
]