# coding=utf-8
from __future__ import unicode_literals
import pymysql
import datetime
def get_table_info(table_name,column,local):
    # 连接本地已有的数据库
    if(local == True):
        db = pymysql.connect("localhost", "root", "你的密码！", 'blogs_set' ,charset="utf8")
    elif(local == False):
        db = pymysql.connect("你的远程服务器IP地址！", "root", "你的密码！", 'blogs_set' ,charset="utf8")
    else:
        print "参数错了！"
    # 获取cursor光标
    cursor = db.cursor()

    # 在已有的数据库csdn中创建一个blogs表格，表头为id，title,page_view 数据类型都是int
    # 构建创建表格的sql语句
#    table_name = '\''+table_name+'\''
    sql_info = 'select %s from %s'%(column,table_name)
    

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
            tem.append("".join(d).encode("utf8"))
#            print d
#            print ''.join(d)
    except Exception , e:
        for d in data:
#            print "d"
#            print d
#            print str(list(d))[1:-1]
            tem.append(str(list(d))[1:-1].encode("utf-8"))
        
    return tem


def mysql_time2date(get_time):
    tem_list = []
    for t in get_time:
        t = t.replace("_",":")
        t_list = t.split(":")
        for num,i in enumerate(t_list):

            if len(i)==1:
                tem = '0' + i
                t_list[num] = tem
                print t_list
        t = "-".join(t_list[:3])+" "+":".join(t_list[3:])
        
        tem_list.append(t.encode("utf-8"))
    get_time = tem_list
        
    tem_list = []
    for t in get_time:
        tem_list.append(t[:])
        
        
    tem2 = []
    for d in tem_list:
#        print d
        ds = datetime.datetime.strptime(d,'%Y-%m-%d %H:%M') 
        print ds
        tem2.append(ds)
    
    datetime_list = tem2
    
    return datetime_list

def date2str(date):
    tem = []
    for d in date:
        tem.append(datetime.datetime.strftime(d,'%Y-%m-%d %H:%M'))
    return tem
	

if __name__ == '__main__':
    table_name = 'blogs_set'
    column = 'get_time'
    data = get_table_info(table_name,column,local = False)
    for d in data:
        print d
#    data = mysql_time2date(data)
#    print (data[2]-data[0]).total_seconds()
#    tem = date2str(data)
#    for t in tem:
#        print t
#        print type(t)
    
#    print data
    #列表和元组转成字符串，必须要用join函数~
#    print ''.join(d)
    
    
    
    
'''
可视化文件夹

这次将存入数据和读取数据分开了。可视化文件夹，是由四个read函数，读取MySQL已经存好的数据。然后分两个画图函数：一个是总访问量随时间的变化，时间最久可以达到5天前，每张图最多可以有50个采样点，随着时间的推移，以后的时间间隔应该稳定在5个小时一次，每隔四个点会在图中标出数字；观看效果还行，然后可以看出工作时间8-11点和下午2-11点的博客访问量是增长的最快的~
另一个是将博主所有的博客都拿出来，然后分为三天进行堆叠柱状图可视化，看看近三天，单篇博客访问量的增长。这仅仅适合博客数量不是特别多的人。如果超过了60篇，基本上一张图就看不清了，如果数据存储没有达到3天，也需要等一等，或者将时间间隔调整一下~
就我目前来说44篇博客，访问量的显示还是可以。清楚明了，每篇博客的柱状图都会标出最新访问量，以及近两天的增长量。确实可以看出热门的博客，增长的确实是很快，冷门的，基本上凉凉，没人能看到。另外对于新发表的博客。我特地将其放到的最前面，然后这种增长效果，看起来还是很舒服的~
'''