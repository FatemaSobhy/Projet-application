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


class tir(Strategy):
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
            

# Create teams
team1 = SoccerTeam(name="Team 1")
team2 = SoccerTeam(name="Team 2")

# Add players
team1.add("Tireur", tir())  # Random strategy
team2.add("Static", Strategy())   # Static strategy

# Create a match
simu = Simulation(team2, team1)

# Simulate and display the match
show_simu(simu)
