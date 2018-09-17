# -*- coding: utf-8 -*-
"""
Created on Mon Sep 03 16:53:19 2018

@author: lenovo
"""
import pymysql

def create_table(id):
    db = pymysql.connect("localhost", "root", "你的密码！", "csdn",charset='utf8')
    # 获取cursor光标，固定操作
    cursor = db.cursor()

    tem = '(num int not null,blog_id int primary key not null,title tinytext not null,page_view int not null,create_time tinytext not null)'
    print tem
#这里的table_id不需要加反斜杠，但是插入表的时候必须要加！任何字符串都需要加上！不管中英文
    table_id = 'table_'+str(id)
    sql = 'create table if not exists %s %s'%(table_id, tem)
    try:

        cursor.execute(sql)
        print 'Sucessfully create table(%s)!'%table_id
    except Exception,e:
        print e
        print 'Fail to create table(%s)'%table_id
    
    
def blog_insert2mysql(id,num,blog_id,title,page_view,create_time):
    db = pymysql.connect("localhost", "root", "131452", "csdn",charset='utf8')
    # 获取cursor光标，固定操作
    cursor = db.cursor()
 
    title = '\''+title+'\''
    create_time = '\''+create_time+'\''

    page_view = int(page_view)
#            sql = 'insert into table_1() values()'
    table_id = 'table_'+str(id)
   
    sql = 'replace into %s (num,blog_id,title,page_view,create_time) values (%d,%d,%s,%d,%s)'%(table_id,num,blog_id,title,page_view,create_time)
    # 执行sql语句
    try:
        print "博客信息 努力插入中..."
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        print 'sucessfully!'
    except Exception, e:
        # 如果发生错误则回滚
        db.rollback()
        print e
        print 'failed!'

    # 关闭数据库连接
    db.close()    
    
#def blog_insert2mysql(blog_list,num,id,title,page_view,create_time):
#    
#    for blog in blog_list:
#
#        print blog.id
#        print blog.page_view
#        blog.id = int(blog.id)
#        print blog.title
# 
#        blog.title = '\''+blog.title+'\''
#        blog.create_time = '\''+blog.create_time+'\''
#        print blog.title
#
#        blog.page_view = int(blog.page_view)
##            sql = 'insert into table_1() values()'
#        sql = 'replace into %s (num,id,title,page_view,create_time) values (%d,%d,%s,%d,%s)'%(table_id,blog.num,blog.id,blog.title,blog.page_view,blog.create_time)
#        # 执行sql语句
#        try:
#            print "努力插入中..."
#            cursor.execute(sql)
#            # 提交到数据库执行
#            db.commit()
#            print 'sucessfully!'
#        except Exception, e:
#            # 如果发生错误则回滚
#            db.rollback()
#            print e
#            print 'failed!'
#
#    # 关闭数据库连接
#    db.close()