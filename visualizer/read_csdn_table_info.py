# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
Created on Tue Sep 04 20:36:33 2018

@author: lenovo
"""

# coding=utf-8
import pymysql

def get_table_info(table_name,column,local):
    # 连接本地已有的数据库
    if(local == True):
        db = pymysql.connect("localhost", "root", "你的密码！", 'csdn' ,charset="utf8")
    elif(local == False):
        db = pymysql.connect("你的远程服务器IP地址！", "root", "你的密码！", 'csdn' ,charset="utf8")
	# 获取cursor光标
    cursor = db.cursor()

    # 在已有的数据库csdn中创建一个blogs表格，表头为id，title,page_view 数据类型都是int
    # 构建创建表格的sql语句
#    table_name = '\''+table_name+'\''
    sql_info = 'select %s from %s order by blog_id'%(column,table_name)
    
#    # 执行sql语句
    try:
        cursor.execute(sql_info)
        # 提交到数据库执行
        db.commit()
        data = cursor.fetchall()
        
        print 'this request is sucessful!'
    except Exception, e:
        # 如果发生错误则回滚
        db.rollback()
        print e
        print 'failed!'

    # 关闭数据库连接
    db.close()
    
    
    tem = []
    try:
        for d in data:
            tem.append("".join(d).encode("utf-8"))
#            print d
#            print ''.join(d)
    except Exception , e:
        for d in data:
#            print "d"
#            print d
#            print str(list(d))[1:-1]
            tem.append(str(list(d))[1:-1])
        
    return tem

if __name__ == '__main__':
    table_name = 'table_1'
    column = 'create_time'
    data = get_table_info(table_name,column,local = False)
    for d in data:
        print d    
        print type(d)
    #列表和元祖转成字符串，必须要用join函数~
#    print ''.join(d)
    
    
    
    