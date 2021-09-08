from sklearn.neural_network import MLPClassifier
from sklearn.datasets import load_breast_cancer 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np 
import pandas as pd
import keras.models 
from keras.models import Sequential 
from keras.layers import Dense

pls = pd.read_csv("C:/Users/N0009/Documents/pls/premleaguescores.csv")

premdict = {
    "Man City":1,
    "Man United":2,
    "Liverpool":3,
    "Chelsea":4,
    "Leicester":5,
    "West Ham":6,
    "Tottenham":7,
    "Arsenal":8,
    "Leeds":9,
    "Everton":10,
    "Aston Villa":11,
    "Newcastle":12,
    "Wolves":13,
    "Crystal Palace":14,
    "Southampton":15,
    "Brighton":16,
    "Burnley":17,
    "Fulham":18,
    "West Brom":19,
    "Sheffield United":20
}

home_team_list = pls['HomeTeam'].tolist()
for i in range(len(home_team_list)):
    home_team_list[i] = float(premdict[home_team_list[i]])
home_team_list = np.array(home_team_list)

away_team_list = pls['AwayTeam'].tolist()
for i in range(len(away_team_list)):
    away_team_list[i] = float(premdict[away_team_list[i]])
away_team_list = np.array(away_team_list)

match_list = [list(x) for x in zip(home_team_list, away_team_list)]

scores = pls['WDL'].tolist()
score_list = [] 
for score in scores:
    score_list.append([score])

model = Sequential()
model.add(Dense(100,input_dim=2, activation = 'relu'))
model.add(Dense(50, activation = 'relu'))
model.add(Dense(50, activation = 'relu'))
model.add(Dense(1, activation = 'sigmoid'))
model.compile(loss = 'mean_squared_error', optimizer = 'adam', metrics = ['accuracy'])

model.fit(match_list,score_list,epochs=500, batch_size=3)

prem_team_list = list(premdict.keys())
twenty_list = []
for i in range(1,21):
    twenty_list.append("{}".format(i))

is_team_selected = False
while(is_team_selected != True):
    team_selected = input("Select Team Name or Rank: ")
    if(team_selected in prem_team_list):
        team = prem_team_list.index(team_selected)
        is_team_selected = True
        print("Team Selected: " + prem_team_list[team] + "/ Rank No. " + str(team+1) + "\n")
    elif(team_selected in twenty_list):
        team = int(team_selected) - 1
        is_team_selected = True
        print("Team Selected: " + prem_team_list[team] + "/ Rank No. " + str(team+1) + "\n")
    else:
        print("Invalid Choice")

team = team + 1

for i in range(1,21):
    if (i!= int(team)):
        print("----------------------------------------------------------------")
        print("PREDICTION: {0} ({1}) vs {2} ({3})".format(list(premdict.keys())[list(premdict.values()).index(team)],team,list(premdict.keys())[list(premdict.values()).index(i)], i))
        print ("HOME FIXTURE")
        print("Chance of {0} Win:".format(list(premdict.keys())[list(premdict.values()).index(team)]))
        print(model.predict(np.array([[team,i]])))
        print("Actual Result:")
        print(score_list[match_list.index([team,i])])
        print("")
        print("PREDICTION: {0} ({1}) vs {2} ({3})".format(list(premdict.keys())[list(premdict.values()).index(i)], i, list(premdict.keys())[list(premdict.values()).index(team)],team))
        print("AWAY FIXTURE")
        print("Chance of {0} Win:".format(list(premdict.keys())[list(premdict.values()).index(i)]))
        print(model.predict(np.array([[i,team]])))
        print("Actual Result:")
        print(score_list[match_list.index([i,team])])
        print("")
        print("----------------------------------------------------------------")