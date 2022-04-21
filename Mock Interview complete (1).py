#!/usr/bin/env python
# coding: utf-8

# <h3> Mock Interview Python Screening test </h3>
# 

# In[682]:


import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
import statsmodels.api as sm
sns.set_style("darkgrid")
mpl.rcParams['figure.figsize'] = (20,5)
df= pd.read_csv("adult_census_data.csv")


# In[683]:


df.head()


# In[684]:


df.info()


# In[ ]:





# In[685]:


df.columns


# <b> Q1. After importing the adult_census_data.csv file, please filter this to include only the following criteria: </b>
# <p>
# 
# <li> State-Gov</li>
# <li> Bachelors </li>
# <li> Never-Married </li>
# <li> Adm-Clerical </li> 
# <li> Not-in-familiy </li>
# <li> White </li>
# <li> Male </li> 
# <li> United States </li>
# <li> <=50K </li> 
# 
# <b> Feel free to any method to complete this tasks. However, we recommend you use either list filtering [], or .loc to complete this task.</b>

# <b> Put your code below </b>

# In[686]:


df[[' State-gov',' Bachelors',' Never-married',' Adm-clerical',' Not-in-family',' White',' Male',' United-States',' <=50K']]


# <b> Currently, the dataframe you are using has the following column names: </b>
# 
# [' State-gov', ' Bachelors', ' Never-married',
#        ' Adm-clerical', ' Not-in-family', ' White', ' Male', ' United-States', ' <=50K']
#        
#      
# <b> Q2. Please re-name all the newly filtered columns in the pandas DataFrame to the following: </b>
# 
# Employment Type, Degree Status, Marriage-Status, Job-Role, Family-Role, Ethnicity, Gender, Country, Earnings
# 
# E.g. State-Gov becomes Employment Type, Bachelors becomes Degree Status, etc.

# <b> Put your code below </b>

# In[687]:


df.rename(columns={' State-gov':'Employment-Type',' Bachelors':'Degree-Status',' Never-married':'Marriage-Status',' Adm-clerical':'Job-Role',' Not-in-family':'Family-Role',' White':'Ethnicity',' Male':'Gender',' United-States':'Country',' <=50K':'Earnings'}, inplace=True)


# In[694]:


df1=df[['Employment-Type','Degree-Status','Marriage-Status','Job-Role','Family-Role','Ethnicity','Gender','Country','Earnings']]
df1


# <b> Q3. The Job Role Columns holds the job information for each individual in this census snapshot. Using this column, create a Bar Chart that shows the count of 'Unique' Jobs per Job Group in the "Job-Role" Column in ascending order, as per the provided image below </b>
# 

# <b> Put your code below </b>

# In[ ]:





# In[692]:





# In[695]:


job_code=df1['Job-Role'].value_counts()
job_code.plot(kind='bar')
plt.show()


# In[ ]:





# In[723]:


newdf=df1[(df1['Degree-Status']==" HS-grad") & (df1['Earnings']==' <=50K')]
newdf['Job-Role'].value_counts().plot(kind='bar')
plt.show()


# <b> Q4. Please create two bar plots as per below that show:
#     
#     1) The number of individuals who have a High School Graduate Diploma AND earn <=50K in the United States
#     2) The number of individuals who have a High School Graduate Diploma AND earn >50K in the United States 
# 
# Please note you will be looking specifically at the *Job Role* column

# <b> Put Your Code Below </b>

# In[724]:


newdf=df1[(df1['Degree-Status']==" HS-grad") & (df1['Earnings']==' >50K')]
newdf['Job-Role'].value_counts().plot(kind='bar')
plt.show()


# In[ ]:





# In[ ]:





# 
# 

# <H2> Challenge Question </H2>
# 
# <b> Q5. Which Job Role has the highest <i> proportion </i> of individuals who earn >50K? </b>

# <b> Put your code below </b>

# In[729]:


newdf2=df1[(df1['Earnings']==' >50K')]
newdf2['Job-Role'].value_counts(normalize=True).round(2)


# In[ ]:




