#!/usr/bin/env python
# coding: utf-8

# In[6]:


dict ={}
x=int(input("Enter Number of Keys:"))
for i in range(x):
    k=input("Enter the(i+1)key:")
    v=input("enter the values for keys(i+1):")
    dict[k]=v
print(dict)
for i in dict:
    print(i, '->',  dict[i])
# searching item in dictionary
name = input("Enter name of student :")
if name in dict.keys():
    print(dict[name])
else :
    print("No student found")


# In[ ]:





# In[ ]:




