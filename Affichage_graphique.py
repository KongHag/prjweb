# -*- coding: utf-8 -*-
"""
Created on Mon May 29 08:39:11 2017

@author: Utilisateur
"""

import matplotlib.pyplot as plt


from extraction_bdd import *

def genere_graphe(date,tp,nom='graphe.png'):
    if len(date) != len(tp):
        return False;
    else:
        fig, ax = plt.subplots()
        #ax.xaxis.set_major_formatter(yearsFmt)
                
        datemin = min(date)
        datemax = max(date)
        delta = datemax-datemin
        
        datemin = datemin - 0.05*delta
        datemax = datemax + 0.05*delta
        ax.set_xlim(datemin, datemax)
        
        plt.savefig(nom)
        return True
