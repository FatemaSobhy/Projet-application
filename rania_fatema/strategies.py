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
            

class Attaquant(Strategy ): 
    def __init__(self):
        Strategy .__init__( self ,"Attaquant")
        
    
    def compute_strategy( self , state , id_team , id_player ):
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
            deplacement = s.balleamelioree - s.player
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
                    return SoccerAction(shoot = shoot.normalize()*6)
                else:
                    shoot = s.coequipierproche - s.player
                    return SoccerAction(shoot = shoot.normalize()*5)
            if Vector2D(s.ball.x -s.player.x, s.ball.y -s.player.y).norm < Vector2D(s.ball.x- s.coequipierproche.x,s.ball.y -s.coequipierproche.y).norm: 
                return SoccerAction(acceleration = s.deplacement(s.ball))
            
            else: 
                    return SoccerAction(s.deplacement(s.pos_att))
            
class Attaquant3(Strategy ): 
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
        Strategy.__init__(self, "Defenseur")
        
#    def compute_strategy(self,state, id_team, id_player):
#        s = SuperState(state, id_team, id_player)    
#        cage = s.goal
#        x = s.pos_def
#        a = ((s.ball.y-cage.y)/s.ball.x - cage.x)
#        b = GAME_HEIGHT/2 - a * x
#        
#        if s.milieu:
#            pos = Vector2D(x, a*x + b)
#            return SoccerAction(s.deplacement(pos))
#        else:
#            for i in s.opponents:
#                if s.has_ball(i):
#                    return SoccerAction(acceleration = s.deplacement(s.balleamelioree2))
#                     if s.estderriere:
#                        return SoccerAction(acceleration = s.deplacement(s.balleamelioree2), shoot = s.tirCoinBasG - s.playerS)
#            if s.has_ball:
#                shoot = (s.coequipierproche - s.player)
#                return SoccerAction(shoot = shoot.normalize()*4)
#            if (s.player == s.player_with_ball):
#                return SoccerAction(s.deplacement(s.balleamelioree))
#            pos = Vector2D(x, a*x + b)
#            return SoccerAction(s.deplacement(pos))
        
    def compute_strategy(self,state, id_team, id_player):
        s = SuperState(state, id_team, id_player)    
        cage = s.goal
        x = s.pos_def
        a = ((s.ball.y-cage.y)/s.ball.x - cage.x)
        b = GAME_HEIGHT/2 - a * x
        
        if s.milieu:
            pos = Vector2D(x, a*x + b)
            return SoccerAction(s.deplacement(pos))
        else:
            for i in s.opponents:
                if s.has_ball(i):
                    return SoccerAction(acceleration = s.deplacement(s.balleamelioree2))
                    if s.estderriere:
                        return SoccerAction(acceleration = s.deplacement(s.balleamelioree2))
            if s.getDistanceTo(s.ball) < PLAYER_RADIUS + BALL_RADIUS:
                shoot = (s.coequipierproche - s.player)
                return SoccerAction(shoot = shoot.normalize()*2)
            if(s.player == s.player_with_ball):
                return SoccerAction(s.deplacement(s.balleamelioree))
            pos = Vector2D(x, a*x + b)
            return SoccerAction(s.deplacement(pos))

#                if s.coequipierproche.x >= s.quart_terrain:
#                    shoot = (s.coequipierproche - s.player)
#                    return SoccerAction(shoot = shoot.normalize()*2)
#                else:
#                    return SoccerAction(shoot = s.tirCoinBasG)
#            if(s.player == s.player_with_ball):
#                return SoccerAction(s.deplacement(s.balleamelioree))
#            pos = Vector2D(x, a*x + b)
#            return SoccerAction(s.deplacement(pos))
                

class Gardien(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Gardien")
        
    def compute_strategy(self, state, id_team, id_player):
        s = SuperState(state, id_team, id_player)
        joueur = s.player
        balle = s.ball
        if s.pos_def:
            if s.getDistanceTo(balle) < PLAYER_RADIUS + BALL_RADIUS:
                shoot = (s.goal_opponent - s.player)
                return SoccerAction(shoot = shoot.normalize() * 6)
            elif s.getDistanceTo(balle) < PLAYER_RADIUS * 3:
                return SoccerAction(acceleration = s.deplacement(balle))
            else:
                return SoccerAction(acceleration = s.deplacement(s.goal))
        else:
            deplacement = balle - joueur
            if id_team == 2:
                tir = Vector2D(0,45) - balle
            else:
                tir = Vector2D(150, 45) - balle
                return SoccerAction(deplacement, tir)     
#        else:
#            if s.milieu:
#                if s.getDistanceTo(balle) < PLAYER_RADIUS + BALL_RADIUS:
#                    shoot = (s.goal_opponent - s.player)
#                    return SoccerAction(shoot = shoot.normalize() * 1500)
#                elif s.getDistanceTo(balle) < PLAYER_RADIUS * 3:
#                    return SoccerAction(acceleration = s.deplacement(balle))
#                else:
#                    return SoccerAction(acceleration = s.deplacement(s.goal))
#            else:
#                deplacement = balle - joueur
#                if id_team == 1:
#                    tir = Vector2D(45,90) - balle
#                else:
#                    tir = Vector2D(0, 45) - balle
#                    return SoccerAction(deplacement, tir)
                
class Gardien1(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Gardien")
        
    def compute_strategy(self, state, id_team, id_player):
        s = SuperState(state, id_team, id_player)
        
        if s.milieu:
            return SoccerAction(acceleration = s.deplacement(s.goal))
        else:
            if s.getDistanceTo(s.ball) < PLAYER_RADIUS + BALL_RADIUS:
                shoot = (s.coequipierprochedugoal - s.player)
                return SoccerAction(shoot = shoot.normalize()*2)
            elif s.player == s.player_with_ball:
                return SoccerAction(acceleration= s.ball - s.player)
#            for i in s.opponents:
#                if i == s.player_with_ball and s.player == s.coequipierproche:
#                    return SoccerAction(acceleration = s.deplacement(s.ball))
        return SoccerAction(acceleration = s.deplacement(s.goal))
        
#        if s.milieu:
#            return SoccerAction(acceleration = s.deplacement(s.goal))
#        else:
#            if s.getDistanceTo(s.ball) < PLAYER_RADIUS + BALL_RADIUS:
#                return SoccerAction(shoot = s.tirCoinHaut.normalize()*1500)
#            else:
#                if s.ball.x <= s.quart_terrain:
#                    return SoccerAction(acceleration = s.deplacement(s.balleamelioree), shoot = s.coequipierproche - s.player)
            
#        
#            elif s.player == s.player_with_ball:
#                return SoccerAction(acceleration= s.ball - s.player)
##            for i in s.opponents:
##                if i == s.player_with_ball and s.player == s.coequipierproche:
##                    return SoccerAction(acceleration = s.deplacement(s.ball))
#        return SoccerAction(acceleration = s.deplacement(s.goal))

#
        
class Gardien3(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Gardien")
        
    def compute_strategy(self, state, id_team, id_player):
        s = SuperState(state, id_team, id_player)
        joueur = s.player
        balle = s.ball
        if s.ball.x < s.pos_def:
            if s.getDistanceTo(balle) < PLAYER_RADIUS + BALL_RADIUS:
                return SoccerAction(shoot = s.goal_opponent - s.player)
            else : 
                return SoccerAction(acceleration = s.balleamelioree - s.player)
        else :
            return SoccerAction(acceleration = s.deplacement(s.goal))
            
            

