
# coding: utf-8

# # String in python

# In[3]:


str1 = "hello world"
print(str1)


# In[5]:


str1 = 'hello'
print(str1)


# In[6]:


str1 = "hello ' world"
print(str1)


# In[7]:


str1 = 'Hello " world'
print(str1)


# In[9]:


str1 = 'hello "  ' world' (use backslash)
print(str1)


# In[10]:


str1 = """ multi line string
line no 2
line no 3
"""


# In[11]:


print(str1)


# In[12]:


str1 = ' Hello '
str2 = 'World'
str3 = str1 + str2
print(str3)


# In[21]:


str3 = "Hello  "" world" #concetation#
print(str3)


# In[15]:


str1 = "apple"
for i in str1:
    print(i)


# In[16]:


i = "XYZ"
print(i)


# In[17]:


for i in "ABC":
    print(i)


# In[20]:


print(i) #don't use same variable name#


# # String Indexing

# #indexing in python start from 0

# In[24]:


str1 = "asdfgh"


# In[25]:


str1[0]


# In[27]:


str1[-1]


# In[28]:


str1[2]


# In[29]:


str1[-2]


# In[30]:


len(str1)


# In[31]:


str1[len(str1)-1]


# In[33]:


str1[len(str1)-2]


# # Slicing

# In[35]:


i = "abcdefgh"


# In[36]:


i[0:2]


# In[39]:


i[0:3] #always get less then 3#


# In[40]:


i[3:-2]


# In[42]:


i[7:4:-1] # -1 determines the direction in this reverse direction #


# # Strings are immutable 

# In[45]:


#which means you can't alter or delete elements inside the string but you can del a entire string


# In[46]:


i[0] = "z"


# In[47]:


del(i[0])


# In[48]:


del(i)


# In[50]:


i


# In[51]:


str1 = "abc"
str1


# In[52]:


i = "abcdefgh"


# In[54]:


result = "b" in i


# In[55]:


result


# # string built-in function (some of the most used)

# In[56]:


i.capitalize()


# In[65]:


i[7].capitalize()


# In[72]:


i = "aabeee dsab"


# In[77]:


i.count("e")


# In[76]:


i.count("abe")


# In[78]:


i.count("i")


# In[79]:


i.count("a",0,4)


# In[80]:


i.endswith("a")


# In[81]:


i.startswith("a")


# In[82]:


i.find("a")


# In[84]:


i.find("d") #return the first index of it


# In[86]:


i.find("z") #which shows the particular doesn't appear in the string


# In[87]:


i = "abc1234"


# In[88]:


i.isalnum()


# In[89]:


i.isalpha()


# In[91]:


i = "abc"


# In[92]:


i.isalpha()


# In[93]:


i.isdecimal()


# In[94]:


i.isupper()


# In[95]:


i.islower()


# In[96]:


i.swapcase() #swappingthecase


# In[97]:


i = " abcd "


# In[98]:


i.lstrip()


# In[99]:


i.rstrip()


# In[101]:


i.strip()


# In[108]:


i.replace("a","z")
#it creates copy but don't replace


# In[104]:


i.strip()


# In[109]:


i.split(",")


# In[110]:


i = "a,b,c,d,e,f"


# In[111]:


i.split(",")

