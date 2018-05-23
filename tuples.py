
# coding: utf-8

# In[1]:


a= ()
b = (1, 'cat','dog',2)
c= b[0]
print(c)


# In[2]:


b[0] = 'bad'
print(b[0])


# In[12]:


a = {1:'sachin',2:'sankeerth',3:'apple'}


# In[13]:


a.keys()


# In[14]:


a.values()


# In[15]:


a.items()


# In[16]:


len(a)


# In[17]:


type(a)


# In[19]:


c={4:'kohli'}
print(b)


# In[25]:


a.update(c)
print(a)


# In[26]:


c.clear()


# In[28]:


print(c)


# In[29]:


a= {}
type(a)


# In[30]:


b= set()
type(b)


# In[31]:


c = set((1,2,3,4))
print(c)


# In[32]:


d = {7,8,9,10,11,12}
type(d)


# In[33]:


c.union(d)


# In[34]:


e = {8,9,10}
d.intersection(e)


# In[36]:


#e.add(11)
#x= e.


# In[37]:


x=e.copy()


# In[38]:


print(x)


# In[39]:


x.clear()
print(x)


# In[40]:


f = {11,12,13,14,15}
g = {12,13,14,15}


# In[41]:


f.issuperset(g)


# In[42]:


f.issubset(g)


# In[43]:


g.remove(16)


# In[44]:


g.discard(16)

