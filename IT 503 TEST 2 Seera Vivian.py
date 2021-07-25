#!/usr/bin/env python
# coding: utf-8

# IT 503 Strategic Planning and Management
# Vivian Seera 
# MAY21/PGDIT/578U
# 
# ATTEMPT
# •	Use python 3.7 or higher for implementation.
# •	Take the screen shots of your codes and upload in the university platform and also share your uploaded codes/output in your Github account with the Instructor.
# •	Make representation of the data set in:
# 1.	A Column chart (10 marks)
# 2.	A Bar chart(10 marks)

# In[1]:


import requests
import pandas as pd
import numpy as np


# In[2]:


#importing libraries 
get_ipython().system(' pip install seaborn')
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler,PolynomialFeatures
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


pip install --upgrade lxml


# In[4]:


import lxml.html as lh


# In[5]:


from lxml import html
import requests
from time import sleep
import json
import argparse
from random import randint


# In[6]:


url='https://www.worldometers.info/bicycles/'


# In[7]:


url


# In[8]:


import urllib.request


# In[9]:


from urllib.request import Request, urlopen

my_request = Request('https://www.worldometers.info/bicycles/', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(my_request).read(10)


# In[10]:


print(my_request)


# In[11]:


pip install matplotlib==3.0.3


# In[12]:


import matplotlib
print(matplotlib.__version__)
'3.0.3'


# In[13]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[14]:


from matplotlib import pyplot as plt


# In[15]:


import matplotlib.dates as mdates


# In[16]:


Data=pd.read_csv("Worldometer Bicycles 3.15.pm.24.07.2021.csv",sep=",")


# In[17]:


Data


# In[18]:


#first ten rows
Data.head(10)


# In[19]:


#last ten rows
Data.tail(10)


# In[20]:


Data.describe()


# In[21]:


Data.shape


# In[22]:


Data.columns.values


# # A Colum chart

# In[42]:


Country=('China', 'USA', 'Japan', 'Germany', 'India')


# In[45]:


Quantity=('450,100,720,620,300')


# In[38]:


bar_coords=range(len(Country))


# In[40]:


num_sold=range(len(Quantity))


# In[46]:


plt.bar(bar_coords,num_sold)


# # A Bar Chart 

# In[44]:


# first five rows
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
Country = ['China', 'USA', 'Japan', 'Germany', 'India']
Quantity = [450,100,720,620,300]
ax.bar(Country,Quantity)
plt.show()


# In[36]:


# last five rows
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
Country = ['Switzerland', 'Hungary', 'Australia', 'Finland', 'Norway']
Quantity = [3.8,3.5,3.3,3.2,3]
ax.bar(Country,Quantity)
plt.show()


# In[ ]:


python 3.7 was used for implementation to create A Column chart and Bar chat for the countries.

