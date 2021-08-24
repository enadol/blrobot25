# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 08:57:19 2020

@author: Enrique Lopez
"""

from precompute import matches, clubes

MDSolov=[]
mdv = []

def getClubData(club, match):
    
    pjv=0
    pgv=0
    pev=0
    ppv=0
    puntosv=0
    gfv=0
    gcv=0
    difv=0
    

    if match['teamaway'] == club:
        pjv = pjv+1
        if match['pointsvisitor'] == 3:
            pgv = pgv+1
        elif match['pointsvisitor']== 1:
            pev= pev+1
        else:
            if match['pointsvisitor'] == 0:
                ppv = ppv+1
    puntosv = match['pointsvisitor']
    gfv = match['goalsaway']
    gcv = match['goalshome']
    difv = gfv - gcv
            
    return([club, pjv,pgv,pev,ppv,gfv,gcv,difv, puntosv])
    
def getClubMDSolov(club):
    for match in matches:
        if match['teamaway'] == club:
            mdv = getClubData(match['teamaway'], match)
            MDSolov.append(mdv)

def injectClubMDsv():
    for club in clubes:
        getClubMDSolov(club)
        
injectClubMDsv()