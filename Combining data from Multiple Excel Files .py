#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd 
import numpy as np
import glob
all_data = pd.DataFrame()
for f in glob.glob("Downloads/datasets/datasets/weekly_call_data/weekdata_*.xlsx"):
    df = pd.read_excel(f)
    all_data = all_data.append(df,ignore_index=True) 


# In[15]:


all_data.describe()


# In[16]:


all_data.head()


# In[17]:


all_data.tail()


# In[ ]:




