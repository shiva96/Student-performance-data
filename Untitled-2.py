#!/usr/bin/env python
# coding: utf-8

# In[12]:


#for some basic operations

import pandas as pd
import numpy as np


#for visualizations

import matplotlib.pyplot as plt
import seaborn as sns


get_ipython().run_line_magic('matplotlib', 'inline')


# In[15]:


student=google_data = pd.read_csv('/Users/shivanimishra/Downloads/ML projects/student performance dataset/StudentsPerformance.csv')
student.head()                        


# In[16]:


google_data.shape


# In[18]:


type(google_data)


# In[7]:


type(google_data)


# In[8]:


google_data.head(10)


# In[9]:


google_data.tail(10)


# In[10]:


google_data.describe()   #summary statistics


# In[11]:


google_data.boxplot()


# In[12]:


google_data.hist()


# In[13]:


google_data.info()


# In[15]:


#datacleaning
google_data.isnull()


# In[16]:


google_data.isnull().sum()


# In[25]:


#no missing values found
#no null values in the data set
google_data[google_data.lunch == "standard"]


# In[31]:


student = google_data.drop(['race/ethnicity','parental level of education'], axis=1)


# In[32]:


student.head()


# In[33]:


correlation = student.corr()


# In[37]:


sns.heatmap(correlation, xticklabels = correlation.columns, yticklabels=correlation.columns, annot=True)


# In[38]:


sns.pairplot(student)


# In[39]:


sns.relplot(x='math score', y ='reading score', hue='gender', data=student)


# In[40]:


sns.distplot(student['math score'])


# In[41]:


sns.distplot(student['writing score'], bins=5)


# In[42]:


sns.catplot(x='math score', kind='box', data=student)


# In[51]:


#comparison of all other attributes with respet to maths marks
plt.rcParams['figure.figsize'] =(18,6)
plt.style.use('fivethirtyeight')
dabl.plot(data, target_col = 'math score')


# In[55]:


pip install klib


# In[56]:


import klib


# In[60]:


plt.figure(figsize=(10,5))
google_data.gender.value_counts().plot(kind='barh',color=['salmon','lightgreen'])
plt.xlabel('Count',fontsize=20)
plt.ylabel('Gender',fontsize=20)
y= google_data.gender.value_counts()
for index, count in enumerate(y):
    plt.text(count, index, str(count))


# In[62]:


plt.figure(figsize=(20,5))
google_data['race/ethnicity'].value_counts().plot(kind='barh',color=['salmon', 'lightgreen', 'lightblue', 'Gainsboro', '#FFE9EE'])
plt.xlabel('Count', fontsize=20)
plt.ylabel('Race', fontsize=20)

y = google_data['race/ethnicity'].value_counts()

for index, count in enumerate(y):
    plt.text(count, index,
             str(count))


# In[63]:


plt.figure(figsize=(20,5))
google_data['parental level of education'].value_counts().plot(kind='barh', color=['#fddc5c','#aefd6c','#efc5b5','#d3b683','#98f6b0','#a2cffe'])
plt.xlabel('Count', fontsize=20)
plt.ylabel('Level of Education', fontsize=20)

y = google_data['parental level of education'].value_counts()

for index, count in enumerate(y):
    plt.text(count, index,
             str(count))
plt.show()


# In[66]:


sns.relplot(x='math score', y='reading score', hue='gender', data=google_data)


# In[68]:


klib.dist_plot(google_data)


# In[70]:


sns.distplot(student['reading score'],color ='grey')


# In[72]:


gender=student.groupby(["gender"])["math score","reading score","writing score"].mean()
gender=gender.reset_index()
gender


# In[74]:


gender.plot(x="gender", y=["math score","reading score","writing score"],kind="bar",color=['purple',"orange","brown"],figsize=(8,4), width=0.2)
plt.xlabel('gender',size=15)
plt.ylabel('Marks',size=15)
plt.title("marks in each category", size=20)
plt.show()


# In[20]:


from sklearn.preprocessing import LabelEncoder

for c in student.columns:
    if student[c].dtype=='object':
        lb1 = LabelEncoder()
        lb1.fit(list(student[c].values))
        student[c] =lb1.transform(student[c].values)
        
    
student.head(10).style.background_gradient(cmap ='hot')


# In[21]:


#plotting the different responses for revents and regions

sns.lineplot(x= "math score", y= "reading score", hue ="gender", data= student)


# In[22]:


sns.lineplot(x= "math score", y= "writing score", hue ="gender", data=student)


# In[24]:


sns.countplot(x = "parental level of education", hue="gender", data=student)


# In[29]:


sns.catplot(x="race/ethnicity", y ="math score", hue="gender", col="lunch", data = student, kind = "bar", height=4 , aspect=.7, saturation=5)


# In[30]:


#meal is important hence we need to lookinto the relation between the lunch type aand math score

sns.catplot(x="race/ethnicity", y="math score", hue="gender", col="parental level of education", data=student, kind="bar", saturation = 10, height =4, aspect)


# In[31]:


#math scores based on parental level comparing the female and male scores. 
sns.catplot(x="race/ethnicity", y="reading score", hue="gender", col="parental level of education", data= student, kind="bar", height=5, aspect=.7, saturation=1)


# In[33]:


#definiteness of the plot 
sns.jointplot(data=student, x="writing score", y="reading score", hue="gender")


# In[34]:


sns.jointplot(data=student, x="math score", y="reading score", hue="gender")


# In[36]:


sns.jointplot(data=student, x="writing score", y="math score", hue="gender")


# In[ ]:


#correlation with distribution plots of continuous variables like math score and reading + writing scores. 


#conclusions:
# meals are important aspect of the dependency between the math score and absentees in lunch , 
# reading , writing and math sores are found to be more related to parental velvel of education specially linked to masters degree. 
#females are ahead in writing and reasding scores whereas in maths males lead

