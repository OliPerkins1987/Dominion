# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 10:57:56 2021

@author: Oli
"""

import random
import numpy as np

class Hand:
    
    def __init__(self, cards, discard):
        
        self.actions = 1
        self.buys    = 1
        self.coins   = 0

        self.cards   = cards
        self.discard = discard
        self.ncoin   = []
        
        
    def initial_draw(self):
        
        if len(self.cards) >= 5:
        
            self.hand = self.cards[0:5]
            self.cards= self.cards[5:(len(self.cards)+1)]
        
        elif len(self.discard) == 0:
            
            self.hand.append([self.cards[x] for x in range(len(self.cards))])
            self.cards = []
        
        elif len(self.discard) > 0:
            
            self.shuffle()
            self.initial_draw()
            
        
    def draw(self, n):
                       
        if len(self.cards) >= n:
            
            [self.hand.append(self.cards[x]) for x in range(n)]
            self.cards = self.cards[n:(len(self.cards)+1)]
            
        elif len(self.discard) == 0:
            
            [self.hand.append(self.cards[x]) for x in range(len(self.cards))]
            self.cards = self.cards[n:(len(self.cards)+1)]
                    
        elif len(self.discard) > 0:
            
            self.shuffle()
            self.draw(n)
            
            
    def shuffle(self):
                    
        newcards = random.sample(self.discard, k = len(self.discard))
        [self.cards.append(newcards[x]) for x in range(len(newcards))]
        self.discard = []
        
    
    def clean_up(self):
        
        for j in range(len(self.hand)):
                    
            self.discard.append(self.hand[j])

        self.hand      = []   
        
        

class choices:
    
    def __init__(self, Hand_owner, Game_owner):
        
        self.Handy     = Hand_owner
        self.Game      = Game_owner
        self.Handy.actions = 1
        
        self.act_gain  = [act_dict[x] for x in self.Handy.hand]
        self.card_gain = [card_gain_dict[x] for x in self.Handy.hand]
        self.coin_gain = [coin_gain_dict[x] for x in self.Handy.hand]
        self.coins     = 0
        self.inplay    = []
        
    def play(self):
        
        ######################################
        ### 1) Do we have spare actions?
        ######################################
        
        ### This should be in seperate concerns
        
        while self.Handy.actions > 0:
        
            
        ######################################
        ### 2) Play action cards in order of most actions generated
        ######################################
        
            if len([x for x in self.act_gain if x > 0]) > 0:           
                            
                self.Handy.actions = self.Handy.actions - 1 + self.act_gain[np.argmax(self.act_gain)]

          
        ### gain cards if appropriate
        
                if self.card_gain[np.argmax(self.act_gain)] > 0:
            
                    self.Handy.draw(self.card_gain[np.argmax(self.act_gain)])    
                
            
        ### remove card from hand
            
                self.inplay.append(self.Handy.hand[np.argmax(self.act_gain)])
                del self.Handy.hand[np.argmax(self.act_gain)]
        
        ### update card list
        
                self.act_gain  = [act_dict[x] for x in self.Handy.hand]
                self.card_gain = [card_gain_dict[x] for x in self.Handy.hand]
                self.coin_gain = [coin_gain_dict[x] for x in self.Handy.hand]
                
        ########################################
        ### 3) If no action cards play card gain cards
        ########################################
        
            elif len([x for x in self.card_gain if x > 0]) > 0:
                
                self.Handy.draw(self.card_gain[np.argmax(self.card_gain)])  
                self.Handy.actions -= 1
                
        ### remove card from hand
        
                self.inplay.append(self.Handy.hand[np.argmax(self.card_gain)])
                del self.Handy.hand[np.argmax(self.card_gain)]
                
        ### update card list
                
                self.act_gain  = [act_dict[x] for x in self.Handy.hand]
                self.card_gain = [card_gain_dict[x] for x in self.Handy.hand]
                self.coin_gain = [coin_gain_dict[x] for x in self.Handy.hand]
            
            
            else:
                
                break
            
    def end_choices(self):
        
        self.Handy.ncoin.append(np.sum(self.coin_gain))
        #self.Game.ncoin.append(np.sum(self.coin_gain))
        [self.Handy.discard.append(x) for x in self.inplay]
        self.inplay = []
    
############################

## testing

############################

ncoin = []
act_dict= {'Copper':0, 'Silver':0, 'Gold':0, 'Estate':0, 'Smithy':0, 'Village':2}
coin_gain_dict= {'Copper':1, 'Silver':2, 'Gold':3, 'Estate':0, 'Smithy':0, 'Village':0}
card_gain_dict= {'Copper':0, 'Silver':0, 'Gold':0, 'Estate':0, 'Smithy':3, 'Village':1}

teg = Hand(cards = ['Estate', 'Copper', 'Copper', 'Estate', 'Copper', 'Smithy',
                    'Copper', 'Copper', 'Copper', 'Estate', 'Copper', 'Silver', 'Village'], 
                   discard = [])


for i in range(10000):
    teg.initial_draw()
    Teg = choices(teg, 0)
    Teg.play()
    Teg.end_choices()
    teg.clean_up()

    

    
    
    
