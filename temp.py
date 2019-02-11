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
            
class Defenseur1(Strategy):
            
            

class Defenseur(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Defenseur")
        
    def compute_strategy(self,state,id_team, id_player):
        s = SuperState(state, id_team, id_player)
        if (s.test_ball):
            goal_adverse = goal_opponent(id_team)
            force = 10
            player = s.player
            move = deplacement(player)
            shoot = Vector2D(0,0)
            if s.can_shoot:
                shoot = shoot(state, id_team, id_player, goal_adverse, force)
                
            return SoccerAction(move, shoot)
      
        goal = self.goal()
        position_balle = self.ball()
        goalTop = goal + Vector2D(0,GAME_GOAL_HEIGHT/2.)
        goalBot = goal - Vector2D(0, GAME_GOAL_HEIGHT/2.)
        
        ballToGoalTop = goalTop - position_balle
        ballToGoalBot = goalBot - position_balle
        angle = (ballToGoalTop.angle + ballToGoalBot.angle)/2.
        vect = Vector2D(norm=1./cos(angle)*ballToGoalBot.x/2., angle=angle)
        
        move = s.deplacement(vect+position_balle)
        shoot = Vector2D(0,0)
        if can_shoot(state, id_team, id_player):
            shoot = shoot(state, id_team, id_player, goal_opponent, force)
            
        return SoccerAction(move, shoot) 
#
class Gardien(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Gardien")
        
    def compute_strategy(self,state, id_team, id_player):
        s= SuperState(state, id_team, id_player)

        if s.player.distance(s.ball) < PLAYER_RADIUS + BALL_RADIUS:
            shoot=(s.goal_opponent - s.player)
            return SoccerAction(shoot= shoot.normalize()*1500)
        elif s.player.distance(s.ball) < PLAYER_RADIUS*3:
            return SoccerAction(acceleration= s.deplacement(s.ball))
        else:
            return SoccerAction(acceleration = s.deplacement(s.goal))

    
# Create teams
team1 = SoccerTeam(name="Team 1")
team2 = SoccerTeam(name="Team 2")

# Add players
team1.add("Tireur", Tir())  # Random strategy
team1.add("Gardien",Gardien())
team2.add("Gardien", Gardien())   # Static strategy
team1.add("Defenseur", Defenseur())
team2.add("Defenseur", Defenseur())

# Create a match
simu = Simulation(team1, team2)

# Simulate and display the match
show_simu(simu)
