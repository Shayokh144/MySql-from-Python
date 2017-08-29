# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 09:55:22 2017

@author: ASUS
"""

import MySQLdb
connection=MySQLdb.connect(host="localhost", user="root", passwd="", db="mysql")
cur=connection.cursor() 
cur.execute("select Host, User, Password from user") 
multiplerow=cur.fetchall()
for row in multiplerow:
    print(row)
connection.close()