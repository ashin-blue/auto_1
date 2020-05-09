# -*- coding: utf-8 -*-
"""
@Author  : ywp
@Time    : 2019/9/4 18:34
@describe: 测试进入派对
"""
import time
from android.module import base
from config.config import *
import uiautomator2 as u2
from tools.loggers import JFMlogging
logger = JFMlogging().getloger()
d = u2.connect()  # connect to device

@allure.feature("测试派对")
@pytest.mark.usefixtures('driver_setup')
class TestPartyList:
    def setup(self):
        try:
            d.xpath('//*[@resource-id="com.immomo.momo:id/iv_tab_profile"]').click()
            time.sleep(1)
            d(resourceId="com.immomo.momo:id/section_title", text="派对").click()
        except:
            logger.info("没有派对入口")
        else:
            logger.info("进入派对")

    def teardown(self):
        pass

    @allure.story('测试进入派对无异常')
    def test_1(self):
        try :
            d.xpath('//*[@resource-id="android:id/content"]/android.view.ViewGroup[1]/android.widget.ImageView[1]').click()
        except:
            logger.info("没有钻石任务")
            x=d(resourceId="com.immomo.momo:id/tab_title_lua", text="语音派对").get_text()
            assert "语音派对" in x
            logger.info("进入派对正常")
        else:
            x = d(resourceId="com.immomo.momo:id/tab_title_lua", text="语音派对").get_text()
            assert "语音派对" in x
            logger.info("进入派对正常")

    @allure.story('测试派对列表切换')
    def test_2(self):
        pass

    @allure.story('测试派对列表加载')
    def test_3(self):
        pass

    def test_4(self):
        pass
    def test_6(self):
        pass
    def test_7(self):
        pass
    def test_8(self):
        pass
    def test_9(self):
        pass

    def test_10(self):
        pass
    def test_11(self):
        pass
    def test_12(self):
        pass
    def test_13(self):
        pass
    def test_14(self):
        pass
    def test_15(self):
        pass