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