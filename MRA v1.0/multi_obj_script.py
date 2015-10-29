"""
Program to call MAR function to find the optimal solutions

Author: Weili Zhang
Email: weili.zhang-1@ou.edu

"""

import pandas as pd
import numpy as np
from gurobipy import *  #gurobi is state-of-the-art LP solver

#custom functions
def sum_dic_by_keyset(dic, key_set):
    
    temp = 0
    for i in key_set:
        temp += dic[i]
        
    return temp


def MRA(Index_ijk, bijk, v, l, g, d, budget, dis_bound, zone_value, zone_building):
    
    """
    Mitigation Resource Allocation, version 1.0
    
    Author: Weili Zhang
    Email: weili.zhang-1@ou.edu
    
    Input:
    
    IIK - set of index (i,j,k)
    b - pre-retrofit number of buildings in zone i type j level k
    l - total loss of a building in zone i type j level k
    v - appraise value of a building in zone i type j level k
    g - building loss of a building in zone i type j level k
    d - pre-retrofit difference of dislocation among high-income, median -income, low-income
    budget - total budget
    other OLS coefficients and parameters are required but not list in the function input
   
    
    Algorithm:
    MRA model
    
    Output:
    
    - total direct economic loss
    - total dislocation
    - optimal policies
    
    """
    
    
    global coe, q, h, m, s, High, Middle, Low, residents_list
    
    #Gurobi model set
    mod = Model('MRA')
    mod.setParam( 'OutputFlag', 0) 
    mod.setParam( 'LogToConsole', 0 )
    mod.setParam( 'LogFile', "" )   
    mod.params.threads = 1
    mod.params.NodefileStart = 0.5
    mod.params.timeLimit = 600
    
    
    Index_ijk = tuplelist(Index_ijk)
    
    x = {}  #post-retrofit number of buildings in zone i type j level k
    y = {}  #post-retrofit number of dislocated household in zone i
    
    #define variables
    for i, j, k in Index_ijk:
        x[i, j, k] = mod.addVar(name='#Building_%s_%s_%s' % (i, j, k), obj=l[i, j, k], lb = 0)
        
    for i in residents_list:
        y[i] = mod.addVar(name='Dislocation_in_zone_%s' % (i), obj=0, lb=0)
    
    
    mod.update()

    #constraint 1, define the function to compute y_i
    for i in residents_list:
        mod.addConstr(y[i] == quicksum(g[a, b, c]*x[a, b, c] for a,b,c in Index_ijk.select(i, '*', '*'))
                    /(100.00*zone_value[i])
                    *(coe[0]+coe[1]*q[i]+coe[2]*h[i]+coe[3]*m[i]+coe[4]*s[i])*zone_building[i])
    
    
    #constraint 2, total dislocation is less or equal to the pre-defined bound
    mod.addConstr(quicksum(y[a] for a in residents_list) <= dis_bound)
    
    
    #constraint 3, number of buildings for type k
    I = {}
    Z = []
    for i, j, k in IJK:
        if i not in Z:
            Z.append(i)
        
        
        
    for i, j, k in IJK:
        if i not in I.keys():
            I[i] = [j]
        else:
            I[i].append(j)
    
    #constraint 3, number of buildings of type j in zone k equal to pre-retrofit        
    for i in Z:
        for j in I[i]:
            mod.addConstr(quicksum(x[a, b, c] for a, b, c in Index_ijk.select(i, j, '*')) ==
                        quicksum(bijk[a, b, c] for a, b, c in Index_ijk.select(i, j, '*')))
    
    #constraint 4, total investment is equal or less to budget
    mod.addConstr(quicksum(v[a, b, c]*x[a, b, c] for a, b, c in Index_ijk)
                - quicksum(v[a, b, c]*bijk[a, b, c] for a, b, c in Index_ijk)
                <= budget)
    
    #constraint 5, the difference of dislocation among high-income, median-income, low-income is equal or less to pre-retrofit
    mod.addConstr(quicksum(y[a] for a in High) - quicksum(y[a] for a in Middle)
                + quicksum(y[a] for a in Middle) - quicksum(y[a] for a in Low)
                + quicksum(y[a] for a in High) - quicksum(y[a] for a in Low)
                <= d)
    
    mod.addConstr(quicksum(y[a] for a in High) - quicksum(y[a] for a in Middle)
                + quicksum(y[a] for a in Middle) - quicksum(y[a] for a in Low)
                + quicksum(y[a] for a in High) - quicksum(y[a] for a in Low)
                >= -1*d)
    
    
    mod.addConstr(quicksum(y[a] for a in Middle) - quicksum(y[a] for a in High)
                + quicksum(y[a] for a in Middle) - quicksum(y[a] for a in Low)
                + quicksum(y[a] for a in High) - quicksum(y[a] for a in Low)
                <= d)

    mod.addConstr(quicksum(y[a] for a in Middle) - quicksum(y[a] for a in High)
                + quicksum(y[a] for a in Middle) - quicksum(y[a] for a in Low)
                + quicksum(y[a] for a in High) - quicksum(y[a] for a in Low)
                >= -1*d)
    
    #************************************************************************
    
    mod.addConstr(quicksum(y[a] for a in High) - quicksum(y[a] for a in Middle)
                + quicksum(y[a] for a in Low) - quicksum(y[a] for a in Middle)
                + quicksum(y[a] for a in High) - quicksum(y[a] for a in Low)
                <= d)

    mod.addConstr(quicksum(y[a] for a in High) - quicksum(y[a] for a in Middle)
                + quicksum(y[a] for a in Low) - quicksum(y[a] for a in Middle)
                + quicksum(y[a] for a in High) - quicksum(y[a] for a in Low)
                >= -1*d)


    mod.addConstr(quicksum(y[a] for a in Middle) - quicksum(y[a] for a in High)
                + quicksum(y[a] for a in Low) - quicksum(y[a] for a in Middle)
                + quicksum(y[a] for a in High) - quicksum(y[a] for a in Low)
                <= d)

    mod.addConstr(quicksum(y[a] for a in Middle) - quicksum(y[a] for a in High)
                + quicksum(y[a] for a in Low) - quicksum(y[a] for a in Middle)
                + quicksum(y[a] for a in High) - quicksum(y[a] for a in Low)
                >= -1*d)    
    
    #************************************************************************
    
    
    mod.addConstr(quicksum(y[a] for a in High) - quicksum(y[a] for a in Middle)
                + quicksum(y[a] for a in Middle) - quicksum(y[a] for a in Low)
                + quicksum(y[a] for a in Low) - quicksum(y[a] for a in High)
                <= d)
    
    mod.addConstr(quicksum(y[a] for a in High) - quicksum(y[a] for a in Middle)
                + quicksum(y[a] for a in Middle) - quicksum(y[a] for a in Low)
                + quicksum(y[a] for a in Low) - quicksum(y[a] for a in High)
                >= -1*d)


    mod.addConstr(quicksum(y[a] for a in Middle) - quicksum(y[a] for a in High)
                + quicksum(y[a] for a in Middle) - quicksum(y[a] for a in Low)
                + quicksum(y[a] for a in Low) - quicksum(y[a] for a in High)
                <= d)

    mod.addConstr(quicksum(y[a] for a in Middle) - quicksum(y[a] for a in High)
                + quicksum(y[a] for a in Middle) - quicksum(y[a] for a in Low)
                + quicksum(y[a] for a in Low) - quicksum(y[a] for a in High)
                >= -1*d)

    #************************************************************************

    mod.addConstr(quicksum(y[a] for a in High) - quicksum(y[a] for a in Middle)
                + quicksum(y[a] for a in Low) - quicksum(y[a] for a in Middle)
                + quicksum(y[a] for a in Low) - quicksum(y[a] for a in High)
                <= d)

    mod.addConstr(quicksum(y[a] for a in High) - quicksum(y[a] for a in Middle)
                + quicksum(y[a] for a in Low) - quicksum(y[a] for a in Middle)
                + quicksum(y[a] for a in Low) - quicksum(y[a] for a in High)
                >= -1*d)


    mod.addConstr(quicksum(y[a] for a in Middle) - quicksum(y[a] for a in High)
                + quicksum(y[a] for a in Low) - quicksum(y[a] for a in Middle)
                + quicksum(y[a] for a in Low) - quicksum(y[a] for a in High)
                <= d)

    mod.addConstr(quicksum(y[a] for a in Middle) - quicksum(y[a] for a in High)
                + quicksum(y[a] for a in Low) - quicksum(y[a] for a in Middle)
                + quicksum(y[a] for a in Low) - quicksum(y[a] for a in High)
                >= -1*d)        
    
    #************************************************************************
    
    #constrain 6, retrofit can only be applied to higher level
    for i, j, k in bijk.keys():
        if bijk[i, j, k] > 0:
            for k_prime in range(1, k):
                mod.addConstr(x[i, j, k_prime]==0.0)
            
    
    mod.update()
    
    
    try:
        mod.optimize()
        if  mod.status == 2 or mod.status == 9:
            tot_loss = mod.objval
            strategy = mod.getAttr('x', x)
            dislocation = mod.getAttr('x', y)
            
            tot_dislocation = sum(dislocation.values())
            
            
            print dislocation_bound, tot_loss, tot_dislocation
            
            
            return tot_loss, tot_dislocation, strategy
        
        else:
            print "Gurobi status is", mod.status
            return - 1, -1, -1
            

  
    except:
        print "Gurobi error", mod.status
        
        
        return - 1, -1, -1
    
    
 

    
#load data from economic damage********************************************************************************
dataframe = pd.DataFrame(pd.read_csv('BuildingData.csv', header='infer'))
    
zone_list =  pd.unique(dataframe['Zone'].values.ravel()).tolist()  #list of zones
IJK =  zip(dataframe['Zone'], dataframe['Building Type'], dataframe['Level'])  #list of i,j,k
dataframe['IJK'] = IJK
data_dic = dataframe.set_index('IJK').to_dict() 

current_building = {} #current number of buildings of ijk
value = {}  #value of building ijk
building_loss = {} #building loss 
total_loss = {}    #total loss with conten

for i,j,k in IJK:
    current_building[i,j,k] = data_dic['CurretBuilding#'][i,j,k]
    value[i,j,k] = data_dic['ValuebyLevel'][i,j,k]
    building_loss[i,j,k] = data_dic['BuildingLoss'][i,j,k]
    total_loss[i,j,k] = data_dic['TotalLoss'][i,j,k]
    
#load data from social dislocation*****************************************************************************


dataframe2 = pd.DataFrame(pd.read_csv('OLSparameters.csv', header='infer'))
data2_dc = dataframe2.set_index('Zone').to_dict()
residents_list =  pd.unique(dataframe2['Zone'].values.ravel()).tolist()  #list of zones
q = {}  #percentage of black in residential zone i
h = {}  #percentage of vacant housing units in zone i
m = {}  #median household income in zone i
s = {}  #percentage of single family detached in zone i

