
import requests
import pandas as pd
import re
import numpy as np
import pickle
from bs4 import BeautifulSoup
import time
from credentials import apiKey

matrix_ratings_movies = pickle.load(open("matrix_ratings_movies.pkl", "rb"))



def nmf_recommender(query, matrix_ratings_movies, m=5):
    '''recommender based on negative matrix factorization
    '''
    
    usersid = matrix_ratings_movies.index.to_list() 
    movies = matrix_ratings_movies.columns.to_list()
    
    # load model
    file = open('nmfmodel.pkl',mode="rb")
    binary = file.read()
    file.close()
    nmf_model = pickle.loads(binary)
    
    # create Q matrix (movie-genre)
    Q_matrix = nmf_model.components_
    
    # create P matrix 
    new_user_ratings = pd.DataFrame(data=query,
                                columns=movies,
                                 index = ['1000'])
    
    
    query_imputed = new_user_ratings.fillna(0)
    P_newuser_matrix = nmf_model.transform(query_imputed)
    
    # compute recunstructed ratings for new user
    Reconstructed_newuser_ratings = pd.DataFrame(data=np.dot(P_newuser_matrix,Q_matrix),
                                              columns=movies,
                                              index=['1000'])
    # Filter out the movie that the user has rated
    Reconstructed_newuser_ratings.drop(query.keys(),axis=1,inplace=True)
    
    # get the m top movies
    top_m = Reconstructed_newuser_ratings.sort_values(['1000'],
                                                axis=1, ascending=False).T.index.to_list()[:m]
    
    return top_m

def get_poster(id):
    '''
    take movie id and return movie poster using OMDb API 
    '''
    if len(id) == 6 or len(id) == 5:
        link = 'http://www.omdbapi.com/?i=tt00'+id+'&apikey='+apiKey
    if len(id) == 7 :
        link = 'http://www.omdbapi.com/?i=tt0'+id+'&apikey='+apiKey
    movieInfo = requests.get(link).json()
    poster = movieInfo['Poster']
    return poster

