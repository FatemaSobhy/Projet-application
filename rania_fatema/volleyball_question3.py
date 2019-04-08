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
       
        if not milieu:
            if(s.opponentavecball != None):
                pos = Vector2D(s.pos_def, s.opponentavecball.y)
                return SoccerAction(s.deplacement(pos))
            else:
                pos = Vector2D(s.pos_def, s.ball.y)
                return SoccerAction(s.deplacement(pos))
       else:
           
           