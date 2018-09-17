# -*- coding: utf-8 -*-
"""
Created on Mon Sep 03 20:18:56 2018

@author: lenovo
"""
#从spider文件夹导入这些模块
#需要去notouch_spider.py文件中修改你的账号，以及在涉及到MySQL的文件中，改你的数据库信息
#在这个文件，需要修改你的最大页面数字last_page
from spider import set_class, set_insert2mysql, log_id, plot_time_total_views
import os
import time

localDir=os.path.dirname(__file__)
path = localDir + "/id.txt"

try:
    id = log_id.read_id(path)
    print "读取上次获取数据ID：%d"%id
    print "继续获取数据..."
    
except Exception,e:
    id = 1
    print "从现在开始获取数据"
    
    

while(1):
    blog_set = set_class.Blog_set(id = id,now_page=1,last_page=2)
    set_insert2mysql.set_main(blog_set.id,blog_set.get_time,blog_set.blogs_num,blog_set.total_views)
    log_id.write_id(id,path)
    
    plot_time_total_views.drawBydata()
    #睡眠一分钟！
    time.sleep(18)
    id += 1
    
    '''
    (1064, u"You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 
    '\\\\xE6\\\\x88\\\\x91\\\\xE6\u7684\u95ee\u9898',47,'2018-09-01 21:10:37')' at line 1")
    '''