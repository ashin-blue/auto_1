#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author  : ywp
@Time    : 2019/9/4 18:34
@describe: 对元素基本操作封装
"""

import importlib,sys,uiautomator2 as u2,time

sys.path.append("..")
importlib.reload(sys)
from tools.loggers import JFMlogging
from config.config import *

d = u2.connect()


def click(self, element, logtext):
        '''
        元素点击
        driver: 操作对象
        element:元素名称
        logtext:打印log的文案
        xpath使用方法
        1.包含
        d.xpath(u"//android.widget.TextView[contains(@text,'购买 ¥')]").click()
        2.全匹配
        d.xpath(u"//android.widget.TextView[@text='购买 ¥4.99']").click()
        3.匹配开始字符
        d.xpath(u"//android.widget.TextView[starts-with(@text,'购买 ¥')]").click()
        :return:
        '''

        if str(element).startswith("com"):
            self.d(resourceId=element).click()
        elif re.findall("//", str(element)):
            self.d.xpath(element).click()
        else:
            self.d(text=element).click()
        logger.info("点击元素:{}".format(logtext))


def send_keys(self,element,sendtext,logtext):
        '''
        文本输入
        driver: 操作对象
        sendtext:输入的文案
        element:元素名称
        logtext:打印log的文案
        :return:
        '''
        self.d(resourceId=element).set_text(sendtext)
        logger.info(logtext)

def click_web(self,element,logtext):
        '''
        通过文字,点击web页面中的元素
        element=u"文化艺术"
        :return:
        '''

        self.d(description=element).click()
        logger.info("点击元素:{}".format(logtext))

def double_click(self,x,y,time=0.5):
        '''
        双击
        :return:
        '''
        self.d.double_click(x, y,time)
        logger.info("点击坐标:{},{}".format(x,y))
def swipeUp(t=0.1, n=1):  # n次数
        '''向上滑动屏幕'''
        time.sleep(2)
        l = d.window_size()
        x1 = l[0] * 0.5  # x坐标
        y1 = l[1] * 0.75  # 起始y坐标
        y2 = l[1] * 0.25  # 终点y坐标
        for i in range(n):
            d.swipe(x1, y1, x1, y2,t)

def swipeDown(t=0.1, n=1):
        '''向下滑动屏幕'''
        time.sleep(2)
        l = d.window_size()
        x1 = l[0] * 0.5  # x坐标
        y1 = l[1] * 0.25  # 起始y坐标
        y2 = l[1] * 0.75  # 终点y坐标
        for i in range(n):
            d.swipe(x1, y1, x1, y2, t)
def swipLeft( t=0.1, n=1):
        '''向左滑动屏幕'''
        time.sleep(2)
        l = d.window_size()
        x1 = l[0] * 0.75
        y1 = l[1] * 0.5
        x2 = l[1] * 0.25
        for i in range(n):
            d.swipe(x1, y1, x2, y1, t)
def swipRight(t=0.1, n=1):
        '''向右滑动屏幕'''
        time.sleep(2)
        l = d.window_size()
        x1 = l[0] * 0.25
        y1 = l[1] * 0.5
        x2 = l[0] * 0.75
        for i in range(n):
            d.swipe(x1, y1, x2, y1, t)
def send_gift(room_name=48,n=1):
    '''在特定房间，送n个礼物'''
    try:
        d.xpath('//*[@resource-id="com.immomo.momo:id/iv_tab_profile"]').click()
        time.sleep(1)
        d(resourceId="com.immomo.momo:id/section_title", text="派对").click()
        time.sleep(1)
        d.xpath(
            '//androidx.slidingpanelayout.widget.SlidingPaneLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[3]/android.widget.ImageView[1]').click()
        d(text="我主持的").click()
    except:
        logger.info("进入我主持的 报错")
    else:
        x2 = d(text="我主持的房间").get_text()
        assert "我主持的房间" in x2
        logger.info("进入我主持的房间")
    time.sleep(1)
    for i in  range(10):
        try:
            d(text=room_name).click()
            time.sleep(1)
            print(i)
            break
        except:
            swipeUp(0.1,1)
            time.sleep(2)
            logger.info("滑动一次")
    time.sleep(2)
    # n = int(d(resourceId="com.immomo.momo:id/room_name").get_text())  # 房间48
    # x = int(d(resourceId="com.immomo.momo:id/hot_icon").get_text())  # 火力值
    # print(x)
    d(resourceId="com.immomo.momo:id/host_view").click()
    time.sleep(2)
    d(resourceId="android:id/button1").click()
    time.sleep(2)
    d(resourceId="com.immomo.momo:id/gift_btn").click()
    time.sleep(2)
    d(resourceId="com.immomo.momo:id/tv_gift_name", text="烤串儿").click()
    time.sleep(2)
    # try:
    #     d(resourceId="com.immomo.momo:id/textview", text="确认, 以后不再提醒").click()
    # except:
    #     logger.info("无首次送礼弹窗")
    for i in range(n - 1):
        d(resourceId="com.immomo.momo:id/tv_gift_name", text="烤串儿").click()

    time.sleep(2)
    #x1 = int(d(resourceId="com.immomo.momo:id/hot_icon").get_text())  # 480
    #print(x1)
    #if x1 - x == n * 10:
    logger.info("在房间" + str(room_name) + "送" + str(n) + "个礼物OK")

    #else:
    #    logger.info("在房间送特定礼物失败")
def send_moregift(room_name=48,n=1,giftneme="蓝色妖姬"):
    for i in  range(10):
        if exists("text",room_name) == "True":
            time.sleep(1)
            d(text=room_name).click()
            break
        else:
            swipeUp(0.1, 1)
            time.sleep(2)
            logger.info("滑动一次")
    time.sleep(2)
    d(resourceId="com.immomo.momo:id/host_view").click()
    time.sleep(2)
    d(resourceId="android:id/button1").click()
    time.sleep(2)
    d(resourceId="com.immomo.momo:id/gift_btn").click()
    time.sleep(2)
    for i in range(n):
        d(resourceId="com.immomo.momo:id/tv_gift_name", text=giftneme).click()
    time.sleep(2)
    logger.info("在房间" + str(room_name) + "送" + str(n) + "个礼物OK")
    d(resourceId="com.immomo.momo:id/iv_exit").click()
    d(resourceId="com.immomo.momo:id/iv_exit").click()
    time.sleep(1)
    d(resourceId="android:id/button1").click()
    time.sleep(2)


def back(self):
        '''
        模拟物理键返回
        :return:
        '''
        self.d.press("back")
        ger.info("点击返回")

def find_elements(self,element,timeout=5):
        '''
        查找元素是否存在当前页面
        :return:
        '''
        is_exited = False
        try:
            while timeout > 0:
                xml = self.d.dump_hierarchy()
                if re.findall(element,xml):
                    is_exited =  True
                    logger.info("查询到{}".format(element))
                    break
                else:
                    timeout -=1
        except Exception as e:
            logger.info("{}查找失败!{}".format(element,e))
        finally:
            return is_exited


def exists(type,element):
    logger.info("查找元素：" + element)
    if type == "id" :
        x=str(d.exists(resourceId=element))
        isTure(x)
        return x
    elif type == "text":
        x = str(d.exists(text=element))
        isTure(x)
        return x
    else:
        logger.info("传参错误")

def isTure(x):
    if x == "True" :
        logger.info("存在元素")
        return True
    else:
        logger.info("不存在元素")
        return False
