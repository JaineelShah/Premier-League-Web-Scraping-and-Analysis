from lxml import html
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import requests
import pandas as pd
import wikipedia as wp
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import csv

'exec(%matplotlib inline)'




teams=[]
goals=[]

top_teams_keys=["Arsenal", "Chelsea","Liverpool","Manchester City", "Manchester United"]
with open('17-18.csv', 'r') as csvFile:
    reader=csv.reader(csvFile)
    for row in reader:
        teams.append(row[0])
        goals.append(int(row[1]))
csvFile.close()
# print(teams, goals)
goals_by_teams=dict(zip(teams,goals))
for i in list(goals_by_teams.keys()):
    if i not in top_teams_keys:
        del goals_by_teams[i]


print(goals_by_teams)


# print(goals_by_teams)

# TeamHeadedGoals = pd.DataFrame.from_dict(goals_by_teams,orient='index')
# TeamHeadedGoals.reset_index(inplace=True)
# TeamHeadedGoals.columns=["Team","   Headed Goals"]
# print("2017-18 Season")
#
# print(TeamHeadedGoals)


# goals_by_teams.clear()
# teams.clear()
# goals.clear()
#
with open('16-17.csv', 'r') as csvFile:
    reader=csv.reader(csvFile)
    for row in reader:
        teams.append(row[0])
        goals.append(int(row[1]))
csvFile.close()
# print(teams, goals)
goals_by_teams2=dict(zip(teams,goals))
# print(goals_by_teams)

for i in list(goals_by_teams.keys()):
    if i not in top_teams_keys:
        del goals_by_teams2[i]


print(goals_by_teams2)

# TeamHeadedGoals = pd.DataFrame.from_dict(goals_by_teams,orient='index')
# TeamHeadedGoals.reset_index(inplace=True)
# TeamHeadedGoals.columns=["Team","   Headed Goals"]
# print("2016-17 Season")
# print(TeamHeadedGoals)

goals_by_teams.clear()
teams.clear()
goals.clear()

with open('15-16.csv', 'r') as csvFile:
    reader=csv.reader(csvFile)
    for row in reader:
        teams.append(row[0])
        goals.append(int(row[1]))
csvFile.close()
# print(teams, goals)
goals_by_teams=dict(zip(teams,goals))
# print(goals_by_teams)

TeamHeadedGoals = pd.DataFrame.from_dict(goals_by_teams,orient='index')
TeamHeadedGoals.reset_index(inplace=True)
TeamHeadedGoals.columns=["Team","   Headed Goals"]
ManC_Headed = [10,5,13,8,12]
ManU_Headed = [10,12,5,9,12]
print("2015-16 Season")
print(TeamHeadedGoals)

goals_by_teams.clear()
teams.clear()
goals.clear()

with open('14-15.csv', 'r') as csvFile:
    reader=csv.reader(csvFile)
    for row in reader:
        teams.append(row[0])
        goals.append(int(row[1]))
csvFile.close()
# print(teams, goals)
goals_by_teams=dict(zip(teams,goals))
# print(goals_by_teams)

TeamHeadedGoals = pd.DataFrame.from_dict(goals_by_teams,orient='index')
TeamHeadedGoals.reset_index(inplace=True)
Arsenal_Headed = [12,10,13,17,13]
Chelsea_Headed = [6,10,6,8,17]
Liverpool_Headed = [14,5,12,12,12]

TeamHeadedGoals.columns=["Team","   Headed Goals"]
print("2014-15 Season")
print(TeamHeadedGoals)

goals_by_teams.clear()
teams.clear()
goals.clear()

with open('13-14.csv', 'r') as csvFile:
    reader=csv.reader(csvFile)
    for row in reader:
        teams.append(row[0])
        goals.append(int(row[1]))
csvFile.close()
# print(teams, goals)
goals_by_teams=dict(zip(teams,goals))
# print(goals_by_teams)

TeamHeadedGoals = pd.DataFrame.from_dict(goals_by_teams,orient='index')
TeamHeadedGoals.reset_index(inplace=True)
TeamHeadedGoals.columns=["Team","   Headed Goals"]
print("2013-14 Season")
print(TeamHeadedGoals)

goals_by_teams.clear()
teams.clear()
goals.clear()

# TeamHeadedGoals.plot(x = 'Team', y = '   Headed Goals', kind='bar')
# plt.show()



Seasons = ['2013-14','2014-15','2015-16','2016-17','2017-18']

plt.plot([],[], color='orangered', label='Arsenal')
plt.plot([],[], color='blue', label='Chelsea')
plt.plot([],[], color='maroon', label='Liverpool')
plt.plot([],[], color='lightblue', label='Manchester Cty.')
plt.plot([],[], color='red', label='Manchester Utd.')

