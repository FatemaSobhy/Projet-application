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

#team1.add("Attaquant 1", Attaquant())  
#team2.add("Attaquant 2", Tir())
#team1.add("Gardien 1", Gardien3())
#team1.add("Defenseur1", Defenseur())
##team1.add("Attaquant", Tir())  
#team2.add("Defenseur 2", Defenseur())
#team2.add("Gardien 2", Gardien3())

team1.add("Tir", Gardien())  
team2.add("Attaquant4", Attaquant4())
#team2.add("Gardien 2", Gardien())
#team2.add("Defenseur2", Defenseur1())
#team1.add("Gardien 1", Gardien())  
team2.add("Attaquant2", Attaquant2())
#team1.add("Defenseur1", Defenseur1())
#team2.add("Striker", Tir())

 
# Create a match
simu = Simulation(team1, team2)

# Simulate and display the match
show_simu(simu) 