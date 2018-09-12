# -*- coding: utf-8 -*-
"""
Created on Mon Sep 03 18:08:17 2018

@author: lenovo
"""
import time
import notouch_spider
import set_insert2mysql
import blog_insert2mysql
import datetime

class Blog_set(object):
    def __init__(self,id,now_page,last_page):
        self.id = id
        self.get_blog(now_page,last_page)
        self.get_time = self.get_time()
        self.blog2mysql()
#        self.blog_sort()
#        self.create_table()
        
    def get_blog(self,now_page,last_page):
        self.blog_id_list,self.blog_url_list,self.title_list,self.page_view_list,self.create_time_list,self.blog_list,self.total_views = notouch_spider.get_list(now_page ,last_page)
        if self.total_views != sum(self.page_view_list):
            print "本次爬虫未获取完整信息"
            
        self.blogs_num = len(self.title_list)
        
    def blog_sort(self):
        for v,t,num in zip(self.view_list,self.title_list,self.num_list):
            print "----------***----------\n题目： 《%s》\n浏览量: %s \n第%d篇文章"%(t,v,num)
            
    def get_time(self):
        
        now_time = datetime.datetime.now()
        print (now_time)
        get_time = now_time.strftime('%Y-%m-%d %H:%M')
#        get_time = datetime.datetime.strftime(a,'%Y-%m-%d %H:%M')
#        get_time = str(a[0])+"_"+str(a[1])+'_'+str(a[2])+":"+str(a[3])+":"+str(a[4])
        print "get_time:",get_time
        return get_time
    
    def blog2mysql(self):
        blog_insert2mysql.create_table(self.id)
        for blog in self.blog_list:
            blog_insert2mysql.blog_insert2mysql(self.id,blog.num,blog.blog_id,blog.title,blog.page_view,blog.create_time)
        
    def set2mysql(self):
        set_insert2mysql.set_table(self.id,self.get_time,self.blogs_num,self.total_views)
        
        
        
if __name__ == '__main__':
    blog_set = Blog_set(id = 1,now_page=2,last_page=2)