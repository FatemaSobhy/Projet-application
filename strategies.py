# -*- coding: utf-8 -*-
# coding: utf-8

# Rayon d'un joueur
PLAYER_RADIUS =1.
#Rayon de la balle 
BALL_RADIUS = 0.65
#Longueur du terrain
GAME_WIDTH = 150 
#Largeur du terrain 
GAME_HEIGHT= 90
GAME_GOAL_HEIGHT = 10 
MAX_GAME_STEPS = 2000
max_PlayerSpeed = 1
maxPlayerAcceleration = 0.2
maxBallAcceleration = 5

from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu
from tools import *
import math
from actions import *

class Tir(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Random")

    def compute_strategy(self, state, id_team, id_player):
        # id_team is 1 or 2
        # id_player starts at 0
        balle = state.ball.position
        joueur = state.player_state(id_team, id_player).position
        cage2 = Vector2D(GAME_WIDTH,GAME_HEIGHT/2,)
        cage1 = Vector2D(0,GAME_HEIGHT/2)
        if (id_team == 1):
            if balle.distance(joueur) < PLAYER_RADIUS + BALL_RADIUS:
                return SoccerAction(shoot=cage2-joueur)
            else:
                return SoccerAction(acceleration=balle-joueur)
        else:
            if balle.distance(joueur) < PLAYER_RADIUS + BALL_RADIUS:
                return SoccerAction(shoot=cage1-joueur)
            else:
                return SoccerAction(acceleration=balle-joueur)
#
##defenseur-attaquant en 1 contre 1
#class Defenseur1(Strategy):
#    def __init__(self):
#        Strategy.__init__(self, "Defenseur 1")
#    def compute_strategy(self, state,id_team, id_player):
#        s = SuperState(state, id_team, id_player)
#        if ( s.player_with_ball){}
#        
#    
#class Defenseur1(Strategy):
#    def __init__(self):
#        Strategy.__init__(self,"Defenseur1")
#    def compute_strategy(self, state, id_team, id_player):
#        s= SuperState(state, id_team, id_player)
#        if(!(s.test_ball)):
#            balle = state.ball.position
#            joueur = state.player_state(id_team, id_player).position
#            cage2 = Vector2D(GAME_WIDTH,GAME_HEIGHT/2,)
#            cage1 = Vector2D(0,GAME_HEIGHT/2)
#            if (id_team == 1):
#                if balle.distance(joueur) < PLAYER_RADIUS + BALL_RADIUS:
#                    return SoccerAction(shoot=cage2-joueur)
#                else:
#                    return SoccerAction(acceleration=balle-joueur)
#            else:
#                if balle.distance(joueur) < PLAYER_RADIUS + BALL_RADIUS:
#                    return SoccerAction(shoot=cage1-joueur)
#                else:
#                    return SoccerAction(acceleration=balle-joueur)
#        else:
#            if(Test_opponents):
#                return deplacement(s.ball)
#    
#    
    
    
    
    
    
    
    
    
    
    
    
#class Defenseur(Strategy):
#    def __init__(self):
#        Strategy.__init__(self, "Defenseur")
#        
#    def compute_strategy(self,state,id_team, id_player):
#        s = SuperState(state, id_team, id_player)
#       move = move(s)
#       shoot = shoot(s)
#       if 
#
class Gardien(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Gardien")
        
    def compute_strategy(self,state, id_team, id_player):
        s= SuperState(state, id_team, id_player)
        if id_team == 1:
            if s.ball.x > GAME_WIDTH/2:
                if s.player.distance(s.ball) < PLAYER_RADIUS + BALL_RADIUS:
                    shoot=(s.goal_opponent - s.player)
                    return SoccerAction(shoot= shoot.normalize()*1500)
                elif s.player.distance(s.ball) < PLAYER_RADIUS*3:
                    return SoccerAction(acceleration= s.deplacement(s.ball))
                else:
                    return SoccerAction(acceleration = s.deplacement(s.goal))
            elif s.ball.x < GAME_WIDTH/2 :
                deplacement= state.ball.position -state.player_state(id_team, id_player).position
                if id_team ==2:
                    tir = Vector2D(0,45) - state.ball. position
                else:
                    tir = Vector2D(150, 45) - state.ball.position
                    return SoccerAction(deplacement, tir)
    