plt.stackplot(Seasons, Arsenal_Headed, Chelsea_Headed, Liverpool_Headed, ManC_Headed,ManU_Headed, edgecolor='black', colors=['orangered', 'blue', 'maroon','lightblue','red'])

plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

plt.title('Headed Goals Top 5 teams over the last 5 years')
plt.xlabel('Seasons')
plt.ylabel('Headed Goals')

plt.show()

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

print(PlayerDetails)
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
        # if i == len(player_club)-1:
        #     mean = sum/(ct - zero_ct)
        #     TeamHeight[player_club[i-1]] = round(mean,2)

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
TeamHeight['West Ham United'] = 181.54

print(TeamHeight)

Teams = list(TeamHeight.keys())
Heights = list(TeamHeight.values())
plt.bar(Teams,Heights)
plt.show()

#Creating DataFrame for dictionary

TeamMeanHeight = pd.DataFrame.from_dict(TeamHeight,orient='index')
TeamMeanHeight.columns = ['Mean Height']
plt.xlabel('Team Name')
plt.ylabel('Mean Height')
plt.title('Mean Height Per Team')


# Goal Difference Table of 13-14 Season

top_teams = ['Arsenal','Manchester United', 'Manchester City (C)','Chelsea','Liverpool']
print('''
2013–14 Season

''')


link4 = wp.page("2013–14 Premier League").html().encode("UTF-8")
GDtable13_14 = pd.read_html(link4)[4]
GDtable13_14.drop([2,3,4,5,6,7,9,10], axis = 1,inplace = True)
PD_LiverpoolPos = {'Seasons':['2013-14','2014-15','2015-16','2016-17','2017-18'],'Position':[2,6,8,4,4]}
GDtable13_14.columns = ["Position","Team","GD"]
GDtable13_14.drop([0],axis = 0,inplace = True)
PD_ArsenalPos = {'Seasons':['2013-14','2014-15','2015-16','2016-17','2017-18'],'Position':[4,3,2,5,6]}
GDtable13_14.reset_index()
print(GDtable13_14)


GDtable13_14_copy = GDtable13_14

GDtable13_14_copy.drop([5,6,8,9,10,11,12,13,14,15,16,17,18,19,20],axis=0, inplace= True)

# GDtable17_18_copy[GDtable17_18_copy.Team not in top_teams]
print('\n\n\n',GDtable13_14_copy)

# Goal Difference Table of 14-15 Season

print('''

2014–15 Season

''')


link3 = wp.page("2014–15 Premier League").html().encode("UTF-8")
GDtable14_15 = pd.read_html(link3)[4]
PD_LiverpoolGD = {'Seasons':['2013-14','2014-15','2015-16','2016-17','2017-18'],'Goal Difference':[51,4,13,36,46]}
GDtable14_15.drop([2,3,4,5,6,7,9,10], axis = 1,inplace = True)
GDtable14_15.columns = ["Position","Team","GD"]
GDtable14_15.drop([0],axis = 0,inplace = True)
GDtable14_15.reset_index()
print(GDtable14_15)

PD_ArsenalGD = {'Seasons':['2013-14','2014-15','2015-16','2016-17','2017-18'],'Goal Difference':[27,35,29,33,23]}
PD_ChelseaGD = {'Seasons':['2013-14','2014-15','2015-16','2016-17','2017-18'],'Goal Difference':[44,41,6,52,24]}

GDtable14_15_copy = GDtable14_15

GDtable14_15_copy.drop([5,7,8,9,10,11,12,13,14,15,16,17,18,19,20],axis=0, inplace= True)

# GDtable17_18_copy[GDtable17_18_copy.Team not in top_teams]
print('\n\n\n',GDtable14_15_copy)

# Goal Difference Table of 15-16 Season

print('''

2015–16 Season

''')

link2 = wp.page("2015–16 Premier League").html().encode("UTF-8")
GDtable15_16 = pd.read_html(link2)[4]
GDtable15_16.drop([2,3,4,5,6,7,9,10], axis = 1,inplace = True)
GDtable15_16.columns = ["Position","Team","GD"]
GDtable15_16.drop([0],axis = 0,inplace = True)
GDtable15_16.reset_index()
print(GDtable15_16)


GDtable15_16_copy = GDtable15_16

GDtable15_16_copy.drop([1,3,6,7,9,11,12,13,14,15,16,17,18,19,20],axis=0, inplace= True)

# GDtable17_18_copy[GDtable17_18_copy.Team not in top_teams]
print('\n\n\n',GDtable15_16_copy)


# Goal Difference Table of 16-17 Season

