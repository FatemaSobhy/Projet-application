#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 17:49:27 2019

@author: 3701014
"""


from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu
from .tools import *
import math
from .actions import *
from soccersimulator import VolleySimulation, volley_show_simu
import math



class Defense(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Random")

    def compute_strategy(self, state, id_team, id_player):
        s = SuperState(state, id_team, id_player)
       
        if not s.milieu:
            pos = Vector2D(s.pos_def, s.closest_opponentball.y)
            return SoccerAction(s.deplacement(pos))
        else:
            if s.test_posball:
                if s.can_shoot:
                    if s.avantmilieu:
                    return SoccerAction(shoot = (s.shootavantmilieu - s.player).normalize()*2)
                else:
                    x = s.xdudef
                    y = (s.loin_opponent.y +GAME_HEIGHT)/2
                    return SoccerAction(shoot = (Vector2D(x,y) - s.player).normalize()*6 )    
                else:
                    deplacement= s.balleamelioree -s.player
                    return SoccerAction(acceleration = deplacement)
            else:
                pos = Vector2D(x, a* x + b)
                return SoccerAction(s.deplacement(pos))
            
           
