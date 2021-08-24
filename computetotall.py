# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 11:33:25 2020

@author: Enrique Lopez
"""
lstTotalsClubl=[]
lstTotalMDRowsl=[]
seasonl=[]


from computelocal import MDSolol
from precompute import clubes

def getTotalsClub():

    for club in clubes:
        MDBufferl=['', 0,0,0,0,0,0,0,0]
        for h in range(0, len(MDSolol)):
            if MDSolol[h][0]==club:
                for e in range(0, len(MDBufferl)):
                    if e > 0:
                        MDBufferl[e]=MDBufferl[e]+MDSolol[h][e]
                    else:
                        MDBufferl[0]=MDSolol[h][0]
        lstTotalsClubl.append(MDBufferl)
    
#getTotalsClub()

def getAll():
    for club in clubes:
        bufferpjl=0
        bufferpgl=0
        bufferpel=0
        bufferpgl=0
        bufferppl=0
        buffergfl=0
        buffergcl=0
        bufferdifl=0
        bufferpuntosl=0
        
        for g in range(0, len(MDSolol)):
            if MDSolol[g][0]==club:
                equipol = club
                bufferpjl = bufferpjl + MDSolol[g][1]
                bufferpgl = bufferpgl + MDSolol[g][2]
                bufferpel= bufferpel + MDSolol[g][3]
                bufferppl = bufferppl + MDSolol[g][4]
                buffergfl = buffergfl + MDSolol[g][5]
                buffergcl = buffergcl + MDSolol[g][6]
                bufferdifl = bufferdifl + MDSolol[g][7]
                bufferpuntosl= bufferpuntosl +MDSolol[g][8]
                seasonl.append([equipol, bufferpjl, bufferpgl, bufferpel, bufferppl, buffergfl, buffergcl, bufferdifl, bufferpuntosl])
                
                
getAll()