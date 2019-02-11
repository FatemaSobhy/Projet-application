#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 17:12:59 2019

@author: 3701014
"""
from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu
from tools import *
import math
from actions import *
from strategies import *
# Create teams
team1 = SoccerTeam(name="Team 1")
team2 = SoccerTeam(name="Team 2")

# Add players
team1.add("Tireur", Tir())  # Random strategy
team1.add("Gardien",Gardien())
team2.add("Gardien", Gardien())   # Static strategy
#team1.add("Defenseur", Defenseur())
#team2.add("Defenseur", Defenseur())
team2.add("Tireur",Defenseur1())  # Random strategy

# Create a match
simu = Simulation(team1, team2)

# Simulate and display the match
show_simu(simu)