# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 11:53:09 2020

@author: Sangram Phadke
"""

def DayFnO():
    #Importing the libraries
    import numpy as np
    import pandas as pd
    from datetime import datetime
    
       
    Starttime = datetime.now().strftime("%Y-%m-%d %H:%M:%S") #program data pull start time
    Pst = datetime.now().strftime("%H:%M")
    Day = datetime.now().strftime("%A")
    Daydate = datetime.now().strftime("%d")
    pdate = datetime.now().strftime("%d-%m-%Y")
    textdate = datetime.now().strftime("%d%m%Y")
    
    ##Importing the dataset
    df_trading_days = pd.read_csv('TradingDays.csv')
    for num_td in range(len(df_trading_days)-1):
        if df_trading_days.iloc[num_td][0] == pdate :
            print (df_trading_days.iloc[num_td][0])
            ptd =  (df_trading_days.iloc[num_td-1][0])
            ptdd = datetime.strptime(ptd, "%d-%m-%Y").date()
            ytextdate = ptdd.strftime("%d%m%Y")
            ytextdatestr = ptdd.strftime("%d-%b-%Y")
    
    Global_Markets_file = 'Global_Markets_Watchlist_'+textdate+'.csv'
    
    dfnodataset = pd.read_csv(Global_Markets_file)
    dfnodataset = dfnodataset.replace('\%','', regex=True)
    dfnodataset = dfnodataset.replace('\,','', regex=True)
    dfnodataset["Chg. %"] = pd.to_numeric(dfnodataset["Chg. %"], downcast="float")
    dfnodataset["Last"] = pd.to_numeric(dfnodataset["Chg. %"], downcast="float")
    
    ## Index / FnO name
    
    def dfno(num):
        point = 0
        if (dfnodataset.iloc[num][7]) > 0 and (dfnodataset.iloc[num][7]) < 0.5:
            point = point + 1
        elif (dfnodataset.iloc[num][7]) > 0.5 and (dfnodataset.iloc[num][7]) < 1:
            point = point + 2
        elif (dfnodataset.iloc[num][7]) > 1 :
            point = point + 3
        elif (dfnodataset.iloc[num][7]) < 0 and (dfnodataset.iloc[num][7]) > -0.5:
            point = point -1
        elif (dfnodataset.iloc[num][7]) < -0.5 and (dfnodataset.iloc[num][7]) > -1:
            point = point -2
        elif (dfnodataset.iloc[num][7]) < -1 :
            point = point -3
        return point
    
    
    
    
    # USD/INR - US Dollar Indian Rupee
    usdinrn = dfno(0)
    usdinr = -usdinrn   
    # US Dollar Index Futures
    if dfnodataset.iloc[1][2] > 93:
        usdix = -1
    else:
        usdix = 1
    # USD/EUR - US Dollar Euro
    usdeur = dfno(2)
    # S&P 500
    snp500 = dfno(3)
    # S&P 500 Futures
    snp500f = dfno(4)
    # Dow Jones Industrial Average
    dowj = dfno(5)
    # Dow Jones 30 Futures
    dowjf = dfno(6)
    # Nasdaq 100
    nas100 = dfno(7)
    # Nasdaq 100 Futures
    nas100f = dfno(8)
    # FTSE 100
    ftse100 = dfno(9)
    # FTSE 100 Futures
    ftse100f = dfno(10)
    # DAX
    dax = dfno(11)
    # DAX Futures
    daxf = dfno(12)
    # Shanghai Composite
    china = dfno(13)
    # Nifty 50
    nf50 = dfno(14)
    # Nifty 50 Futures
    nf50f = dfno(15)
    # Nifty Bank
    bn = dfno(16)
    
    # India VIX
    ivixN = dfno(17)
    ivix = -ivixN 
    # CBOE Volatility Index
    usvixN = dfno(18)
    usvix = -usvixN
    # S&P 500 VIX Futures
    usvixfN = dfno(19)
    usvixf = -usvixfN
    
    # #################
    
    points = (usdinr + usdix + usdeur + snp500 + snp500f + dowj + dowjf + nas100 + nas100f + ftse100 + ftse100f + dax +daxf + china + nf50 + nf50f + bn + ivix + usvix + usvixf)/22
    
    if (points) >= 0 and (points) < 0.5:
        print('Sideways Market')
        pt = 'Sideways Market'
    elif (points) >= 0.5 and (points) < 1:
        print('Up and Positive Market')
        pt = 'Up and Positive Market'
    elif (points) >= 1 :
        print('Strong Buy / Buy CE')
        pt = 'Strong Buy / Buy CE'
    elif (points) <= 0 and (points) > -0.5:
        print('Sideways Market')
        pt = 'Sideways Market'
    elif (points) <= -0.5 and (points) > -1:
        print('Down and Negative market')
        pt= 'Down and Negative market'
    elif (points) <= -1 :
        print('Strong Sell / Buy PE')
        pt = 'Strong Sell / Buy PE'
    
    print(('{},{}'.format(pdate,pt)),file=open("WorldMarket_View.csv", "a"))

##Function call
DayFnO_pos = DayFnO()