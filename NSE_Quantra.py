# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 09:06:36 2020

@author: Sangram Phadke
"""

"""
Risk profiles of put option buyer and seller
Buying a put option gives you the right, but not the obligation to sell the underlying security at the given strike price, within a specific time period. 
Therefore a put option payoff at expiration depends on where the underlying price is relative to the put option strike price.

In this notebook, we will plot a put buyer's and a put seller's payoff graph for a 900 strike price put on the Infosys stock.

"""
#Import labs

import numpy as np
import matplotlib.pyplot as plt
# For making attractive and informative statistical graph
plt.style.use('seaborn-darkgrid')

"""
Put payoff
We define a function put_payoff that calculates the payoff from buying a put option. 
The function takes sT(Stock price range) which is a range of possible values of the stock price at expiration, 
the strike price of the put option and the premium of the put option as input.

It returns a numpy array containing the profit from put option for different stock prices. 
When the stock price is less than the strike price, the profit is measured as the difference 
between strike price and stock price, and when the stock price is greater than the strike price 
then the profit is zero. 
After this, a put premium is deducted from the Profit-n-Lose(pnl) to compute the payoff.


Coding guide
np.where can be used to create put payoff structure. The syntax of it is as follows:

payoff_array = np.where(condition, true_value, false_value)

If the condition is true then the payoff_array is assigned true_value else false_value.

The condition, true and false value for put payoff from buyer's perspective can be as follows:

condition: sT < strike_price
true_value: strike_price - sT
false_value: 0

"""
def put_payoff (sT, strike_price, premium):
    pnl = np.where(sT<strike_price, strike_price - sT, 0)
    return pnl - premium

"""
Define parameters
We will define the spot price, 
the strike price, premium, and a range of possible values for the Infosys stock price at expiry.
"""
# Infosys stock price
spot_price = 900

# Put strike price and cost
strike_price = 900
premium = 20

# Stock price range at the expiration of the put
# We have defined range for the stock price at expiry as +/- 10% from spot price
# Syntax: numpy.arange(start price, stop price)
sT = np.arange(0.9*spot_price,1.1*spot_price)


## Put option buyer payoff

payoff_long_put = put_payoff(sT, strike_price, premium)
# Plot the graph
fig, ax = plt.subplots(figsize=(8,5))
ax.spines['bottom'].set_position('zero')
ax.plot(sT,payoff_long_put,label='Put option buyer payoff')
plt.xlabel('Infosys Stock Price')
plt.ylabel('Profit and loss')
plt.legend()
plt.show()

"""
So what do you observe?

Even if the price of Infosys goes above the strike price of 900, 
the maximum loss seems to be just INR 20/-. 
Therefore, the loss to the put option buyer is restricted to the extent of the premium he has paid.

The profit from this put option seems to increase linearly as and 
when Infosys starts to move below the strike price of 900. 

Therefore, the lower the spot price goes, the higher will be the profit.

Though the put option is supposed to make a profit when the spot price moves below the strike price, 
the put option buyer first needs to recover the premium he has paid.

From the above points, we can say that the buyer of the put option has limited risk and the potential 
to make a huge profit.
"""


##Put option seller payoff
"""
To get the payoff graph for option seller, 
we have multiplied the payoff of option buyer by -1.0, 
as the option buyer makes the profit, 
the option seller will lose the exact same amount and vice-versa.

"""

payoff_short_put = payoff_long_put * -1.0
# Plot
fig, ax = plt.subplots(figsize=(8,5))
ax.spines['bottom'].set_position('zero')
ax.plot(sT,payoff_short_put,label='Put option seller payoff',color='r')
plt.xlabel('Infosys Stock Price')
plt.ylabel('Profit and loss')
plt.legend()
plt.show()

"""
The put option seller payoff looks like a mirror image of the put option buyer payoff.

The profit is restricted to INR 20/- as long as the spot price is trading at any price above the strike price of 900.
From 900 to 880, we can see the profits getting reduced.
Below 880, the put option seller starts losing money. The losses increase with a decrease in stock price.
Therefore, you sell a put option only when your view is that the underlying asset will not fall beyond the strike price.

"""

##########################  PUT Exercise ############################

"""
Let’s assume that the stock Tata Motors is trading at INR 430. We bought 430 strike put for INR 3. In this exercise, we will learn to calculate the payoff from the put option.

For a put buyer at the option expiry:
      A. If the stock price is less than the strike price, then the put buyer profits the difference.
      B. If the stock price is greater than the strike price, then the put buyer loses the premium.
To enter into this payoff structure the put buyer pays a premium to the put seller.

Coding guide
np.where can be used to create put payoff structure. The syntax of it is as follows:

payoff_array = np.where(condition, true_value, false_value)

If the condition is true then the payoff_array is assigned true_value else false_value.

