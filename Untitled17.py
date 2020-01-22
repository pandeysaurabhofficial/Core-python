
# coding: utf-8

# # Pandas in Python

# In[19]:


#for data analysis library
#it has two main data structures - series(one dimensional) - Dataframe (two dimensional)


# In[20]:


import pandas as pd


# In[21]:


#series in pandas


# In[22]:


s1 = pd.Series([1,2,3,4,5])


# In[23]:


s1


# In[24]:


s1 = pd.Series({'A':1,'B':2,'C':3})
s1


# In[25]:


#Dataframes - it is two dimensional data type


# In[41]:


import pandas as pd


# In[42]:


my_dict = {
    'Name':['A','B','C'],
    'Height':[20,30,40],
    'Weight':[50,60,70]
}


# In[43]:


df1 = pd.DataFrame(my_dict)


# In[44]:


df1


# In[47]:


df1.columns


# In[48]:


df1.Height.mean()


# In[49]:


df1['Height'].mean()


# In[50]:


df1.Height.max()


# In[51]:


df1.Height.min()


# In[52]:


#you can import data of excel and do analysis by pandas as well


# In[69]:


df1.loc[df1['Height'].idxmax()]


# In[70]:


df2 = pd.DataFrame(df1,columns=['sex','occupation'])


# In[71]:


df2.head()


# In[72]:


df2 = df2.drop('sex',1)


# In[73]:


df2


# In[74]:


df2 = df2.drop(2,0)
df2


# # Matplotlib for Visualization

# In[103]:


import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')


# In[104]:


#scatter chart #it is use to displaying charts in jupyter notebook (not necessary for other ide)


# In[105]:


x = [1,2,3,4,5,6]
y = [10,20,30,20,50,60]


# In[106]:


plt.scatter(x,y)


# In[107]:


#to display the poin values


# In[108]:


fig, ax = plt.subplots()

for i,j in zip(x,y):
    ax.annotate('(%s,'%i,xy=(i,j))
    ax.annotate('%s),'%j,xy=(i,j),xytext=(25,0),textcoords='offset points')
    
plt.scatter(x,y)


# In[109]:


fig, ax = plt.subplots()

for i,j in zip(x,y):
    ax.annotate('(%s,'%i,xy=(i,j))
    ax.annotate('%s),'%j,xy=(i,j),xytext=(25,0),textcoords='offset points')
    
plt.scatter(x,y)
plt.plot(x,y, linewidth = 1)

 for blue dots - plt.point(x,y,'bo')
# In[110]:


x = [1,2,3,4,5,6]
y = [10,20,30,20,50,60]


# In[111]:


plt.plot(x,y,'r+',markersize=12)


# In[112]:


x = [1,2,3,4,5,6]
y = [10,20,30,20,50,60]
y2 = [12,32,4,3,54,65]


# In[113]:


plt.plot(x,y,'bo',x,y2, 'r+')


# In[114]:


#drwaing sine wave using matplotlib


# In[122]:


import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')


# In[125]:



t = np.arrange(0.0,2.0,0.01)
s = np.sin(2*np.pi*t)

plt.plot(t,s)


# In[124]:


import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')


# In[126]:



t = np.arrange(0.0,2.0,0.01)
s = np.sin(2*np.pi*t)

plt.plot(t,s)
plt.xlabel('time(s)')
plt.ylabe;('Voltage(MV)')


# In[128]:


#how to draw subplots


# In[133]:



t = np.arange(0.0,2.0,0.01)
s = np.sin(2*np.pi*t)

plt.plot(t,s)
plt.xlabel('time(s)')
plt.ylabel;('Voltage(MV)')


# In[136]:



x = np.arange(0.0,5.0,0.1)
y1 = np.sin(2*np.pi*x) * np.exp(-x)
y2 = np.sin(2*np.pi*x)

plt.subplot(2,1,1)
plt.plot(x,y1)

plt.subplot(2,1,2)
plt.plot(x,y2)


# In[139]:



x = np.arange(0.0,5.0,0.1)
y1 = np.sin(2*np.pi*x) * np.exp(-x)
y2 = np.sin(2*np.pi*x)

plt.subplot(2,2,1)
plt.plot(x,y1)

plt.subplot(2,2,2)
plt.plot(x,y2)

plt.subplot(2,2,3)
plt.plot(x,y1)

plt.subplot(2,2,4)
plt.plot(x,y2)


# In[140]:


#Bar Chart


# In[148]:


country = ['a','b','c','d','e']
population = [10,20,30,40,50]


# In[149]:


index = np.arange(len(country))
index


# In[150]:


index = np.arange(len(country))

plt.bar(index,population,align='center',alpha=0.5)
plt.xticks(index,country)
plt.show()


# In[151]:


#horizontal bar charts


# In[152]:


index = np.arange(len(country))

plt.barh(index,population,align='center',alpha=0.5)
plt.yticks(index,country)
plt.show()


# In[153]:


#stack bar chart


# In[154]:


country = ['a','b','c','d','e']
populationMale = [10,20,30,40,50]
populationFemale = [4,11,12,19,43]


# In[161]:


index = np.arange(len(country))
bar_width = 0.35

plt.bar(index,populationMale, bar_width,
       alpha=0.8,
        color='b',
       label = 'Male')

plt.bar(index+bar_width,populationFemale, bar_width,
       alpha=0.8,
        color='g',
       label = 'Female')

plt.xticks(index+bar_width,country)
plt.legend()


# In[162]:


#Pie Chart


# In[163]:


country = ['a','b','c','d','e']
population = [10,20,30,40,50]


# In[164]:


plt.pie(population,labels=country, autopct='%1.1f%%',shadow=True,
       startangle=90)
plt.axis('equal')
plt.show()


# In[165]:


#Donut Chart


# In[166]:


country = ['a','b','c','d','e']
population = [10,20,30,40,50]


# In[168]:


plt.pie(population,labels=country, autopct='%1.1f%%',shadow=True,
       startangle=90)

centre_circle = plt.Circle((0,0),0.7,color='black',fc='white',linewidth=0)

fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.axis('equal')
plt.show()

