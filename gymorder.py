# -*- coding:utf8 -*-
"""
程序在当晚12点前启动,第二天早晨预约2天后的场地
2015-12-23 18:38:05
xuchen
"""
import ssl
import urllib2
import urllib
import cookielib
import gzip
from PIL import Image
from StringIO import StringIO
import zlib
import os
import datetime
import time
import thread

import PicProcess

DATEFORMAT_Ymd = '%Y-%m-%d'
DATEFORMAT_YmdHMS = '%Y-%m-%d %H:%M:%S'


# ssl._create_default_https_context = ssl._create_unverified_context


class OrderRobot:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
            # 'Origin': 'http://ids2.seu.edu.cn',
            # 'Referer': 'http://ids2.seu.edu.cn/amserver/UI/Login',
            # 'Host' : 'ids2.seu.edu.cn'
        }
        self.orderheaders = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
            'Origin': 'http://yuyue.seu.edu.cn',
            'Host' : 'yuyue.seu.edu.cn'
        }

        self.loginUrl = 'http://ids1.seu.edu.cn/amserver/UI/Login'
        self.postOrderUrl = 'http://yuyue.seu.edu.cn/eduplus/order/order/order/insertOredr.do?sclId=1'
        self.validateimageUrl = 'http://yuyue.seu.edu.cn/eduplus/control/validateimage'
        today = datetime.date.today()
        self.orderday = today + datetime.timedelta(days=3)    #预约第四天的场地

        self.time = {'1' : '09:00-10:00', '2' : '10:00-11:00', '3' : '11:00-12:00', '4' : ' 18:00-19:00', '5' : ' 19:00-20:00', '6' : ' 20:00-21:00','7': '11:30-12:30', '8':'12:30-13:30'}
        self.t = raw_input('starttime:\n 1---09:00-10:00;\n2---10:00-11:00;\n3---11:00-12:00;\n4---18:00-19:00;\n5---19:00-20:00;\n6---20:00-21:00\n7---11:30-12:30;\n8---12:30-13:30;\n>')
        self.starttime = self.time[self.t]
        self.loginPostdata = urllib.urlencode({
            'IDToken1': '用户名',
            'IDToken2': '密码',
            'IDButton': 'Submit',
            'goto': 'http://yuyue.seu.edu.cn/eduplus/order/initOrderIndex.do?sclId=1',
            'gx_charset': 'utf-8'
        })
        self.friendId = '75496'
        self.islogin = False

        self.cookie = cookielib.CookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookie))
        urllib2.install_opener(self.opener)

    def login(self):

        req = urllib2.Request(
            url=self.loginUrl,
            data=self.loginPostdata,
            headers=self.headers
        )

        result = self.opener.open(req).read()
        if '你的名字' in result:
            self.islogin = True
            print 'login successfuly!'
            return self.islogin
        else:
            self.login()

    def orderBadminton(self):
        validateResult = self.opener.open(self.validateimageUrl)
        validateNum = PicProcess.getResutlFromStr(validateResult.read())
        print 'varify number is: %s' % validateNum
        print 'order time is: %s' % self.orderday.strftime(DATEFORMAT_Ymd) + self.starttime
        orderPostdata = urllib.urlencode({
            'orderVO.useTime': self.orderday.strftime(DATEFORMAT_Ymd) + self.starttime,
            'orderVO.itemId': '10',
            'orderVO.useMode': '2',
            'useUserIds': '你朋友的ID',    #需要抓包看一下
            'orderVO.phone': '你的手机号',
            'orderVO.remark': '',
            'validateCode': validateNum
        })
        self.orderheaders['Referer'] = 'http://yuyue.seu.edu.cn/eduplus/order/order/initEditOrder.do?sclId=1&dayInfo=' + str(self.orderday) + '&itemId=10&time=' + str(self.time)
        req = urllib2.Request(
            url=self.postOrderUrl,
            data=orderPostdata,
            headers=self.orderheaders
        )
        result = self.opener.open(req)
        return result.read()


now = datetime.datetime.now()

nextDay = now + datetime.timedelta(days=1)
# 登陆时间 8:00:00s
loginTime = datetime.datetime(nextDay.year, nextDay.month, nextDay.day, 8, 0, 0)
# 登出时间 8:04:00s
exitTime = datetime.datetime(nextDay.year, nextDay.month, nextDay.day, 8, 4, 0)


if __name__ == '__main__':
    myOrderRobot = OrderRobot()
    now = datetime.datetime.now()
    time.sleep(1)
    print "Login Time: %s Now: %s Target Time: %s" % (loginTime, now, myOrderRobot.orderday)
    result = ''

    if myOrderRobot.login():
        result = myOrderRobot.orderBadminton()
    if 'success' in result :
        print 'order successfully!!!'



