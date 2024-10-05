# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 08:57:19 2020

@author: Enrique Lopez
"""
#cambié a precomputewd 2024
from precomputewd import matches, clubes

MDSolol=[]
mdl = []

def get_club_data(club, match):
    """compute club data"""
    pjl=0
    pgl=0
    pel=0
    ppl=0
    puntosl=0
    gfl=0
    gcl=0
    difl=0

    if match['teamhome']== club:
        pjl= pjl +1
        if match['pointslocal'] == 3:
            pgl = pgl +1
        elif match['pointslocal'] == 1:
            pel = pel +1
        else:
            if match['pointslocal'] == 0:
                ppl = ppl+1
        puntosl= match['pointslocal']
        gfl = match['goalshome']
        gcl = match['goalsaway']
        difl = gfl - gcl

    return([club, pjl,pgl,pel,ppl,gfl,gcl,difl, puntosl])

def get_club_md_solo_l(club):
    """compute club data local"""
    for match in matches:
        if match['teamhome'] == club:
            mdl = get_club_data(match['teamhome'], match)
            MDSolol.append(mdl)

def inject_club_mds_l():
    """inject club data local"""
    for club in clubes:
        get_club_md_solo_l(club)

inject_club_mds_l()
