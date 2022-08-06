#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Pandas - Open source python library for data manipulation and analysis.


# In[ ]:


Steps - Load data(importing data)---> Prepare(clean)---> Manipulate---> Model/Analyze


# In[ ]:


Series - 1D - Homogenous array, size immutable
Data Frame - 2D - size mutable table structure
panel - 3D


# In[ ]:


# Inside a dataframe, if we consider single column - it will be a series.
# to get a particular series from dataframe - pd.Series(df["column name"])


# In[ ]:


# Data Frame: 1. Heterogenous data
              2. Size mutable
              3. Data mutable


# In[1]:


import pandas as pd


# In[2]:


# Creation of Pandas Series / DataFrames

series=pd.Series([0.2,0.5,0.75,1.6])
dataframe1=pd.DataFrame([0.2,0.5,0.75,1.6])
print("pandas Series:\n",series)
print("pandas Dataframe:\n", dataframe1)


# In[3]:


# Attributes of Series

series2=pd.Series([0.2,0.5,0.75,1.6,0.75])
series2.unique()
#dataframe.unique()


# In[4]:


# to give custom index along with series

s=pd.Series([5,4,3], index=[100,200,300])
s


# In[5]:


# creating series from list # implicit indexing(auto generated index)

List=[20,15,42,55,8,94]
ser_list=pd.Series(List)
ser_list


# In[6]:


# giving explicit indexing for series using list # manual indexing(custom)

print(pd.Series(List, index=['i','ii','iii','iv','v','vi']))


# In[7]:


# creating Series from dictionary

d={'monkey':24,"rat":67,"cat":30}
ser_dict=pd.Series(d)
ser_dict


# ## indexing and slicing

# ### Slicing

# In[9]:


print(ser_dict)
print("*******************")
print(ser_dict["monkey":"rat"]) # sliced till range


# In[11]:


d=pd.Series(['a','b','c'], index=[1,2,3])
print(d)
print("*******************")
print(d[1:3])
print("*******************")
print(d[0:100])
print("*******************")
print(d[2:3])


# In[15]:


# Masking works on values

s1=pd.Series([1,2,3,4,5], index=['A','B','C','D','E'])
print(s1[(s1>1) & (s1<4)])


# ### Series Operations

# In[18]:


# Appending two series

s2=pd.Series([1,2,3,4], index=['a','b','c','d'])
s3=s1.append(s2)
s3


# In[22]:


# deleting a row with particular element

# drop works only with index, we have to specify the index of element to be dropped

s3_drop=s3.drop(['C'])
s3_drop


# ### Arithmetic Operations

# In[23]:


s4=pd.Series([6,7,8,9,10,1])
s5=pd.Series([0,1,2,3,4,5])
print(s4,'\n',s5)


# In[24]:


# operations

print("Add: ",s4.add(s5))
print("Substraction: ",s4.sub(s5))
print("Multiplication: ",s4.mul(s5))
print("Division: ",s4.div(s5))


# ### Aggregate functions / statistical functions
# ##### Helps to fill missing values in large datasets

# In[25]:


s4=pd.Series([6,7,8,9,10,1])
print("Median",s4.median())
print("Mean",s4.mean())
print("Maximum",s4.max())
print("Minimum",s4.min())


# In[26]:


# we should check the uppper and lower for strings as when working on multiple datasets, data might be in different cases(upper/lower). To standardise, we should do this

# upper and lower works on string values only

string=pd.Series(['a','b','c','E','D','f','g','h'])
print(string.str.upper())
print(string.str.lower())


# ## Pandas Data Frames
# - Genaralization of Numpy 2D arrays
# - multidimensional arrays with attached row and column labels
# - can be seen as sequence of aligned series objects, i.e share same index
# - with heterogenous data/or with missing values
# - no. of powerful data operations
# - data munging tasks

# In[28]:


population_d={'california':1230,'texas':6742,'New york':8345,'ohio':2464,'florida':6592}
population=pd.Series(population_d)
population


