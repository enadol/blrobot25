import urllib.request
import datetime

lstdates=[]
clubes = []
locations=[]
homes=[]
aways=[]
played=[]
lsthome= []
lstaway = []
lstgoalshome=[]
lstgoalsaway=[]
matches=[]
lstindexes=[]
lstrepeats=[]
doc=[]
datesStructured=[]

def buildMatch(club, pj):
    match= {"club": club,
            "pj": pj}
    return(match)

def getPuntos(goalshome, goalsaway):
    if goalshome > goalsaway:
        pointslocal=3
        pointsvisitor =0
    elif goalshome == goalsaway:
        pointslocal = 1
        pointsvisitor = 1
    else:
        pointslocal= 0
        pointsvisitor = 3
        
    return([pointslocal, pointsvisitor])

def getRepeats():
    #lstindexes=[]   

    for line in lines:
        if len(line) >0:
            if not line.startswith('Spieltag'):
                if not line.startswith('='):
                    linea = line
                    doc.append(linea)
  #      if line.startswith('') and len(line) > 0:
                    if linea.startswith('['):
                        if not linea.startswith('Spieltag'):
                            lstindexes.append(doc.index(linea))
            
            
    for repeat in lstindexes:
        i = lstindexes.index(repeat)
        if i == 0:
           newrepeat = 0
           #lstrepeats.append(newrepeat)
        else:
            newrepeat = (lstindexes[i] - lstindexes[i-1])-len(lstindexes)
            lstrepeats.append(newrepeat)
           
    #print(lstindexes)
    lstrepeats.append(9)
   # print(lstrepeats)
    
def structureDates():
    for fecha in lstdates:
        i = lstdates.index(fecha)
        for e in range(0,lstrepeats[i]):
            fechaformat = fecha.split(' ')
            fechaformat = fechaformat[1].split(']')
            fechaformat = fechaformat[0].split('.')
            if int(fechaformat[1]) >=8:
                #change
                year = '2021'
            else:
                #change
                year = '2022'
            fechaformat = year+'-'+fechaformat[1].zfill(2)+'-'+fechaformat[0].zfill(2)
            datesStructured.append(fechaformat)
        
    

clubcodes={"Eintracht Frankfurt": "FFM","TSG Hoffenheim": "HOF","Bayern Muenchen": "FCB","VfL Wolfsburg": "WOB","Borussia Dortmund": "BVB","FC Augsburg": "FCA","RB Leipzig": "RBL","SC Freiburg":"SCF","Hertha BSC":"BSC","SpVgg Greuther Fuerth": "fuerth","Bor. Moenchengladbach":"BMG", "Bayer 04 Leverkusen":"B04","VfL Bochum":"bochum","1. FSV Mainz 05":"M05", "VfB Stuttgart": "STU", "1. FC Koeln": "KOE", "1. FC Union Berlin": "FCU", "Arminia Bielefeld": "BIE"}
clubkeys={"Eintracht Frankfurt":"frankfurt", "TSG Hoffenheim":"hoffenheim","Bayern Muenchen": "bayern","VfL Wolfsburg":"wolfsburg","Borussia Dortmund":"dortmund","FC Augsburg":"augsburg","RB Leipzig": "leipzig","SC Freiburg":"freiburg","Hertha BSC":"herthabsc","SpVgg Greuther Fuerth": "fuerth","Bor. Moenchengladbach": "mgladbach","Bayer 04 Leverkusen":"leverkusen","VfL Bochum":"bochum","1. FSV Mainz 05":"mainz", "VfB Stuttgart": "stuttgart", "1. FC Koeln": "KOE", "1. FC Union Berlin": "FCU", "Arminia Bielefeld": "BIE"}

for item in clubcodes:
    clubes = list(clubcodes.keys())

with urllib.request.urlopen('https://raw.githubusercontent.com/enadol/bundesliga/main/bundesliga-2022.txt') as response:
	data = response.read()

	data2 = data.decode('utf-8')

	filename = "core.txt"

	archivo = open(filename, "w", newline = '\n')

	data2 = data2.replace("ö", "oe")

	data2 = data2.replace("ü", "ue")

	lines = data2.splitlines()
    
getRepeats()
        
archivo.close()



    
for line in lines:
    if line.startswith('['):
        date = line
        lstdates.append(date)
    elif line == ' ':
        vacia = line
    elif line.startswith('Spieltag'):
        mday = line
    elif "Bundesliga" in line:
        titulo = line
    else:
        if line.startswith('  20.30'):
            line = line.split('20.30')[1]
        elif line.startswith('  18.30'):
            line = line.split('18.30')[1]
        elif line.startswith('  15.30'):
            line = line.split('15.30')[1]
        elif line.startswith('  18.00'):
            line = line.split('18.00')[1]
        else:
            line = line
        
        
        
        location = line.split('-', 1) #puede ser :
        locations.append(location) #se puede borrar luego
        if len(location) > 1:
            home = location[0]
            homes.append(home.lstrip())
            away = location[1]
            aways.append(away)
            

        
for i in range(0, len(homes)):
    local = homes[i].split('  ')
    if local[len(local)-1] != '':
        if local[len(local)-1] !=' ':
            goalshome = local[len(local)-1]
            lstgoalshome.append(goalshome.strip())
            lsthome.append(local[0])
            
    visitante = aways[i].split('  ')
    #visitante = visitante[0].split(' ', 1)            

    if visitante[0] != '':
        goalsaway = visitante[0][0]
        lstgoalsaway.append(goalsaway)
        lstaway.append(visitante[1].strip())
        i = i+1

structureDates() 
for f in range(0, len(lsthome)):
    
    element={
            "teamhome": lsthome[f],
            "teamaway": lstaway[f],
            "goalshome": int(lstgoalshome[f]),
            "goalsaway": int(lstgoalsaway[f]),
            "pointslocal": getPuntos(int(lstgoalshome[f]), int(lstgoalsaway[f]))[0],
            "pointsvisitor": getPuntos(int(lstgoalshome[f]), int(lstgoalsaway[f]))[1],
            "date": datesStructured[f]
            }
    matches.append(element) 

for club in clubes:
    count = 0
    for y in range(0, len(lsthome)):
        if lsthome[y]==club or lstaway[y] == club:
            count = count+1

      