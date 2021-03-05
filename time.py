# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 21:05:19 2019

@author: ftxun
"""

#import time
#import tkinter as tk
#
#grad = time.mktime(time.strptime('Jun 30 2021',"%b %d %Y"))
#
#while 1:
#    ticks = time.time()
#    delta = grad - ticks
#    days = int(delta/86400)
#    day_sec = delta%86400
#    hours = int(day_sec/3600)
#    hour_sec = day_sec%3600
#    mins = int(hour_sec/60)
#    secs = hour_sec%60
#    print('\r距离毕业还有 %03d天 %02d时 %02d分 %02d秒' %(days,hours,mins,secs),end='')
#    time.sleep(1)

import tkinter, time
root = tkinter.Tk()
root.wm_attributes('-topmost', 1)  # 锁定窗口置顶
root.title('毕业倒计时')
root.minsize(233, 10)
Label1=tkinter.Label(text='开始倒计时')
Label1.pack()

grad = time.mktime(time.strptime('Jun 30 2021',"%b %d %Y"))
start = time.mktime(time.strptime('Sep 01 2016',"%b %d %Y"))

def trickit():
    ticks = time.time()
    delta = grad - ticks
    delta_start = ticks - start
    days = int(delta/86400)
    day_sec = delta%86400
    hours = int(day_sec/3600)
    hour_sec = day_sec%3600
    mins = int(hour_sec/60)
    secs = hour_sec%60
    sub_secs = (delta*10+0.5)%10
    
    days_start = int(delta_start/86400)
    day_sec_start = delta_start%86400
    hours_start = int(day_sec_start/3600)
    hour_sec_start = day_sec_start%3600
    mins_start = int(hour_sec_start/60)
    secs_start = hour_sec_start%60
    sub_secs_start = (delta_start*10+0.5)%10
    
    #currentTime = '\n您已入学%.1f秒\n亦即：%04d天 %02d时 %02d分 %02d秒 %01d\n\n距离毕业还有%.1f秒\n亦即：%04d天 %02d时 %02d分 %02d秒 %01d\n\n革命尚未成功，同志仍需努力！\n' %(delta_start,days_start,hours_start,mins_start,secs_start,sub_secs_start, delta,days,hours,mins,secs,sub_secs)
    currentTime = '\n距离毕业还有 %03d天 %02d时 %02d分 %02d.%d秒\n\n革命尚未成功，同志仍需努力！\n' %(days,hours,mins,secs,sub_secs)
    Label1.config(text=currentTime)
    root.update()
    Label1.after(100, trickit)
    
Label1.after(100, trickit)

root.mainloop()
