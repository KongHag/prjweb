# -*- coding: utf-8 -*-
"""
Created on Mon May 29 08:39:11 2017

@author: Utilisateur
"""

import matplotlib.pyplot as plt


from extraction_bdd import *

def genere_graphe(date,tp,nom='temperature.png'):
    if len(date) != len(tp):
        return False;
    else:
        fig, ax = plt.subplots()
                
        datemin = min(date)
        datemax = max(date)
        delta = datemax-datemin
        
        datemin = datemin - 0.05*delta
        datemax = datemax + 0.05*delta
        ax.set_xlim(datemin, datemax)
        
        tpmin = min(tp)
        tpmax = max(tp)
        deltatp = tpmax-tpmin
        tpmin = tpmin - 0.05*deltatp
        tpmax = tpmax + 0.05*deltatp
        ax.set_ylim(tpmin, tpmax)
        
        plt.plot(date,tp)
        plt.savefig('client/graphes/'+nom)
        return True

def genere_graphe_id(i):
    id_stat = i
    data=get_data(id_stat)
    date,tp = moyenne_annee(data[0],data[1],data[2])
    genere_graphe(date,tp)




