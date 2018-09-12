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

    interval_num = 48
    table_name_3 = table_name[-1]
    table_name_2 = table_name[-1-interval_num*1]
    # print "table_name_2:",table_name_2
    table_name_1 = table_name[-1-interval_num*2]

    view_1 = str2int(get_info(table_name_1,"page_view",local = False))
    id_1 = str2int(get_info(table_name_1,"blog_id",local = False))
    dict_1 = dict(zip(id_1,view_1))

    view_2 = str2int(get_info(table_name_2,"page_view",local = False))
    id_2 = str2int(get_info(table_name_2,"blog_id",local = False))
    dict_2 = dict(zip(id_2,view_2))

    y3 = str2int(get_info(table_name_3,"page_view",local = False))[::-1]
    id_3 = str2int(get_info(table_name_3,"blog_id",local = False))[::-1]

    y1 = []
    y2 = []
    for d in id_3:
        if(dict_2.get(d)):
            y2.append(dict_2.get(d))
        else:
            y2.append(0)

        if(dict_1.get(d)):
            y1.append(dict_1.get(d))
        else:
            y1.append(0)
        
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
    
    # 清空画布，这样可以连续画两张图~
    plt.figure()
    width = 0.35
    plt.bar(range(len(x1)), y1,width = width, label='before yesterday',alpha=0.4,fc = 'r')
    plt.bar(range(len(x2)), y2,width = width, label='yesterday',alpha=0.3,fc = 'y')
    plt.bar(range(len(x3)), y3,width = width, label='today',alpha=0.2,fc = 'b')
 
    plt.xticks(range(len(x3)), id_3,rotation=70)
    
    for a,b in zip(range(len(x3)),y3):
        plt.text(a+width/2, 1.05*b, '%.0f' % b, ha='center', va= 'bottom',fontsize=10)
    
    cha = list(map(lambda x: x[0]-x[1], zip(y3, y1)))
    for a,b,c in zip(range(len(x3)),y1,cha):
        plt.text(a+1.5*width, 0.95*b, '%.0f' % c,ha='center', va= 'bottom',fontsize=10)
    
    # plt.bar(x1, y1, label='the third last',fc='y')
    # plt.bar(x2, y2, label='the second last',fc='b')
    # plt.bar(x3, y3, label='the last',fc='k')
    
    plt.rcParams['savefig.dpi'] = 1400 #图片像素


    plt.legend(loc='upper center', bbox_to_anchor=(0.6,0.95),ncol=1,fancybox=True,shadow=True)
    plt.xlabel('number')
    plt.ylabel('value')
    
    plt.title("page_view")
    plt.grid()
    plt.savefig("bars.png")

    plt.show()


if __name__ == '__main__':
    plot3bar(increment = 0)
    
    
    
    
    
    
    
    
    
    
    
    
    