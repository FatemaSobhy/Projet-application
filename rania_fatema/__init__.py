#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 12:22:07 2019

@author: 3701014
"""

from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu
from .strategies import *
#
#def get_team(nb_players):
#    team = SoccerTeam (name = "Fateam & Rania")
#    if nb_players == 1:
#        team.add ("Striker", SimpleStrategy(attaquant, 'Attaquant1'))
#    if nb_players == 2:
#        team.add ("Attaquant1", SimpleStrategy(attaquant, 'Attaquant1'))
#        team.add ("Defenseur1", SimpleStrategy(defenseur, 'Defenseur1'))
#    return team

def get_team(nb_players):
    team = SoccerTeam (name = "Fatema & Rania")
    if nb_players == 1:
        team.add("Striker", Tir())
    if nb_players == 2:
        team.add("Attaquant", Tir())
        team.add("Defenseur", Defenseur())
    return team

