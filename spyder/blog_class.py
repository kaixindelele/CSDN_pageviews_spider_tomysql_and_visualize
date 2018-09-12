# -*- coding: utf-8 -*-
"""
Created on Mon Sep 03 16:11:00 2018

@author: lyl
"""

class Blog(object):
    def __init__(self,num,blog_id,title,page_view,create_time):
        self.num = num
        self.blog_id = blog_id
        self.title = title
        self.page_view = page_view
        self.create_time = create_time
        
                
    def print_info(self):
        print "the %dth blog , and the title is ——\n《%s》\n\t\tthe page_view is %s ! \n-----------***----------"%(self.num,self.title,self.page_view)
        print self.create_time
        

        
        
