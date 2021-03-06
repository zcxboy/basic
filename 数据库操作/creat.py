#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sqlite3
import time
import sys
import os

# 连接到SQLite数据库
# 数据库文件是test.db
# 如果文件不存在，会自动在当前目录创建:

os.chdir(os.path.dirname(__file__))
conn = sqlite3.connect('test.db')

# 创建一个Cursor:
cursor = conn.cursor()

cursor.execute('create table table1 (链接 varchar(30) primary key, 线报 varchar(30), 权限 varchar(20), 时间 varchar(20))')


# 提交事务:execute后数据已经进入了数据库,但是如果最后没有commit 的话已经进入数据库的数据会被清除掉，自动回滚
conn.commit()

# 关闭Cursor:
cursor.close()

# 关闭数据库
conn.close()