print('''

2016–17 Season

''')
PD_ManUPos = {'Seasons':['2013-14','2014-15','2015-16','2016-17','2017-18'],'Position':[7,4,5,6,2]}
link = wp.page("2016–17 Premier League").html().encode("UTF-8")
GDtable16_17 = pd.read_html(link)[5]
GDtable16_17.drop([2,3,4,5,6,7,9,10], axis = 1,inplace = True)
GDtable16_17.columns = ["Position","Team","GD"]
GDtable16_17.drop([0],axis = 0,inplace = True)
GDtable16_17.reset_index()
print(GDtable16_17)

GDtable16_17_copy = GDtable16_17

GDtable16_17_copy.drop([2,7,8,9,10,11,12,13,14,15,16,17,18,19,20],axis=0, inplace= True)

# GDtable17_18_copy[GDtable17_18_copy.Team not in top_teams]

print('\n\n\n',GDtable16_17_copy)

#Goal Difference Table of 17-18 Season

print('''
2017–18 Season

''')

# Opening HTML form page of the season
link = wp.page("2017–18 Premier League").html().encode("UTF-8")
#Reading the 5th table from the wikipedia page
GDtable17_18 = pd.read_html(link)[4]

#Now Dropping Unrequired Columns from the table
GDtable17_18.drop([2,3,4,5,6,7,9,10], axis = 1,inplace = True)
PD_ManCPos = {'Seasons':['2013-14','2014-15','2015-16','2016-17','2017-18'],'Position':[1,2,4,3,1]}

#Renaming Columns of the Dataframe
GDtable17_18.columns = ["Position","Team","GD"]
GDtable17_18.drop([0], axis = 0, inplace = True)
print(GDtable17_18)


GDtable17_18_copy = GDtable17_18

GDtable17_18_copy.drop([3,7,8,9,10,11,12,13,14,15,16,17,18,19,20],axis=0, inplace= True)
PD_ChelseaPos = {'Seasons':['2013-14','2014-15','2015-16','2016-17','2017-18'],'Position':[3,1,10,1,5]}

# GDtable17_18_copy[GDtable17_18_copy.Team not in top_teams]
print('\n\n\n',GDtable17_18_copy)


Arsenal_GD= PD_ArsenalGD
Arsenal_GD = pd.DataFrame.from_dict(Arsenal_GD)
Arsenal_Pos =  PD_ArsenalPos
Arsenal_Pos = pd.DataFrame.from_dict(Arsenal_Pos)


Chelsea_GD= PD_ChelseaGD
Chelsea_GD = pd.DataFrame.from_dict(Chelsea_GD)
Chelsea_Pos= PD_ChelseaPos
Chelsea_Pos = pd.DataFrame.from_dict(Chelsea_Pos)



Liv_GD= PD_LiverpoolGD
Liv_GD = pd.DataFrame.from_dict(Liv_GD)
Liv_Pos = PD_LiverpoolPos
Liv_Pos = pd.DataFrame.from_dict(Liv_Pos)

ManC_GD = {'Seasons':['2013-14','2014-15','2015-16','2016-17','2017-18'],'Goal Difference':[65,45,30,41,79]}
ManC_GD = pd.DataFrame.from_dict(ManC_GD)
ManC_Pos = PD_ManCPos
ManC_Pos = pd.DataFrame.from_dict(ManC_Pos)

ManU_GD = {'Seasons':['2013-14','2014-15','2015-16','2016-17','2017-18'],'Goal Difference':[21,25,14,25,40]}
ManU_GD = pd.DataFrame.from_dict(ManU_GD)
ManU_Pos = PD_ManUPos
ManU_Pos = pd.DataFrame.from_dict(ManU_Pos)

print('''
Plotting these dataframes
''')


print(ManC_GD)
print(ManC_Pos)
print(ManU_GD)
print(ManU_Pos)
print(Liv_GD)
print(Liv_Pos)
print(Chelsea_GD)
print(Chelsea_Pos)
print(Arsenal_GD)
print(Arsenal_Pos)


#Plotting Arsenal

fig = plt.figure(figsize=(10,6))

ax1 = fig.add_axes([0, 0, 1, 1])
ax2 = fig.add_axes([0.05, 0.65, 0.5, 0.3])
ax1.set_title('Arsenal Position')
ax1.plot(Arsenal_Pos['Seasons'],
         Arsenal_Pos['Position'],
         color='blue')
ax2.set_title('Arsenal GD')

ax2.plot(Arsenal_GD['Seasons'],
         Arsenal_GD['Goal Difference'],
         color='green')

plt.show()

#Plotting Chelsea
fig = plt.figure(figsize=(10,6))

ax1 = fig.add_axes([0, 0, 1, 1])
ax2 = fig.add_axes([0.05, 0.65, 0.5, 0.3])
ax1.set_title('Chelsea Position')
ax1.plot(Chelsea_Pos['Seasons'],
         Chelsea_Pos['Position'],
         color='blue')
ax2.set_title('Chelsea GD')

