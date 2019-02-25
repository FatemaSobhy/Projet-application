#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 17:12:59 2019

@author: 3701014
"""
from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu
import math
from rania_fatema import *
# Create teams
team1 = SoccerTeam(name="Team 1")
team2 = SoccerTeam(name="Team 2")

# Add players
#team1.add("attaquant1", SimpleStrategy(attaquant, 'Attaquant1'))
#team1.add("defenseur1", SimpleStrategy(defenseur, 'Defenseur1'))
#team2.add("attaquant2", SimpleStrategy(attaquant, 'Attaquant2'))
#team2.add("defenseur2", SimpleStrategy(defenseur, 'Defenseur2'))

team1.add("Attaquant 1", Tir())  
#team1.add("Defenseur 1", Defenseur1())
team1.add("Gardien 1", Gardien())
team2.add("Gardien 2", Gardien())  
#team2.add("Defenseur 2", Defenseur())
#team2.add("Fonceur",Fonceur())


# Create a match
simu = Simulation(team1, team2)

# Simulate and display the match
show_simu(simu) 