#!/usr/bin/env python
# coding: utf-8

# # Education and Related Statistics for the U.S. States Data Analysis

# ## Importing the data

# In[1]:


import pandas as pd


# In[2]:


df_1992 = pd.read_csv('States_1992.csv')
df_1992.head()


# In[3]:


df_1992.shape


# In[4]:


df_1992.size


# In[5]:


df_1992.columns


# In[6]:


df_1993 = pd.read_csv('States_1993.csv')
df_1993.head()


# In[7]:


df_1993.shape


# In[8]:


df_1993.size


# In[9]:


df_1993.columns


#  ## Missing data

# In[10]:


df_1992.isna().sum()


# In[11]:


#removing dropna() = rows; dropna(1) = columns
df_clean_1992 = df_1992.dropna()


# In[12]:


df_clean_1992.shape


# In[13]:


df_1993.isna().sum()


# In[14]:


#removing dropna() = rows; dropna(1) = columns
df_clean_1993 = df_1993.dropna()


# In[15]:


df_clean_1993.shape


# ## Exploratory data

# In[16]:


# Descriptive statistics
df_clean_1992.describe()


# In[17]:


pd.set_option('display.float_format', lambda x: '%.3f' %x)
df_clean_1992.describe().style.format("{:,.0f}")


# In[18]:


import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[19]:


sns.boxplot(x=df_clean_1992['pay'])


# ## Outliers

# In[20]:


columns = df_clean_1992.columns
columns


# In[21]:


#len of the columns and 2 index since the country and region cannot be boxplot
for i in range(2, len(columns)):
  print(columns[i])


# In[22]:


for i in range(2, len(columns)):
  fig = plt.figure(figsize=(10,5))
  sns.boxplot(x=df_clean_1992[columns[i]])


# In[23]:


dollars_max = df_clean_1992['dollars'].max()
df_clean_1992[df_clean_1992['dollars'] == dollars_max]

#State spending on public education, in \$1000s per student.


# In[25]:


df_clean_1992[df_clean_1992['pop'] > 1000]


# ## Exploring Relationships

# In[26]:


# Correlations
df_clean_1992.corr(method='pearson', numeric_only=True).style.background_gradient(cmap='viridis')


# In[37]:


df_clean_1993.corr(method='spearman', numeric_only=True).style.background_gradient(cmap='coolwarm')


# In[27]:


df_clean_1993.corr(method='spearman', numeric_only=True).style.background_gradient(cmap='viridis')


# In[28]:


# Update the code to plot a scatter chart
df_clean_1992.plot.scatter(x='dollars', y='percent')


# In[29]:


#remove the outliear
df_clean_out = df_clean_1992[df_clean_1992['State'] != 'NJ']


# In[30]:


#correlation plot
df_clean_out.plot.scatter(x='dollars',y='percent')


# ## T-tests

# In[31]:


import scipy.stats as stats


# In[32]:


a = df_clean_1992['pay']
b = df_clean_1993['pay']
stats.ttest_ind(a,b)


# In[33]:


for i in range(2, len(columns)):
  a = df_clean_1992[columns[i]]
  b = df_clean_1993[columns[i]]
  print(columns[i])
  print(stats.ttest_ind(a,b))


# In[34]:


for i in range(2, len(columns)):
  a = df_clean_1992[columns[i]]
  b = df_clean_1993[columns[i]]
  print(columns[i])
  statistic, pvalue = stats.ttest_ind(a,b)
  print("Statistics: %s p-value: %s" %(statistic, pvalue))
  if pvalue < 0.05:
    print("Significant")
  else:
    print("Not Significant")

