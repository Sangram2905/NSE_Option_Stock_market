# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 11:14:35 2021

@author: Q & A.I
"""
class ML_Reg:
    def __int__(self):
        pass
    def ml_regration_auto():
        print("\n")
        #Importing the libraries
        import numpy as np
        import pandas as pd
        import math
        from datetime import datetime,date
        import matplotlib.pyplot as plt

        import yfinance as yf   # for data of intex
        
        #Vareus date formats req. in program
        Starttime = datetime.now().strftime("%Y-%m-%d %H:%M:%S") #program data pull start time
        pdate = datetime.now().strftime("%d-%m-%Y")
        textdate = datetime.now().strftime("%d%m%Y")
        yahoo_date = datetime.now().strftime("%Y-%m-%d")
        Day = datetime.now().strftime("%A")
        Daydate = datetime.now().strftime("%d")

        
        ## Import from yahoo finance python lab function
        nasdaq = yf.download("NDX", start="2016-01-01", end=yahoo_date)
        dowJones = yf.download("DJI", start="2016-01-01", end=yahoo_date)

        
        # Updating / adjusting data 
        cust_nq_index = pd.Series(range(len(nasdaq)))
    
        nqdataset = nasdaq.set_index(cust_nq_index) # Replacing date to simple index number
        nqdataset['pdAvg'] = (nqdataset['Open']+nqdataset['High']+nqdataset['Low']+nqdataset['Close'])/4
        
        nqdataset['YClose'] = nqdataset['Close'].shift(1)
        nqdataset['pdAvg'] = nqdataset['pdAvg'].shift(2)

        

        ## slicing to input and out put
        nqx_o_h = nqdataset.iloc[2:, [0,1,6,7]].values    #values # Taking x as open and high & avrage of previous values & yclose value 
        nqx_o_l = nqdataset.iloc[2:, [0,2,6,7]].values    #values # Taking x as open and Low & avrage of previous values & yclose value 
        nqy_l = nqdataset.iloc[2:, 2].values # Taking y as low value
        nqy_h = nqdataset.iloc[2:, 1].values # Taking y as high value
        
        ## For Dow ## Updating / adjusting data 
        cust_dj_index = pd.Series(range(len(dowJones)))
        
        djdataset = dowJones.set_index(cust_dj_index) # Replacing date to simple index number
        djdataset['pdAvg'] = (djdataset['Open']+djdataset['High']+djdataset['Low']+djdataset['Close'])/4
        
        djdataset['YClose'] = djdataset['Close'].shift(1)
        djdataset['pdAvg'] = djdataset['pdAvg'].shift(2)

        
        
        djx_o_h = djdataset.iloc[2:, [0,1,6,7]].values # Taking x as open,high & avrage of previous values & yclose  value 
        djx_o_l = djdataset.iloc[2:, [0,2,6,7]].values # Taking x as open,Low & avrage of previous values &   yclose value 
        djy_l = djdataset.iloc[2:, 2].values # Taking y as low value
        djy_h = djdataset.iloc[2:, 1].values # Taking y as high value
        
        ## For test data use ##x_test1.reshape(3,1) if needed
        ## For Current values Importing the dataset from file NQ_DJ_ML.csv from "in.investing.com"
        
        
        ## Manual process need to automated
        
        #COLUMN_NAMES = ['Name', 'Symbol', 'Last', 'Open', 'High', 'Low', 'Chg.', 'Chg. %','Vol.', 'Time']
        ML_file = 'NQ_DJ_ML_Watchlist_'+textdate+'.csv'
        
        cvdataset = pd.read_csv(ML_file) # CSV file
        df_cvdataset1 = cvdataset.replace('\,','', regex=True)
        df_cvdataset = df_cvdataset1.replace('\%','', regex=True)
        df_cvdataset['Chg. %'].astype(float) # converting in to float
        df_cvdataset['Chg.'].astype(float) # converting in to float
        
        def nqcurrentvalue(CurrentLOC):
            CurrentValue = (float(df_cvdataset.iloc[CurrentLOC][2])+float(df_cvdataset.iloc[CurrentLOC][3])+float(df_cvdataset.iloc[CurrentLOC][4])+float(df_cvdataset.iloc[CurrentLOC][5]))/4
            return CurrentValue
        
        
        #nasdaq values from Watchlist file
        nqltpv = float(df_cvdataset.iloc[0][2])
        nqov = float(df_cvdataset.iloc[0][3])
        nqhv = float(df_cvdataset.iloc[0][4])
        nqlv = float(df_cvdataset.iloc[0][5])
        nqycv = float(nqdataset.iloc[-1][3])
        nqpdAvg = (nqov+nqhv+nqlv+nqltpv)/4 

        #Dow
        djltpv = float(df_cvdataset.iloc[1][2])
        djov = float(df_cvdataset.iloc[1][3])
        djhv = float(df_cvdataset.iloc[1][4])
        djlv = float(df_cvdataset.iloc[1][5])
        djycv = float(djdataset.iloc[-1][3])
        djpdAvg = (djov+djhv+djlv+djltpv)/4 
        

            
        for mlploop  in range(1):
            if mlploop == 0: # taking ML values for predicting nasdaq 50 Resistance
                x = nqx_o_l # input as low and open values
                y = nqy_h # output as high values act as Resistance
                
                ##offline current  data
                x_test1 = np.array([[nqov,nqhv,nqycv,nqpdAvg]]) 
            
            elif mlploop == 1:  # taking ML values for predicting nasdaq 50 Support
                x = nqx_o_h # input as high and open values
                y = nqy_l # output as low values act as support
                
                ##offline current  data
                x_test1 = np.array([[nqov,nqlv,nqycv,nqpdAvg]]) 
            
            elif mlploop == 2: # taking ML values for predicting Dow nasdaq Resistance
                x = djx_o_l # input as low and open values
                y = djy_h # output as high values act as Resistance
                
                ##offline current  data
                x_test1 = np.array([[djov,djhv,djycv,djpdAvg]])
            elif mlploop == 3:  # taking ML values for predicting Dow nasdaq Support
                x = djx_o_h # input as high and open values
                y = djy_l # output as low values act as support
                
                ##offline current  data
                x_test1 = np.array([[djov,djlv,djycv,djpdAvg]])
            
                
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
            
            # # Use score method to get accuracy of model
            # score = lr_regressor.score(x_test, y_pred_lr)
            # print(score)
            
            
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
            
            if mlploop == 0:
                print('nasdaq , Resistance , {} '.format(y_pred))
                nq_y_pred_r = y_pred
                
            elif mlploop == 1:
                print('nasdaq , Support    , {} '.format(y_pred))
                print("\n")
                nq_y_pred_s = y_pred
                
            elif mlploop == 2:
                print('Dow , Resistance , {} '.format(y_pred))
                dj_y_pred_r = y_pred
               
            elif mlploop == 3:
                print('Dow , Support    , {} '.format(y_pred))
                print("\n")
                dj_y_pred_s = y_pred
                
                
        
        
        
        # Calculate the Pchange with respect to yesterday close price
        nq_y_pred_r = float(nq_y_pred_r) # Conerting to float
        nq_y_pred_s = float(nq_y_pred_s)
        dj_y_pred_r = float(dj_y_pred_r)
        dj_y_pred_s = float(dj_y_pred_s)
        
        nqPChange_R_ML1 = ((nq_y_pred_r-nqycv)/nqycv)*100
        nqPChange_S_ML1 = ((nq_y_pred_s-nqycv)/nqycv)*100
        djPChange_R_ML1 = ((dj_y_pred_r-djycv)/djycv)*100
        djPChange_S_ML1 = ((dj_y_pred_s-djycv)/djycv)*100
        
        # Converting to print format
        nqPChange_R_ML = format(nqPChange_R_ML1,'.2f')
        nqPChange_S_ML = format(nqPChange_S_ML1,'.2f')
        djPChange_R_ML = format(djPChange_R_ML1,'.2f')
        djPChange_S_ML = format(djPChange_S_ML1,'.2f')
        
        #Append the Range in CSV file and write it to data frame
        print(('NASDAQ_ML,{},{},{},{},{},{}'.format(pdate,nq_y_pred_s,nqov,nq_y_pred_r,nqPChange_S_ML,nqPChange_R_ML)),file=open("nq_Support_Resistance_data.csv", "a"))
        print(('Dow_ML,{},{},{},{},{},{}'.format(pdate,dj_y_pred_s,djov,dj_y_pred_r,djPChange_S_ML,djPChange_R_ML)),file=open("dj_Support_Resistance_data.csv", "a"))
        
        if nqPChange_R_ML1>1.5 or djPChange_R_ML1>1.5 or nqPChange_S_ML1< -1.5 or djPChange_S_ML1<-1.5 :
            print("Best chance for Trading")
        
        # Taking close value of previous day
        nq_y_close =  nqdataset.iloc[-2][3]
        dj_y_close = djdataset.iloc[-2][3]
        
        #Open High Low export for classification bot
        print(('NASDAQ_ML,{},{},{},{},{}'.format(pdate,nqov,nq_y_pred_r,nq_y_pred_s,nq_y_close)),file=open("nq_Classification_input_data.csv", "a"))
        print(('Dow_ML,{},{},{},{},{}'.format(pdate,djov,dj_y_pred_r,dj_y_pred_s,dj_y_close)),file=open("dj_Classification_input_data.csv", "a"))
        

    
    #Function call
    ml_reg_auto = ml_regration_auto()
    
   
