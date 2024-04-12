#!/usr/bin/env python
# coding: utf-8

# # Covid19 Data Analysis Notebook

# In[2]:


import numpy as np 
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt 
print('Modules imported.')


# ### importing covid19 dataset

# In[19]:


# Read the CSV file while skipping lines with errors
corona = pd.read_csv('covid19_Confirmed_dataset.csv')
corona.head()


# #### Let's check the shape of the dataframe

# In[20]:


#check the shape of the dataframe
corona.shape


# ### Delete unwanted columns

# In[21]:


corona.drop(['Lat','Long', 'Province/State'],axis=1,inplace=True)


# In[22]:


corona.head()


# ### Aggregate rows by country

# In[ ]:


corona_countries = corona.groupby("Country/Region").sum()


# In[24]:


corona_countries.head(10)


# In[25]:


corona_countries.shape


# ### Visualize data related to a country

# In[30]:


#corona_countries = corona_countries.apply(pd.to_numeric, errors='coerce')

# Plot data for China, Italy, and Spain
corona_countries.loc['Italy'].plot()
corona_countries.loc['China'].plot()
corona_countries.loc['US'].plot()
# Set y-axis lower limit to 0
plt.ylim(bottom=0)
plt.legend()
plt.show()


# ### Calculating a good measure 

# In[36]:


corona_countries.loc['US'].plot()


# ### Caculating the first derivative of the curve

# In[35]:


corona_countries.loc['US'].diff().plot()


# ### Find maximum infection rate for US, Italy and China

# In[39]:


corona_countries.loc['US'].diff().max()


# In[40]:


corona_countries.loc['Italy'].diff().max()


# In[41]:


corona_countries.loc['China'].diff().max()


# ### Find maximum infection rate for all of the countries. 

# In[42]:


countries = list(corona_countries.index)
max_infection_rates = []
for country in countries :
    max_infection_rates.append(corona_countries.loc[country].diff().max())
corona_countries['max infection rate'] = max_infection_rates


# In[43]:


corona_countries.head()


# In[52]:


# Filter data for the specified countries
selected_countries = corona_countries.loc[['US', 'Italy', 'China']]


# In[53]:


# Calculate maximum infection rate for each country
max_infection_rate = selected_countries.max(axis=1)


# In[54]:


# Display the results
print("Maximum Infection Rates:")
print(max_infection_rate)


# ### Create a new dataframe with only needed column 

# In[59]:


corona_data = pd.DataFrame(corona_countries['max infection rate'])


# In[60]:


corona_data.head()


# In[68]:


# Plot the dataset
plt.figure(figsize=(10, 6))
selected_countries.T.plot(marker='o')  # Transpose DataFrame to plot dates on x-axis
plt.title('Infection Numbers by Dates')
plt.xlabel('Date')
plt.ylabel('Infection Numbers')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend(title='Country/Region')
plt.tight_layout()
plt.show()

