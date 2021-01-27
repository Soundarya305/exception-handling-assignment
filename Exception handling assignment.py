#!/usr/bin/env python
# coding: utf-8

# In[2]:


### Write a function to compute 5/0 and use try/except to catch the exceptions
try:
    5/0
except Exception as e :
    print("this block is having some kind of issue : " , e)


# In[9]:


####Implement a Python program to generate all sentences where subject is in ["Americans", "Indians"] and verb is in ["Play", "watch"] and the object is in["Baseball","cricket"].
subject = ['Americans' , 'Indians']
verb = ['play','watch']
object = ['basketball','cricket']

All_sentences = [(sub + " " + ver + " " + obj) for sub in subject for ver in verb for obj in object ]
for sentence in All_sentences:
    print(sentence)


# In[ ]:




