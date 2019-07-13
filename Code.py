#!/usr/bin/env python
# coding: utf-8
import pandas as pd
import numpy as np
import googlemaps
import gmaps

API_KEY = 'AI...' #API KEY goes here
gm = googlemaps.Client(key=API_KEY)
gmaps.configure(api_key=API_KEY)

# data read

df=pd.read_csv('ds1.csv', usecols=["latitude","longitude","weight"])  
locations = df[['latitude', 'longitude']]          
weights = df['weight']                                  

# heatmap plot

fig = gmaps.figure() 
fig.add_layer(gmaps.heatmap_layer(locations, weights=weights, max_intensity=15000, point_radius=18, dissipating= True))
fig