# -*- coding: utf-8 -*-
# coding: utf-8


from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu
from .tools import *
import math
from .actions import *

class Tir(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Random")

    def compute_strategy(self, state, id_team, id_player):
        # id_team is 1 or 2
        # id_player starts at 0
        s = SuperState(state, id_team, id_player)
        balle = s.ball
        joueur = s.player
       
        if (id_team == 1):
            if s.can_shoot:
                return SoccerAction(shoot = s.goal_opponent - joueur)
            else:
                return SoccerAction(acceleration = balle-joueur)
        else:
            if s.can_shoot:
                return SoccerAction(shoot = s.goal_opponent-joueur)
            else:
                return SoccerAction(acceleration=balle - joueur)


class Attaquant(Strategy): 
    def __init__(self):
        Strategy .__init__( self ,"Attaquant")
        
    
    def compute_strategy(self , state , id_team , id_player):
        s = SuperState(state, id_team, id_player)
#       
#        if s.player.distance(s.ball) < PLAYER_RADIUS+BALL_RADIUS:
#            shoot = s.ball- s.player
##            if s.terrain_5:
##                return SoccerAction(shoot.normalize()*6)
##            else: 
##                return SoccerAction(shoot.normalize()*2)
#            return SoccerAction(shoot.normalize()*6)
##        elif s.dist_opponent_player < PLAYER_RADIUS + BALL_RADIUS:
##            if s.dist_coequipier_player< 10:
##                shoot = s.coequipierproche - s.player
##                return SoccerAction(shoot)
##            else:
#                SoccerAction(acceleration = s.player - s.goal_opponent)
#        return SoccerAction(acceleration = s.ball - s.player) 
        
        
        if s.player.distance(s.ball) < PLAYER_RADIUS + BALL_RADIUS:
            if s.closest_opponent.distance(s.player) < (PLAYER_RADIUS*20):
                return s.dribble
            elif  s.getDistanceTo(s.goal_opponent) < (PLAYER_RADIUS * 20) :#Si il est dans la surface de tir : shoot, sinon avance
                shoot = s.goal_opponent - s.player
                return SoccerAction(shoot = shoot.normalize()*115)
            else :
                shoot = s.goal_opponent - s.player
                return SoccerAction(shoot = shoot.normalize()*1.2)
        else:
            deplacement = s.ball - s.player
            return SoccerAction(acceleration = deplacement.normalize()* 1500)
        
class Attaquant2(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Defenseur")
        
    def compute_strategy(self,state, id_team, id_player):
        s= SuperState(state, id_team, id_player)    
        
        if s.milieu:
            return SoccerAction(s.deplacement(s.pos_att))
        else:
            if s.has_ball(s.closest_opponent):
                return SoccerAction(acceleration = s.deplacement(s.ball))
            if s.getDistanceTo(s.ball) < PLAYER_RADIUS + BALL_RADIUS:
                if  s.getDistanceTo(s.goal_opponent) < (PLAYER_RADIUS * 20):
                    shoot = s.goal_opponent - s.player
                    return SoccerAction(shoot = shoot.normalize()*115)
                else:
                    shoot = s.coequipierproche - s.player
                    return SoccerAction(shoot = shoot.normalize()*15)
            if Vector2D(s.ball.x -s.player.x, s.ball.y -s.player.y).norm < Vector2D(s.ball.x- s.coequipierproche.x,s.ball.y -s.coequipierproche.y).norm: 
                return SoccerAction(acceleration = s.deplacement(s.ball))
            
            else: 
                return SoccerAction(s.deplacement(s.pos_att))
            
class Attaquant3(Strategy): 
    def __init__(self):
        Strategy .__init__( self ,"Attaquant")
        
    
    def compute_strategy( self , state , id_team , id_player ):
        s = SuperState(state, id_team, id_player)
        
        if s.milieu: 
            if s.player.distance(s.ball) < PLAYER_RADIUS + BALL_RADIUS:
                if s.closest_opponent.distance(s.player) < (PLAYER_RADIUS*20):
                    return s.dribble
                else:
                    shoot= s.coequipierproche - s.player
                    return SoccerAction(shoot=shoot.normalize()* 6)
            
            else:
                deplacement = s.ball - s.player
                return SoccerAction(acceleration = deplacement)
            
        else:
            if s.has_ball(s.closest_opponent):
                return SoccerAction(acceleration = s.deplacement(s.pos_att2))
            if s.getDistanceTo(s.ball) < PLAYER_RADIUS + BALL_RADIUS:
                if s.player.distance(s.goal_opponent) < PLAYER_RADIUS*20:
                    shoot = s.goal_opponent - s.player
                    return SoccerAction(shoot = shoot.normalize()*6)
                else:
                    shoot = s.coequipierproche - s.player
                    return SoccerAction(shoot = shoot.normalize()*6)
            if Vector2D(s.ball.x -s.player.x, s.ball.y -s.player.y).norm < Vector2D(s.ball.x- s.coequipierproche.x,s.ball.y -s.coequipierproche.y).norm: 
                return SoccerAction(acceleration = s.deplacement(s.ball))            
            else: 
                return SoccerAction(acceleration = s.deplacement(s.pos_att2))
                

class Defenseur(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Def")
        
    def compute_strategy(self,state, id_team, id_player):
        s = SuperState(state, id_team, id_player)    
        cage = s.goal
        x = s.pos_def
        a = ((s.ball.y-cage.y)/s.ball.x - cage.x)
        b = (GAME_HEIGHT/2) - (a * x)
        
        if s.milieu:
            pos = Vector2D(x, a* x + b)
            return SoccerAction(s.deplacement(pos))
        else:
            if s.can_shoot:
                shoot = s.coequipierproche - s.player
                return SoccerAction(shoot = shoot.normalize()*2)
            else:
                return SoccerAction(acceleration = s.deplacement(s.balleamelioree))
            pos = Vector2D(x, a* x + b)
            return SoccerAction(s.deplacement(pos))
       
             
class Defenseur1(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Def")
        
    def compute_strategy(self,state, id_team, id_player):
        s = SuperState(state, id_team, id_player) 
        cage = s.goal
        x = s.pos_def
        a = ((s.ball.y-cage.y)/s.ball.x - cage.x)
        b = (GAME_HEIGHT/2) - (a * x)
	        
        if s.milieu:
            pos = Vector2D(x, a* x + b)
            return SoccerAction(s.deplacement(pos))
        else:	           
             if s.has_ball(s.closest_opponent):
                 return SoccerAction(acceleration = s.deplacement(s.balleamelioree))
             if s.can_shoot:
                 shoot = (s.coequipierprochegoal_op - s.player)
                 return SoccerAction(shoot = shoot.normalize()*2)
             pos = s.balleamelioree
             return SoccerAction(s.deplacement(pos))          
    
class Gardien(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Gardien")
        
    def compute_strategy(self, state, id_team, id_player):
        s = SuperState(state, id_team, id_player)
        
        if s.test_posball:
            if s.can_shoot:
                return SoccerAction(shoot = (s.goal_opponent - s.player)*2)
            else : 
                return SoccerAction(acceleration = s.balleamelioree - s.player)
        else :
            return SoccerAction(acceleration = s.deplacement(s.goal))
        

        
                    
