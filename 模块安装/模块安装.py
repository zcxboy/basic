# -*- coding: UTF-8 -*-
import os
import sys

#a="\""+ sys.prefix + "\python.exe\"" +" -m pip install  pymem -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host=mirrors.aliyun.com"
#a="\""+ sys.prefix + "\python.exe\"" +" -m pip install --upgrade pyinstaller -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host=mirrors.aliyun.com"
a="\""+ sys.prefix + "\python.exe\"" +" -m pip uninstall pymem"
#生成command命令,指定安装源为阿里云
print("command命令是："+ a)
os.system(a) #执行command