ax2.plot(Chelsea_GD['Seasons'],
         Chelsea_GD['Goal Difference'],
         color='green')

plt.show()

#Plotting Liverpool
fig = plt.figure(figsize=(10,6))

ax1 = fig.add_axes([0, 0, 1, 1])
ax2 = fig.add_axes([0.05, 0.65, 0.5, 0.3])
ax1.set_title('Liverpool Position')
ax1.plot(Liv_Pos['Seasons'],
         Liv_Pos['Position'],
         color='blue')
ax2.set_title('Liverpool GD')

ax2.plot(Liv_GD['Seasons'],
         Liv_GD['Goal Difference'],
         color='green')

plt.show()

#Plotting Manchester City
fig = plt.figure(figsize=(10,6))

ax1 = fig.add_axes([0, 0, 1, 1])
ax2 = fig.add_axes([0.05, 0.65, 0.5, 0.3])
ax1.set_title('Manchester City Position')
ax1.plot(ManC_Pos['Seasons'],
         ManC_Pos['Position'],
         color='blue')
ax2.set_title('Manchester City GD')

ax2.plot(ManC_GD['Seasons'],
         ManC_GD['Goal Difference'],
         color='green')

plt.show()

#Plotting Manchester United
fig = plt.figure(figsize=(10,6))

ax1 = fig.add_axes([0, 0, 1, 1])
ax2 = fig.add_axes([0.05, 0.65, 0.5, 0.3])
ax1.set_title('Manchester United Position')
ax1.plot(ManU_Pos['Seasons'],
         ManU_Pos['Position'],
         color='blue')
ax2.set_title('Manchester United GD')

ax2.plot(ManU_GD['Seasons'],
         ManU_GD['Goal Difference'],
         color='green')

plt.show()


response=requests.get('https://www.fctables.com/england/premier-league/')
soup=BeautifulSoup(response.text,'html.parser')
posts=soup.find_all(class_='table table-striped table-bordered table-hover table-condensed small')
# print(posts)
# rows = soup.find_all('tr')
# print(posts)
for item in posts:
    slist=str(item)


# slist=slist.replace(" ","")
slist = re.sub('\n', '', slist).lstrip('[').rstrip(']')
slist = re.sub('<[^>]+>', '', slist).lstrip('[').rstrip(']')

avg_pass=[]
# print(slist)

for x in range(6):
    avg_pass.append(slist.split("%")[x+1][-5:])
    # print(avg_pass[x])
# avg_pass.append('0')
avg_pass.sort()
team_name=[]
for x in range(6):
    team_name.append(slist.split("%")[x+1][9:-5])
    team_name[0]="Manchester City"

# team_name[0], team_name[5] = team_name[5], team_name[0]
# team_name[1], team_name[4] = team_name[4], team_name[1]
# team_name[2], team_name[3] = team_name[3], team_name[2]



    # print(team_name[x])
# team_name.append('')
print("Top 6 Teams list by pass%:",team_name)
print("Avg.pass % per matchfor top 6 teams:", avg_pass)


response2=requests.get('https://www.fctables.com/england/premier-league/')
soup2=BeautifulSoup(response2.text,'html.parser')
posts2=soup2.find_all(class_='table table-striped table-bordered table-hover table-condensed')[2]
slist2=str(posts2)

team_name_2=team_name
slist2 = re.sub('<[^>]+>', '', slist2)
slist2 = re.sub('\n','',slist2)

poss=[]

for item in slist2.split(' '):
    poss.append(item)



# print(poss)
avg_poss=[]

avg_poss.append(poss[47].split("%")[0])
avg_poss.append(poss[132].split("%")[0])
avg_poss.append(poss[217].split("%")[0])
avg_poss.append(poss[302].split("%")[0])
avg_poss.append(poss[387].split("%")[0])
avg_poss.append(poss[473].split("%")[0])

avg_poss.sort()

team_name_2[0], team_name_2[5] = team_name_2[5], team_name_2[0]
team_name_2[1], team_name_2[4] = team_name_2[4], team_name_2[1]
team_name_2[2], team_name_2[3] = team_name_2[3], team_name_2[2]
# team_name_2[0], team_name_2[5] = team_name_2[5], team_name_2[0]
print("Top 6 team list by possesion%",team_name_2)


print("Avg. possesion % per match for Top 6 Teams:",avg_poss)

plt.xlabel('Team Name')
plt.ylabel('Avg.Pass %')
plt.title('Average pass % for Top 6 Teams for (2018-19)')
plt.bar(team_name,avg_pass)

plt.show()

plt.xlabel('Team Name')
plt.ylabel('Avg.Possession %')
plt.title('Average possession % for Top 6 Teams for (2018-19)')
plt.bar(team_name_2,avg_poss)

plt.show()


