from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
from datetime import datetime

def writecsv(data):
    date = datetime.now().strftime('%Y-%m-%d')
    with open('excsv.csv','a',newline='',encoding='utf-8') as file:
        filewriter = csv.writer(file)
        filewriter.writerow(data)

alldata = {}

def footballtable(season):
    url = 'https://www.sanook.com/sport/football/table/premierleague/20'+ str(season) + '-20' + str(season + 1) + '/'
    webopen = urlopen(url)
    html_page = webopen.read()
    webopen.close()
    data = BeautifulSoup(html_page,'html.parser')

    try:
        team = data.find('td',{"class":"jsx-827658710"})
        year = data.find('h1',{"class":"jsx-1187604094"})
        
        champ = team.text.strip()
        year = year.text
        alldata[champ] = year
    except:
        pass
    
    
for i in range(10,20):
    footballtable(i)
    
for k,v in alldata.items():
    data = [k,v]
    writecsv(data)
    
print('save')
