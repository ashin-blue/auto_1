#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author  : ywp
@Time    : 201/9/4 18:34
@describe: 创建driver
"""
import os,sys,subprocess,pytest,time,allure
import base64,atx
import uiautomator2 as u2
from android.module import base
from driver import Driver
from config.config import *
sys.path.append('..')
from tools.loggers import JFMlogging
logger = JFMlogging().getloger()

# 当设置autouse为True时,
# 在一个session内的所有的test都会自动调用这个fixture
d = u2.connect()
@pytest.fixture()
def driver_setup():
    #前置
    logger.info("自动化测试开始!")
    driver = Driver().init_driver(device_name)
    logger.info("driver初始化")
    driver.app_start(pck_name,activity, stop=True)
    time.sleep(lanuch_time)
    yield
    #后置
    logger.info("自动化测试结束!")
    driver.app_stop(pck_name)


def lock():  # 手机屏幕解
    time.sleep(1)
    screen = d.info
    if screen["screenOn"] == False:  # 屏幕状态
        logger.info("灭屏状态")
        d.screen_on()  # 唤醒屏幕
        base.swipeUp()
        logger.info("解锁手机")
    elif screen["screenOn"] == True:  # 屏幕状态
        logger.info("亮屏状态")



@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    '''
    hook pytest失败
    :param item:
    :param call:
    :return:
    '''
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    # we only look at actual failing test calls, not setup/teardown
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("failures") else "w"
        with open("failures", mode) as f:
            # let's also access a fixture for the fun of it
            if "tmpdir" in item.fixturenames:
                extra = " (%s)" % item.funcargs["tmpdir"]
            else:
                extra = ""
            f.write(rep.nodeid + extra + "\n")
        pic_info = adb_screen_shot()
        with allure.step('添加失败截图...'):
            allure.attach("失败截图", pic_info, allure.attach_type.JPG)



def allow(driver):
    driver.watcher("允许").when(text="允许").click(text="允许")
    driver.watcher("跳过 >").when(text="跳过 >").click(text="跳过 >")
    driver.watcher("不要啦").when(text="不要啦").click(text="不要啦")


def screen_shot(driver):
    '''
    截图操作
    pic_name:截图名称
    :return:
    '''
    try:
        fail_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        fail_pic = str(fail_time) + "截图"
        pic_name = os.path.join(screenshot_folder, fail_pic)
        driver.screenshot("{}.jpg".format(pic_name))
        logger.info('截图:{}'.format(pic_name))
        f = open(pic_name, 'rb')  # 二进制方式打开图文件
        base64_str = base64.b64encode(f.read())  # 读取文件内容，转换为base64编码
        f.close()
        return base64_str
    except Exception as e:
        logger.info("{}截图失败!{}".format(pic_name, e))


def adb_screen_shot():
    '''
    adb截图
    :return:
    '''
    file_info = ''
    fail_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    fail_pic = str(fail_time) + "截图.jpg"
    pic_name = os.path.join(screenshot_folder, fail_pic)
    cmd = 'adb shell /system/bin/screencap -p /sdcard/screenshot.jpg'
    subprocess.call(cmd,shell=True)
    cmd = 'adb pull /sdcard/screenshot.jpg {}'.format(pic_name)
    subprocess.call(cmd, shell=True)
    with open(pic_name, 'rb') as r:
        file_info = r.read()
    return file_info


# 当设置autouse为True时,
# 在一个session内的所有的test都会自动调用这个fixture
# @pytest.fixture(autouse=True)
# def ios_driver_setup(request):
#     logger.info("ios自动化测试开始!")
#     request.instance.driver = Driver().init_ios_driver(ios_device_name)
#     logger.info("driver初始化")
#     ios_allow(request.instance.driver)
#     def driver_teardown():
#         logger.info("ios自动化测试结束!")
#         request.instance.driver.stop_app()
#     request.addfinalizer(driver_teardown)


def ios_allow(driver):
    elem = driver(name="允许")
    if elem.exists:
       elem.click()
    if elem.exists:
       elem.click()
    elem = driver(xpath='//XCUIElementTypeButton[@name="upgradeClose"]')
    if elem.exists:
        elem.click()
        logger.info("关闭升级")
