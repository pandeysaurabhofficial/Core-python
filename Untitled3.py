
# coding: utf-8

# #     lists in python 

# In[1]:


list_of_strings = ["cat","dog","cow"]
list_of_strings


# In[2]:


list_of_numbers = [1,2,3,4]
list_of_numbers


# In[3]:


lst_of_lists = [[1,2],["hi","hey"]]
lst_of_lists


# In[4]:


lst_mixed_items = ["hello",23,4.0,["hi",12]]
lst_mixed_items


# In[5]:


emptylist = []


# In[6]:


emptylist


# In[7]:


emptylist = list()
emptylist


# # list comprehension

# In[8]:


listofnum = [i for i in range (0,10)]


# In[9]:


listofnum


# In[12]:


listofnum = list(range(10))


# In[13]:


listofnum


# In[14]:


lsteven = list(range(10))


# In[15]:


lsteven


# In[22]:


lsteven = [i for i in range (1,10,2)]


# In[23]:


lsteven


# In[24]:


str1 = "hi,hey,ABC,DEF"


# In[26]:


strlst = str1.split(",")


# In[27]:


strlst


# In[28]:


str2 = "hello"
lst2 = list(str2)


# In[29]:


lst2


# In[30]:


int1 = 123456
lst2 = list(int1)


# In[31]:


#it work on string not on integer so, we have to convert int into string


# In[37]:


lst1 = [ int(i) for i in str(int1)]
lst1


# In[38]:


my_dict = {'a':1,'b':2,'c':3}


# In[39]:


key_list = list(my_dict.keys())


# In[40]:


key_list


# In[41]:


value_list = list(my_dict.values())
value_list


# Built-in functions of lists:

# In[42]:


lst1 = ['cat','dog','cow']
lst1


# In[43]:


lst1.append('goat')
lst1


# In[44]:


lst1.append('1')
lst1


# In[46]:


lst1.append(['parrot','penguin'])
lst1


# In[47]:


lst1.extend(['parrot','penguin'])
lst1


# In[48]:


lst1.insert(2,'owl')
lst1


# In[49]:


lst1 = ['penguin','parrot','sparrow','goose']


# In[50]:


lst1


# In[51]:


lst1.index('sparrow')


# In[52]:


lst1.insert(3,'owl')


# In[53]:


lst1


# In[55]:


lst1.insert(lst1.index('owl')+1,'duck')
lst1


# In[56]:


lst1.remove('sparrow')
lst1


# In[58]:


popped = lst1.pop()
popped


# In[59]:


lst1


# In[60]:


popped = lst1.pop(2)
popped


# In[61]:


lst1


# # Sorting

# In[64]:


lst1 = [2,5,4,7]
lst1


# In[66]:


lst1.sort()


# In[67]:


lst1


# In[68]:


lst1.sort(reverse = True)
lst1


# In[69]:


lst1.reverse()


# In[70]:


lst1


# In[71]:


len(lst1)


# In[72]:


max(lst1)


# In[73]:


min(lst1)


# In[74]:


lst1 = ['A','B','C','A','A']
lst1


# In[75]:


lst1.count('A')


# In[77]:


lst1.clear()


# In[78]:


lst1


# In[79]:


lst1 = ['cat','dog','squirrel']
lst1


# In[80]:


if 'dog' in lst1:
    print('lst1 has dog')


# In[81]:


lst2 = [2,3,4,1,5,6,7,8,3,5]
lst2


# In[84]:


lst2[0]


# In[85]:


lst2[-1]


# In[86]:


lst2[-2]


# In[87]:


#slicing of list


# In[88]:


lst2[0:3]


# In[91]:


lst2[0:5:1]


# In[93]:


lst2[::-1]#reverse way


# In[97]:


for i in reversed(lst2):
    print(i)


# In[98]:


lst2[:5]


# In[99]:


lst2[5:]


# In[100]:


a = [1,2,3]
a


# In[101]:


b = a


# In[103]:


b # copying list


# In[104]:


a[0] = 20
a


# In[105]:


b


# In[106]:


a = [1,2,3]
a


# In[107]:


b = list(a)


# In[108]:


b


# In[109]:


a[0] = 6
a


# In[111]:


b #value doesnot depend on a now


# In[136]:


a = [[1,2,3],[4,5]]
a


# In[137]:


b = list(a)
b


# In[138]:


a[0][0] = 20
a


# In[139]:


b

#to solve this problem we use moduleto use deep copy
# In[144]:


a = [[1,2,3],[4,5]]
a


# In[147]:


import copy


# In[148]:


b = copy.deepcopy(a)
b


# In[149]:


a[0][0] = 20
a


# In[150]:


b


# In[151]:


# how to use loops on our list


# In[153]:


lst1 = ['cat','dog','duck']
lst1


# In[155]:


for i in lst1:
    print(i)


# In[156]:


for i in range(0,len(lst1)):
    print("index=",i,"value=",lst1[i])


# In[157]:


#to join in single string


# In[158]:


" ".join(lst1)


# In[159]:


"".join(lst1)


# In[160]:


lstoflist = [[1,2,3],[4,5]]
lstoflist


# In[162]:


import itertools #to convert into flat list


# In[163]:


flatlist = list(itertools.chain(*lstoflist))


# In[164]:


flatlist


# In[165]:


#to check if it have duplicate elements


# In[167]:


lst = [1,2,3,4,5,6,1,2,3,4,2,1,2]
lst


# In[168]:


lst2 =[i for i in lst if lst.count(i)>1]


# In[170]:


lst2


# In[173]:


unique = set(lst)


# In[174]:


unique


# In[175]:


#how to shift or rotate a list


# In[176]:


lst2 = [1,2,3]
lst2


# In[177]:


from collections import deque


# In[180]:


lst2 = deque(lst2)


# In[181]:


lst2.rotate(1)


# In[182]:


lst2


# In[183]:


lst2.rotate(-2)


# In[184]:


lst2

