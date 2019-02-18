#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 18:22:46 2019

@author: 3701014
"""
from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu
from sklearn.model_selection import ParameterGrid
from rania_fatema.actions import *
from rania_fatema.GoalSearch import*
import math

class GoTestStrategy ( Strategy ):
    def __init__ ( self , strength = None ):
        Strategy.__init__(self, " Go - getter " )
        self.strength = strength

    def compute_strategy ( self , state , id_team , id_player ):
        s = SuperState ( state , id_team , id_player )
        move = Move(s)
        shoot = Shoot(s)
        return move.to_ball() + shoot.to_goal(self.strength )
    

expe = GoalSearch (strategy= GoTestStrategy() ,params ={ 'strength': [0.1 , 1]})
expe.start()
print(expe.get_res())
print(expe.get_best())