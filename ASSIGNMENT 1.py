#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[4]:


import matplotlib.pyplot as plt


# In[10]:


import seaborn as sns


# ###  Read the dataset to python environment.

# In[8]:


df = pd.read_excel("iris (1).xls")
print(df)


# In[11]:


df.head(10)


# ### 2. Display the columns in the dataset.
# 

# In[19]:


pd.set_option("display.max_columns", None)
df


# ### 3. Calculate the mean of each column of the dataset.

# In[27]:


Mean = ['SL','SW','PL','PW']
df[Mean].mean()


# ### 4. Check for the null values present in the dataset.
# 

# In[35]:


df.isnull()


# ### 5. Perform meaningful visualizations using the dataset. Bring at least 3 visualizations.

# In[37]:


plt.figure(figsize=(10,5))
sns.histplot(x = df['SL'])
plt.title("Distribution of SL")
plt.show()


# In[39]:


plt.figure(figsize=(10,5))
sns.countplot(x = df['SL'])
plt.show()


# In[45]:


sns.boxplot(y = df['PW'])
plt.xlabel('PW')


# In[54]:


plt.figure(figsize=(10,5))
sns.boxplot(x = df['PW'], y = df['SL'])
plt.xticks(rotation = 90)
plt.show()


# In[56]:


sns.pairplot(df[['SL', 'PW']])
plt.show()

