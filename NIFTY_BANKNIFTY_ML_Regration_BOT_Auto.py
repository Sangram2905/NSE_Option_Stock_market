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
    nf50_History = get_history(symbol="NIFTY 50",start=date(2014,1,1),end=date(dy,dm,dd),index=True)
    bn_History = get_history(symbol="NIFTY BANK",start=date(2018,1,1),end=date(dy,dm,dd),index=True)
   
   
    
    
    #columns = ['Date'0, Open'1, 'High'2, 'Low'3, 'Close'4, 'volume'6, 'Turnover'7 ] 
    
    ## For NIFTY 50 # Importing the dataset from csv file
    ## NFdataset = pd.read_csv('NIFTY_50_Data_2021.csv') #Csv file for offline

    NFdataset = nf50_History 
    NFx_o_h = NFdataset.iloc[:, [0,1,3]].values    #values # Taking x as open and high yclose value
    NFx_o_l = NFdataset.iloc[:, [0,2,3]].values    #values # Taking x as open and Low yclose value
    NFy_l = NFdataset.iloc[:, 2].values # Taking y as low value
    NFy_h = NFdataset.iloc[:, 1].values # Taking y as high value
    
    ## For BANKNIFTY # Importing the dataset from csv file.
    ##BNdataset = pd.read_csv('BANKNIFTY_Data_2021.csv') # CSV file
    BNdataset = bn_History 
    BNx_o_h = BNdataset.iloc[:, [0,1,3]].values # Taking x as open,high & yclose value
    BNx_o_l = BNdataset.iloc[:, [0,2,3]].values # Taking x as open,Low & yclose value
    BNy_l = BNdataset.iloc[:, 2].values # Taking y as low value
    BNy_h = BNdataset.iloc[:, 1].values # Taking y as high value
    
    ## For test data use ##x_test1.reshape(3,1) if needed
    ## For Current values Importing the dataset from file NF_VIX_BN.csv from "in.investing.com"
    
    
    ## Manual process need to automated
    
    #COLUMN_NAMES = ['Name', 'Symbol', 'Last', 'Open', 'High', 'Low', 'Chg.', 'Chg. %','Vol.', 'Time']
    ML_file = 'ML_Watchlist_'+textdate+'.csv'
    
    cvdataset = pd.read_csv(ML_file) # CSV file
    df_cvdataset1 = cvdataset.replace('\,','', regex=True)
    df_cvdataset = df_cvdataset1.replace('\%','', regex=True)
    df_cvdataset['Chg. %'].astype(float) # converting in to float
    df_cvdataset['Chg.'].astype(float) # converting in to float
    
    def NFcurrentvalue(CurrentLOC):
        CurrentValue = (float(df_cvdataset.iloc[CurrentLOC][2])+float(df_cvdataset.iloc[CurrentLOC][3])+float(df_cvdataset.iloc[CurrentLOC][4])+float(df_cvdataset.iloc[CurrentLOC][5]))/4
        return CurrentValue
    
    
    #Nifty 50
    nfltpv = float(df_cvdataset.iloc[13][2])
    nfov = float(df_cvdataset.iloc[13][3])
    nfhv = float(df_cvdataset.iloc[13][4])
    nflv = float(df_cvdataset.iloc[13][5])
    nfycv = float(NFdataset.iloc[-2][3])
    
    """
    ##Old CSV file logic
    NF_VIX_BN_file = 'NF_VIX_BN_Watchlist_'+textdate+'.csv'
    cvdataset = pd.read_csv(NF_VIX_BN_file) # CSV file
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
    bnov = float(df_cvdataset.iloc[12][3])
    bnhv = float(df_cvdataset.iloc[12][4])
    bnlv = float(df_cvdataset.iloc[12][5])
    bnycv = float(BNdataset.iloc[-1][3])
    
    
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
            x = NFx_o_l # input as low and open values
            y = NFy_h # output as high values act as Resistance
            ##offline current  data
            x_test1 = np.array([[nfov,nfhv,nfycv]]) 
        elif mlploop == 1:  # taking ML values for predicting Nifty 50 Support
            x = NFx_o_h # input as high and open values
            y = NFy_l # output as low values act as support
            ##offline current  data
            x_test1 = np.array([[nfov,nflv,nfycv]]) 
        elif mlploop == 2: # taking ML values for predicting Bank Nifty Resistance
            x = BNx_o_l # input as low and open values
            y = BNy_h # output as high values act as Resistance
            ##offline current  data
            x_test1 = np.array([[bnov,bnhv,bnycv]])
        elif mlploop == 3:  # taking ML values for predicting Bank Nifty Support
            x = BNx_o_h # input as high and open values
            y = BNy_l # output as low values act as support
            ##offline current  data
            x_test1 = np.array([[bnov,bnlv,bnycv]])
        
            
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
    
    NFPChange_R_ML1 = ((nf_y_pred_r-nfycv)/nfycv)*100
    NFPChange_S_ML1 = ((nf_y_pred_s-nfycv)/nfycv)*100
    BNPChange_R_ML1 = ((bn_y_pred_r-bnycv)/bnycv)*100
    BNPChange_S_ML1 = ((bn_y_pred_s-bnycv)/bnycv)*100
    # Converting to print format
    NFPChange_R_ML = format(NFPChange_R_ML1,'.2f')
    NFPChange_S_ML = format(NFPChange_S_ML1,'.2f')
    BNPChange_R_ML = format(BNPChange_R_ML1,'.2f')
    BNPChange_S_ML = format(BNPChange_S_ML1,'.2f')
    
    print(('Nifty50_ML,{},{},{},{},{},{}'.format(pdate,nf_y_pred_s,nfov,nf_y_pred_r,NFPChange_S_ML,NFPChange_R_ML)),file=open("NF_Support_Resistance_data.csv", "a"))
    print(('BankNifty_ML,{},{},{},{},{},{}'.format(pdate,bn_y_pred_s,bnov,bn_y_pred_r,BNPChange_S_ML,BNPChange_R_ML)),file=open("BN_Support_Resistance_data.csv", "a"))
    
    if NFPChange_R_ML1>1.5 or BNPChange_R_ML1>1.5 or NFPChange_S_ML1< -1.5 or BNPChange_S_ML1<-1.5 :
        print("Best chance for option buying")
    
    # Taking close value of previous day
    nf_y_close =  NFdataset.iloc[-2][3]
    bn_y_close = BNdataset.iloc[-2][3]
    
    #Open High Low export for classification bot
    print(('Nifty50_ML,{},{},{},{},{}'.format(pdate,nfov,nf_y_pred_r,nf_y_pred_s,nf_y_close)),file=open("NFClassification_input_data.csv", "a"))
    print(('BankNifty_ML,{},{},{},{},{}'.format(pdate,bnov,bn_y_pred_r,bn_y_pred_s,bn_y_close)),file=open("BNClassification_input_data.csv", "a"))
    
    # #VIX Graph
    
    # print('VIX Graph')
    # NFLTP_PLOT = NFdataset.plot(x='Date',y='VIXClose')
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
    
    NFPChange_R_ML1 = ((ndp-nfycv)/nfycv)*100
    NFPChange_S_ML1 = ((ndn-nfycv)/nfycv)*100
    # Converting to print format
    NFPChange_R_ML = format(NFPChange_R_ML1,'.2f')
    NFPChange_S_ML = format(NFPChange_S_ML1,'.2f')
    
    #Append the Range in CSV file and write it to data frame with Simple print fuction use for append value 
    print('Nifty_VIX,{},{},{},{},{},{}'.format(pdate,ndnf,n50p,ndpf,NFPChange_S_ML,NFPChange_R_ML),file=open("NF_Support_Resistance_data.csv", "a")) #Simple print fuction use for append value 

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
    
    
    ## For Current values Importing the dataset from file NF_VIX_BN.csv from "in.investing.com"
    ## Manual process need to automated
    
    #COLUMN_NAMES = ['Name', 'Symbol', 'Last', 'Open', 'High', 'Low', 'Chg.', 'Chg. %','Vol.', 'Time']
    ML_file = 'ML_Watchlist_'+textdate+'.csv'
    
    cvdataset = pd.read_csv(ML_file) # CSV file
    df_cvdataset1 = cvdataset.replace('\,','', regex=True)
    df_cvdataset = df_cvdataset1.replace('\%','', regex=True)
    df_cvdataset['Chg. %'].astype(float) # converting in to float
    df_cvdataset['Chg.'].astype(float) # converting in to float
    
    #Axis_value = float(df_cvdataset.iloc[0][2])+float(df_cvdataset.iloc[0][3])+float(df_cvdataset.iloc[0][4])+float(df_cvdataset.iloc[0][5])
    
    def BNcurrentvalue(CurrentLOC):
        CurrentValue = (float(df_cvdataset.iloc[CurrentLOC][2])+float(df_cvdataset.iloc[CurrentLOC][3])+float(df_cvdataset.iloc[CurrentLOC][4])+float(df_cvdataset.iloc[CurrentLOC][5]))/4
        return CurrentValue
    
    Axis_value = BNcurrentvalue(0)
    Bandhan_value = BNcurrentvalue(1)
    Baroda_value = BNcurrentvalue(2)
    Federal_value = BNcurrentvalue(3)
    HDFC_value = BNcurrentvalue(4)
    ICICI_value = BNcurrentvalue(5)
    IDFC_value = BNcurrentvalue(6)
    IndusInd_value = BNcurrentvalue(7)
    Kotak_value = BNcurrentvalue(8)
    Punjab_value = BNcurrentvalue(9)
    RBL_value = BNcurrentvalue(10)
    SBI_value = BNcurrentvalue(11)
    
    #BankNifty
    Bnltpv = float(df_cvdataset.iloc[12][2])
    Bnov = float(df_cvdataset.iloc[12][3])
    Bnhv = float(df_cvdataset.iloc[12][4])
    Bnlv = float(df_cvdataset.iloc[12][5])
    bnvalue = (Bnltpv+Bnov+Bnhv+Bnlv)/4
    
    stockPCtoBN = [14.95,2.58,0.66,1.33,28.39,19.48,0.85,4.37,16.31,0.46,1.06,9.56]
    stockValues = [Axis_value,Bandhan_value,Baroda_value,Federal_value,HDFC_value,ICICI_value,IDFC_value,IndusInd_value,Kotak_value,Punjab_value,RBL_value,SBI_value]
    
    
    ## Need to add nifty 50 PCB as well
    
    def pvaluesfun ():
        pvnList = []
        pvpList = []
        pvBNvalue = []
        for mulVal in range(12):
            pvalueby2d5 = float(df_cvdataset.iloc[mulVal][6])/2.5
            pvaluemul2d5 = float(df_cvdataset.iloc[mulVal][6])*2.5
            if  float(df_cvdataset.iloc[mulVal][7]) > 0:
                pvn = (stockValues[mulVal] - pvalueby2d5)*(stockPCtoBN[mulVal]/100)
                pvp = (stockValues[mulVal] + pvaluemul2d5)*(stockPCtoBN[mulVal]/100)
            elif float(df_cvdataset.iloc[mulVal][7]) < 0:
                pvn = (stockValues[mulVal] + pvalueby2d5)*(stockPCtoBN[mulVal]/100)
                pvp = (stockValues[mulVal] - pvaluemul2d5)*(stockPCtoBN[mulVal]/100)
            pvnList.append(pvn) 
            pvpList.append(pvp)
            
        pvnListm = bnvalue-(bnvalue*(((sum(pvnList)/1000))/100))
        pvpListm = bnvalue+(bnvalue*(((sum(pvpList)/1000))/100))
        pvBNvalue.append(pvnListm)
        pvBNvalue.append(pvpListm)
        return pvBNvalue
    
    
    bn_pvalueList = pvaluesfun()
    
    print("\n")
    print("For Todays BankNifty PCB Range at support {} and Resistance {}".format(format(bn_pvalueList[0],'.2f'),format(bn_pvalueList[1],'.2f')))
    print(('BankNifty_PCB,{},{},{},{},{},{}'.format(pdate,format(bn_pvalueList[0],'.2f'),bnvalue,format(bn_pvalueList[1],'.2f'),0,0)),file=open("BN_Support_Resistance_data.csv", "a"))
    
    ## ADR program
    ## Same do for nifty 50
    
#Function call    
Bank_pcb= bank_pcb()