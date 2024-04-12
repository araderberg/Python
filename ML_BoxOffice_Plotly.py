#!/usr/bin/env python
# coding: utf-8

# # Analyze Worldwide Box Office Revenue with Plotly and Python

# In[1]:


# Import libraries
import numpy as np
import pandas as pd

# Set display options
pd.set_option('display.max_columns', None)

import matplotlib.pyplot as plt
import seaborn as sns

get_ipython().run_line_magic('matplotlib', 'inline')
plt.style.use('ggplot')

import nltk
nltk.download('stopwords')

# Import stopwords
from nltk.corpus import stopwords
stop = set(stopwords.words('english'))

from wordcloud import WordCloud

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn import linear_model
from sklearn.model_selection import train_test_split, KFold
from sklearn import model_selection
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

import plotly.offline as py
py.init_notebook_mode(connected=True)
import plotly.graph_objs as go


# ## Data Loading and Exploration

# In[2]:


train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')


# In[3]:


train.head()


#  

#  

# ## Visualizing the Target Distribution

# In[4]:


# Distribution of target values
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# First subplot: Histogram of revenue
axes[0].hist(train['revenue'])
axes[0].set_title('Distribution of revenue')

# Second subplot: Histogram of log of revenue
axes[1].hist(np.log1p(train['revenue']))
axes[1].set_title('Distribution of log of revenue')

plt.show()



# In[5]:


train['log_revenue'] = np.log1p(train['revenue'])


# ## Relationship between Film Revenue and Budget

# In[6]:


fig, ax = plt.subplots(figsize = (16, 6))
plt.subplot(1, 2, 1)
plt.hist(train['budget']);
plt.title('Distribution of budget');
plt.subplot(1, 2, 2)
plt.hist(np.log1p(train['budget']));
plt.title('Distribution of log of budget');


# In[7]:


plt.figure(figsize=(16, 8))
plt.subplot(1, 2, 1)
plt.scatter(train['budget'], train['revenue'])
plt.title('Revenue vs budget');
plt.subplot(1, 2, 2)
plt.scatter(np.log1p(train['budget']), train['revenue'])
plt.title('Log Revenue vs log budget');


# In[8]:


train['log_budget'] = np.log1p(train['budget'])
test['log_budget'] = np.log1p(test['budget'])


# ## Does having an Official Homepage Affect Revenue?

# In[9]:


train['homepage'].value_counts().head(7)


# In[10]:


train['has_homepage'] = 0
train.loc[train['homepage'].isnull() == False, 'has_homepage'] = 1
test['has_homepage'] = 0
test.loc[test['homepage'].isnull() == False, 'has_homepage'] = 1


# In[11]:


import warnings

# Suppress the warning
warnings.filterwarnings("ignore", message="The figure layout has changed to tight")

# Create the catplot
sns.catplot(x='has_homepage', y='revenue', data=train)

# Set the title
plt.title('Revenue for film with and w/o homepage')

# Adjust the layout manually
plt.tight_layout()

# Show the plot
plt.show()



# ## Distribution of Languages in Film

# In[12]:


plt.figure(figsize=(16, 8))
plt.subplot(1, 2, 1)
sns.boxplot(x='original_language', y='revenue', data=train.loc[train['original_language'].isin(train['original_language'].value_counts().head(10).index)]);
plt.title('Mean revenue per language');
plt.subplot(1, 2, 2)
sns.boxplot(x='original_language', y='log_revenue', data=train.loc[train['original_language'].isin(train['original_language'].value_counts().head(10).index)]);
plt.title('Mean log revenue per language');


# ## Frequent Words in Film Titles and Discriptions

# In[13]:


plt.figure(figsize = (12, 12))
text = ' '.join(train['original_title'].values)
wordcloud = WordCloud(max_font_size=None, background_color='white', width=1200, height=1000).generate(text)
plt.imshow(wordcloud)
plt.title('Top words in Movie Titles')
plt.axis("off")
plt.show()


# ## Analyze Movie Release Dates

# In[14]:


test.loc[test['release_date'].isnull() == False, 'release_date'].head()


# In[15]:


# Preprocessing Features
def fix_date(x):
    year = x.split('/')[2]
    if int(year) <= 19:
        return x[:-2] + '20' + year
    else:
        return x[:-2] + '19' + year
        


