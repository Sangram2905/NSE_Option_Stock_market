# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 09:01:48 2020

@author: Sangram Phadke
"""
def fii_dii_pos():
    #Importing the libraries
    import numpy as np
    import pandas as pd
    from datetime import datetime , timedelta
    import csv
    
     
    Starttime = datetime.now().strftime("%Y-%m-%d %H:%M:%S") #program data pull start time
    Todaysdate = datetime.now().strftime("%d-%m-%Y")
    
    textdate = datetime.now().strftime("%d%m%Y")
    pdate = datetime.now().strftime("%d-%m-%Y")
    
    #yesterday = datetime.now() - timedelta(1)
    
    #ytextdate = datetime.strftime(yesterday, '%d%m%Y')
    
    #ytextdatestr = datetime.strftime(yesterday, "%d-%b-%Y")
    
    
    ##Importing the dataset
    
    ## Trading days logic 
    df_trading_days = pd.read_csv('TradingDays.csv')
    for num_td in range(len(df_trading_days)-1):
        if df_trading_days.iloc[num_td][0] == pdate :
            #print (df_trading_days.iloc[num_td][0])
            ptd =  (df_trading_days.iloc[num_td-1][0])
            ptdd = datetime.strptime(ptd, "%d-%m-%Y").date()
            ytextdate = ptdd.strftime("%d%m%Y")
            ytextdatestr = ptdd.strftime("%d-%b-%Y")
    
 
    
    FDPosition_file = 'fao_participant_oi_'+ytextdate+'.csv'
    FDPosition_file_Update = 'fao_participant_oi_'+ytextdate+'_up.csv'
    
    FD_stats_file = 'fii_stats_'+ytextdatestr+'.xls' 
    FD_stats_file_up = 'fii_stats_'+ytextdatestr+'_up.xls' 
    
    
    #Removing the header of CSV file
    
    with open(FDPosition_file,'r') as f:
        with open(FDPosition_file_Update,'w') as f1:
            next(f) # skip header line
            for line in f:
                f1.write(line)
                
                
    # conert to CSV to DataFrame
    dfnopos = pd.read_csv(FDPosition_file_Update)
    
    # Replacing absolute zero values 
    dfnopos = dfnopos.replace(0,1, regex=True)
    dfnopos = dfnopos.replace('\t,','', regex=True)
    
    
    #dfnopos["Last"] = pd.to_numeric(dfnopos["Chg. %"], downcast="float") ## convert string to numaric data
    
    ## Convert dat to float
    convert_dict = {'Future Index Long': float, 'Future Index Short': float,
           'Future Stock Long': float, 'Future Stock Short\t': float, 'Option Index Call Long': float,
           'Option Index Put Long': float, 'Option Index Call Short': float,
           'Option Index Put Short': float, 'Option Stock Call Long': float,
           'Option Stock Put Long': float, 'Option Stock Call Short': float,
           'Option Stock Put Short': float, 'Total Long Contracts\t': float,
           'Total Short Contracts': float} 
      
    dfnopos = dfnopos.astype(convert_dict) 
    #print(dfnopos.dtypes)
    
    # ## Index / FnO name
    # def fipo(num1,num2,num3):
    #     fipo_v = (dfnopos.iloc[num1][num2]) / ((dfnopos.iloc[num1][num2])+(dfnopos.iloc[num1][num3])) 
    #     fipo_v = fipo_v*100
    #     return fipo_v
    
    # fii_FI_long = fipo(2,1,2)
    # fii_FI_short = fipo(2,2,1)
    # fii_FS_long = fipo(2,3,4)
    # fii_FS_short = fipo(2,4,3)
    
    
    ## Empty list for calculation and append data
    
    idx_list= ['Client','DII','FII','Pro']
    fii_stat_list_name=['FII INDEX FUT','FII INDEX OPT','FII STOCK FUT','FII STOCK OPT',]
    
    
    fil_list = []
    fis_list = []
    fsl_list = []
    fss_list = []
    
    opIcl_list = []
    opIpl_list = []
    
    opIcs_list = []
    opIps_list = []
    
    opStcl_list = []
    opStpl_list = []
    
    opStcs_list = []
    opStps_list = []
    
    totall_list = []
    totals_list = []
    
    todayDate = []
    num1 = 0 # reseting loop variable
    for num1 in range(4):
        #Logic for Future index and Future stock
        filpo_v = (dfnopos.iloc[num1][1]) / ((dfnopos.iloc[num1][1])+(dfnopos.iloc[num1][2])) 
        filpo_v = filpo_v*100
        fil_list.append(filpo_v)
        fispo_v = (dfnopos.iloc[num1][2]) / ((dfnopos.iloc[num1][1])+(dfnopos.iloc[num1][2])) 
        fispo_v = fispo_v*100
        fis_list.append(fispo_v)
        fslpo_v = (dfnopos.iloc[num1][3]) / ((dfnopos.iloc[num1][3])+(dfnopos.iloc[num1][4])) 
        fslpo_v = fslpo_v*100
        fsl_list.append(fslpo_v)
        fsspo_v = (dfnopos.iloc[num1][4]) / ((dfnopos.iloc[num1][3])+(dfnopos.iloc[num1][4])) 
        fsspo_v = fsspo_v*100
        fss_list.append(fsspo_v)
        
    
        #Logic for Option index call and put option long and short
        opIclpo_v = (dfnopos.iloc[num1][5]) / ((dfnopos.iloc[num1][5])+(dfnopos.iloc[num1][7])) 
        opIclpo_v = opIclpo_v*100
        opIcl_list.append(opIclpo_v)
        
        opIplpo_v = (dfnopos.iloc[num1][6]) / ((dfnopos.iloc[num1][6])+(dfnopos.iloc[num1][8])) 
        opIplpo_v = opIplpo_v*100
        opIpl_list.append(opIplpo_v)
        
        opIcspo_v = (dfnopos.iloc[num1][7]) / ((dfnopos.iloc[num1][5])+(dfnopos.iloc[num1][7])) 
        opIcspo_v = opIcspo_v*100
        opIcs_list.append(opIcspo_v)
        
        opIpspo_v = (dfnopos.iloc[num1][8]) / ((dfnopos.iloc[num1][6])+(dfnopos.iloc[num1][8])) 
        opIpspo_v = opIpspo_v*100
        opIps_list.append(opIpspo_v)
        
        #Logic for Option stock call and put option long and short
        opStclpo_v = (dfnopos.iloc[num1][9]) / ((dfnopos.iloc[num1][9])+(dfnopos.iloc[num1][11])) 
        opStclpo_v = opStclpo_v*100
        opStcl_list.append(opStclpo_v)
        
        opStplpo_v = (dfnopos.iloc[num1][10]) / ((dfnopos.iloc[num1][10])+(dfnopos.iloc[num1][12])) 
        opStplpo_v = opStplpo_v*100
        opStpl_list.append(opStplpo_v)
        
        opStcspo_v = (dfnopos.iloc[num1][11]) / ((dfnopos.iloc[num1][9])+(dfnopos.iloc[num1][11])) 
        opStcspo_v = opStcspo_v*100
        opStcs_list.append(opStcspo_v)
        
        opStpspo_v = (dfnopos.iloc[num1][12]) / ((dfnopos.iloc[num1][10])+(dfnopos.iloc[num1][12])) 
        opStpspo_v = opStpspo_v*100
        opStps_list.append(opStpspo_v)
        
        #Logic for Total
        totallpo_v = (dfnopos.iloc[num1][13]) / ((dfnopos.iloc[num1][13])+(dfnopos.iloc[num1][14])) 
        totallpo_v = totallpo_v*100
        totall_list.append(totallpo_v)
        totalspo_v = (dfnopos.iloc[num1][14]) / ((dfnopos.iloc[num1][13])+(dfnopos.iloc[num1][14])) 
        totalspo_v = totalspo_v*100
        totals_list.append(totalspo_v)
        
        #Adding date to every row
        todayDate.append(ytextdatestr)
    
    ## Logic for Stat file
    dfiiStat = pd.read_excel(FD_stats_file) 
    num = num1 = 0 # reseting loop variable
    fiistat_b_list = []
    fiistat_s_list = []
    for num in range(2,6):
        for num1 in range(1,6):
            dfiiStat.iloc[num][num1] =  pd.to_numeric(dfiiStat.iloc[num][num1], downcast="float") # Logic for convertion to float
            
        fiistat_b_v = (dfiiStat.iloc[num][1]/(dfiiStat.iloc[num][1]+dfiiStat.iloc[num][3]))*100
        fiistat_b_list.append(fiistat_b_v)
        fiistat_s_v = (dfiiStat.iloc[num][3]/(dfiiStat.iloc[num][1]+dfiiStat.iloc[num][3]))*100
        fiistat_s_list.append(fiistat_s_v)
            
    ## Combining lists
    comb_list = { 'Client Type': idx_list, "Todays Date" : todayDate,
                 "Future Index Long  " : fil_list,
                "Future Index Short " : fis_list,
                "Future Stock Long " : fsl_list,
                "Future Stock Short" : fss_list,
                "Option Index Call Long" : opIcl_list,
                "Option Index Put Long" : opIpl_list,
                "Option Index Call Short" : opIcs_list,
                "Option Index Put Short" : opIps_list,
                "Option Stock Call Long" : opStcl_list,
                "Option Stock Put Long" : opStpl_list,
                "Option Stock Call Short" : opStcs_list,
                "Option Stock Put Short" : opStps_list,
                "Total Long Contracts" : totall_list,
                "Total Short Contracts" : totals_list,
                'FII_Stat': fii_stat_list_name,
                "FII_Buy_Stat": fiistat_b_list,
                "FII_Sell_Stat": fiistat_s_list}
    
    ## Convering to pandas dataframe
    df_Calculated = pd.DataFrame(comb_list)
    df_Calculated.set_index('Client Type', inplace = True)
    df_Calculated.to_csv('FII_DII_OI_Position.csv',header= False,mode = 'a') 
    



fii_dii_postion = fii_dii_pos()






