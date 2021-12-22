import numpy as np
import pandas as pd
import math 
import warnings

def computeStats(data, team):
    df = data[data['team'] == team]  #filter by team
    #record FGM and FGA 
    FGM = (df.loc[(df['fgmade']  == 1 )]).shape[0]
    FGA = df.shape[0]


    df['dist'] = (df["x"] ** 2 + df['y'] ** 2) ** (1/2) #Calculate distance from center of hoop for non corner 3s 

    C3 = df.loc[(df['x'] > 22) & (df['y'] <= 7.8)] # corner 3s
    df = df.drop(df[(df.x > 22) & (df.y <= 7.8)].index)

    NC = df.loc[(df['dist'] > 23.75) ] # Non corner 3s 
    twoPT = df.drop(df[(df.dist > 23.75)].index) #All 3 pointers are removed from the df 

    threePM = ((C3.loc[(C3['fgmade']  == 1 )]).shape[0]) + ((NC.loc[(NC['fgmade']  == 1 )]).shape[0])

    eFG = (FGM + (.5 * threePM))/(FGA)

    twoPercentage  = (twoPT.shape[0] / FGA) * 100
    twoPeFG = (((twoPT.loc[(twoPT['fgmade']  == 1 )]).shape[0]) + (.5 * 0))/(twoPT.shape[0])

    NCPercentage  = (NC.shape[0] / FGA) * 100
    NCeFG = (((NC.loc[(NC['fgmade']  == 1 )]).shape[0]) + (.5 * ((NC.loc[(NC['fgmade']  == 1 )]).shape[0])))/(NC.shape[0])

    c3Percentage  = (C3.shape[0] / FGA) * 100
    C3PeFG = (((C3.loc[(C3['fgmade']  == 1 )]).shape[0]) + (.5 * ((C3.loc[(C3['fgmade']  == 1 )]).shape[0])))/(C3.shape[0])
    
    return twoPeFG,NCeFG,C3PeFG, twoPercentage,NCPercentage,c3Percentage

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    data = pd.read_csv('shots_data.csv')
    data['x'] = data['x'].abs()
    twoPeFG,NCeFG,C3PeFG, twoPercentage,NCPercentage,c3Percentage = computeStats(data, 'Team A')
    print('Team A')
    print('2 point eFG = ', twoPeFG)
    print('Non Corner eFG = ', NCeFG)
    print('Corner eFG = ', C3PeFG)
    print('Percentage of shots that were two pointers = ', twoPercentage)
    print('Percentage of shots that were threes but not in the corner = ', NCPercentage)
    print('Percentage of shots that were corner threes = ', c3Percentage)
    twoPeFG,NCeFG,C3PeFG, twoPercentage,NCPercentage,c3Percentage = computeStats(data, 'Team B')
    print('Team B')
    print('2 point eFG = ', twoPeFG)
    print('Non Corner eFG = ', NCeFG)
    print('Corner eFG = ', C3PeFG)
    print('Percentage of shots that were two pointers = ', twoPercentage)
    print('Percentage of shots that were threes but not in the corner = ', NCPercentage)
    print('Percentage of shots that were corner threes = ', c3Percentage)