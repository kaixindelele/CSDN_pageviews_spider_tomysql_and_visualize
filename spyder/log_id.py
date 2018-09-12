# -*- coding: utf-8 -*-
"""
Created on Tue Sep 04 15:02:49 2018

@author: lenovo
"""
import os

def write_id(id,path):
#    localDir=os.path.dirname(__file__)
#    path = localDir + "/id.txt"
    f_id = open(path,'w')
    f_id.write(str(id))
    f_id.close()

def read_id(path):
#    localDir=os.path.dirname(__file__)
#    path = localDir + "/id.txt"
    f_id = open(path,'r')
    id = f_id.read()
    f_id.close()
    return int(id)

if __name__ == '__main__':
    localDir=os.path.dirname(__file__)
    path = localDir + "/id.txt"
    write_id(2,path)
    id = read_id(path)
    print id