# ML program for stock


def ml_regration_auto():
    #Importing the libraries
    import numpy as np
    import pandas as pd
    import math
    from datetime import datetime,date
    import matplotlib.pyplot as plt
    from nsepy import get_history
    
    Starttime = datetime.now().strftime("%Y-%m-%d %H:%M:%S") #program data pull start time
    pdate = datetime.now().strftime("%d-%m-%Y")
    textdate = datetime.now().strftime("%d%m%Y")
    Pst = datetime.now().strftime("%H:%M")
    Day = datetime.now().strftime("%A")
    Daydate = datetime.now().strftime("%d")
    
    Ddn = datetime.now().strftime("%d")
    Dmn = datetime.now().strftime("%m")
    Dyn = datetime.now().strftime("%Y")
    
    dd = int(Ddn)
    dm = int(Dmn)
    dy = int(Dyn)
    
    ## Import from NSEpy python lab function
    nf50_History = get_history(symbol="NIFTY 50",start=date(2016,1,1),end=date(dy,dm,dd),index=True)
    bn_History = get_history(symbol="NIFTY BANK",start=date(2016,1,1),end=date(dy,dm,dd),index=True)

    ## For NIFTY 50 # Importing the dataset from csv file
    ## nfdataset = pd.read_csv('NIFTY_50_Data_2021.csv') #Csv file for offline

    nfdataset = nf50_History
    nfdataset['pdAvg'] = (nfdataset['Open']+nfdataset['High']+nfdataset['Low']+nfdataset['Close'])/4
    
    nfdataset['YClose'] = nfdataset['Close'].shift(1)
    nfdataset['pdAvg'] = nfdataset['pdAvg'].shift(2)
    nfx_o_h = nfdataset.iloc[2:, [0,1,7,6]].values    #values # Taking x as open and high & avrage of previous values & yclose value
    nfx_o_l = nfdataset.iloc[2:, [0,2,7,6]].values    #values # Taking x as open and Low & avrage of previous values & yclose value
    nfy_l = nfdataset.iloc[2:, 2].values # Taking y as low value
    nfy_h = nfdataset.iloc[2:, 1].values # Taking y as high value
    
    ## For BANKNIFTY # Importing the dataset from csv file.
    ##bndataset = pd.read_csv('BANKNIFTY_Data_2021.csv') # CSV file
    bndataset = bn_History
    bndataset['pdAvg'] = (bndataset['Open']+bndataset['High']+bndataset['Low']+bndataset['Close'])/4
    
    bndataset['YClose'] = bndataset['Close'].shift(1)
    bndataset['pdAvg'] = bndataset['pdAvg'].shift(2)
    bnx_o_h = bndataset.iloc[2:, [0,1,7,6]].values # Taking x as open,high & avrage of previous values & yclose  value
    bnx_o_l = bndataset.iloc[2:, [0,2,7,6]].values # Taking x as open,Low & avrage of previous values &   yclose value
    bny_l = bndataset.iloc[2:, 2].values # Taking y as low value
    bny_h = bndataset.iloc[2:, 1].values # Taking y as high value
    
    ## For test data use ##x_test1.reshape(3,1) if needed
    ## For Current values Importing the dataset from file nf_VIX_bn.csv from "in.investing.com"
    
    
    ## Manual process need to automated
    
    #COLUMN_NAMES = ['Name', 'Symbol', 'Last', 'Open', 'High', 'Low', 'Chg.', 'Chg. %','Vol.', 'Time']
    ML_file = 'ML_Watchlist_'+textdate+'.csv'
    
    cvdataset = pd.read_csv(ML_file) # CSV file
    df_cvdataset1 = cvdataset.replace('\,','', regex=True)
    df_cvdataset = df_cvdataset1.replace('\%','', regex=True)
    df_cvdataset['Chg. %'].astype(float) # converting in to float
    df_cvdataset['Chg.'].astype(float) # converting in to float
    
    def nfcurrentvalue(CurrentLOC):
        CurrentValue = (float(df_cvdataset.iloc[CurrentLOC][2])+float(df_cvdataset.iloc[CurrentLOC][3])+float(df_cvdataset.iloc[CurrentLOC][4])+float(df_cvdataset.iloc[CurrentLOC][5]))/4
        return CurrentValue
    
    
    #Nifty 50
    nfltpv = float(df_cvdataset.iloc[13][2])
    nfov = float(df_cvdataset.iloc[13][3])
    nfhv = float(df_cvdataset.iloc[13][4])
    nflv = float(df_cvdataset.iloc[13][5])
    nfycv = float(nfdataset.iloc[-1][3])
    nfpdAvg = (nfov+nfhv+nflv+nfltpv)/4 
    
    """
    ##Old CSV file logic
    nf_VIX_bn_file = 'nf_VIX_bn_Watchlist_'+textdate+'.csv'
    cvdataset = pd.read_csv(nf_VIX_bn_file) # CSV file
    df_cvdataset1 = cvdataset.replace('\,','', regex=True)
    df_cvdataset = df_cvdataset1.replace('\%','', regex=True)
    """
    
    
    #VIX is use for VIX logic
    
    nfovix = float(df_cvdataset.iloc[14][3])
    nfhvix = float(df_cvdataset.iloc[14][4])
    nflvix = float(df_cvdataset.iloc[14][5])
    nfltpvix = float(df_cvdataset.iloc[14][2])
    nfpchangevix = float(df_cvdataset.iloc[14][7])  
    nfypcvix = float(df_cvdataset.iloc[14][2])
    
    #BankNifty
    bnltpv = float(df_cvdataset.iloc[12][2])
    bnov = float(df_cvdataset.iloc[12][3])
    bnhv = float(df_cvdataset.iloc[12][4])
    bnlv = float(df_cvdataset.iloc[12][5])
    bnycv = float(bndataset.iloc[-1][3])
    bnpdAvg = (bnov+bnhv+bnlv+bnltpv)/4 
    
    
    """
    # Manual entry
    print('For current values enter Nifty 50 & bankNifty Open, High , Low value & Yesterdays Close')
    
    current_values = [11539.45,11579.950,11520.70,11604.55,19.66,20.03,17.55,19.66,22352.35,22429.15,22292.35,22573.65] # Offline manual entry data 
    
    #Nifty
    nfov = float(current_values[0])
    nfhv = float(current_values[1])
    nflv = float(current_values[2])
    nfycv = float(current_values[3])
    nfovix = float(current_values[4])
    nfhvix = float(current_values[5])
    nflvix = float(current_values[6])
    nfypcvix = float(current_values[7])
    
    #BankNifty
    bnov = float(current_values[8])
    bnhv = float(current_values[9])
    bnlv = float(current_values[10])
    bnycv = float(current_values[11])
    """
        
    for mlploop  in range(4):
        if mlploop == 0: # taking ML values for predicting Nifty 50 Resistance
            x = nfx_o_l # input as low and open values
            y = nfy_h # output as high values act as Resistance
            ##offline current  data
            x_test1 = np.array([[nfov,nfhv,nfycv,nfpdAvg]]) 
        elif mlploop == 1:  # taking ML values for predicting Nifty 50 Support
            x = nfx_o_h # input as high and open values
            y = nfy_l # output as low values act as support
            ##offline current  data
            x_test1 = np.array([[nfov,nflv,nfycv,nfpdAvg]]) 
        elif mlploop == 2: # taking ML values for predicting Bank Nifty Resistance
            x = bnx_o_l # input as low and open values
            y = bny_h # output as high values act as Resistance
            ##offline current  data
            x_test1 = np.array([[bnov,bnhv,bnycv,bnpdAvg]])
        elif mlploop == 3:  # taking ML values for predicting Bank Nifty Support
            x = bnx_o_h # input as high and open values
            y = bny_l # output as low values act as support
            ##offline current  data
            x_test1 = np.array([[bnov,bnlv,bnycv,bnpdAvg]])
        
            
        # # # Splitting the dataset into the Training set and Test set ** if need to test accuresy 
        # from sklearn.model_selection  import train_test_split
        # x, x_test, y, y_test = train_test_split(x, y, test_size = 0.20, random_state = 10)
        
        
        ## Simple Linear Regression
        # Fitting Simple Linear Regression to the Training set
        from sklearn.linear_model import LinearRegression
        lr_regressor = LinearRegression()
        lr_regressor.fit(x, y)
        # Predicting the Test set results
        y_pred_lr = lr_regressor.predict(x_test1)
        #y_pred_lr = lr_regressor.predict(x_test)
        
        
        ##Polynomial Regression
        # Fitting Polynomial Regression to the dataset
        from sklearn.preprocessing import PolynomialFeatures
        poly_reg = PolynomialFeatures(degree = 4)
        x_poly = poly_reg.fit_transform(x)
        poly_reg.fit(x_poly, y)
        # New Fitting Linear Regression model to fit Polynomial Regression object
        pr_regressor = LinearRegression()
        pr_regressor.fit(x_poly, y)
        # Predicting the Test set results
        #y_pred_ploy = pr_regressor.predict(poly_reg.fit_transform(x_test))
        y_pred_ploy = pr_regressor.predict(poly_reg.fit_transform(x_test1))
        
        
        ## Decision Tree Regression
        # Fitting Decision Tree Regression to the dataset
        from sklearn.tree import DecisionTreeRegressor
        dtr_regressor = DecisionTreeRegressor(random_state = 0)
        dtr_regressor.fit(x, y)
        # Predicting a new result
        y_pred_dtr = dtr_regressor.predict(x_test1)
        #y_pred_dtr = dtr_regressor.predict(x_test)
        
        
        ## RandomFores Regressor Regression
        # Fitting RandomFores Regressor Regression to the dataset
        from sklearn.ensemble import RandomForestRegressor
        rf_regressor = RandomForestRegressor(n_estimators= 300,random_state = 0)
        rf_regressor.fit(x, y)
        # Predicting a new result
        y_pred_rf = rf_regressor.predict(x_test1)
        #y_pred_rf = rf_regressor.predict(x_test)
        
        ## Total prediction:
        y_predn = (y_pred_lr+y_pred_ploy+y_pred_dtr+y_pred_rf)/4
        y_pred = format(y_predn[0],'.2f')  #Converting array to string 
        #Print function
        #Append the Range in CSV file and write it to data frame
        if mlploop == 0:
            print('NIFTY 50  , Resistance , {} '.format(y_pred))
            nf_y_pred_r = y_pred
            #print(('Nifty50_ML,{},{},{},{}'.format(pdate,'',nfov,y_pred)),file=open("Support_Resistance_data.csv", "a"))
        elif mlploop == 1:
            print('NIFTY 50  , Support    , {} '.format(y_pred))
            nf_y_pred_s = y_pred
            #print(('Nifty50_ML,{},{},{},{}'.format(pdate,y_pred,nfov,'')),file=open("Support_Resistance_data.csv", "a"))
        elif mlploop == 2:
            print('BANKNIFTY , Resistance , {} '.format(y_pred))
            bn_y_pred_r = y_pred
            #print(('BankNifty_ML,{},{},{},{}'.format(pdate,'',bnov,y_pred)),file=open("Support_Resistance_data.csv", "a"))
        elif mlploop == 3:
            print('BANKNIFTY , Support    , {} '.format(y_pred))
            bn_y_pred_s = y_pred
            #print(('BankNifty_ML,{},{},{},{}'.format(pdate,y_pred,bnov,'')),file=open("Support_Resistance_data.csv", "a"))
            
    
    
    
    # Calculate the Pchange with respect to yesterday close price
    nf_y_pred_r = float(nf_y_pred_r) # Conerting to float
    nf_y_pred_s = float(nf_y_pred_s)
    bn_y_pred_r = float(bn_y_pred_r)
    bn_y_pred_s = float(bn_y_pred_s)
    
    nfPChange_R_ML1 = ((nf_y_pred_r-nfycv)/nfycv)*100
    nfPChange_S_ML1 = ((nf_y_pred_s-nfycv)/nfycv)*100
    bnPChange_R_ML1 = ((bn_y_pred_r-bnycv)/bnycv)*100
    bnPChange_S_ML1 = ((bn_y_pred_s-bnycv)/bnycv)*100
    # Converting to print format
    nfPChange_R_ML = format(nfPChange_R_ML1,'.2f')
    nfPChange_S_ML = format(nfPChange_S_ML1,'.2f')
    bnPChange_R_ML = format(bnPChange_R_ML1,'.2f')
    bnPChange_S_ML = format(bnPChange_S_ML1,'.2f')
    
    print(('Nifty50_ML,{},{},{},{},{},{}'.format(pdate,nf_y_pred_s,nfov,nf_y_pred_r,nfPChange_S_ML,nfPChange_R_ML)),file=open("nf_Support_Resistance_data.csv", "a"))
    print(('BankNifty_ML,{},{},{},{},{},{}'.format(pdate,bn_y_pred_s,bnov,bn_y_pred_r,bnPChange_S_ML,bnPChange_R_ML)),file=open("bn_Support_Resistance_data.csv", "a"))
    
    if nfPChange_R_ML1>1.5 or bnPChange_R_ML1>1.5 or nfPChange_S_ML1< -1.5 or bnPChange_S_ML1<-1.5 :
        print("Best chance for option buying")
    
    # Taking close value of previous day
    nf_y_close =  nfdataset.iloc[-2][3]
    bn_y_close = bndataset.iloc[-2][3]
    
    #Open High Low export for classification bot
    print(('Nifty50_ML,{},{},{},{},{}'.format(pdate,nfov,nf_y_pred_r,nf_y_pred_s,nf_y_close)),file=open("nfClassification_input_data.csv", "a"))
    print(('BankNifty_ML,{},{},{},{},{}'.format(pdate,bnov,bn_y_pred_r,bn_y_pred_s,bn_y_close)),file=open("bnClassification_input_data.csv", "a"))
    
    # #VIX Graph
    
    # print('VIX Graph')
    # nfLTP_PLOT = nfdataset.plot(x='Date',y='VIXClose')
    # plt.show()
    
    
    #For next month Aprox NIFTY 50 movment in persent:
    vixmpc = (float(nfltpvix)/3.465) 
    nmp = nfltpv+vixmpc
    nmn = nfltpv-vixmpc
    
    if float(nfpchangevix ) < 0.0 :
        ndpr = nfltpv-(float(nfltpvix) * float(nfpchangevix))
    else:
        ndpr = nfltpv+(float(nfltpvix) * float(nfpchangevix))
    
    
    if float(nfpchangevix ) > 0.0 :
        ndnr = nfltpv-(float(nfltpvix) * float(nfpchangevix))
    else:
        ndnr = nfltpv+(float(nfltpvix) * float(nfpchangevix))
    
    ndpf = format(ndpr,'.2f')
    ndnf = format(ndnr,'.2f')
    ndp = int(50 * round(float(ndpf)/50))
    ndn = int(50 * round(float(ndnf)/50))
    
    n50p = nfltpv
    
    nfPChange_R_ML1 = ((ndp-nfycv)/nfycv)*100
    nfPChange_S_ML1 = ((ndn-nfycv)/nfycv)*100
    # Converting to print format
    nfPChange_R_ML = format(nfPChange_R_ML1,'.2f')
    nfPChange_S_ML = format(nfPChange_S_ML1,'.2f')
    
    #Append the Range in CSV file and write it to data frame with Simple print fuction use for append value 
    print('Nifty_VIX,{},{},{},{},{},{}'.format(pdate,ndnf,n50p,ndpf,nfPChange_S_ML,nfPChange_R_ML),file=open("nf_Support_Resistance_data.csv", "a")) #Simple print fuction use for append value 

