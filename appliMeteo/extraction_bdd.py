# -*- coding: utf-8 -*-
"""
Created on Mon May 29 08:44:28 2017

@author: matthieuweber
"""

import sqlite3



def get_data(id_station):
    conn = sqlite3.connect('base_temperature.sqlite') 
    c=conn.cursor()
    date=[]
    tp=[]
    q_tp=[]
    
    c.execute("""SELECT * FROM temperatures ORDER BY date""")
    for line in c.execute("""SELECT date,tp,q_tp,nom FROM temperatures JOIN stations_meteo ON temperatures.id = stations_meteo.id WHERE temperatures.id={}""".format(id_station)):
        date.append(line[0])
        tp.append(line[1])
        q_tp.append(line[2])
        nom_complet = line[3]
    nom =''
    i = 0
    while (i<len(nom_complet) and nom_complet[i] != ' '):
        nom += nom_complet[i]
        i += 1
    conn.close()
    return date,tp,q_tp,nom
    
def get_station():
    conn = sqlite3.connect('base_temperature.sqlite') 
    c=conn.cursor()
    c2=conn.cursor()
    id_station=[]
    nom=[]
    lat=[]
    lon=[]
    alt=[]
    
    for line in c.execute("""SELECT * FROM stations_meteo"""):
        for test in c2.execute("""SELECT COUNT(date) FROM temperatures WHERE id={}""".format(line[0])):
            True
        
        if test[0]>0:
            id_station.append(line[0])
            nom.append(line[1])
            lat.append(min_to_dec(line[2]))
            lon.append(min_to_dec(line[3]))
            alt.append(line[4])
    conn.close()   
    return id_station,nom,lat,lon,alt
    
def min_to_dec(a):
    [deg,minu,sec]=a.split(':')
    if int(deg)>=0:
        return int(deg)+int(minu)/60+int(sec)/3600
    else:
        return int(deg)-int(minu)/60-int(sec)/3600
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


#date,tp,q_tp=get_data(742)    
#print(moyenne_annee(date,tp,q_tp))    

