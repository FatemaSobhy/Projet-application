#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 19:07:02 2019

@author: 3701014
"""
from strategies import *
from soccersimulator import SoccerTeam, Simulation, show_simu

def get_team (nb_players):
    team = SoccerTeam (name = "Fateam & Rania")
    if nb_players == 1:
        team.add ("Striker", Tir())
    if nb_players == 2:
        team.add ("Striker", Tir())
        team.add ("Random", RandomStrategy())
    
    return team

