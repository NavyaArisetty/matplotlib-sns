#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df = pd.read_csv(r"C:\Users\17819\OneDrive\Desktop\pandas\COVID-19 Coronavirus.csv")


# In[3]:


df.head()


# In[4]:


df.tail()


# In[5]:


df.describe()


# In[6]:


df.info()


# In[16]:


df[["Population","Total Cases","Total Deaths"]].mean()


# In[17]:


df.isnull()


# In[21]:


df.isnull().sum()


# In[24]:


df.fillna(0, inplace=True)


# In[26]:


df.isnull().sum()


# In[33]:


plt.plot(df["Total Cases"], df["Total Deaths"])
plt.title("Total Cases vs Total Deaths")
plt.xlabel("Total Cases")
plt.ylabel("Total Deaths")
plt.show()


# In[49]:


plt.scatter(df["Total Deaths"],df["Total Cases"])
plt.title("Covid Cases vs Death rate")
plt.xlabel("Total Cases")
plt.ylabel("Total Deaths")
plt.show()


# In[52]:


plt.boxplot(df["Total Deaths"])
plt.title("Covid Cases vs Death rate")
plt.xlabel("Total Cases")
plt.ylabel("Total Deaths")
plt.show()


# In[50]:


plt.hist(df["Total Deaths"], bins=10, color = "pink")
plt.title("Covid Cases vs Death rate")
plt.xlabel("Total Cases")
plt.ylabel("Total Deaths")
plt.show()


# In[54]:


sns.scatterplot(data=df, x="Total Cases", y="Total Deaths")
plt.title("Seaborn Scatter Plot")
plt.show()


# In[60]:


sns.boxplot(data=df, x="Total Cases", y="Total Deaths")
plt.title("Seaborn Box Plot")
plt.show()


# In[61]:


sns.pairplot(df)
plt.show()


# In[62]:


corr = df.corr()
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Heatmap of Correlation Matrix")
plt.show()

