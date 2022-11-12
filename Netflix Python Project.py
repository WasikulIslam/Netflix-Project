#!/usr/bin/env python
# coding: utf-8

# # Importing Packages

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math


# # Read CSV

# In[2]:


netflix = pd.read_csv('/Users/wasikulislam/Desktop/My Python Project/netflix_data.csv')
netflix[0:5]


# # Filtering for movies only

# In[3]:


netflix_movies_only = netflix[netflix['type'] == 'Movie']
print(netflix_movies_only)


# # Columns of interest

# In[4]:


netflix_movies_col = netflix_movies_only[['title', 'genre', 'release_year', 'duration']]
netflix_movies_col[0:5]


# # Scatter plot

# In[5]:


fig = plt.figure(figsize=(12,8))

# Scatter plot of duration versus year
plt.scatter(netflix_movies_col["release_year"], netflix_movies_col["duration"])

# Title
plt.title("Netflix Movie Duration Throughout the Years")

# Show
plt.show()


# # Movies less than 60 minutes

# In[6]:


short_movies = netflix_movies_col[netflix_movies_col['duration'] < 60]
short_movies[0:20]


# # Organizing the films with color

# In[7]:


colors = []

# Iterate over rows
for lab, row in short_movies.iterrows():
    if row['genre'] == "Documentaries" : 
        colors.append("red")
    elif row['genre'] == "Stand-Up" :
        colors.append("green")
    elif row['genre'] == "Children" :
        colors.append("blue")
    elif row['genre'] == "Dramas" :
        colors.append("brown")
    elif row['genre'] == "Comedies" :
        colors.append("yellow")
    else:
        colors.append("black")
colors[0:10]


# # Scatter plot with color

# In[8]:


plt.style.use('fivethirtyeight')
fig = plt.figure(figsize=(12,8))

# Duration versus genre
plt.scatter(short_movies["genre"], short_movies["duration"], c=colors)

# Title
plt.title("Genre Duration")
plt.xlabel("Genre")
plt.ylabel("Duration (min)")
plt.xticks(rotation=90)
# Show
plt.show()


# # Make bargraph

# In[9]:


# Duration versus genre
plt.bar(short_movies["genre"], short_movies["duration"])

# Title
plt.title("Genre Duration")
plt.xlabel("Genre")
plt.ylabel("Duration (min)")
plt.xticks(rotation=90)
# Show
plt.show()


# In[ ]:




