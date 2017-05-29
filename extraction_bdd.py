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
    for line in c.execute("""SELECT date,tp,q_tp FROM temperatures WHERE id={}""".format(id_station)):
        date.append(line[0])
        tp.append(line[1])
        q_tp.append(line[2])
        
    return date,tp,q_tp
    

def moyenne_annee(date,tp,q_tp):
    
    n=len(date)
    d=0
    current_year=str(date[0])[0:4]
    current_mean=0
    current_nb=0
    annee=[]
    tp_annee=[]
    
    for d in range(n):
        if q_tp[d]==0:
            if str(date[d])[0:4]==current_year:
                current_mean+=tp[d]
                current_nb+=1
            else:
                annee.append(int(current_year))
                tp_annee.append(current_mean/current_nb)
                current_year=str(date[d])[0:4]
                current_nb=1
                current_mean=tp[d]
        
    annee.append(int(current_year))
    tp_annee.append(current_mean/current_nb)  
     
    return annee,tp_annee

#date,tp,q_tp=get_data(33)    
#print(moyenne_annee(date,tp,q_tp))    
        
  #coupe la connection