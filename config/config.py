# -*- coding: utf-8 -*-
import os,re
from tools.loggers import JFMlogging
logger = JFMlogging().getloger()

pck_name="com.immomo.momo"
activity="com.immomo.momo.android.activity.WelcomeActivity"

def get_connect_android_deviceid():  #获取设备uuid
   p = os.popen('adb devices')
   outstr = p.read()
   connectdeviceid = re.findall(r'(\w+)\s+device\s', outstr)
   if 0 == len(connectdeviceid):
      logger.info(u'没有adb连接的设备')
      exit()
   else:
      return connectdeviceid
device_name=get_connect_android_deviceid()[0]

wait_timeout = 15
click_post_delay = 0.5
lanuch_time = 3
#bundle_id = "com..iphone"
#ios_device_name=""
current_path = os.path.abspath(os.path.dirname(__file__))
screenshot_folder = os.path.join(current_path,"screenshot")
if not os.path.exists(screenshot_folder):
   os.mkdir(screenshot_folder)
   print ("创建截图目录:{}".format(screenshot_folder))
