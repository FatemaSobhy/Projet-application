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
        team.add("Attaquant", Attaquant())
    if nb_players == 2:
        team.add("Attaquant", Attaquant())
        team.add("Defenseur", Defenseur2())        
    if nb_players == 3:
        team.add("Attaquant", Attaquant())
        team.add("Defenseur", Defenseur2())
        team.add("le gardien", Gardien4())     
    if nb_players == 4:
        team.add("Attaquant 4", Attaquant4())
        team.add("Attaquant 2", Attaquant2())
        team.add("Gardien", Gardien4())
        team.add("Defenseur", Defenseur2())
        
    return team




