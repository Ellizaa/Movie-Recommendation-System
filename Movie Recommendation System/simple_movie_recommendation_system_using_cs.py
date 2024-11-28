# -*- coding: utf-8 -*-
"""Simple Movie Recommendation System using CS.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1DFOWyWvq67h63nbXcrEYNl09YUB6qspp
"""

import numpy as np
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Read the dataset
movies_data = pd.read_csv('/content/movies.csv')
#movies_data.head()

# Data cleaning
selected_features = ['title','genres','cast','keywords','director','original_language']
for feature in selected_features:
  movies_data[feature] = movies_data[feature].fillna('')

# Making the model
combined_features = movies_data['title']+' '+movies_data['genres']+' '+movies_data['cast']+' '+movies_data['keywords']+' '+movies_data['director']+' '+movies_data['original_language']
#print(combined_features)

# Vectorization
vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(combined_features)
#print(feature_vectors)

# Calculating the similarity score
similarity = cosine_similarity(feature_vectors)
#print(similarity)

# Receiving the input
movie_name = input(' Enter your favourite movie name : ')

# Finding the matched movie title
list_of_all_titles = movies_data['title'].tolist()
find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)
close_match = find_close_match[0]

# Converting into index
index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]

# Comparing with the index
similarity_score = list(enumerate(similarity[index_of_the_movie]))

# Sorting the matched index
sorted_similar_movies = sorted(similarity_score, key = lambda x:x[1], reverse = True)
sorted_similar_movies.pop(0)
#print(sorted_similar_movies)

# Output movie title based on thr sorted index
print('Movies suggested for you : \n')

i = 1
for movie in sorted_similar_movies:
  index = movie[0]
  title_from_index = movies_data[movies_data.index==index]['title'].values[0]
  if (i<11):
    print(i, '.',title_from_index)
    i+=1