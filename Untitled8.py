#!/usr/bin/env python
# coding: utf-8

# In[34]:


import pandas as pd
import numpy as np

def read_csv():
    data = pd.read_csv('Tableaupanda.csv', sep=";")
    print(data.sort_values(by-'id', ascending=True).head(20))
    
read_csv()


# In[4]:


import pandas as pd
import numpy as np
series = pd. Series ( [ 1 , 2 , 3 , 4 , 5 , np.nan, "a string" , 6 ])
series

dtype: object
    
data = data.replace('Tableaupanda.csv', np.nan)

    data['prod_cost'] = pd.to_numeric(data['prod_cost'])
    print(data['prod_cost'])
    data['prod_cost'] = data['prod_cost'].replace(np.nan, data['prod_cost'].mean())
    print(data['prod_cost']
          
def product_type():
    data = pd.read_csv('panda1.csv', sep=";")
    data.product_type = pd.Categorical(data.product_type)
    data['product_type'] = data.product_type.cat.codes
    data['product_type'] = pd.factorize(data['product_type'])[0] + 1
    print(data['product_type'])

product_type()        


# In[32]:


def warranty():
    data = pd.read_csv('Tableaupanda.csv', sep=";")
    data['warranty'] = pd.to_numeric(data['warranty'].str[0])
    print(data['warranty'])
    
warranty()

def warranty():
    data = pd.read_csv('Tableaupanda.csv', sep=";")
    data['warranty'] = pd.to_numeric(data['warranty'].str[0])
    print(data['warranty'])
    
warranty()


# In[20]:


def product_type():
    data = pd.read_csv('Tableaupanda.csv', sep=";")
    data.product_type = pd.Categorical(data.product_type)
    data['product_type'] = data.product_type.cat.codes
    data['product_type'] = pd.factorize(data['product_type'])[0] + 1
    print(data['product_type'])

product_type() 


# In[36]:


dtype: object
    
data = data.replace('Tableaupanda.csv', np.nan)

data['prod_cost'] = pd.to_numeric(data['prod_cost'])
print(data['prod_cost'])
data['prod_cost'] = data['prod_cost'].replace(np.nan, data['prod_cost'].mean())
print(data['prod_cost'])


# In[25]:


for numbers in data.price:
       if numbers <= float(300):
           print(numbers, "1")
       elif numbers >= float(301) and numbers <= float(500):
           print(numbers, "2")
       else:
           print(numbers, "3")


# In[35]:


def price():
    data = pd.read_csv('Tableaupanda.csv', sep=";")
    print(data.head(20))
    inf = float("inf")
    data['price'] = pd.cut(data['price'], bins=[0,301,501,inf])
    print(data['price'].head(20))
    
price()


# In[ ]:




