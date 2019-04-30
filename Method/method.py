# -*- coding: utf-8 -*-
__author__ = "Justin"

from airtest.core.api import *
import os, sys
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
from poco.exceptions import InvalidOperationException
auto_setup(__file__)
from parameters import *



PWD = os.path.dirname(__file__)
PKG = "com.mjgf"
APK = os.path.join(PWD, "com.mjgf.apk")

def install():
	'''安装'''
	if PKG not in device().list_app():
		install(APK)
	stop_app(PKG)
	

def start():
	'''启动'''
	wake()
	start_app(PKG)

def stop():
	'''停止'''
	clear_app(PKG)
	stop_app(PKG)


def update():
	'''热更新'''
	touch(Template(r"tpl1554091195296.png", record_pos=(0.201, 0.486), resolution=(1080, 2160)))
	sleep(15)
	touch(Template(r"tpl1554095137138.png", record_pos=(0.031, 0.106), resolution=(1080, 2160)))
	print("立即更新成功")	

def login():
	'''登陆'''
	touch(Template(r"tpl1554089967597.png", record_pos=(-0.009, -0.199), resolution=(1080, 2160)))
	text(username)
	touch(Template(r"tpl1554090044149.png", record_pos=(-0.003, -0.002), resolution=(1080, 2160)))
	text(password)
	touch(Template(r"tpl1554090077238.png", record_pos=(-0.011, 0.599), resolution=(1080, 2160)))
	touch(Template(r"tpl1554090106054.png", record_pos=(-0.177, -0.733), resolution=(1080, 2160)))
	text(store)
	touch(Template(r"tpl1554090159594.png", record_pos=(0.377, -0.727), resolution=(1080, 2160)))
	touch(Template(r"tpl1554777586117.png", record_pos=(0.383, -0.497), resolution=(1080, 2160)))
	touch(Template(r"tpl1554090184268.png", record_pos=(0.01, 0.733), resolution=(1080, 2160)))

def Cash_register():
	'''收银'''
	touch(Template(r"tpl1554863022418.png", record_pos=(-0.153, -0.463), resolution=(720, 1280)))

def Value_meals():
	'''超值套餐'''
	touch(Template(r"tpl1554863311984.png", record_pos=(-0.379, 0.018), resolution=(720, 1280)))

	sleep(10)
	if poco(text = "测试卡项3（升卡测试专用，请勿购买）").exists():
		touch(Template(r"tpl1554866707427.png", record_pos=(0.361, -0.356), resolution=(720, 1280)))
		sleep(3)
		touch(Template(r"tpl1554863277645.png", record_pos=(-0.254, 0.085), resolution=(720, 1280)))
		sleep(5)
		#assert_exists(Template(r"tpl1554863348952.png", record_pos=(-0.161, -0.554), resolution=(720, 1280)), "溜了溜了")
		touch(Template(r"tpl1554874266050.png", record_pos=(0.014, 0.762), resolution=(720, 1280)))
		sleep(3)
		#assert_exists(Template(r"tpl1554863559901.png", record_pos=(-0.289, -0.065), resolution=(720, 1280)), "微信支付")
	else:
		print("没有找到相关套餐")

def ItemCard():
	'''卡项'''
	touch(Template(r"tpl1554878718412.png", record_pos=(-0.369, 0.161), resolution=(720, 1280)))
	sleep(3)
	touch(Template(r"tpl1554878726693.png", record_pos=(-0.376, -0.165), resolution=(720, 1280)))
	sleep(3)
	if poco(text="测试卡项2（升卡测试专用，请勿购买）").exists():
		touch(Template(r"tpl1554878838831.png", record_pos=(0.374, 0.567), resolution=(720, 1280)))
		sleep(3)
		touch(Template(r"tpl1554878869536.png", record_pos=(-0.078, 0.096), resolution=(720, 1280)))
		sleep(3)
		touch(Template(r"tpl1554878947731.png", record_pos=(0.003, 0.762), resolution=(720, 1280)))
		sleep(3)
	else:
		print("没有找到相关卡项")

def ItemCard2():#卡项(代码+截图)
	#poco(text="收银").click()
	'''
	touch(Template(r"tpl1554878718412.png", record_pos=(-0.369, 0.161), resolution=(720, 1280)))
	sleep(7)
	poco(text="品项").click()
	sleep(3)
	'''
	poco(text="基础管理").click()
	sleep(10)
	#items = poco("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup")[1].child("android.view.ViewGroup")[1].offspring("android.widget.ScrollView").child("android.view.ViewGroup").child("android.view.ViewGroup")[0].offspring("android.widget.TextView")
	#print(items)
	try:
		poco("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View")[1].child("android.view.View")[1].offspring("android.widget.ScrollView").child("android.view.View").child("android.view.View")[0].offspring("android.widget.TextView").click()
	except InvalidOperationException:
		print('fuck')
	#print(actual_value)

	#print(a.get_text())
	'''
	first_one = items[0]
	print(first_one.get_text())
	if poco(text="测试卡项").exists():
		#touch(Template(r"tpl1554878838831.png", record_pos=(0.374, 0.567), resolution=(720, 1280)))
		first_one.click()
		sleep(3)
		poco(text="溜了溜了").click()
		sleep(3)
		poco(text="去收款").click()
		sleep(3)
	'''

	#for item in poco("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup")[1].child("android.view.ViewGroup")[1].offspring("android.widget.ScrollView").child("android.view.ViewGroup"):
	#	print(item)
