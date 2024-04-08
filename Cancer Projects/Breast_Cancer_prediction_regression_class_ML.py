#!/usr/bin/env python
# coding: utf-8

# # Import Libraries

# # Breast Cancer Prediction Using Machine Learning
# 1.	Build a Logistic Regression classifier to classify cancer as malignant or benign
# 2.	Download dataset directly from Kaggle using Kaggle API (setup a kaggle acct.)

# In[1]:


#import libraries
import pandas as pd
import seaborn as sns


# # Download dataset from Kaggle

# In[7]:


#set kaggle API credentials
import os
os.environ['KAGGLE_USERNAME']='enter your username'
os.environ['KAGGLE_KEY']='enter your key'


# In[9]:


#download dataset
get_ipython().system(' kaggle datasets download -d uciml/breast-cancer-wisconsin-data')


# In[11]:


#unzip file
get_ipython().system(' unzip C:/Users/rader/breast-cancer-wisconsin-data.zip')


# # Load & Explore Data

# In[16]:


# Assign a directory path (note the single backslashes for Windows paths)
dir_path = "your_path_to_file"

# Load data into a DataFrame
df = pd.read_csv(dir_path + '/data.csv')


# In[17]:


#display dataframe
df.head()


# In[18]:


#count of rows and columns
df.shape


# In[19]:


#count number of null(empty) values
df.isna().sum()


# In[20]:


# Drop the column with null values
df.dropna(axis=1,inplace=True)


# In[21]:


# count of rows and columns
df.shape


# In[22]:


#Get count of number of Malignant  or Benign cells in diagnosis variable
df.head()


# In[23]:


#get count of number of M or B cells in diagnosis
df['diagnosis'].value_counts()


# # Label Encoding

# In[24]:


#Get Datatypes of each column in our dataset
df.dtypes


# In[25]:


#Encode the diagnosis values
from sklearn.preprocessing import LabelEncoder
Labelencoder = LabelEncoder()
#Labelencoder.fit_transform(df.iloc[:,1]).values
#Target variable isolates the second column and converts it to a NumPy array.
df.iloc[:,1].values


# In[26]:


#Target variable isolates the second column and converts it to a NumPy array.
Labelencoder.fit_transform(df.iloc[:,1].values)


# In[28]:


df.iloc[:,1]=Labelencoder.fit_transform(df.iloc[:,1].values)


# In[50]:


#display df
df


# # Split Dataset & Feature Scaling

# In[51]:


#Splitting the dataset into independent and dependent datasets features
X=df.iloc[:,2:].values


# In[52]:


#depended column
Y=df.iloc[:,1].values


# In[53]:


#Splitting datasets into training(80%) and testing(20%)
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.20)


# In[54]:


#Scaling the data(feature scaling)
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.fit_transform(X_test)


# In[55]:


#print data
X_train


# # Build a Logistic Regression Model

# In[65]:


from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
Y = label_encoder.fit_transform(df.iloc[:,1].values)


# In[66]:


from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

# Encode the diagnosis values
label_encoder = LabelEncoder()
Y = label_encoder.fit_transform(df.iloc[:,1].values)

# Splitting the dataset into independent and dependent datasets features
X = df.iloc[:,2:].values

# Splitting datasets into training(75%) and testing(25%)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25)

# Scaling the data (feature scaling)
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Build a logistic regression classifier
classifier = LogisticRegression()
classifier.fit(X_train, Y_train)


# # Performance Evaluation

# In[67]:


#plot confusion matrix
from sklearn.metrics import confusion_matrix
import seaborn as sns
cm = confusion_matrix(Y_test,predictions)
print(cm)
sns.heatmap(cm,annot=True)


# In[68]:


#make use of trained model to make predictions on test data
predictions = classifier.predict(X_test)


# In[69]:


#get accuracy score for model
from sklearn.metrics import accuracy_score
print(accuracy_score(Y_test,predictions))


# In[70]:


print(Y_test)


# In[71]:


print(predictions)


# In[ ]:




