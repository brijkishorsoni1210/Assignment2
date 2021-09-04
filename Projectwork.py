#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install seaborn')


# In[2]:


import seaborn as sns
sns.set()
sns.set(style="darkgrid")
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
plt.rcParams['figure.figsize']=(10,10)


# In[4]:


data_BM=pd.read_csv('Train.csv')
data_BM=data_BM.dropna(how="any")
data_BM["Visibility_Scaled"]=data_BM["Item_Visibility"]*100
data_BM.head()


# In[8]:


sns.lineplot(x="Item_Weight",y="Item_MRP",data=data_BM[:50]);


# In[9]:


sns.lineplot(x="Item_Weight",y="Item_MRP",data=data_BM);


# In[10]:


sns.barplot(x="Item_Type",y="Item_MRP",data=data_BM)


# In[11]:


sns.distplot(data_BM["Item_MRP"])


# In[12]:


sns.boxplot(data_BM["Item_Outlet_Sales"],orient="vertical")


# In[13]:


sns.boxplot(data_BM["Item_MRP"],orient="vertical")


# In[14]:


sns.violinplot(data_BM["Item_Outlet_Sales"],orient="vertical",color="orange")


# In[16]:


sns.relplot(x="Item_MRP",y="Item_Outlet_Sales",data=data_BM,kind="scatter");


# In[19]:


sns.relplot(x="Item_MRP",y="Item_Outlet_Sales",hue="Item_Type",data=data_BM,kind="scatter");


# In[20]:


sns.lineplot(x="Item_Weight",y="Item_MRP",hue="Outlet_Size",data=data_BM);


# In[22]:


sns.relplot(x="Item_MRP",y="Item_Outlet_Sales",data=data_BM,kind="scatter",size="Visibility_Scaled",hue="Visibility_Scaled");


# In[24]:


plt.figure(figsize=(10,10))
sns.distplot(data_BM["Item_Outlet_Sales"]);


# In[ ]:




