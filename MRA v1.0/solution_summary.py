import pandas as pd


solution = {('ES3', 'RM3', 3): 1.0, ('Fire1', 'RM2', 4): 0.0, ('Z2', 'W4', 1): 0.0, ('Z1', 'W2', 1): 0.0, ('Fire1', 'RM2', 2): 0.0, ('Z2', 'W4', 3): 0.0, ('Z1', 'W2', 3): 0.0, ('Z4', 'W1', 4): 0.0, ('Z7', 'W6', 4): 0.0, ('Z9', 'RC1', 4): 13.0, ('Govt', 'RC1', 4): 8.0, ('Z7', 'W6', 2): 1352.0, ('Z9', 'RC1', 1): 0.0, ('Z4', 'W1', 2): 0.0, ('Z9', 'RC1', 3): 0.0, ('ES1', 'RM3', 2): 0.0, ('ES4', 'RM3', 4): 0.0, ('Z8', 'RM1', 4): 0.0, ('Z1', 'W4', 2): 2196.0, ('MS2', 'RC3', 3): 1.0, ('HS', 'RC3', 1): 0.0, ('Z6', 'W5', 2): 0.0, ('HC', 'RC2', 4): 0.0, ('ES4', 'RM3', 2): 0.0, ('Z8', 'RM1', 2): 0.0, ('Z9', 'S2', 4): 6.0, ('MS2', 'RC3', 1): 0.0, ('Z8', 'RC1', 2): 0.0, ('Z6', 'W1', 2): 0.0, ('ES1', 'RM3', 4): 0.0, ('Z8', 'RC1', 4): 0.0, ('Z1', 'W4', 4): 0.0, ('Z3', 'W4', 1): 0.0, ('Z6', 'W5', 4): 0.0, ('HC', 'RC2', 2): 1.0, ('Z3', 'W2', 3): 0.0, ('Z3', 'W1', 3): 0.0, ('Z9', 'S2', 2): 0.0, ('Z3', 'W4', 3): 0.0, ('Z4', 'W5', 1): 0.0, ('Z3', 'W2', 1): 0.0, ('Z4', 'W2', 1): 0.0, ('Z3', 'W1', 1): 300.0, ('Z4', 'W5', 3): 25.0, ('Z8', 'S1', 4): 0.0, ('Z9', 'RM1', 3): 46.0, ('Z4', 'W2', 3): 0.0, ('Z11', 'S4', 2): 0.0, ('Z9', 'RM1', 1): 0.0, ('Z1', 'W3', 3): 50.0, ('Z5', 'W1', 4): 0.0, ('Z6', 'W1', 3): 0.0, ('MS1', 'RC3', 4): 1.0, ('Z11', 'S4', 4): 45.0, ('Z1', 'W3', 1): 0.0, ('Z6', 'W1', 1): 700.0, ('Z8', 'S1', 2): 0.0, ('ES2', 'RM3', 1): 0.0, ('Z2', 'W2', 4): 0.0, ('ES3', 'RM3', 4): 0.0, ('ES2', 'RM3', 3): 1.0, ('Z9', 'S1', 1): 0.0, ('Fire2', 'RM2', 4): 0.0, ('Fire2', 'RM2', 2): 0.0, ('MS1', 'RC3', 2): 0.0, ('Z2', 'W1', 2): 0.0, ('Z9', 'S1', 3): 0.0, ('Z10', 'S3', 2): 0.0, ('ES3', 'RM3', 2): 0.0, ('Z10', 'S3', 4): 0.0, ('Fire1', 'RM2', 3): 1.0, ('Z2', 'W4', 2): 800.0, ('Z2', 'W1', 4): 0.0, ('Z7', 'W6', 3): 0.0, ('Fire1', 'RM2', 1): 0.0, ('Z2', 'W4', 4): 0.0, ('Z1', 'W2', 2): 2000.0, ('Z5', 'W1', 2): 0.0, ('Z1', 'W2', 4): 0.0, ('Z4', 'W1', 1): 2482.6974458134937, ('MS1', 'RC3', 1): 0.0, ('Z2', 'W2', 2): 700.0, ('Z7', 'W6', 1): 0.0, ('Z1', 'W4', 3): 0.0, ('Z9', 'RC1', 2): 0.0, ('ES1', 'RM3', 3): 1.0, ('Z6', 'W5', 3): 0.0, ('Z5', 'W1', 3): 0.0, ('ES4', 'RM3', 3): 1.0, ('Z1', 'W4', 1): 0.0, ('Govt', 'RC1', 2): 0.0, ('MS2', 'RC3', 2): 0.0, ('ES1', 'RM3', 1): 0.0, ('Z6', 'W5', 1): 77.0, ('Z8', 'RC1', 1): 0.0, ('ES4', 'RM3', 1): 0.0, ('Z8', 'RM1', 3): 30.0, ('Z3', 'W4', 4): 0.0, ('Z8', 'RC1', 3): 11.0, ('Z4', 'W2', 4): 0.0, ('Z8', 'RM1', 1): 0.0, ('Z9', 'S2', 1): 0.0, ('HS', 'RC3', 4): 0.0, ('HC', 'RC2', 1): 0.0, ('Z3', 'W2', 4): 0.0, ('Z3', 'W1', 2): 0.0, ('MS1', 'RC3', 3): 0.0, ('Z9', 'S2', 3): 0.0, ('HC', 'RC2', 3): 0.0, ('Z3', 'W2', 2): 300.0, ('Z3', 'W4', 2): 200.0, ('Z4', 'W1', 3): 84.30255418650631, ('Z11', 'S4', 1): 0.0, ('Z4', 'W2', 2): 1000.0, ('Z4', 'W5', 2): 0.0, ('Z11', 'S4', 3): 0.0, ('Z9', 'RM1', 2): 0.0, ('Z1', 'W3', 2): 0.0, ('Z3', 'W1', 4): 0.0, ('Z6', 'W1', 4): 0.0, ('Z4', 'W5', 4): 0.0, ('Z8', 'S1', 1): 0.0, ('ES2', 'RM3', 4): 0.0, ('Z9', 'S1', 4): 29.0, ('HS', 'RC3', 3): 2.0, ('Z8', 'S1', 3): 16.0, ('Fire2', 'RM2', 1): 0.0, ('Z9', 'RM1', 4): 0.0, ('Z1', 'W3', 4): 0.0, ('Z5', 'W1', 1): 1856.0, ('Fire2', 'RM2', 3): 1.0, ('Z10', 'S3', 1): 0.0, ('MS2', 'RC3', 4): 0.0, ('Govt', 'RC1', 1): 0.0, ('Z2', 'W1', 3): 0.0, ('ES2', 'RM3', 2): 0.0, ('Z9', 'S1', 2): 0.0, ('Z2', 'W2', 3): 0.0, ('HS', 'RC3', 2): 0.0, ('Z10', 'S3', 3): 25.0, ('Govt', 'RC1', 3): 0.0, ('Z2', 'W1', 1): 767.0, ('Z2', 'W2', 1): 0.0, ('ES3', 'RM3', 1): 0.0} 

csv_file = open('Policy.csv', 'w')
csv_file.write("" + "Zone" + "," + "Type" + "," + "Level" + "," + "Num_buding" "\n")
    
for key,value in solution.items():
    
    csv_file.write("" + str(key[0]) + ", " + str(key[1]) + ", " + str(key[2]) + "," + str(value) + "\n")



dataframe2 = pd.DataFrame(pd.read_csv('OLSparameters.csv', header='infer'))
data2_dc = dataframe2.set_index('Zone').to_dict()
residents_list =  pd.unique(dataframe2['Zone'].values.ravel()).tolist()  #list of zones

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
    

loss = 0
for i,j,k in solution.keys():
    loss += solution[i,j,k]*total_loss[i,j,k]
    

print loss

investment = {"H":0,"M":0,"L":0}

for i,j,k in IJK:
    if i in residents_list:
        if data2_dc['Income'][i] == "H":
            investment["H"] += (solution[i,j,k] - current_building[i,j,k])*value[i,j,k]
        elif data2_dc['Income'][i] == 'M':
            investment['M'] += (solution[i,j,k] - current_building[i,j,k])*value[i,j,k]
        else:
            investment['L'] += (solution[i,j,k] - current_building[i,j,k])*value[i,j,k]
        
total_investment = sum(investment.values())

print total_investment

for key,value in investment.items():
    investment[key] = value/float(total_investment)

print investment