# In[29]:


area_d = {'california':23425,'texas':82452,'New york':23649,'ohio':36589,'florida':25492}
area=pd.Series(area_d)
area


# In[33]:


states=pd.DataFrame({"Population":population,"Area":area})
states


# In[40]:


# Dataframe as specialized dictinoary
 - Data frame maps a column name to a Series of column data


# In[41]:


# creating a data frame directly using dictionary format
pd.DataFrame([{'a':1,'b':2,'c':3,'d':4},{'a':5,'b':6,'c':7}])


# In[42]:


# data using range function
data=[{'a':i,'b':2*i} for i in range(3)]
df=pd.DataFrame(data)
df


# In[44]:


# using default indexing

data={"Animals":['cat','bat','dog'],
     'Age':[1,2,3],
     'priority':['y','y','n']}
df=pd.DataFrame(data)
df


# In[64]:


# using customized index giving labels next to index

data={"Animals":['cat','bat','dog'],
     'Age':[1,2,3],
     'priority':['y','y','n']}
labels=[1,'a','b']
df=pd.DataFrame(data,index=labels)
df


# ## Data Frame Operations

# ### Attributes 

# In[47]:


print(df.dtypes) # data types of all columns
print("\n ****************** \n")
print(df.index)  # index of whole data frames
print("\n ****************** \n")
print(df.columns) # column names of data frame
print("\n ******************\n") 
print(df.values)  # values in each row


# In[50]:


df.head(2)


# In[51]:


df.tail(2)


# In[52]:


# details of data frame

df.info()


# In[53]:


# describe gives statistical values

df.describe()


# In[54]:


# Transpose - rows to columns and columns to rows

df.T


# ### Sorting data frame
# - by default it's in ascending order
# - Mandatory to provide(by=' ')
# - can also combine sorting with slicing

# In[59]:


print(df.sort_values(by='Animals')) # sort by single


# In[63]:


print(df.sort_values(by=['Animals','priority'])) # sort by multiple values


# ### Displaying only particular columns

# In[66]:


df[["Animals","Age"]] # give the required columns in side a list


# ### Creating a copy of data frame

# In[67]:


df2=df.copy()
df2


# In[70]:


# when we want to update/change values of a particular field
df2.loc['b','Age']=4
df2


# ### Aggregate functions

# In[74]:


# mean works only for numerical values, whereas sum concatenates all strings in column, and while min and max gives as alphabtical order
print(df2.mean())
print("\n ****************** \n")
print(df2[['Age']].mean())
print("\n ****************** \n")
print(df2.sum())
print("\n ****************** \n")
print(df2[['Age']].sum())
print("\n ****************** \n")
print(df2.min())
print("\n ****************** \n")
print(df2.max())


# ### Handling Missing values

# #### Detecting null values

# In[77]:


data=pd.Series([1,None,'Hi',None])
print(data)
print("\n ****************** \n")
print(data.isnull())#### gives bool outputif None its true else false
print("\n ****************** \n")
print(data.notnull())  ## gives bool output if none its false else true


# In[78]:


# To drop all null values
print(data.dropna())


# In[ ]:


# if we use drop, it may remove even good data as it removes complete row for single null also
# for better control, we use thresh to give limit for removing null values


# In[79]:


df.dropna(axis='rows',thresh=1)


# #### Filling Null values

# In[82]:


data=pd.Series([1,2,None,None,None,5])   # usually axis will be zero i.e X axis
print(data)
print("\n ****************** \n")
print(data.fillna(0))  # Here we are filling all the null values with constant value like 0. Also we can do that by mean, median,mode etc
print("\n ****************** \n")
print(data.fillna(method='ffill')) # Here we are filling with the value which is beofer to it(from forward)
print("\n ****************** \n")
print(data.fillna(method='bfill'))  # Here we are filling with the values which is next to it(from backwards)

