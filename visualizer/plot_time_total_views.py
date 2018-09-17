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
    #先限定数据量不能超过2500个点，也就是时间跨度不超过5天
    tem_views = tem_views[-2500:]
    tem_str = tem_str[-2500:]
    
    #这段保证从最新的采样点开始，往前数很多个~
    num = 50
    length = len(tem_str)
    interval = int(length/num)+1
    d = length%interval
    if(d==0):
        s = interval-1
    else:
		s = d - 1  
    get_time_str = tem_str[s::interval]
    total_views = tem_views[s::interval]
    print get_time_str[-1]

    real_length = len(get_time_str)

    x = range(real_length)

    print "real_length:",real_length
    # 清空画布，这样可以连续画两张图~
    plt.figure()
    plt.rcParams['savefig.dpi'] = 1400 #图片像素
    # plt.rcParams['figure.dpi'] = 300 #分辨率
    markersize_str = str(int(160/real_length))
    width = 0.5

    plt.plot(x,total_views,'ro-', linewidth  = 2, markersize=markersize_str)
    i = real_length
    j = i%4
    print range(real_length)
    for a,b in zip(range(real_length),total_views):
    	#和上面一样，也是确保最后一个能显示
        if(j==0):
            #这里的思路还是要讲一下的，和上面其实差不多
            #长度假设是45,但是列表是从0-44计数，恰好a取值也是0-44，
            #j是根据长度来的，范围是0-3，如果非0，a%4=j-1刚好可以满足最后一个元素取到
            #以及这点前面每四个值都能取到。
            #但是如果j是0，j-1就不成了，其实也就是j=4,然后4-1=3就好了
            #具体的数学证明还没理清楚~
            if(a%4==3):
                plt.text(a-width/2, int(b)+width, '%.0f' % int(b), ha='center', va= 'bottom',fontsize=14)
        else:
            if(a%4==j-1):
                plt.text(a-width/2, int(b)+width, '%.0f' % int(b), ha='center', va= 'bottom',fontsize=14)
#    plt.rotation,x轴字体旋转的角度
    plt.xticks(x, get_time_str,rotation=70)
    #根据显示点的数量调整字体大小
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
