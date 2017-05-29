# -*- coding: utf-8 -*-
"""
Created on Mon May 22 11:00:58 2017

@author: matthieuweber
"""

import sqlite3
import csv

#connection à la bdd
conn = sqlite3.connect('base_temperature.sqlite') 

c=conn.cursor()

### table stations_meteo

#suppression si table existante
c.execute("""DROP TABLE IF EXISTS stations_meteo""")

#création de la table stations_meteo
c.execute("""CREATE TABLE stations_meteo
(id INT PRIMARY KEY,
nom TEXT,
lat TEXT,
lon TEXT,
alt INT)""")


premier=True #pour éliminer la première ligne

#ouv du ficher: content contient les données
with open('stations-meteo.csv',newline='',encoding='ISO8859-1') as csvfile:
    content=csv.reader(csvfile,delimiter=";",quotechar="\n")
    
    for station in content:
        if premier: #première ligne
            premier=False
        else:
            cmd1="""INSERT INTO stations_meteo VALUES ({},"{}","{}","{}",{})""".format(int(station[0]),station[1],station[2],station[3],int(station[4]))
        
            c.execute(cmd1) #creation de la ligne
            
### table temperatures

c.execute("""DROP TABLE IF EXISTS temperatures""")   

#creation de la table

c.execute("""CREATE TABLE temperatures
(id INT,
date INT,
tp INT,
q_tp INT,
tp_min INT,
q_tp_min INT,
tp_max INT,
q_tp_max INT)""")
      
premier=True

#ouv du fichier
with open('temp-histo.csv',newline='',encoding='ISO8859-1') as csvfile:
    content2=csv.reader(csvfile,delimiter=";",quotechar="\n")
    
    for releve in content2:
        if premier: 
            premier=False
        else:
            cmd2="""INSERT INTO temperatures VALUES ({},{},{},{},{},{},{},{})""".format(releve[0],releve[1],releve[2],releve[3],releve[4],releve[5],releve[6],releve[7])
            c.execute(cmd2)

conn.commit() #sauvegarde des changements
conn.close()  #coupe la connection