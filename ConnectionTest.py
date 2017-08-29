# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 09:55:22 2017

@author: Asif
"""

import MySQLdb
connection=MySQLdb.connect(host="host_name", user="user_name", passwd="your_password", db="database_name")
cur=connection.cursor() 
cur.execute("select Host, User, Password from user") 
multiplerow=cur.fetchall()
for row in multiplerow:
    print(row)
connection.close()
