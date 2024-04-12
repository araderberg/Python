#!/usr/bin/env python
# coding: utf-8

# # Visualizing COVID-19 Data with Python: Exploring Pandemic Trends and Insights

# In[98]:


#Import libraries
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt 


# In[99]:


# Loading the Dataset
df_url = 'https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv'
df = pd.read_csv(df_url)


# In[100]:


#check dataframe
df.head()


# In[101]:


df.tail()


# In[102]:


#check the shape of the dataframe
df.shape


# ### Preprocessing 

# In[103]:


df = df[df.Confirmed > 0]


# In[104]:


# check data related to country = Netherlands 
df[df.Country == 'Netherlands']


# ### Global spread among countries of Covid19

# In[105]:


fig = px.choropleth(df, locations = 'Country', locationmode='country names', color='Confirmed'
                   ,animation_frame='Date')
fig.update_layout(title_text = 'Global Spread of COVID')
fig.show()


# ## Review global deaths of Covid19

# In[106]:


fig = px.choropleth(df , locations = 'Country', locationmode='country names', color='Deaths'
                   ,animation_frame='Date')
fig.update_layout(title_text = 'Global Deaths of COVID')
fig.show()


# ## check the intensive of Covid19 Transmission in each of the country

# In[107]:


df_usa = df[df.Country =='US']
df_usa.head()


# In[108]:


#Select a small sub-set of the data
df_usa = df_usa[['Date','Confirmed']]


# In[109]:


df_usa.tail(10)


# In[110]:


# Calculate the first derivative of confirmed cases for Spain and assign it to a new column
df_usa.loc[:, 'Infection Rate'] = df_usa['Confirmed'].diff()

# Display the DataFrame with the new column
print(df_usa)



# In[111]:


px.line(df_usa , x = 'Date' , y = ['Confirmed', 'Infection Rate'])


# In[112]:


df_usa['Infection Rate'].max()


# ### Calculate maximum infection rate for all of the countries

# In[113]:


countries = list(df['Country'].unique())
#countries
max_infection_rate = []
for c in countries:
    MIR = df[df.Country == c].Confirmed.diff().max()
    max_infection_rate.append(MIR)

print(max_infection_rate)


# ## Create a new dataframe 

# In[114]:


df_MIR = pd.DataFrame()
df_MIR['Country'] = countries
df_MIR['Max Infection Rate'] = max_infection_rate
df_MIR.head()


# ## Plot the barchart

# In[115]:


# Display the maximum infection rate per country
px.bar(df_MIR, x='Country', y='Max Infection Rate', color = 'Country', title = 'Global Maximum Infection Rate')


# ## Check how National Lockdowns Impacted Covid19 transmission in the United Kingdom

# In[116]:


# UK data the initial lockdown measures were announced by Prime Minister
# Boris Johnson in a televised address to the nation on March 23, 2020.
uk_lockdown_start_date = '2020-03-23'
uk_lockdown_a_month_later = '2020-04-23'


# In[117]:


# get data for UK
df_uk = df[df.Country == 'United Kingdom']


# ## Calculate the infection rate in the UK

# In[118]:


# Calculate the first derivative of confirmed cases for the UK and assign it to a new column
df_uk.loc[:, 'Infection Rate'] = df_uk['Confirmed'].diff()

# Display the DataFrame with the new column
print(df_uk.head())


# In[119]:


import plotly.express as px

# Visualize the UK data
fig = px.line(df_uk, x='Date', y='Infection Rate', title="Before and After Lockdown in the UK")

# Add vertical line for the starting date of the lockdown
fig.add_shape(
    dict(
        type="line",
        x0=uk_lockdown_start_date,
        y0=0,
        x1=uk_lockdown_start_date,
        y1=df_uk['Infection Rate'].max(),
        line=dict(color='red', width=2)
    )
)

# Add annotation for the starting date of the lockdown
fig.add_annotation(
    dict(
        x=uk_lockdown_start_date,
        y=df_uk['Infection Rate'].max(),
        text="       Starting date of the lockdown",
        showarrow=True,
        arrowhead=1,
        arrowcolor='red',
        ax=50,
        ay=-50
    )
)

# Add vertical line for a month later
fig.add_shape(
    dict(
        type="line",
        x0=uk_lockdown_a_month_later,
        y0=0,
        x1=uk_lockdown_a_month_later,
        y1=df_uk['Infection Rate'].max(),
        line=dict(color='green', width=2)
    )
)

# Add annotation for a month later
fig.add_annotation(
    dict(
        x=uk_lockdown_a_month_later,
        y=df_uk['Infection Rate'].max(),
        text="A month later",
        showarrow=True,
        arrowhead=1,
        arrowcolor='green',
        ax=-100,
        ay=-50
    )
)

fig.show()


# ## Check how National Lockdowns Impacted Covid19 active cases in the United Kingdom

# In[120]:


#deaths rate calculation number of active cases day by day 
df_uk.loc[:, 'Deaths Rate'] = df_uk.Deaths.diff()


# In[121]:


# check dataframe again
df_uk.head()


# ## Plot a line chart to compare COVID19 national lockdowns impacts on spread of the virus and number of active cases

# In[122]:


# Visualize the UK data
fig = px.line(df_uk, x='Date', y=['Infection Rate', 'Deaths Rate'])
fig.show()

# Normalize the columns using .loc
df_uk.loc[:, 'Infection Rate'] = df_uk['Infection Rate'] / df_uk['Infection Rate'].max()
df_uk.loc[:, 'Deaths Rate'] = df_uk['Deaths Rate'] / df_uk['Deaths Rate'].max()


# ## COVID19 lockdown in Germany 
# Lockdown was started in Freiburg, Baden-Württemberg and Bavaria on 20 March 2020. Three days later, it was expanded to the whole of Germany

# In[123]:


Germany_lockdown_start_date = '2020-03-23' 
Germany_lockdown_a_month_later = '2020-04-23'


# In[124]:


# select the data related to Germany
df_germany = df[df.Country == 'Germany']


# In[125]:


# check the dataframe
df_germany.head()


# In[126]:


df_germany.loc[:, 'Infection Rate'] = df_germany.Confirmed.diff()
df_germany.head()


# ## Plot the line chart

# In[127]:


# Visualize the Germany data
fig = px.line(df_germany, x='Date', y='Infection Rate', title="Before and After Lockdown in Germany")

# Add vertical line for the starting date of the lockdown
fig.add_shape(
    dict(
        type="line",
        x0=Germany_lockdown_start_date,
        y0=0,
        x1=Germany_lockdown_start_date,
        y1=df_germany['Infection Rate'].max(),
        line=dict(color='red', width=2)
    )
)

# Add annotation for the starting date of the lockdown
fig.add_annotation(
    dict(
        x=Germany_lockdown_start_date,
        y=df_germany['Infection Rate'].max(),
        text="Starting date of the lockdown",
        showarrow=True,
        arrowhead=1,
        arrowcolor='red',
        ax=50,
        ay=-50
    )
)

# Add vertical line for a month later
fig.add_shape(
    dict(
        type="line",
        x0=Germany_lockdown_a_month_later,
        y0=0,
        x1=Germany_lockdown_a_month_later,
        y1=df_germany['Infection Rate'].max(),
        line=dict(color='green', width=2)
    )
)

# Add annotation for a month later
fig.add_annotation(
    dict(
        x=Germany_lockdown_a_month_later,
        y=df_germany['Infection Rate'].max(),
        text="A month later",
        showarrow=True,
        arrowhead=1,
        arrowcolor='green',
        ax=50,
        ay=-50
    )
)

fig.show()


# In[ ]:




