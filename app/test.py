import xml.etree.ElementTree as Etree
import re

xml_str = """<xml><ToUserName><![CDATA[gh_2886768bf21d]]></ToUserName>
<FromUserName><![CDATA[ojuLjv4-]]></FromUserName>
<CreateTime>1512459610</CreateTime>
<MsgType><![CDATA[text]]></MsgType>
<Content><![CDATA[哈哈哈]]></Content>
<MsgId>6495964561991021898</MsgId>
</xml>"""
notify_data_tree = Etree.fromstring(xml_str)
str_value = notify_data_tree.find("Content").text
# print(str_value)
# a=22222
# def test():
#     print(a)
#
# def dd(func):
#     func()
# json ={'test':test}
# json['test']()

line = "s:13"

matchObj = re.match( r'^s:(\d*)$', line)

if matchObj:
   print ("matchObj.group() : ", matchObj.group())
   print ("matchObj.group(1) : ", matchObj.group(1))
else:
   print ("No match!!")