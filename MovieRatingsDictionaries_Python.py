# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 11:16:02 2017

@author: manoj
"""
import math
import random
#IMDB Movie ratings for Scorsese and Tarantino in dictionary form

Ratings1 = dict(Movie1 = 6.8,Movie2 = 6.1,Movie3 = 7.4,Movie4 = 7.4,Movie5 = 6.7)#ScorseseIMDBMovieRatings
Ratings2 = dict(Movie1 = 5.8,Movie2 = 8.4,Movie3 = 8.9,Movie4 = 7.5,Movie5 = 8.1)#TarantinoIMDBMovieRatings

def distanceD(ratings1,ratings2,r):
     
     if (r <= 0):
        print(), print('Minkowski debug:r < 0; returning -2')
        return -2
        
     measure = 0
     for i in sorted(list(set(ratings1.keys()&ratings2.keys()))):
#    if i in UserARatingsD.keys()&UserBRatingsD.keys():
#        print (i,ratings1[i],ratings2[i])
#        print()
        measure += math.fabs(pow(ratings1[i]-ratings2[i],r))
     return pow(measure,1/r)
     
r = random.randrange(1, 4, 1)
print('Power Rating:',r,end = '\n\n')
if r == 1:
    mdD= distanceD(UserARatingsD,UserBRatingsD,r)
    print('Manhattan Distance between Ratings Dictionaries',round(mdD,3))
elif r == 2:
    mdD= distanceD(UserARatingsD,UserBRatingsD,r)
    print('Euclidian Distance between Ratings Dictionaries',round(mdD,3))
else:
    mdD= distanceD(UserARatingsD,UserBRatingsD,r)
    print('Minkowski Distance between Ratings Dictionaries',round(mdD,3))

