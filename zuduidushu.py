# coding=utf-8
import time
import itchat
import os
import requests
import urllib

def zuduidushu_reply():
    @itchat.msg_register
    def default_reply(msg):
        # itchat.send_image('@img@test.gif', msg['RecommendInfo']['UserName']);
        # return '@img@test.gif';
        pass

    @itchat.msg_register('Friends')
    def add_friend(msg):
        itchat.add_friend(**msg['Text']);
        itchat.get_contract();
        itchat.send(u'我是小书童，终于等到愿意改变的你，从今天开始你就是我的主人了，有什么吩咐尽快说！', msg['RecommendInfo']['UserName']);
        time.sleep(5);
        itchat.send(u'主人，为了能陪你完成读书的计划，偶们需要完成一个小任务获得共读的资格和电子书资源。将小的发的图片分享到朋友圈然后截图发给小的。然后我们就可以一起去群里完成每日的读书计划，群内每天都有小的发的领读。小的一直会伴你读书，陪你成长！', msg['RecommendInfo']['UserName']);
        # itchat.send_image('@img@test.gif' ,  msg['RecommendInfo']['UserName']);
        return '@img@test.gif';

    itchat.run()


if __name__ == '__main__':
    itchat.auto_login(  )
    zuduidushu_reply()