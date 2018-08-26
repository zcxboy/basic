# -*- coding: UTF-8 -*-
import psutil
import os


#根据进程名获取进程pid，如果没有该进程，则返回None
def processinfo(processName):
    #返回全部进程的list
    pids = psutil.pids()
    for pid in pids:
        p = psutil.Process(pid)
        if p.name() == processName:
            return pid

#使用os.popen是非阻塞的，os.system会阻塞在该行
os.popen("notepad.exe")        
p=processinfo("notepad.exe")
print(p)

