# -*- encoding=utf8 -*-
__author__ = "Justin"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
auto_setup(__file__)

swipe(Template(r"tpl1555299303693.png", record_pos=(0.007, 0.688), resolution=(1080.0, 2160.0)), vector=[-0.0524, -0.5155])

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
auto_setup(__file__)
#poco(text="收款").click()
poco("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup")[1].child("android.view.ViewGroup")[1].offspring("android.widget.ScrollView").child("android.view.ViewGroup").child("android.view.ViewGroup")[0].offspring("android.widget.TextView").click()





