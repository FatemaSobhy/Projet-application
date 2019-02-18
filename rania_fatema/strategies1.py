#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 11:15:14 2019

@author: 3701014
"""

from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu
from .tools import *
import math
from .actions import *


def gobetter(state):
    if state.player.distance(state.ball) < PLAYER_RADIUS + BALL_RADIUS:
        return SoccerAction(shoot=state.goal - state.player) 
    else:
        return SoccerAction(acceleration=state.ballameliorer - state.player) 


def gobetterdef(state):
    if state.player.distance(state.ball) < PLAYER_RADIUS + BALL_RADIUS:
        return SoccerAction(shoot= state.coequipier - state.player)
    else:
        return SoccerAction(acceleration = state.ballameliorer -state.player)
    
def defenseur(state):
    if state.teamdef[1]:
        return SoccerAction(Vector2D(GAME_WIDTH *(state.teamdef[0]),(state.ballameliorer.y + state.goal.y)/2)-state.player, state.goal -state.player)
    else:
        return gobetterdef(state)

def gobetteratt (state):
    if state.teamatt[0]:
        if state.player.y < GAME_HEIGHT/2:
            if state.player.distance(state.ball) < PLAYER_RADIUS + BALL_RADIUS:
                return SoccerAction(shoot = Vector2D(state.teamatt[1],0)-state.player)
            else: 
                return SoccerAction(acceleration = state.ballameliorer-state.player)
        else:
            if state.player.distance(state.ball) < PLAYER_RADIUS + BALL_RADIUS:
                return SoccerAction(shoot = Vector2D(state.teamatt[1],GAME_HEIGHT)-state.player)
            else:
                return SoccerAction(acceleration= state.ballameliorer -state.player)
    else:
        if state.player.distance(state.ball) < PLAYER_RADIUS + BALL_RADIUS:
            return SoccerAction(shoot = state.goal -state.player)
        else:
            return SoccerAction(acceleration = state.ballameliorer -state.player)

def attaquant(state):
     if not state.teamdef[1]:
         return SoccerAction(Vector2D(GAME_WIDTH*(state.teamdef[0]), (state.ballameliorer.y+state.goal.y)/2)-state.player,state.goal -state.player)
     else: 
         return gobetteratt(state)

##Create teams
#team1 = SoccerTeam(name="Team 1")
#team2 = SoccerTeam(name="Team 2")
#
##Add players
#team1.add("attaquant1", SimpleStrategy(attaquant, 'Attaquant1'))
#team1.add("defenseur1", SimpleStrategy(defenseur, 'Defenseur1'))
#team2.add("attaquant2", SimpleStrategy(attaquant, 'Attaquant2'))
#team2.add("defenseur2", SimpleStrategy(defenseur, 'Defenseur2'))
#
##Create a match
#simu = Simulation(team1, team2)
#
##Simulate and display the match
#show_simu(simu) 