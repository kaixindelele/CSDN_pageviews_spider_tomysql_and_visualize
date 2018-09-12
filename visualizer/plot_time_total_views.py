# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
Created on Tue Sep 04 18:19:35 2018

@author: lenovo
"""

#coding=utf-8

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

import datetime  
import decimal
import time

import read_blogs_set_table_info

def get_info(table_name,db_name,local):
    try:
        info = read_blogs_set_table_info.get_table_info(table_name,db_name,local)
    except Exception,e:
        try:
            print e
            print "the first request is failure~"
            print "maybe the server is busy!"
            print "please wait 10 seconds and try again~"
            time.sleep(10)
            info = read_blogs_set_table_info.get_table_info(table_name,db_name,local)
        except Exception,e:
            print e
            print "the server is really busy! give up this time!"
            return None
    return info
def get_all_info():
    get_time_str = get_info("blogs_set","get_time",local = False)
    id = get_info("blogs_set","id",local = False)
    total_views = get_info("blogs_set","total_views",local = False)
    return get_time_str,id,total_views

#根据数据动态画图
def drawBydata():
    print "total_views image is begining to get info from mysql :"
    tem_str,id,tem_views = get_all_info()
    total_views = tem_views[-2500:]
    get_time_str = tem_str[-2500:]
    length = len(get_time_str)
    num = 50
    interval = int(length/num)+1
    get_time_str = get_time_str[::interval]
    real_length = len(get_time_str)

    x = range(real_length)

    print "real_length:",real_length
    # 清空画布，这样可以连续画两张图~
    plt.figure()
    plt.rcParams['savefig.dpi'] = 1400 #图片像素
    # plt.rcParams['figure.dpi'] = 300 #分辨率
    markersize_str = str(int(160/real_length))
    width = 0.5

    plt.plot(x,total_views[::interval],'ro-', linewidth  = 2, markersize=markersize_str)
    i = len(total_views[::interval])
    j = i%4
    for a,b in zip(range(len(x)),total_views[::interval]):
        if(i%4==j):
            plt.text(a-width/2, int(b)+width, '%.0f' % int(b), ha='center', va= 'bottom',fontsize=14)
        i += -1
#    plt.rotation,x轴字体旋转的角度
    
    plt.xticks(x, get_time_str,rotation=70)
    plt.xticks(fontsize=int(real_length/5))
    plt.margins(0.08)
    plt.subplots_adjust(bottom=0.15)
    #设置x轴的名字
    plt.xlabel("Date")
    plt.ylabel("Visitors")
    #图的标题
    plt.title("My blog visit analysis")
    plt.grid()
    plt.savefig("views.png")
    plt.show()
    print 'plot success!'

if __name__ == '__main__':
    drawBydata()