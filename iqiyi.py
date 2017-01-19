# coding=utf-8
import time
import itchat
import os

def test_reply():
    @itchat.msg_register([TEXT])
    def get_pic(msg):
	if msg['Text']=="ok": 
            itchat.send(u'ok', msg['FromUserName'])
    
    @itchat.msg_register('Friends')
    def add_friend(msg):
        itchat.add_friend(**msg['Text'])
        itchat.get_contract()
        itchat.send(u'爱奇艺VIP 账号13539956455  密码fujoshi123\n\n爱奇艺VIP 账号13873248477  密码jiro201151\n\n爱奇艺VIP 账号15912592375  密码zxc521523\n\n爱奇艺VIP 账号18657196137  密码gmail.com\n\n爱奇艺VIP 账号18629016101  密码slh8023.\n\n爱奇艺VIP 账号18574303268  密码ting1314520\n\n爱奇艺VIP 账号18620300513  密码sammie123\n\n爱奇艺VIP 账号15008159500  密码jxm19880713\n\n爱奇艺VIP 账号18215523978  密码8298290\n\n爱奇艺VIP 账号15153768558  密码zhang523\n\n亲~这些都是我辛苦收集来的哦。不能登的。晚些收集后还会更新，多留意哦。', msg['RecommendInfo']['UserName'])

    itchat.run()

if __name__ == '__main__':
    itchat.auto_login(enableCmdQR = 2)
    itchat.userInfo()
    test_reply()