from lxml import html
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import requests
import pandas as pd
import numpy as np
import seaborn as sns

'exec(%matplotlib inline)'

player_name=[]
player_club=[]
player_height=[]

baselink = "https://www.worldfootball.net/players_list/eng-premier-league-2016-2017/nach-mannschaft/"
for i in range(1,13):
    url = baselink
    url = url + str(i) + "/"
    # print(url)
    html = urlopen(url)
    soup = BeautifulSoup(html, 'lxml') #using html.parser instead of lmxl due to parser library issue

    # Finding all <tr> of the table
    rows = soup.find_all('tr')

    for row in rows[2:52]:
        row_td_name = str(row.find_all('td')[0].contents)
        row_td_name = re.sub('<[^>]+>', '', row_td_name).lstrip('[').rstrip(']') #removes HTML tags
        player_name.append(row_td_name)

        row_td_club= str(row.find_all('td')[2].contents)
        row_td_club=re.sub('<[^>]+>', '', row_td_club).lstrip('[').rstrip(']') #removes HTML tags
        player_club.append(row_td_club)

        row_td_height= str(row.find_all('td')[4].contents)
        row_td_height = row_td_height.lstrip('[\'').rstrip('\'] cm') #removes HTML tags. Default unit cm
        player_height.append(row_td_height)

#print(player_name)
# player_club = list(set(player_club))
#elements getting randomised when converting into set. Have to FIx!!
# print(len(player_club))
#print(player_height)

PlayerDetails = []
for i in range(len(player_name)):
    a = []
    a.append(player_name[i])
    a.append(player_height[i])
    a.append(player_club[i])
    PlayerDetails.append(a)

#print(PlayerDetails)
mean = []

#Dropping  ??? from height list
player_height = ['0' if x == '???' else x for x in player_height]

#Converting List to int
player_height = list(map(int,player_height))


#Finding Mean Height Of Each Team
i = 0
sum = 0
mean = 0
ct = 1
zero_ct = 0
prev = player_club[0]
TeamHeight = {}
while i < len(player_club):
    if player_club[i] == prev:
        if player_height[i] == 0:
            zero_ct += 1
            i += 1
            continue
        if i == len(player_club)-1:
            mean = sum/(ct - zero_ct)
            TeamHeight[player_club[i-1]] = round(mean,2)

        sum += player_height[i]

    else:
        mean = sum/(ct - zero_ct)
        zero_ct = 0
        TeamHeight[player_club[i-1]] = round(mean,2)
        ct = 0
        sum = 0
        mean = 0
        sum += player_height[i]
    ct += 1
    prev = player_club[i]
    i += 1

# Substituting the unknown height(0) with the mean height of other players
player_height = [TeamHeight[player_club[x]] if x == 0 else x for x in player_height]

#Now Parsing the list again to update the mean height of players per team
i = 0
sum = 0
mean = 0
ct = 1

prev = player_club[0]
TeamHeight = {}
while i < len(player_club):
    if player_club[i] == prev:
        sum += player_height[i]
        if i == len(player_club)-1:
            mean = sum/(ct)
            TeamHeight[player_club[i-1]] = round(mean,2)

    else:
        mean = sum/(ct)
        TeamHeight[player_club[i-1]] = round(mean,2)
        ct = 0
        sum = 0
        mean = 0
        sum += player_height[i]
    ct += 1
    prev = player_club[i]
    i += 1



#Adding Westbrom

print(TeamHeight)

#Creating DataFrame for dictionary

TeamMeanHeight = pd.DataFrame.from_dict(TeamHeight,orient='index')

print(TeamMeanHeight)