# In[16]:


test.loc[test['release_date'].isnull() == True].head()


# In[17]:


test.loc[test['release_date'].isnull() == True, 'release_date'] = '05/01/00'


# In[18]:


train['release_date'] = train['release_date'].apply(lambda x: fix_date(x))
test['release_date'] = test['release_date'].apply(lambda x: fix_date(x))


#  

# ### Task 4: Creating Features Based on Release Date

# In[19]:


train['release_date'] = pd.to_datetime(train['release_date'])
test['release_date'] = pd.to_datetime(test['release_date'])


# In[20]:


def process_date(df):
    date_parts = ['year', 'weekofyear', 'month', 'weekday', 'day', 'quarter']
    for part in date_parts:
        part_col = 'release_date' + '_' + part
        if part == 'weekofyear':
            df[part_col] = df['release_date'].dt.isocalendar().week.astype(int)
        else:
            df[part_col] = getattr(df['release_date'].dt, part).astype(int)
    return df

# Assuming train and test DataFrames are already defined and contain 'release_date' column
train = process_date(train)
test = process_date(test)


# ### Task 5: Using Plotly to Visualize the Number of Films Per Year

# In[21]:


d1 = train['release_date_year'].value_counts().sort_index()
d2 = test['release_date_year'].value_counts().sort_index()


# In[22]:


import plotly.offline as py
py.init_notebook_mode(connected=True)
import plotly.graph_objs as go

data = [go.Scatter(x=d1.index, y=d1.values, name='train'),
        go.Scatter(x=d2.index, y=d2.values, name='test')]

layout = go.Layout(dict(title = 'Number of films per year',
                       xaxis = dict(title = 'Year'),
                       yaxis = dict(title = 'Count'),
                        ), legend = dict(orientation='v'))
py.iplot(dict(data=data, layout=layout))


# ## Number of Films and Revenue Per Year

# In[23]:


d1 = train['release_date_year'].value_counts().sort_index()
d2 = train.groupby(['release_date_year'])['revenue'].sum()

data = [go.Scatter(x=d1.index, y=d1.values, name='film_count'),
        go.Scatter(x=d2.index, y=d2.values, name='total revenue', yaxis='y2')]

layout = go.Layout(dict(title = 'Number of films and total revenue per year',
                       xaxis = dict(title = 'Year'),
                       yaxis = dict(title = 'Count'),
                       yaxis2 = dict(title='Total Revenue', overlaying='y', side='right')), 
                   legend = dict(orientation='v'))
py.iplot(dict(data=data, layout=layout))


# In[24]:


# Group by 'release_date_year' and calculate the count and mean revenue
grouped_data = train.groupby('release_date_year').agg({'revenue': ['count', 'mean']})
grouped_data.columns = ['film_count', 'average_revenue']

# Create traces for plotting
trace1 = go.Scatter(x=grouped_data.index, y=grouped_data['film_count'], name='Film Count')
trace2 = go.Scatter(x=grouped_data.index, y=grouped_data['average_revenue'], name='Average Revenue', yaxis='y2')

# Define layout
layout = go.Layout(title='Number of films and average revenue per year',
                   xaxis=dict(title='Year'),
                   yaxis=dict(title='Film Count'),
                   yaxis2=dict(title='Average Revenue', overlaying='y', side='right'))

# Plot the data
fig = go.Figure(data=[trace1, trace2], layout=layout)
py.iplot(fig)


# ## Do Release Days Impact Revenue?

# In[25]:


sns.catplot(x='release_date_weekday', y='revenue', data=train);
plt.title('Revenue on different days of the week')


# ## Relationship between Runtime and Revenue

# In[26]:


#divide by 60 to convert to hrs
# Convert runtime to hours and plot using displot
sns.displot(train['runtime'].fillna(0) / 60, bins=40, kde=False)
plt.title('Distribution of the length of films in hours')
plt.show()


# In[27]:


#film are within 1 to 3 hrs
# Create scatter plot of runtime vs revenue
sns.scatterplot(x=train['runtime'].fillna(0) / 60, y=train['revenue'])
plt.title('Runtime vs Revenue')
plt.show()

