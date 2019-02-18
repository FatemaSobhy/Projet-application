#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 16:12:52 2019

@author: 3522495
"""
from math import *
from soccersimulator import*


class SuperState(object):
    def __init__(self, state, id_team, id_player):
        self.state = state
        self.id_team = id_team 
        self.id_player = id_player

    def __getattr__(self, attr):
        return getattr(self.state, attr)     

    @property
    def ball(self):
        return self.state.ball.position
    
    @property
    def player(self):
        return self.state.player_state(self.id_team, self.id_player).position
   
    @property 
    def goal(self):
        return Vector2D(GAME_WIDTH * ((self.id_team-1)), GAME_HEIGHT /2)
    
    @property 
    def goal_opponent(self):
        return Vector2D(GAME_WIDTH * (2- self.id_team), GAME_HEIGHT /2)
    
    def deplacement(self, obj):
        return (obj -self.player).normalize()*1500
    
    #foncer vers le but 
    @property
    def foncer_vers_but(self):
        return SoccerAction(shoot = (self.goal - self.ball).normalize())
   
    #shoot vers le but 
    @property
    def tirer_au_but(self):
        return SoccerAction(shoot =(self.goal - self.ball).normalize()*maxPlayerShoot) 
    
    @property
    def can_shoot(self):
        return (self.state.ball.position - self.state.player_state(self.id_team, self.id_player).position).norm <= BALL_RADIUS + PLAYER_RADIUS
    
    @property
    def shoot(self, target, strength):
        return (target-state.player_state(id_team, id_player).position).normalize() * strength
    
	#liste des opposants
    @property
    def opponents(self):
        return [self.state.player_state(id_team, id_player).position for (id_team, id_player) in self.state.players if id_team != self.id_team]
    #si il est un opposants ou pas
    @property
    def Test_opponents(self):
        for i in opponents:
            return True
        return False
	#trouver l'adversaire le plus proche 
    def proche_adversaire(self):
        return min([(self.player.distance(player), player) for player in self.opponents])
	#liste des players
    @property
    def list_player(self):
        return [self.state.player_state(it, ip) for (it, ip) in self.state.players]

	#joeur avec la balle 
    @property
    def player_with_ball(self):
        return min([(self.player.distance(self.ball),player) for player in self.list_player])[1]
    
    #test balle avec le joueur
    @property
    def test_ball(self):
        return (self.player_with_ball == self.player)
    
    @property
    def ballameliorer(self):
        return self.state.ball.position  + 5* self.state.ball.vitesse
    @property 
    def teamdef(self):
        if self.id_team == 1:
            (posdef, condition) = (1/4, self.ballameliorer.x > GAME_WIDTH*(1/3))
        else:
            (posdef,condition) =(3/4, self.ballameliorer.x < GAME_WIDTH*(2/3))
        return (posdef, condition)
    @property 
    def teamatt(self):
        if self.id_team == 1:
            (posatta, nextpos) = (self.player.x < GAME_WIDTH*(1/2), GAME_WIDTH*(6/10))
        else:
            (posatta,nextpos) =(self.player.x > GAME_WIDTH*(1/2), GAME_WIDTH*(4/10))
        return (posatta, nextpos)
        
    @property
    def coequipier(self):
        for(id_team, id_player) in self.state.players:
            if (id_team == self.id_team) and (id_player != self.id_player):
                return self.state.player_state(id_team, id_player).position


class SimpleStrategy ( Strategy ):
    def __init__ ( self , action , name ):
        super().__init__ ( name )
        self.action = action
        
    def compute_strategy (self, state , id_team , id_player):
        s = SuperState (state , id_team , id_player )
        return self.action(s)
            
            
