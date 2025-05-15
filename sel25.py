# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 12:50:41 2021

@author: enado
"""
# WORKFLOW -> sel25 -> MEROBOT A GIT EN SHELL - LAUNCHWD
"""import packages"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from gateSEL import lst_dates_cumul, TORNEO, MD
import codecs

lstJornadas=[]
lstClubes=[]
lstHome=[]
lstAway=[]
count=0
countgoles=0
lstMatch=[]
lstMD=[]
lstGoles=[]
lstGHome=[]
lstGAway=[]
lstGHomeH=[]
lstGAwayH=[]
lstIndexesH=[]
lstIndexesA=[]
#lstOdds=[]

#MD=22

DRIVER_PATH='C:/Users/enado/ChromeDriver'
service = webdriver.ChromeService(executable_path = 'C:/Users/enado/ChromeDriver/chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(0.5)
driver.maximize_window()

driver.get(f'https://kicker.de/bundesliga/spieltag/{TORNEO}/-1')

# 3. Wait for the "Google Web" option to be clickable
WebDriverWait(driver, 10)

# 4. Click the "Google Web" option
#google_web_option.click()

# 5. Wait for the "Accept" button to be clickable
accept_button = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.XPATH,"//a[contains(text(), 'Zustimmen & weiter')]")))

# 6. Click the "Accept" button
accept_button.click()
klass=["kick__v100-scoreBoard__scoreHolder__score", "kick__v100-scoreBoard__scoreHolder__text"]

clubes=driver.find_elements(By.CLASS_NAME, "kick__v100-gameCell__team__name")
goles=driver.find_elements(By.CLASS_NAME, "kick__v100-scoreBoard__scoreHolder__score")
goles_text=driver.find_elements(By.CLASS_NAME, "kick__v100-scoreBoard__scoreHolder__text")

for club in clubes:
    lstClubes.append(club.text.strip())

for gol in goles:
    lstGoles.append(gol.text.strip())

# SOLO PARA EL TORNEO 2024-2025 POR EL PARTIDO
# DE LA JORNADA 14 REASIGNADO EN EL RESULTADO POR PIROTECNIA 
lstGoles.insert(486, "0")
lstGoles.insert(487, "2")


def classifyTeams():
    for ind, club in enumerate(lstClubes):
    #count=2
        if ind%2==0:
            lstHome.append(club)
        #count=count+1
        else:
            lstAway.append(club)
            #count=count+1

classifyTeams()

    #por partido suspendido hasta el 6 de abril
    #del lstHome[161]
    #del lstAway[161]


            
def golesClass():
    nbuffer=0
    for n in range(0, len(lstGoles)):
        nbuffer=nbuffer+n
        goal=lstGoles[nbuffer]
        lstGHome.append(goal)
        nbuffer=nbuffer+1
        goal=lstGoles[nbuffer]
        lstGHomeH.append(goal)
        nbuffer=nbuffer+1
        goal=lstGoles[nbuffer]
        lstGAway.append(goal)
        nbuffer=nbuffer+1
        goal=lstGoles[nbuffer]
        lstGAwayH.append(goal)
        nbuffer=nbuffer+1

        
jornadas=driver.find_elements(By.CLASS_NAME, "kick__section-headline")

for jornada in jornadas:
    lstJornadas.append(jornada.text.strip())

def getGAIndexes():
    factor=2
    while(factor<len(lstGoles)):
        lstIndexesA.append(factor)
        factor=factor+4

def getGHIndexes():
    factor=0
    while(factor<len(lstGoles)):
        lstIndexesH.append(factor)
        factor=factor+4


getGAIndexes()
getGHIndexes()

           
for index in lstIndexesA:
    element=lstGoles[index-1]
    lstGAway.append(element)


for index in lstIndexesH:
    element=lstGoles[index]
    lstGHome.append(element)
        
        
def matchIn():
    for i in range(0, len(lstGHome)):
        if(i <len(lstGHome)):
            #lstMatch.append("    "+ lstHome[i] + "  "+lstGHome[i]+"-"+lstGAway[i]+"  "+ lstAway[i]+"\n")
            lstMatch.append(f'    {lstHome[i]}  {lstGHome[i]}-{lstGAway[i]}  {lstAway[i]}\n')
        
def mdIn():
    for j in range(1,35):
        #f.write(lstJornadas[j]+"\n")
        md=matchIn()
        lstMD.append(md)
        

def meRobot():
    with codecs.open("C:/Users/enado/Proyectos/Python33/merobot/bundesliga-2025.txt", "w", "utf-8") as file:
        file.write("\ufeff")
        countjornadas=0
        count2=0
        for line in lstMatch:
            g=lstMatch.index(line)
            if g%9==0:
                file.write(lstJornadas[countjornadas]+ "\n")
                file.write(lst_dates_cumul[countjornadas]+'\n')
                    #file.write("    "+ line)
                file.write(f'    {line}')
                countjornadas=countjornadas+1
            else:
                if count2<=len(lstMatch):
                        #file.write("    "+line)
                    file.write(f'    {line}')
            count2=count2+1
                                   
                #else:
                    #file.write("    "+line)
    file.close() 
        

matchIn()
meRobot()

driver.close()