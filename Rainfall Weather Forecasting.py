#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


# In[2]:


df=pd.read_csv(r"C:\Users\HP\Downloads\weatherAUS.csv")


# In[3]:


df


# In[4]:


df.head()


# In[5]:


df.isnull().sum()


# In[6]:


import matplotlib.pyplot as plt
plt.figure(figsize = (16,5))
sns.heatmap(df.isnull()) #Looking for null values if any, in heatmap


# In[7]:


df.info()


# In[8]:


# dropping all null values
df=df.dropna()


# In[9]:


df.isnull().sum()


# In[10]:


import matplotlib.pyplot as plt
plt.figure(figsize = (16,5))
sns.heatmap(df.isnull())


# In[11]:


df.describe()


# In[12]:


dfcor=df.corr()


# In[13]:


plt.figure(figsize=(20,10))
sns.heatmap(dfcor,annot=True,linewidths=0.1,linecolor='black',fmt='0.2f')


# In[14]:


df.columns


# In[17]:


plt.figure(figsize=(20,5))
plt.title('RainToday vs Rain Tomorrow')
sns.lineplot(x='RainToday',y='RainTomorrow',data=df)
plt.show()


# In[18]:


plt.figure(figsize=(20,5))
plt.title('MinTemp vs MaxTemp')
sns.lineplot(x='MinTemp',y='MaxTemp',data=df)
plt.show()


# In[22]:


plt.title('Next day maximum Temperature')
sns.distplot(df['MaxTemp'],kde=True)


# In[23]:


plt.title('Next day minimum Temperature')
sns.distplot(df['MinTemp'],kde=True)


# In[24]:


import datetime as ddt
df['Date']=pd.to_datetime(df['Date'])
df['Date']=df['Date'].map(ddt.datetime.toordinal)


# In[25]:


df.isnull().sum()


# In[26]:


df.head()


# In[31]:


df.skew()


# In[ ]:




