# -*- coding: utf-8 -*-
"""
Created on Mon May 29 09:59:11 2017

@author: Utilisateur
"""

from Affichage_graphique import *


id_stat = 33
data=get_data(id_stat)

date,tp = moyenne_annee(data[0],data[1],data[2])


genere_graphe(date,tp)