for i in residents_list:
    q[i], h[i], m[i], s[i] = data2_dc['%B'][i], data2_dc['%VHU'][i], data2_dc['MHI'][i], data2_dc['%SFD'][i]

#compute current dislocation for each zone
coe = [0.99459, -0.00255,-0.01397,0.01114,-0.00297]  #coefficients in OLS

value_of_zone = {}  #appraize value of each zone
for zone in residents_list:
    value_of_zone[zone] = 0
    for i,j,k in IJK:
        if i==zone:
            value_of_zone[zone] += value[i,j,k]*current_building[i,j,k]
            
buildings_of_zone = {}  #number of buildings in each zone
for zone in residents_list:
    buildings_of_zone[zone] = 0
    for i,j,k in IJK:
        if i==zone:
            buildings_of_zone[zone] += current_building[i,j,k]

current_zone_dislocation = {} #current dislocation of each zone (the uppbound of social objective)
for zone in residents_list:
    current_zone_dislocation[zone] = 0
    temp = 0
    for i,j,k in IJK:
        if i  == zone:
            temp += building_loss[i,j,k]*current_building[i,j,k]
    current_zone_dislocation[zone] = (temp/(float(value_of_zone[zone])))*(coe[0]+coe[1]*q[zone]+coe[2]*q[zone]+coe[3]*m[zone]+coe[4]*s[zone])*buildings_of_zone[zone] / 100.00
        
        
