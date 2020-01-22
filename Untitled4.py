
# coding: utf-8

# # Dictionaries in python

# In[1]:


#{key:value}pairs


# In[2]:


my_dict = {'Sam':25,'Bob':26,'John':29}


# In[3]:


my_dict


# In[4]:


#dict have to be enclosed in curly braces and key in '' and value after :


# In[6]:


my_dict = {'Sam':{'Age':25,'Weight':'55 kg'},
          'Bob':{'Age':26,'Weight':'68 kg'},
          'John':{'Age':29,'Weight':'82 kg'}}


# In[7]:


my_dict


# In[8]:


#keys in a dictionary should be unique


# In[9]:


#if not it will get lost


# In[10]:


my_dict = {'a':1,'b':2,'c':3,'a':5}


# In[11]:


my_dict


# In[15]:


my_dict = {'a':1,'b':2,'c':3,'A':5}#case sensitive


# In[16]:


my_dict


# In[19]:


my_dict = {"a":1, 12:2, True: 3, 5.0:[1,23]} #keys can have different data types


# In[20]:


my_dict


# In[21]:


my_dict = {}


# In[22]:


my_dict


# In[24]:


my_dict = dict()
my_dict


# In[25]:


#create dict using nested lists


# In[26]:


my_dict = dict([[1,'a'],[2,'b'],[3,'b']])


# In[27]:


my_dict


# In[28]:


my_dict = {}


# In[29]:


my_dict


# In[30]:


my_dict[0] = 'a'


# In[32]:


my_dict #adding value in dict


# In[34]:


del my_dict[0]
my_dict


# In[35]:


#loop through all the keys in a dict


# In[36]:


my_dict = {1:'a',2:'b',3:'c'}
my_dict


# In[37]:


for key in my_dict:
    print(key)


# In[38]:


for key in my_dict:
    print(my_dict[key])


# In[39]:


my_dict = {1:'a',2:'b',3:'c'}
my_dict


# In[40]:


for key in my_dict.keys():
    print(key)


# In[44]:


for value in my_dict.values():
    print(value)


# In[45]:


for key,value in my_dict.items():
    print('key :', str(key),'value :', str(value))


# In[46]:


my_dict = {1:'a',2:'b',3:'c'}
my_dict


# In[47]:


if 2 in my_dict:
    print('present')


# In[48]:


my_dict = {1:'a',2:'b',3:'c'}
my_dict


# In[49]:


if 5 in my_dict:
    print('present')
else:
    print('absent')


# In[50]:


#Deep copy 


# In[52]:


my_dict = {1:['a','b'],2:['c','d']}
my_dict


# In[54]:


import copy


# In[55]:


my_dict_copy = copy.deepcopy(my_dict)
my_dict_copy


# In[56]:


my_dict[2][0] = 'g'
my_dict


# In[57]:


my_dict_copy #proper way of copying not shallow copy


# In[58]:


# Built-in functions in Dict:


# In[59]:


my_dict = {1:'a',2:'b'}
my_dict


# In[60]:


my_dict.clear()


# In[61]:


my_dict


# In[62]:


#get funtion/method


# In[63]:


my_dict = {1:'a',2:'b',3:'c'}
my_dict


# In[64]:


value_of_2 = my_dict.get(2)
value_of_2


# In[65]:


my_dict = {1:'a',2:'b',3:'c'}
my_dict


# In[67]:


my_dict.popitem() #return type is tuple


# In[68]:


my_dict


# In[69]:


my_dict = {1:'a',2:'b',3:'c'}
my_dict


# In[71]:


my_dict.pop(2)


# In[72]:


my_dict


# In[73]:


#update function


# In[74]:


my_dict = {'a':1,'b':2,}
my_dict


# In[75]:


my_dict.update({'a':50,'c':7})


# In[76]:


my_dict


# In[77]:


len(my_dict)

