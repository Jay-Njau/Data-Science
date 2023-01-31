#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
arr=[6,7,8,9]
print(type(arr))


# In[2]:


a=np.array(arr)
print(type(a))


# In[3]:


a=np.array(arr)
print(type(a))
print(a.shape)
print(a.dtype)
print(a.ndim)


# In[5]:


b=np.array([[1,2,3],[4,5,6]])
print(b)
print(b.ndim)
b.shape


# In[7]:


np.random.random((4,4))


# In[14]:


np.zeros(2)


# In[9]:


np.ones((2,2))


# In[12]:


np.identity(3)


# In[19]:


c=np.array([[9.0,8.0,7.0],[1.0,2.0,3.0]])
d=np.array([[4.0,5.0,6.0],[9.0,8.0,7.0]])
c+d
c*d


# In[21]:


import pandas as pd
days=pd.Series(['Monday','Tuesday','Wednesday'])
print(days)

