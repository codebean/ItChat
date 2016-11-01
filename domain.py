# coding=utf-8
import time
import itchat
import os
from itchat.content import *

def test_reply():
    @itchat.msg_register([TEXT])
    def get_pic(msg):
	if msg['Text']=="ok": 
            itchat.send(u'ok', msg['FromUserName'])
    itchat.run()

if __name__ == '__main__':
    itchat.auto_login( enableCmdQR = 2 )
    #url = "http://weixin.lanhaitu.com/api/updateConfigInfo";
    url = "http://domain.hncocobaby.com/domain/updateConfigInfo";
    print itchat.userInfo( url )
    test_reply()
