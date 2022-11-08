import pandas as pd
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

#Target stock:American Express (AXP)
#Industry comparables: Visa, Discover, Mastercard

trgt_st = 'AXP'
indus_st = ['MA','V','DFS']

# Getting the P/E ratio for the stocks by creating functions
                
def calculate_PE(tic):
    df = yf.Ticker(tic)
    fin = df.financials
    bs = df.balance_sheet
    shares = df.info['sharesOutstanding']
    earnings = df.earnings['Earnings'].iloc[-1]
    price = df.info['regularMarketPrice']
    eps = earnings/shares
    PE = price/eps
    return(PE)

for tic in trgt_st:
    PE_ratio = calculate_PE(trgt_st)
    print(trgt_st, "PE Ratio is:", PE_ratio)

new_list = []
for tic in indus_st:
    PE_ratio = calculate_PE(tic)
    new_list.append(PE_ratio)
    print(tic, "PE Ratio is:", PE_ratio)

indus_avg = sum(new_list)/len(new_list)   

# Plotting bar chart     
a = trgt_st
b = indus_st
c = 'indus_avg'
a1 = calculate_PE(trgt_st)
b1 = new_list
c1 = indus_avg
plt.bar(a,a1, color='purple')
plt.bar(b,b1, color='cyan')
plt.bar(c,c1, color='orange')
plt.show()

# Finding the implied price
df1 = yf.Ticker(trgt_st)
shares = df1.info['sharesOutstanding']
earnings = df1.earnings['Earnings'].iloc[-1]
df1_eps = earnings/shares    
implied_price = c1*df1_eps
print(implied_price)

# Finding whether AXP is an overvalued or undervalued stock compared to industry comparables  
if(a1<c1):
    print('The target stock is Undervalued')
elif(a1>c1):
    print('The target stock is Overvalued')
    
   