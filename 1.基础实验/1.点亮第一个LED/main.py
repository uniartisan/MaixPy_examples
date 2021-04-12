'''
实验名称：点亮LED_B蓝灯
版本：v1.0
日期：2021.4
作者：CYH
实验目的：学习led点亮。
'''

import sensor, image, lcd, time
import KPU as kpu
import gc, sys
from Maix import GPIO
from fpioa_manager import fm


#将蓝灯引脚IO12配置到GPIO0，K210引脚支持任意配置
fm.register(12, fm.fpioa.GPIO0)

LED_B = GPIO(GPIO.GPIO0, GPIO.OUT) #构建LED对象
LED_B.value(0) #点亮LED