The condition, true and false value for put payoff from buyer's perspective can be as follows:

condition: sT < strike_price
true_value: strike_price - sT
false_value: 0
Instructions

Calculate the put payoff without premium using np.where and store it in the payoff_put array.
"""
# Import libraries
import numpy as np
import pandas as pd

# Tata motors stock price 
spot_price = 430 

# Stock price range at expiration of the call
sT = np.arange(0.98*spot_price,1.03*spot_price)

# Put strike and premium
strike_price = 430 
premium = 3

# Put payoff
# Type your code here
payoff_put = np.where(sT < strike_price, strike_price - sT, 0) 


#################  Call ######################

"""
Risk profiles of call option buyer and seller
Buying a call option gives you the right, but not the obligation, to buy the underlying security at the given strike price. Therefore a call option payoff at expiration depends on where the underlying price is relative to the call option strike price.

In this notebook, we will plot a call buyer's and a call seller's payoff graph for a 900 strike price call on the Infosys stock.
"""
import numpy as np
import matplotlib.pyplot as plt
# For making attractive and informative statistical graph
plt.style.use('seaborn-darkgrid')


"""
Call payoff
We define a function call_payoff that calculates the payoff from buying a call option. The function takes sT, a range of possible values of the stock price at expiration, the strike price of the call option and premium of the call option as input.

It returns a numpy array containing the profit from call option for different the stock price. When the stock price is greater than the strike price, the profit is the difference between stock price and strike price and when the stock price is less than the strike price the profit is zero. After this, a call premium is deducted from the Profit-n-Loss(pnl).
"""

def call_payoff(sT, strike_price, premium):
    pnl = np.where(sT > strike_price, sT - strike_price, 0)    
    return pnl - premium

"""
Define parameters
We will define the spot price, the strike price, premium, and a range of possible values for the Infosys stock price at expiry.
"""

# Infosys stock price 
spot_price = 900 

# Call strike price and cost
strike_price = 900 
premium = 20

# Stock price range at the expiration of the call
# We have defined range for the stock price at expiry as +/- 10% from spot price
# Syntax: numpy.arange(start price, stop price)
sT = np.arange(0.9*spot_price,1.1*spot_price) 

## Call option buyer payoff
payoff_long_call = call_payoff(sT, strike_price, premium)
# Plot the graph
fig, ax = plt.subplots(figsize=(8,5))
ax.spines['bottom'].set_position('zero')
ax.plot(sT,payoff_long_call,label='Call option buyer payoff')
plt.xlabel('Infosys Stock Price')
plt.ylabel('Profit and loss')
plt.legend()
plt.show()

"""
So what do you observe?

Even if the price of Infosys goes below the strike price of 900, the maximum loss seems to be just INR 20/-. Therefore, the loss to the call option buyer is restricted to the extent of the premium he has paid.

The profit from this call option seems to increase linearly as and when Infosys starts to move above the strike price of 900. Therefore, the higher the spot price goes from the strike price, the higher is the profit.

Though the call option is supposed to make a profit when the spot price moves above the strike price, the call option buyer first needs to recover the premium he has paid.

From the above points, we can say that the buyer of the call option has limited risk and the potential to make an unlimited profit.
"""

"""
#Call option seller payoff
Option buyer and option seller are the two sides of the same coin.
 Therefore, to get the payoff graph for option seller, 
 we have multiplied the payoff of option buyer by -1.0 as when the option buyer makes the profit, 
 the option seller will lose the exact same amount and vice-versa.
 
""" 

payoff_short_call = payoff_long_call * -1.0
# Plot
fig, ax = plt.subplots(figsize=(8,5))
ax.spines['bottom'].set_position('zero')
ax.plot(sT,payoff_short_call,label='Short 940 Strike Call',color='r')
plt.xlabel('Infosys Stock Price')
plt.ylabel('Profit and loss')
plt.legend()
plt.show()
 
"""
The call option seller payoff looks like a mirror image of the call option buyer payoff.

The profit is restricted to INR 20/- as long as the spot price is trading at any price below the strike of 900.
From 900 to 920, we can see the profits getting reduced.
Above 920, the call option seller starts losing money. The losses increase with an increase in stock price.
Therefore, you sell a call option only when your view is that the underlying asset will not increase beyond the strike price.
"""
 
######################## Bear put spread payoff ##########################

payoff_bear_put_spread = payoff_long_put + payoff_short_put

print ("Max Profit:", max(payoff_bear_put_spread))
print ("Max Loss:", min(payoff_bear_put_spread))

# Plot
fig, ax = plt.subplots(figsize=(8,5))
ax.spines['bottom'].set_position('zero')
ax.plot(sT,payoff_long_put,'--',label='Long 880 Strike Put',color='g')
ax.plot(sT,payoff_short_put,'--',label='Short 860 Strike Put',color='r')
ax.plot(sT,payoff_bear_put_spread,label='Bear Put Spread')
plt.xlabel('Infosys Stock Price')
plt.ylabel('Profit and loss')
plt.legend()
plt.show()




##########################  Call Exercise ############################
"""
Let’s assume that the stock Tata Motors is trading at INR 430. We bought 430 strike call for INR 3. In this exercise, we will learn to calculate the payoff from the call option.

