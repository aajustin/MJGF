# -*- encoding=utf8 -*-
__author__ = "Justin"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
auto_setup(__file__)


poco("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View")[1].child("android.view.View")[1].offspring("android.widget.ScrollView").child("android.view.View").child("android.view.View")[0].offspring("android.widget.TextView").click()
