# coding=utf-8
import time
import itchat
import os

def test_reply():
    @itchat.msg_register(['Text'])
    def get_pic(msg):
	if msg['Text']=="ok": 
            itchat.send(u'ok', msg['FromUserName'])
    itchat.run()

if __name__ == '__main__':
    itchat.auto_login(enableCmdQR = True)
    itchat.userInfo()
    test_reply()
