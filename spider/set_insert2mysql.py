# -*- coding: utf-8 -*-
"""
Created on Sat Sep 01 22:13:16 2018

@author: lele
"""
#import csdn_demo
#import notouch_spider
import time
import pymysql

def set_main(id,get_time,blogs_num,total_views):
    db = pymysql.connect("localhost", "root", "你的密码！", "blogs_set",charset='utf8')
    # 获取cursor光标，固定操作
    cursor = db.cursor()

    tem = '(id int primary key not null,get_time tinytext not null,blogs_num int not null,total_views int not null ,blogs_table_name tinytext not null)'
    print tem

    table_name = 'blogs_set'
    sql = 'create table if not exists %s %s'%(table_name, tem)
    try:
        cursor.execute(sql)
        print 'Sucessfully create table(%s)!'%table_name
    except Exception,e:
        print e
        print 'Fail to create table(%s)'%table_name
    
    id = int(id)
    print "开始插入博客数据集"
    get_time = '\''+str(get_time)+'\''

    blogs_num = int(blogs_num)
    
    total_views = int(total_views)
    blogs_table_name = '\''+'table_'+str(id)+'\''
    
    sql = 'replace into blogs_set (id,get_time,blogs_num,total_views,blogs_table_name) values (%d,%s,%d,%d,%s)'%(id,get_time,blogs_num,total_views,blogs_table_name)
    # 执行sql语句
    print sql
    try:
        print "努力插入中..."
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        print 'sucessfully!'
        print '--------------------'
    except Exception, e:
        # 如果发生错误则回滚
        db.rollback()
        print e
        print 'failed!'

    # 关闭数据库连接
    db.close()
        

if __name__ == '__main__':    
    id = 1
    while (1):
        try:
            blog_set = Blog_set(id,now_page=1,last_page=2)
            print type(blog_set.total_view)
            set_main(id,blog_set.get_time,len(blog_set.blog_list),blog_set.total_view)
            id += 1
        except Exception, e:
            print e
            print "好像有错误哎~"
    #set_table(1,"2018_9_02:9.53",39,3212)
        
    
    
    
    
