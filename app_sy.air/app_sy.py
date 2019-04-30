# -*- coding: utf-8 -*-
__author__ = "Justin"
import sys
from airtest.core.api import *
import os
from time import sleep
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
#from Method import method
#sys.path.append('../Method')
sys.path.append('G:\\AirtestIDE_2019-01-15_py3_win64\\MultiDeviceRunner\\Method')
import method
auto_setup(__file__)


method.install()
method.start()
sleep(10)

#判断是否存在立即更新按钮
if poco(text = "立即更新").exists():	
	method.update()
	method.login()
else:
	method.login()

method.Cash_register()
method.Value_meals()

log("Test OK")

sleep(2)
method.stop()

