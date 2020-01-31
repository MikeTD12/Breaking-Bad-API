#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
import pandas as pd
import requests


# In[37]:


url = 'https://www.breakingbadapi.com/api/quote?author=Jesse+Pinkman'
response = requests.get(url)
print(response.text)


# In[38]:


df = pd.DataFrame.from_dict(response.json())
print(len(df))
print(df.columns)
df


# In[41]:


response2 = requests.get('https://www.breakingbadapi.com/api/episodes/')
df2 = pd.DataFrame.from_dict(response2.json())
print(len(df))
print(df.columns)
df2


# In[60]:


response3 = requests.get('https://www.breakingbadapi.com/api/deaths/')
df3 = pd.DataFrame.from_dict(response3.json())
print(len(df))
print(df.columns)
df3.head(20)


# In[93]:


death_by_character = df3.groupby(['responsible'])['number_of_deaths'].sum()
death_by_character


# In[95]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[126]:


import seaborn as sns
plot_dims = (12, 12)
fig, ax = plt.subplots(figsize=plot_dims)
death_chart = sns.barplot(y='responsible', x='number_of_deaths',
                          data=df3.query('number_of_deaths != 167'))


# In[131]:


url5 = 'http://nflarrest.com/api/v1/crime/timeline/Theft'
response5 = requests.get(url5)
print(response5.text)


# In[ ]:




