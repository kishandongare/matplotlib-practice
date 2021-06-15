#!/usr/bin/env python
# coding: utf-8

# # practice matplotlib

# In[ ]:


NAME = KISHAN DONGARE
EMAIL = kishan.soft25@gmail.com

   # why Data Visualization?

   # brain can process information easily when it is in pictorial or graphical form

   # matplotlib is apython packeage used for 2D graphics


# # Linear Graph

# In[4]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[5]:


apple_price = [45,17,56,12,65,37,98,]
microsoft_price = [65,89,12,56,78,32,50]
year = [2014,2015,2016,2017,2018,2019,2020]


# In[54]:


plt.plot(year,apple_price)  #x,y axis
plt.show()


# In[55]:


plt.plot(year,apple_price)  #x,y axis
plt.xlabel('year')
plt.ylabel('Stock price')
plt.show()


# In[56]:


plt.plot(year,apple_price) #x,y axis
plt.plot(year,microsoft_price)

plt.xlabel('year')
plt.ylabel('Stock price')
plt.show()


# In[57]:


plt.plot(year,apple_price,'k') #x,y axis
plt.plot(year,microsoft_price,'g')
plt.title('info')
plt.xlabel('year')
plt.ylabel('Stock price')
plt.show()


# In[58]:


plt.plot(year,apple_price,  #x,y axis
         year,microsoft_price)
plt.title('info')
plt.xlabel('year')
plt.ylabel('Stock price')
plt.show()


# In[76]:


plt.plot(year,apple_price,'k',
         year,microsoft_price,'g')
plt.title('info')
plt.xlabel('year')
plt.ylabel('Stock price')
plt.axis([2013,2021,10,200])
plt.show()


# In[71]:


fig = plt.figure(1,figsize = (20,5)) #no. of figure 1,width 6.5 height 5
apple = fig.add_subplot(121) #row #column #positon
microsoft = fig.add_subplot(122)
apple.plot(year,apple_price,"k")
microsoft.plot(year,microsoft_price,'g')
plt.show()


# # Scatter plot

# In[79]:


plt.scatter(year,apple_price,color='k')
plt.scatter(year,microsoft_price,color='g')
plt.title('info')
plt.xlabel('year')
plt.ylabel('Stock price')
plt.show()


# # Bar Graph

# In[16]:


import numpy as np
np.arange(7)


# In[27]:


import numpy as np
group = 7
index = np.arange(group)
bar_width = 0.30
plt.bar(index + bar_width,apple_price,bar_width,label ="Apple") 
plt.bar(index,microsoft_price,bar_width,label = "Microsoft" )
plt.xticks(index + bar_width, ('2014','2015','2016','2017','2018','2019','2020'))  #Get or set the x-limits of the current tick locations and labels
plt.legend() # A legend is an area describing the elements of the graph.
plt.title('info')
plt.xlabel('year')
plt.ylabel('Stock price')
plt.tight_layout()   #Adjust the padding between and around subplots.
plt.show()


# # Histogram
# A histogram is basically used to represent data provided in a form of some groups.It is accurate method for the graphical representation of numerical data distribution.It is a type of bar plot where X-axis represents the bin ranges while Y-axis gives information about frequency.
# 
# To create a histogram the first step is to create bin of the ranges, then distribute the whole range of the values into a series of intervals, and the count the values which fall into each of the intervals.Bins are clearly identified as consecutive, non-overlapping intervals of variables

# In[35]:


population_ages = [22,29,35,36,40,45,47,23,25,49,48,53,33,55,59,29,21,59,]
bins = [20,30,40,50,60]
plt.hist(population_ages,bins,histtype = 'bar',rwidth = 0.7)
plt.xlabel('group')
plt.ylabel('Ages')
plt.title('Histogram')
plt.legend()
plt.show()


# # Stack plot
# A stack plot is a plot that shows the whole data set with easy visualization of how each part makes up the whole. Each constituent of the stack plot is stacked on top of each other. It shows the part makeup of the unit, as well as the whole unit

# In[100]:


days = [1,2,3,4,5,6,7]
sleeping  =[9,7,8,9,8,8,6]
eating = [5,3,4,3,6,4,5]
working =[2,6,4,2,3,2,3]
playing = [4,6,7,6,7,6,7]
plt.plot([],[],color ='m',label = 'sleeping',linewidth ='7')
plt.plot([],[],color ='c',label = 'eating',linewidth ='7')
plt.plot([],[],color ='r',label = 'working',linewidth ='7')
plt.plot([],[],color ='k',label = 'playing',linewidth ='7')

plt.stackplot(days,sleeping,eating,working,playing,colors = ['m','c','r','k'])

plt.title('Stack Plot')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()


# # Pie Chart
# A Pie Chart can only display one series of data. Pie charts show the size of items (called wedge) in one data series, proportional to the sum of the items. The data points in a pie chart are shown as a percentage of the whole pie.
# 
# 
# explode() = pie() to create a plot. You can define it's sizes, which parts should explode (distance from center), which labels it should have and which colors it should have
# 
# autopct() =  enables you to display the percent value 
# 
# 
# 
# This formats the percentage to the tenth place autopct='%1.1f%%'
# 
# If you want to format the percentage to the hundredths place, you would use the statement, autopct='%1.2f%%'
# 
# If you want to format the percentage to the thousandths place, you would use the statement, autopct='%1.3f%%'

# In[11]:


fig = plt.figure(figsize =(10, 7))

y = [49, 14, 21, 35]

myfruit = ["sleeping", "working", "eating", "playing"]

plt.pie(y,labels = myfruit,startangle =90,shadow =True,explode=(0,0.1,0,0),autopct = '%1.1f%%' )

plt.title("Pie Chart")
plt.show() 


# In[ ]:




