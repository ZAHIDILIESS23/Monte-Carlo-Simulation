#!/usr/bin/env python
# coding: utf-8

# # Monto Carlo Simulation
# you have 1000 now and need to pay 1050 in one year, you have available to you two assets, a risk free asset that returns 3% and a stock that return 10% with a 20% standard deviation, how much should you invest in the two asset to maximize your probability of having at least 1050 in one year?
# 

# # the basic model

# ## Portfolio return

# In[110]:


import matplotlib.pyplot as plt
def port_end_value(stock_ret=0.1,stock_weight=0.5,rf=0.03,portfolio_initial_value=1000):
    
    portfolio_ret=rf*(1 - stock_weight)+stock_ret*stock_weight
    portfolio_end_value=portfolio_initial_value*(1+portfolio_ret)
    return portfolio_end_value
port_end_value()


# ## Monte Carlo Simulation

# In[107]:


import random


# In[133]:


def port_end_value_simulation(stock_mean=0.1, stock_std=0.2, stock_weight=0.5,n_inter=90000):
    output=[]
    for i in range(n_inter):
        stock_ret=random.normalvariate(stock_mean,stock_std)
        result=port_end_value(stock_ret,stock_weight)
        output.append(result)
    return output
result=port_end_value_simulation()
print(f'there are {len(result)}results,Firstfive:')
result[:5]


# In[134]:


df=pd.DataFrame()
df['Portfolio End Value']=result
df.plot.hist(bins=1000)
df.plot.kde()
plt.show()


# In[135]:


percentile=[i/20 for i in range(1,20)]
df['Portfolio End Value'].quantile(percentile)


# In[136]:


(df['Portfolio End Value']>=desired_cash).astype(int).mean()


# ## Analyze the outputs

# ### visualize

# In[137]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
def create_dataframe_from_result(result):
    df=pd.DataFrame()
    df['Portfolio End Value']=result
    return df

def visualize_result(df):
    df.plot.hist(bins=1000)
    plt.show()
    
def probability_table(df):
    percentile=[i/20 for i in range(1,20)]
    return df['Portfolio End Value'].quantile(percentile)

def probability_of_objective(df,desired_cash=1050):
    return (df['Portfolio End Value']>=desired_cash).astype(int).mean()

def model_output(result,desired_cash=1050):
    df=create_dataframe_from_result(result)
    visualize_result(df)
    prob_table=probability_table(df)
    prob_objective=probability_of_objective(df, desired_cash)
    return prob_table,prob_objective
def display_model_sumary(result,desired_cash=1050):
    prob_table,prob_objective=model_output(result,desired_cash=desired_cash)
    print('Probability Table')
    print(prob_table.apply(lambda x:f'${x:.2f}'))
    print('')
    print(f'probability of getting ${desired_cash:,.0f}in cash:{prob_objective:.1%}')
    print('')

    
    


# In[138]:


display_model_sumary(result)


# ## choosing an approriate weight

# In[149]:


from IPython.display import display,HTML 
display(HTML('<h2> My Title</h2>'))


# In[151]:


def display_header(header):
    display(HTML(f'<h2> {header}</h2>'))
display_header('Another Title')


# In[153]:


weight=[i/10 for i in range(1,10)]
weight


# In[154]:


for weight in weight:
    display_header(f' Result with {weight:.0%}in the stock')
    result=port_end_value_simulation(stock_weight=weight)
    display_model_sumary(result)
    


# In[ ]:




