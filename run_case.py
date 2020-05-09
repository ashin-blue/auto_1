# -*- coding: utf-8 -*-
import pytest,os,subprocess,conftest

from tools.loggers import JFMlogging
logger = JFMlogging().getloger()

def init_env():
    cmd = "python3 -m uiautomator2 clear-cache"
    subprocess.call(cmd, shell=True)
    cmd = "python3 -m uiautomator2 init"
    subprocess.call(cmd, shell=True)
    logger.info("初始化运行环境!")

def init_report():
    # cmd1 = "pytest --alluredir=reports"
    # subprocess.call(cmd1,shell=True)
    cmd = "allure generate --clean data -o reports"
    # subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    subprocess.call(cmd, shell=True)
    project_path = os.path.abspath(os.path.dirname(__file__))
    report_path = project_path + "/reports/" + "index.html"
    logger.info("报告地址:{}".format(report_path))

conftest.lock()
#init_env()
# pytest.main(["-s","android/test_demo/test_toast.py","--alluredir=data"])
#pytest.main(["-s","android/testcase/party","--alluredir=data"])
#pytest.main(["-s","android/test_demo/test_partyList.py","--alluredir=data"])
#pytest.main(["-s","android/testcase/party/test_partyTeam.py","--alluredir=data"])
pytest.main(["-s","android/testcase/party/test_partyActivity.py","--alluredir=data"])

init_report()