current_total_dislocation = sum(current_zone_dislocation.values())

#compute the current dislocation difference for each residential zones
High, Middle, Low = [], [], []
for i in residents_list:
    if data2_dc['Income'][i] == "H":
        High.append(i)
    elif data2_dc['Income'][i] == "M":
        Middle.append(i)
    else:
        Low.append(i)
        

High_dislocation = sum_dic_by_keyset(current_zone_dislocation,High)
Middle_dislocation = sum_dic_by_keyset(current_zone_dislocation,Middle)
Low_dislocation = sum_dic_by_keyset(current_zone_dislocation,Low)

current_dislocation_difference = abs(High_dislocation-Middle_dislocation) + abs(High_dislocation-Low_dislocation) + abs(Low_dislocation-Middle_dislocation)  #difference among different income level zones


#compute the best dislocation for each zone
#assume all the buildings are at the highest level, what is the number of dislocatin
#this value is the lowbound for dislocation objective


best_buildings = {}

for i,j,k in IJK:
    if k == 4:
        best_buildings[i,j,k] = sum([current_building[i,j,1],current_building[i,j,2],current_building[i,j,3],current_building[i,j,4]])
    else:
        best_buildings[i,j,k] = 0
        

best_zone_dislocation = {} #current dislocation of each zone (the uppbound of social objective)
for zone in residents_list:
    best_zone_dislocation[zone] = 0
    temp = 0
    for i,j,k in IJK:
        if i  == zone:
            temp += building_loss[i,j,k]*best_buildings[i,j,k]
    best_zone_dislocation[zone] = (temp/(float(value_of_zone[zone])))*buildings_of_zone[zone]*(coe[0]+coe[1]*q[zone]+coe[2]*q[zone]+coe[3]*m[zone]+coe[4]*s[zone]) / 100.00
        
        
best_total_dislocation = sum(best_zone_dislocation.values())  #low bound for dislocated objective


#compute the maximun budget
max_budget = 0

for i, j, k in IJK:
    max_budget += value[i, j, k] * (best_buildings[i, j, k] - current_building[i, j, k])

#set a loop to find the pareto front

f1 = open('Pareto Front.txt','w')
f1.write('Total Loss, Total Dislocation \n')
f1.close()

   
step = 10




for percentage in np.arange(0, 1+0.01, 0.01):
    
    budget = percentage* (max_budget + 1) #percentage of max budget
    
    f2 = open('All solutions_budget_{}.txt'.format(percentage),'w')
    f2.write('Total Loss \t Total Dislocation \t Strategy \n')
    f2.close()     
    
    for dislocation_bound in np.arange(best_total_dislocation+1,current_total_dislocation+1+step, step):
        
        
        total_direct_loss, total_dislocation, strategy = MRA(IJK, current_building, value, total_loss,
                                                             building_loss, current_dislocation_difference,
                                                             budget, dislocation_bound, value_of_zone, buildings_of_zone)
        
        if total_direct_loss != -1:
            
        
            f1 = open('Pareto Front.txt','a')
            f1.write('{}, {}, {}, {} \n'.format(percentage, budget, total_direct_loss, total_dislocation))
            f1.close()
        
            f2 = open('All solutions_budget_{}.txt'.format(percentage),'a')
            f2.write('{}, {}, {} \n'.format(total_direct_loss, total_dislocation, strategy))
            f2.close()
        
