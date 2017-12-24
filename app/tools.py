import time
def toXml(dic):
    xml = '<xml>'
    for key in dic:
        if is_int(value=dic[key]):
            xml += '<'+key+'>'+dic[key]+'</'+key+'>'
        else:
            xml += '<' + key + '><![CDATA[' + dic[key] + ']]></' + key + '>'
    xml += '</xml>'
    return xml
def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False
def sendTextToMsg(dataTree,content):
    xmlDic = {
        'ToUserName': dataTree.find('FromUserName').text,
        'FromUserName': dataTree.find('ToUserName').text,
        'CreateTime': str(int(time.time())),
        'MsgType': 'text',
        'Content': content,
    }
    return toXml(xmlDic)

test = {
    'ToUserName':'gh_2886768bf21d',
    'FromUserName':'ojuLjv4-',
    'CreateTime':'1512459610',
    'MsgType':'text',
    'Content':'哈哈哈',
    'MsgId':'6495964561991021898'
}