For a call buyer at the option expiry:
      A. If the stock price is greater than the strike price, then the call buyer profits the difference.
      B. If the stock price is less than the strike price, then the call buyer loses the premium.
To enter into this payoff structure the call buyer pays a premium to the call seller.


Coding guide
np.where can be used to create call payoff structure. The syntax of it is as follows:
payoff_array = np.where(condition, true_value, false_value)
If the condition is true then the payoff_array is assigned true_value else false_value.

The condition, true and false value for call payoff from buyer's perspective can be as follows:
condition: sT > strike_price
true_value: sT - strike_price
false_value: 0
 

Instructions

Calculate the call payoff without premium using np.where and store it in payoff_call array.
"""

import numpy as np
import pandas as pd
# Tata motors stock price
spot_price = 430
# Stock price range at expiration of the call
sT = np.arange(0.98*spot_price, 1.03*spot_price)
# Call strike price
strike_price = 430
# Call premium paid
premium = 3
# Type your code here
payoff_call = np.where(sT > strike_price,sT-strike_price,0)
print(payoff_call)


"""
In the previous exercise, you learned to calculate the payoff of call option without premium. In this exercise, we will continue the previous exercise example and calculate the payoff of a call option with premium.    

Instructions

1. Calculate the call payoff with premium by subtracting premium from call_payoff and store it in payoff_call_with_premium array.
"""

import numpy as np
import pandas as pd
# Tata motors stock price
spot_price = 430
# Stock price range at expiration of the call
sT = np.arange(0.98*spot_price, 1.03*spot_price)
# Call strike price
strike_price = 430
# Call premium paid
premium = 3
# Call payoff without premium
payoff_call = np.where(sT > strike_price, sT - strike_price, 0)
# Call payoff with premium
# Type your code here
payoff_call_with_premium = payoff_call - premium
print(payoff_call_with_premium)


######################### Computing Historical Volatility ###########

"""
Computing Historical Volatility
In this notebook, we will be computing the 20 trading days (or 1 month) historical volatility for the time period starting from 20th April, 2016 to 13th April, 2018. Historical Volatility gauges the fluctuations of underlying securities by measuring the price changes over a predetermined period of time in the past.

Import the libraries
First, we will import the necessary libraries.

Volatility helps us understand how much an asset is expected to move in a particular duration. It is a good indicator of risk in an investment. Volatility is measured by standard deviation of log returns for an asset. In this exercise, you will be computing the 20-day historical volatility using the log returns, following which the standard deviation will be computed.

Syntax:
DataFrame.rolling(window=n).std()

Parameter
window: number of observations used to calculate the statistics.

Instructions

We have already calculated the log returns of the adjusted closing price and stored in the data['Log Returns'].

You need to write only one line of code.

Create a column called 20 day Historical Volatility in the data dataframe and assign the following to it.

Call the rolling() function on data['Log Returns']
Pass the value 20 as the parameter to the rolling() function
Call the std() function
And multiply the whole with 100
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# For making attractive and informative statistical graph
plt.style.use('seaborn-darkgrid')


"""
Stock data

We will fetch the Apple data using the pandas read_csv function. We will then, print the data to visualize it by using the head() function which prints the top 5 rows of the dataset."""

data = pd.read_csv('apple_stock_data.csv')
data.head()

"""Computing Log Returns
Now we will compute the daily log returns by using the shift() function for adjusted closing prices of the security. We make use of the numpy library for computing log of today's closing price divided by yesterday's closing price. The log returns are stored in the DataFrame data under the column header 'Log Returns'."""

data['Log Returns'] = np.log(data['Adj_Close']/data['Adj_Close'].shift(1))


"""Computing Historical Volatility
The one month (or 20 trading days) historical volatility will be computed by using the DataFrame.rolling(window).std() function which computes the rolling standard deviation of data['Log Returns'] for a period of 20 trading days. The standard deviation is multiplied by 100 to compute the percentage value for volatility. The historical volatility will be stored in the DataFrame under the column header '20 day Historical Volatility'."""

data['20 day Historical Volatility'] = 100*data['Log Returns'].rolling(window=20).std()

##Plot the volatility
##We will now plot the historical volatilty to visualise how it changes over the period of one year.

plt.plot(data['20 day Historical Volatility'], color = 'b', label ='20 day Historical Volatility')
plt.legend(loc='best')
plt.show()

