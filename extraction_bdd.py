# -*- coding: utf-8 -*-
"""
Created on Mon May 29 08:44:28 2017

@author: matthieuweber
"""

import sqlite3


#connection à la bdd
conn = sqlite3.connect('base_temperature.sqlite') 


def get_data(id_station):
    
    c=conn.cursor()
    date=[]
    tp=[]
    q_tp=[]
    
    c.execute("""SELECT * FROM temperatures ORDER BY date""")
    for line in c.execute("""SELECT date,tp,q_tp FROM temperatures WHERE id=33"""):
        date.append(line[0])
        tp.append(line[1])
        q_tp.append(line[2])
        
    return date,tp,q_tp
    
    
  #coupe la connection