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

import tkinter as tk
import time
root = tk.Tk()
root.wm_attributes('-topmost', 1)  # 锁定窗口置顶
root.title('毕业倒计时')
root.minsize(233, 90)
root.wm_attributes('-alpha', 0.8)
Label1=tk.Label(text='开始倒计时')
Label1.pack()

grad = time.mktime(time.strptime('Jun 30 2021',"%b %d %Y"))
start = time.mktime(time.strptime('Sep 01 2016',"%b %d %Y"))
global stamp, play, study, flag
play = 0.0
study = 0.0
flag = 0
stamp = time.time()

def trickit():
    ticks = time.time()
    delta = grad - ticks
    delta_start = ticks - start
    delta_stamp = ticks - stamp
    
    if flag == 0:
        delta_study = 0
        delta_play = 0
    elif flag == 1:
        delta_play = play + ticks - stamp
        delta_study = study
    elif flag == 2:
        delta_play = play
        delta_study = study + ticks - stamp
    
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
    
    #days_stamp = int(delta_stamp/86400)
    #day_sec_stamp = delta_stamp%86400
    hours_stamp = int(delta_stamp/3600)
    hour_sec_stamp = delta_stamp%3600
    mins_stamp = int(hour_sec_stamp/60)
    secs_stamp = hour_sec_stamp%60
    sub_secs_stamp = (delta_stamp*10+0.5)%10
    
    hours_play = int(delta_play/3600)
    hour_sec_play = delta_play%3600
    mins_play = int(hour_sec_play/60)
    secs_play = hour_sec_play%60
    sub_secs_play = (delta_play*10+0.5)%10
    
    hours_study = int(delta_study/3600)
    hour_sec_study = delta_study%3600
    mins_study = int(hour_sec_study/60)
    secs_study = hour_sec_study%60
    sub_secs_study = (delta_study*10+0.5)%10
    
    #currentTime = '\n您已入学%.1f秒\n亦即：%04d天 %02d时 %02d分 %02d秒 %01d\n\n距离毕业还有%.1f秒\n亦即：%04d天 %02d时 %02d分 %02d秒 %01d\n\n革命尚未成功，同志仍需努力！\n' %(delta_start,days_start,hours_start,mins_start,secs_start,sub_secs_start, delta,days,hours,mins,secs,sub_secs)
    
    currentTime = '''距离毕业还有 %03d天 %02d时 %02d分 %02d.%d秒
您已学习  %03d时 %02d分 %02d.%d秒
您已休息  %03d时 %02d分 %02d.%d秒''' %(days,hours,mins,secs,sub_secs, hours_study,mins_study,secs_study,sub_secs_study, hours_play,mins_play,secs_play,sub_secs_play)
    #widget = root.focus_get()
    
    Label1.config(text=currentTime)
    root.update()
    Label1.after(100, trickit)
    
Label1.after(100, trickit)

#触发功能即按下按钮后想要程序做什么
def start_play():
    global stamp, study, flag
    if flag == 2:
        study = study + time.time() - stamp
        with open("./工作记录.txt", 'a') as f:
            print('学习时间自 %s 至 %s 共计 %f 秒' %(time.asctime(time.localtime(stamp)), time.asctime(time.localtime(time.time())), time.time() - stamp), file=f)
        stamp = time.time()
    elif flag == 1:
        pass
    else:
        stamp = time.time()
    flag = 1

def start_study():
    global stamp, play, flag
    if flag == 1:
        play = play + time.time() - stamp
        with open("./休息记录.txt", 'a') as f:
            print('休息时间自 %s 至 %s 共计 %f 秒' %(time.asctime(time.localtime(stamp)), time.asctime(time.localtime(time.time())), time.time() - stamp), file=f)
        stamp = time.time()
    elif flag == 2:
        pass
    else:
        stamp = time.time()
    flag = 2
    

#按钮1及其功能
B = tk.Button(root, text ="休息一会", command=start_play)
B.pack(side='left')

C = tk.Button(root, text ="开始学习", command=start_study)
C.pack(side='right')
root.mainloop()
