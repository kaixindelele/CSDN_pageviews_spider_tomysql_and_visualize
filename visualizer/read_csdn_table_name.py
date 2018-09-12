# coding=utf-8
from __future__ import unicode_literals
import pymysql

def get_table_name(table_name,db_name,local):
    # 连接本地已有的数据库
    if(local == True):
        db = pymysql.connect("localhost", "root", "你的密码！", 'csdn' ,charset="utf8")
    elif(local == False):
        db = pymysql.connect("你的远程服务器IP地址！", "root", "你的密码！", 'csdn' ,charset="utf8")
    else:
        print "参数错了！"
    # 获取cursor光标
    cursor = db.cursor()

    # 在已有的数据库csdn中创建一个blogs表格，表头为id，title,page_view 数据类型都是int
    # 构建创建表格的sql语句
    table_name = '\''+table_name+'\''
    db_name = '\''+db_name+'\''
    sql_name = 'select COLUMN_NAME from information_schema.COLUMNS where table_name = %s and table_schema = %s'%(table_name,db_name)
    
#    # 执行sql语句
    try:
        cursor.execute(sql_name)
        # 提交到数据库执行
        db.commit()
        data = cursor.fetchall()
        # print "data is :",data
        print 'this request is sucessful!'
    except Exception, e:
        # 如果发生错误则回滚
        db.rollback()
        print e
        print 'failed!'

    # 关闭数据库连接
    db.close()
    
    table_name_list = []
    for d in data:
#        print "".join(d)
        table_name_list.append("".join(d).encode("utf8"))
    
    return table_name_list

if __name__ == '__main__':
    table_name = 'table_1'
    db_name = 'csdn'
    table_name_list = get_table_name(table_name,db_name,local=False)
    for n in table_name_list:
        print n