#Function call
ml_reg_auto = ml_regration_auto()


def bank_pcb():
    #Importing the libraries
    import numpy as np
    import pandas as pd
    import math
    from datetime import datetime
    
    
    Starttime = datetime.now().strftime("%Y-%m-%d %H:%M:%S") #program data pull start time
    Pst = datetime.now().strftime("%H:%M")
    Day = datetime.now().strftime("%A")
    Daydate = datetime.now().strftime("%d")
    pdate = datetime.now().strftime("%d-%m-%Y")
    textdate = datetime.now().strftime("%d%m%Y")
    
    
    ## For Current values Importing the dataset from file nf_VIX_bn.csv from "in.investing.com"
    ## Manual process need to automated
    
    #COLUMN_NAMES = ['Name', 'Symbol', 'Last', 'Open', 'High', 'Low', 'Chg.', 'Chg. %','Vol.', 'Time']
    ML_file = 'ML_Watchlist_'+textdate+'.csv'
    
    cvdataset = pd.read_csv(ML_file) # CSV file
    df_cvdataset1 = cvdataset.replace('\,','', regex=True)
    df_cvdataset = df_cvdataset1.replace('\%','', regex=True)
    df_cvdataset['Chg. %'].astype(float) # converting in to float
    df_cvdataset['Chg.'].astype(float) # converting in to float
    
    #Axis_value = float(df_cvdataset.iloc[0][2])+float(df_cvdataset.iloc[0][3])+float(df_cvdataset.iloc[0][4])+float(df_cvdataset.iloc[0][5])
    
    def bncurrentvalue(CurrentLOC):
        CurrentValue = (float(df_cvdataset.iloc[CurrentLOC][2])+float(df_cvdataset.iloc[CurrentLOC][3])+float(df_cvdataset.iloc[CurrentLOC][4])+float(df_cvdataset.iloc[CurrentLOC][5]))/4
        return CurrentValue
    
    Axis_value = bncurrentvalue(0)
    Bandhan_value = bncurrentvalue(1)
    Baroda_value = bncurrentvalue(2)
    Federal_value = bncurrentvalue(3)
    HDFC_value = bncurrentvalue(4)
    ICICI_value = bncurrentvalue(5)
    IDFC_value = bncurrentvalue(6)
    IndusInd_value = bncurrentvalue(7)
    Kotak_value = bncurrentvalue(8)
    Punjab_value = bncurrentvalue(9)
    RBL_value = bncurrentvalue(10)
    SBI_value = bncurrentvalue(11)
    
    #BankNifty
    bnltpv = float(df_cvdataset.iloc[12][2])
    bnov = float(df_cvdataset.iloc[12][3])
    bnhv = float(df_cvdataset.iloc[12][4])
    bnlv = float(df_cvdataset.iloc[12][5])
    bnvalue = (bnltpv+bnov+bnhv+bnlv)/4
    
    stockPCtobn = [14.95,2.58,0.66,1.33,28.39,19.48,0.85,4.37,16.31,0.46,1.06,9.56]
    stockValues = [Axis_value,Bandhan_value,Baroda_value,Federal_value,HDFC_value,ICICI_value,IDFC_value,IndusInd_value,Kotak_value,Punjab_value,RBL_value,SBI_value]
    
    
    ## Need to add nifty 50 PCB as well
    
    def pvaluesfun ():
        pvnList = []
        pvpList = []
        pvbnvalue = []
        for mulVal in range(12):
            pvalueby2d5 = float(df_cvdataset.iloc[mulVal][6])/2.5
            pvaluemul2d5 = float(df_cvdataset.iloc[mulVal][6])*2.5
            if  float(df_cvdataset.iloc[mulVal][7]) > 0:
                pvn = (stockValues[mulVal] - pvalueby2d5)*(stockPCtobn[mulVal]/100)
                pvp = (stockValues[mulVal] + pvaluemul2d5)*(stockPCtobn[mulVal]/100)
            elif float(df_cvdataset.iloc[mulVal][7]) < 0:
                pvn = (stockValues[mulVal] + pvalueby2d5)*(stockPCtobn[mulVal]/100)
                pvp = (stockValues[mulVal] - pvaluemul2d5)*(stockPCtobn[mulVal]/100)
            pvnList.append(pvn) 
            pvpList.append(pvp)
            
        pvnListm = bnvalue-(bnvalue*(((sum(pvnList)/1000))/100))
        pvpListm = bnvalue+(bnvalue*(((sum(pvpList)/1000))/100))
        pvbnvalue.append(pvnListm)
        pvbnvalue.append(pvpListm)
        return pvbnvalue
    
    
    bn_pvalueList = pvaluesfun()
    
    print("\n")
    print("For Todays BankNifty PCB Range at support {} and Resistance {}".format(format(bn_pvalueList[0],'.2f'),format(bn_pvalueList[1],'.2f')))
    print(('BankNifty_PCB,{},{},{},{},{},{}'.format(pdate,format(bn_pvalueList[0],'.2f'),bnvalue,format(bn_pvalueList[1],'.2f'),0,0)),file=open("bn_Support_Resistance_data.csv", "a"))
    
    ## ADR program
    ## Same do for nifty 50
    
#Function call    
Bank_pcb= bank_pcb()