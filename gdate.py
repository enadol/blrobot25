# -*- coding: utf-8 -*-
"""
Created on Mon May  9 18:47:36 2022

@author: enado
"""
# SOLO ACTUALIZAR MD !!
#NO CORRER SOLO!! CORRE EN BS23!!
import requests
from bs4 import BeautifulSoup

md=5
torneo='2024-25'
lstDates=[]
lstDatesCumul=[]

def getMDDates(mday):
    lstMDDates=[]

    mdpage= requests.get(f'https://kicker.de/bundesliga/spieltag/{torneo}/{mday}')
    if mdpage.status_code== 200:
        content = mdpage.content

        
    klass=["kick__v100-gameList__header"]

    soup = BeautifulSoup(content, 'html.parser')
    #print(soup.prettify())
    dates=soup.find_all("div", attrs={"class": klass})

    for date in dates:
        lstMDDates.append(date.text.strip())
 
    mddate1=lstMDDates[0][:2].strip()
    mddate2=lstMDDates[0].split(',')[1].split('.')[0].strip().lstrip("0")
    mddate3=lstMDDates[0].split(',')[1].split('.')[1].lstrip("0")

    MDdateDef=f'[{mddate1}. {mddate2}.{mddate3}.]'
    lstDatesCumul.append(MDdateDef)

for i in range(1, md+1):
    aggdate=getMDDates(i)
