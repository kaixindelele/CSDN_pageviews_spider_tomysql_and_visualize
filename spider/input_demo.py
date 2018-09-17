# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
Created on Sun Sep 09 10:04:05 2018

@author: lenovo
"""

import matplotlib.pyplot as plt
import datetime
import time

import read_csdn_table_info
import read_blogs_set_table_info

def get_table_name(table_name,column,local):
    try:
        info = read_blogs_set_table_info.get_table_info(table_name,column,local)
    except Exception,e:
        try:
            print e
            print "the first request is failure~"
            print "maybe the server is busy!"
            print "please wait 10 seconds and try again~"
            time.sleep(10)
            info = read_blogs_set_table_info.get_table_info(table_name,column,local)
        except Exception,e:
            print e
            print "the server is really busy! give up this time!"
            return None
    return info

def get_info(table_name,db_name,local):
    try:
        info = read_csdn_table_info.get_table_info(table_name,db_name,local)
    except Exception,e:
        try:
            print e
            print "the first request is failure~"
            print "maybe the server is busy!"
            print "please wait 10 seconds and try again~"
            time.sleep(10)
            info = read_csdn_table_info.get_table_info(table_name,db_name,local)
        except Exception,e:
            print e
            print "the server is really busy! give up this time!"
            return None
    return info

def str2int(li):
    tem = []
    for l in li:
        tem.append(int(l))
    li = tem
    return li

def plot3bar(increment):
    print "-----------***----------"
    print "3bars image is beginning to get info from mysql:"
    table_name = read_blogs_set_table_info.get_table_info("blogs_set","blogs_table_name",local = False)
    # table_name = get_table_name("blogs_set","blogs_table_name",local = False)

    interval_num = 24
    table_name_last = table_name[-1]
    last_time = read_csdn_table_info.get_table_info(table_name_last,'create_time',False)
    for t in last_time:
    	print t
    last_view = read_csdn_table_info.get_table_info(table_name_last,'page_view',False)

    table_name_3 = table_name[-1]
    table_name_2 = table_name[-1-interval_num*1]
    print "table_name_2:",table_name_2
    table_name_1 = table_name[-1-interval_num*2]
    print "table_name_1:",table_name_1
    table_name_0 = table_name[-1-interval_num*3]
    print "table_name_0:",table_name_0


    y0 = str2int(get_info(table_name_0,"page_view",local = False))
    print "y0:",y0
    print "len(y0):",len(y0)
    y1 = str2int(get_info(table_name_1,"page_view",local = False))
    print "y1:",y1
    print "len(y1):",len(y1)
    y2 = str2int(get_info(table_name_2,"page_view",local = False))
    print "y2:",y2
    print "len(y2):",len(y2)
    y3 = str2int(get_info(table_name_3,"page_view",local = False))
    print "y3:",y3
    print "len(y3):",len(y3)
    
#     if(increment == True):
# #    v = list(map(lambda x: x[0]-x[1], zip(v2, v1)))
#         y3 = list(map(lambda x: x[0]-x[1], zip(y3, y2)))
#         y2 = list(map(lambda x: x[0]-x[1], zip(y2, y1)))
#         y1 = list(map(lambda x: x[0]-x[1], zip(y1, y0)))
  
    space = 4
    x1 = []
    for i in range(len(y1)):
        x1.append( space * i +1)
    
    x2 = []
    for i in range(len(y2)):
        x2.append( space * i +2)
    x3 = []
    for i in range(len(y3)):
        x3.append( space * i +3)
    
    print "x1:",x1
    print "x2:",x2
    print "x3:",x3
    # 清空画布，这样可以连续画两张图~
    plt.figure()

    name_list = get_info(table_name_3,"num",local = False)
    num_list = y2
    num_list1 = y3
    plt.bar(range(len(num_list)), num_list, label='today',fc = 'y')
    plt.bar(range(len(num_list)), num_list1, bottom=num_list, label='yesterday',tick_label = name_list,fc = 'r')
    plt.legend()
    plt.show()

    # plt.bar(x1, y1, label='the third last',fc='r')
    # plt.bar(x2, y2, label='the second last',fc='b')
    # plt.bar(x3, y3, label='the last',fc='g')
    
    # plt.rcParams['savefig.dpi'] = 1400 #图片像素


    # plt.legend()
    # plt.xlabel('number')
    # plt.ylabel('value')
    
    # plt.title("page_view")
    # plt.grid()
    # plt.savefig("bars.png")

    # plt.show()


if __name__ == '__main__':
    plot3bar(increment = 0)
    
    

