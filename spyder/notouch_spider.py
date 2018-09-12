# -*- coding: utf-8 -*-
"""
Created on Sun Sep 02 20:38:13 2018

@author: lyl
"""

import urllib2
import re
from bs4 import BeautifulSoup 
import sys
import chardet
import time
import pymysql


#这里需要修改称为你的博客账号
account = 'hehedadaq'
baseUrl = 'http://blog.csdn.net/'+account


#导入的这个模块是我接下来定义的一个类，不在这个文件里，所以这段代码无法直接运行~
import blog_class
 
def getPage(url):
 
    #伪装成浏览器访问，直接访问的话csdn会拒绝
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent':user_agent}
    #构造请求
    # print("url:",url)
    req = urllib2.Request(url,headers=headers)
    #访问页面
    try:
        myResponse = urllib2.urlopen(req)
    #    print myResponse.info()
        myPage = myResponse.read()    
        return myPage
    
    except Exception,e:
        print e
        print "本次请求失败，尝试第二次也是最后一次请求！"
        try:
            myResponse = urllib2.urlopen(req)
        #    print myResponse.info()
            myPage = myResponse.read()
            return myPage
        
        except Exception,e:
            print e
            print "最后一次请求失败，凉了，选择放弃！"

def get_list(now_page,last_page):

    blog_id_list = []
    blog_url_list = []
    title_list = []
    page_view_list = []
    create_time_list = []
    blog_list = []
    
    num = 1
    while now_page <= last_page:
        print'-----------------------------the %d page ---------------------------------' % (now_page,)
        
    #    获取网页源码     
        myUrl = baseUrl+'/article/list/'+str(now_page)
        myPage = getPage(myUrl)
     
        # 获取总访问量
        soup = BeautifulSoup(myPage,'html.parser',from_encoding='utf-8')
        contents = soup.find_all('div',class_ = 'article-item-box csdn-tracking-statistics')

        total_views = soup.find('div',class_ = 'grade-box clearfix').find_all('dl')
        
#        for t in total_views:
#            print t.find('dd').get('title')
            
        print total_views[1].find('dd').get('title')
        total_views = total_views[1].find('dd').get('title').encode('utf8')
        
        print type(total_views)

        for c in contents:
#            print "total_view: %s"%(c)        
            blog_id = int(c.get('data-articleid').encode('utf-8'))
            blog_url = c.find('a').get('href').encode('utf-8')
            title = c.find('a').get_text().encode('utf-8')
			#在'a'标签中提取文本信息，utf8编码后，先去除空格，然后除去“原”“转”“译”三种标签，再去除空格
            title = title.strip().replace('原 ','').replace('转 ','').replace('译 ','').strip()
            #因为我的一个标题里有反斜杠，插入MySQL总是会报错！所以我要把反斜杠都转为斜杠！
            title = title.replace("\\\\x","/x")
            page_view = int(c.find('span',class_ = 'read-num').get_text()[4:])
            create_time = c.find('span',class_='date').text.encode('utf-8')
            

            
            blog_id_list.append(blog_id)
            blog_url_list.append(blog_url)
            title_list.append(title)
            page_view_list.append(page_view)
            create_time_list.append(create_time)
            
            tem = locals()['blog_'+str(num)] = blog_class.Blog(num = num,blog_id = blog_id ,title = title,page_view = page_view,create_time = create_time)
            blog_list.append(tem)
            
            num += 1
        now_page += 1
        
    return blog_id_list,blog_url_list,title_list,page_view_list,create_time_list,blog_list,total_views

if __name__ == '__main__':
    print "---------*提取网页信息：博客id、URL、浏览量和标题*---------"
    blog_id_list,blog_url_list,title_list,page_view_list,create_time_list,blog_list = get_list(1,1)

#    for i in blog_id_list:
#        print type(i)
#        print i
#    for u in blog_url_list:
#        print u
#        print type(u)
#    for t in title_list:
#        print "---^^---"
#        print t
#        print type(t)
#    print page_view_list
#    for c in create_time_list:
#        print c
    
#    for b in blog_list:
#        b.print_info()