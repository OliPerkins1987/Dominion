# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 16:44:04 2021

@author: Oli
"""


import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

os.chdir(r'C:\Users\Oli\Documents\PhD\Training\Dominion')

from Hand import Hand, choices

results = {}

act_dict= {'Copper':0, 'Silver':0, 'Gold':0, 'Estate':0, 'Smithy':0, 'Village':2}
coin_gain_dict= {'Copper':1, 'Silver':2, 'Gold':3, 'Estate':0, 'Smithy':0, 'Village':0}
card_gain_dict= {'Copper':0, 'Silver':0, 'Gold':0, 'Estate':0, 'Smithy':3, 'Village':1}

Starting_hand = ['Estate', 'Copper', 'Copper', 'Estate', 'Copper',
                    'Copper', 'Copper', 'Copper', 'Estate', 'Copper']

additions = [['Silver'], ['Village'], ['Smithy'], 
             ['Silver', 'Village'], ['Silver', 'Smithy'], ['Smithy', 'Village'], 
             ['Silver', 'Village', 'Smithy'], ['Silver', 'Smithy', 'Smithy'], 
             ['Silver', 'Village', 'Village'],
             ['Silver', 'Silver', 'Village'], ['Silver', 'Silver', 'Silver'], 
             ['Silver', 'Silver', 'Silver', 'Silver'], ['Silver', 'Silver', 'Silver', 'Smithy'],
             ['Silver', 'Silver', 'Smithy', 'Smithy'], ['Silver', 'Silver', 'Smithy', 'Village']]

additions = [['Village'],
             ['Silver'], 
             ['Silver', 'Silver'], 
             ['Silver', 'Silver', 'Silver'], 
             ['Silver', 'Silver', 'Silver', 'Silver'], 
             ['Silver', 'Silver', 'Silver', 'Silver', 'Silver'], 
             ['Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver'], 
             ['Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver'], 
             ['Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver'], 
             ['Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver'],
             ['Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver'],
             ['Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver'],
             ['Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver']]


additions = [['Village'],
             ['Smithy'],
             ['Smithy', 'Silver'], 
             ['Smithy', 'Silver', 'Silver'], 
             ['Smithy', 'Silver', 'Silver', 'Silver'], 
             ['Smithy', 'Silver', 'Silver', 'Silver', 'Silver'], 
             ['Smithy', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver'], 
             ['Smithy', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver'], 
             ['Smithy', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver'], 
             ['Smithy', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver'], 
             ['Smithy', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver'],
             ['Smithy', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver'],
             ['Smithy', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver'],
             ['Smithy', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver']]

additions = [['Village'],
             ['Smithy'],
             ['Smithy', 'Smithy'], 
             ['Smithy', 'Smithy', 'Silver', 'Silver'], 
             ['Smithy', 'Smithy', 'Silver', 'Silver', 'Silver'], 
             ['Smithy', 'Smithy', 'Silver', 'Silver', 'Silver', 'Silver'], 
             ['Smithy', 'Smithy', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver'], 
             ['Smithy', 'Smithy', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver'], 
             ['Smithy', 'Smithy', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver'], 
             ['Smithy', 'Smithy', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver'], 
             ['Smithy', 'Smithy', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver'],
             ['Smithy', 'Smithy', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver'],
             ['Smithy', 'Smithy', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver'],
             ['Smithy', 'Smithy', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver']]


additions = [['Village'],
             ['Smithy'],
             ['Smithy', 'Smithy'], 
             ['Smithy', 'Smithy', 'Smithy'], 
             ['Smithy', 'Smithy', 'Smithy', 'Silver'], 
             ['Smithy', 'Smithy', 'Smithy', 'Silver', 'Silver', 'Silver'], 
             ['Smithy', 'Smithy', 'Smithy', 'Silver', 'Silver', 'Silver', 'Silver'], 
             ['Smithy', 'Smithy', 'Smithy', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver'], 
             ['Smithy', 'Smithy', 'Smithy', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver'], 
             ['Smithy', 'Smithy', 'Smithy', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver'], 
             ['Smithy', 'Smithy', 'Smithy', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver'], 
             ['Smithy', 'Smithy', 'Smithy', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver'],
             ['Smithy', 'Smithy', 'Smithy', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver'],
             ['Smithy', 'Smithy', 'Smithy', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver'],
             ['Smithy', 'Smithy', 'Smithy', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver']]

additions = [['Village'],
             ['Village'],
             ['Village','Smithy'],
             ['Village','Smithy', 'Smithy'], 
             ['Village', 'Smithy', 'Smithy', 'Silver'], 
             ['Village', 'Smithy', 'Smithy', 'Silver', 'Silver', 'Silver'], 
             ['Village', 'Smithy', 'Smithy', 'Silver', 'Silver', 'Silver', 'Silver'], 
             ['Village', 'Smithy', 'Smithy', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver'], 
             ['Village', 'Smithy', 'Smithy', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver'], 
             ['Village', 'Smithy', 'Smithy', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver'], 
             ['Village', 'Smithy', 'Smithy', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver'], 
             ['Village', 'Smithy', 'Smithy', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver'],
             ['Village', 'Smithy', 'Smithy', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver'],
             ['Village', 'Smithy', 'Smithy', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver'],
             ['Village', 'Smithy', 'Smithy', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver']]

additions = [['Village'],
             ['Village'],
             ['Village', 'Village'],
             ['Village','Village','Smithy'],
             ['Village','Village','Smithy', 'Smithy'], 
             ['Village','Village', 'Smithy', 'Smithy', 'Silver'], 
             ['Village','Village', 'Smithy', 'Smithy', 'Silver', 'Silver', 'Silver'], 
             ['Village','Village', 'Smithy', 'Smithy', 'Silver', 'Silver', 'Silver', 'Silver'], 
             ['Village','Village', 'Smithy', 'Smithy', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver'], 
             ['Village','Village', 'Smithy', 'Smithy', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver'], 
             ['Village','Village', 'Smithy', 'Smithy', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver'], 
             ['Village','Village', 'Smithy', 'Smithy', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver'], 
             ['Village','Village', 'Smithy', 'Smithy', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver'],
             ['Village','Village', 'Smithy', 'Smithy', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver'],
             ['Village','Village', 'Smithy', 'Smithy', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver'],
             ['Village','Village', 'Smithy', 'Smithy', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver', 'Silver']]






### Run experiment

for j in range(len(additions)):

    run = Hand(Starting_hand + additions[j], [])    

    for i in range(25000):
        run.initial_draw()
        Run = choices(run, 0)
        Run.play()
        Run.end_choices()
        run.clean_up()
    
    
    results[j] = np.mean(run.ncoin)
    
results = pd.DataFrame(results.items())

plt.plot(results[1])

#combined = pd.DataFrame({'Smithy':results[1], 'Silver':cache[1]})
combined['Village Double Smithy'] = results[1]
combo = combined.iloc[:, [1, 0, 2, 3, 4, 5]]

#combo.to_csv('Modelruns.csv')
