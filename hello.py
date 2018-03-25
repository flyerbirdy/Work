# -*- coding:utf-8 -*-
from flask import Flask
from flask import request
import requests
from tuling import tulin
import hashlib
from time import time
import xml.etree.ElementTree as et
import re

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def wechat():

    if request.method == 'GET':
       
        token = 'hahaha'
        data = request.args
        signature = data.get('signature','')
        timestamp = data.get('timestamp','')
        nonce = data.get('nonce','')
        echostr = data.get('echostr','')
        list = [token, timestamp, nonce]
        list.sort()

        s = list[0] + list[1] + list[2]
              
        hascode = hashlib.sha1(s.encode('utf-8')).hexdigest()

        if hascode == signature:
       	  return echostr
        else:
       	  return ""


    if request.method == 'POST':
         xmldata = request.data
         xml_rec = et.fromstring(xmldata)

         ToUserName = xml_rec.find('ToUserName').text
         fromUser = xml_rec.find('FromUserName').text
         MsgType = xml_rec.find('MsgType').text
         MsgId = xml_rec.find('MsgId').text
         
         if MsgType == "text":
            Content =xml_rec.find('Content').text
            openl = re.search("开",Content)             
            close = re.search("关",Content)


            if openl != None:
               requests.get(url="http://led.flyerbirdy.com:9088/on")
               return "success"
            
            elif close != None:
               requests.get(url="http://led.flyerbirdy.com:9088/off")
               return "success"
            
            else:
               text_str = '''<xml>
               <ToUserName><![CDATA[%s]]></ToUserName>
	           <FromUserName><![CDATA[%s]]></FromUserName>
               <CreateTime>%d</CreateTime>
               <MsgType><![CDATA[%s]]></MsgType>
               <Content><![CDATA[%s]]></Content>
               </xml>'''
               Content = tulin(Content)
               return text_str % (fromUser, ToUserName, int(time()),MsgType,Content)  






         if MsgType == "voice":
            Recognition = xml_rec.find('Recognition').text
            openl = re.search("开",Recognition)
            close = re.search("关",Recognition)


            if openl !=None:
               requests.get(url="http://led.flyerbirdy.com:9088")
               return "success"
         
            elif close !=None:
               requests.get(url="http://led.flyerbirdy.com:9088/close")
               return "success"
            else:
               text_str = '''<xml>
               <ToUserName><![CDATA[%s]]></ToUserName>
               <FromUserName><![CDATA[%s]]></FromUserName>
               <CreateTime>%d</CreateTime>
               <MsgType><![CDATA[text]]></MsgType>
               <Content><![CDATA[%s]]></Content>
               </xml>'''
               #with open('/home/work/test.txt', 'w') as f:
               #     f.write(Recognition)
               #Recognition = tulin(Recognition)
               #Recognition = "语音识别结果是" + Recognition                
               return text_str % (fromUser, ToUserName, int(time()),Recognition)  




  # return "success"

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=80)
