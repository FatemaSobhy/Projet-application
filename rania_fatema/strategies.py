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
                return SoccerAction(shoot = s.goal_opponent - s.player)
            else:
                return SoccerAction(acceleration = balle-s.player)
        else:
            if s.can_shoot:
                return SoccerAction(shoot = s.goal_opponent-s.player)
            else:
                return SoccerAction(acceleration=balle - s.player)


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
        Strategy.__init__(self, "Attaquant")
        
    def compute_strategy(self,state, id_team, id_player):
        s = SuperState(state, id_team, id_player) 
        shoot = Shoot(s)
        move = Move(s)
        
        if s.milieu:
            return SoccerAction(s.deplacement(s.pos_att))
        else:
            if s.getDistanceTo(s.ball) < s.coequipierDistanceTo(s.ball):
                if s.getDistanceTo(s.ball) < PLAYER_RADIUS + BALL_RADIUS:
                    if s.testjoueurdevant:
                        shoot = s.coequipierproche - s.player
                        return SoccerAction(shoot = shoot.normalize()*3)
                    else:
                        shoot= s.goal_opponent -s.player
                        return SoccerAction(shoot = shoot) 
                return SoccerAction(acceleration = s.balleamelioree - s.player)
            if s.has_ball(s.coequipierproche):
                return s.attaquant_avance
            return SoccerAction(s.deplacement(s.pos_att))


           
#            if s.getDistanceTo(s.ball) < PLAYER_RADIUS + BALL_RADIUS:
#                if  s.getDistanceTo(s.goal_opponent) < (PLAYER_RADIUS * 20):
#                    shoot = s.goal_opponent - s.player
#                    return SoccerAction(shoot = shoot.normalize()*6)
#                if s.getDistanceTo(s.closest_opponent) < 3:
#                    if s.testjoueurdevant:
#                        shoot= s.coequipierprochedevant - s.player
#                        return SoccerAction(shoot=shoot.normalize()* 6)
#                    else:
#                        return s.dribble
#                
#            for player in s.opponents:
#                if s.has_ball(player):
#                    if Vector2D(s.closest_opponent.x -s.player.x, s.closest_opponent.y -s.player.y).norm < Vector2D(s.closest_opponent.x- s.coequipierproche.x,s.closest_opponent.y -s.coequipierproche.y).norm: 
#                        return SoccerAction(acceleration = s.closest_opponent - s.player)
#            else:
#                return SoccerAction(s.deplacement(s.pos_att))
                    
class Attaquant3(Strategy): 
    def __init__(self):
        Strategy .__init__( self ,"Attaquant")
        
    
    def compute_strategy( self , state , id_team , id_player ):
        s = SuperState(state, id_team, id_player)
        
        if s.milieu: 
            if s.player.distance(s.balleamelioree) < PLAYER_RADIUS + BALL_RADIUS:
                if s.closest_opponent.distance(s.player) < (PLAYER_RADIUS*20):
                    return s.dribble
                else:
                    shoot= s.coequipierproche - s.player
                    return SoccerAction(shoot=shoot.normalize()* 6)
            
            else:
                deplacement = s.balleamelioree - s.player
                return SoccerAction(acceleration = deplacement)
            
        else:
            if s.has_ball(s.closest_opponent):
                return SoccerAction(acceleration = s.deplacement(s.pos_att2))
            if s.getDistanceTo(s.balleamelioree) < PLAYER_RADIUS + BALL_RADIUS:
                if s.player.distance(s.goal_opponent) < PLAYER_RADIUS*20:
                    shoot = s.goal_opponent - s.player
                    return SoccerAction(shoot = shoot.normalize()*6)
                else:
                    shoot = s.coequipierproche - s.player
                    return SoccerAction(shoot = shoot.normalize()*6)
            if Vector2D(s.balleamelioree.x -s.player.x, s.balleamelioree.y -s.player.y).norm < Vector2D(s.balleamelioree.x- s.coequipierproche.x,s.balleamelioree.y -s.coequipierproche.y).norm: 
                return SoccerAction(acceleration = s.deplacement(s.balleamelioree))            
            else: 
                return SoccerAction(acceleration = s.deplacement(s.pos_att2))

class Attaquant4(Strategy):
    def __init__(self):
        Strategy .__init__( self ,"Attaquant")
        
    
    def compute_strategy( self , state , id_team , id_player ):
        s = SuperState(state, id_team, id_player)
        if s.milieu: 
            if s.player.distance(s.balleamelioree) < PLAYER_RADIUS + BALL_RADIUS:
                if s.testjoueurdevant:
                    shoot= s.coequipierprochedevant - s.player
                    return SoccerAction(shoot=shoot.normalize()* 5)
                else:
                     shoot = s.goal_opponent - s.balleamelioree
                     return SoccerAction(shoot= shoot.normalize()*3)
                
            else:
                acceleration = s.balleamelioree - s.player
                return SoccerAction(acceleration = acceleration)
            
            
        else:
            if s.getDistanceTo(s.ball) <= s.coequipierDistanceTo(s.ball):
                if s.getDistanceTo(s.ball) < PLAYER_RADIUS + BALL_RADIUS:
                    if s.player.distance(s.goal_opponent) < PLAYER_RADIUS*30:
                        shoot = s.goal_opponent -s.player
                        return SoccerAction(shoot = shoot.normalize()*4)
                    if s.testjoueurdevant:
                        shoot = s.coequipierprochegoal_op - s.player
                        return SoccerAction(shoot =shoot.normalize()*4)

                acceleration= s.balleamelioree -s.player
                return SoccerAction(acceleration = acceleration)
            if s.has_ball(s.coequipierproche):
                return s.attaquant_avance
                print('4')
            
            return SoccerAction(s.deplacement(s.pos_att2))
#                if s.player.distance(s.goal_opponent) < PLAYER_RADIUS*5 and s.player.distance(s.closest_opponent)<3:
#                    if s.testjoueurdevant:
#                        shoot= s.coequipierprochedevant - s.player
#                        return SoccerAction(shoot=shoot.normalize()* 6)
#                    else:
#                         return s.dribble 
#                 
#                else:
#                    if s.testjoueurdevant:
#                        shoot= s.coequipierprochedevant - s.player
#                        return SoccerAction(shoot=shoot.normalize()* 6)
#                    if s.player.distance(s.goal_opponent) < PLAYER_RADIUS*5 and s.player.distance(s.closest_opponent)>3:
#                        shoot = s.goal_opponent - s.player
#                        return SoccerAction(shoot = shoot.normalize()*6)
#            for player in s.opponents:
#                    if s.has_ball(player):
#                        if Vector2D(s.closest_opponent.x -s.player.x, s.closest_opponent.y -s.player.y).norm < Vector2D(s.closest_opponent.x- s.coequipierproche.x,s.closest_opponent.y -s.coequipierproche.y).norm: 
#                            return SoccerAction(acceleration = s.closest_opponent - s.player)
#            else:
#                 return SoccerAction(acceleration = s.deplacement(s.pos_att2))

class Attaquant5(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Random")

    def compute_strategy(self, state, id_team, id_player):
        s = SuperState(state, id_team, id_player)
       
        if s.milieu:
            if s.can_shoot:
                return SoccerAction(shoot = s.goal_opponent - s.player)
            else:
                return SoccerAction(acceleration = s.balleamelioree-s.player)
        else:
            if s.can_shoot:
                if s.testjoueurdevant:
                    return SoccerAction(shoot = s.coequipierprochedevant-s.player)
                else:
                     return SoccerAction(shoot = s.goal_opponent-s.player)
            else:
                return SoccerAction(acceleration=s.balleamelioree - s.player)
                

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
	        
        if not s.milieu:
            pos = Vector2D(x, a* x + b)
            return SoccerAction(s.deplacement(pos))
        else:
            if s.can_shoot:
                shoot = (s.coequipierprochegoal_op - s.player)
                return SoccerAction(shoot = shoot.normalize()*4)
            if not s.testopponentderriere:
                return SoccerAction(s.deplacement(Vector2D(x, a* x + b)))
            else:
                deplacement= s.balleamelioree -s.player
                return SoccerAction(acceleration = deplacement)  

class Defenseur2(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Def") 
    def compute_strategy(self,state, id_team, id_player):
        s = SuperState(state, id_team, id_player) 
        cage = s.goal
        x = s.pos_def
        a = ((s.ball.y-cage.y)/s.ball.x - cage.x)
        b = (GAME_HEIGHT/2) - (a * x)
	        
        if not s.milieu:
            pos = Vector2D(x, a* x + b)
            return SoccerAction(s.deplacement(pos))
        else:
            if s.test_posball:
                if s.can_shoot:
                    shoot = (s.coequipierprochegoal_op - s.player)
                    return SoccerAction(shoot = shoot.normalize()*4)    
                else:
                    deplacement= s.balleamelioree -s.player
                    return SoccerAction(acceleration = deplacement)
            else:
                if not s.testopponentderriere and not s.has_ball(s.closest_opponent): 
                    deplacement = s.closest_opponent -s.player
                    return SoccerAction(acceleration = deplacement)
                if s.can_shoot:
                    shoot = (s.coequipierprochegoal_op - s.player)
                    return SoccerAction(shoot = shoot.normalize()*4)
                if s.testopponentderriere:
                    deplacement= s.balleamelioree -s.player
                    return SoccerAction(acceleration = deplacement)
                else:
                    pos = Vector2D(x, a* x + b)
                    return SoccerAction(s.deplacement(pos))

class Defenseur3(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Def")
    def compute_strategy(self,state, id_team, id_player):
        s = SuperState(state, id_team, id_player)
        cage = s.goal
        x = s.pos_def
        a = ((s.ball.y-cage.y)/s.ball.x - cage.x)
        b = (GAME_HEIGHT/2) - (a * x)
       
        if not s.milieu:
            pos = Vector2D(x, a* x + b)
            return SoccerAction(s.deplacement(pos))
        else:
            if s.test_posball:
                if s.can_shoot:
                    shoot = (s.coequipierprochegoal_op - s.player)
                    return SoccerAction(shoot = shoot.normalize()*4)    
                else:
                    deplacement= s.balleamelioree -s.player
                    return SoccerAction(acceleration = deplacement)
            else:
                if s.getDistanceTo(s.ball) <= s.coequipierDistanceTo(s.ball):
                    if s.getDistanceTo(s.ball) < PLAYER_RADIUS + BALL_RADIUS:
                        shoot = s.coequipierprochegoal_op -s.player
                        return SoccerAction(shoot = shoot.normalize()*4)
                    if not s.testopponentderriere and not s.has_ball(s.closest_opponent):
                        deplacement = s.balleamelioree -s.player
                        return SoccerAction(acceleration = deplacement)
                    else:
                        pos = Vector2D(x, a* x + b)

                
class Gardien(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Gardien")
        
    def compute_strategy(self, state, id_team, id_player):
        s = SuperState(state, id_team, id_player)
        
        if s.test_posball:
            if s.can_shoot:
                return SoccerAction(shoot = (s.coequipierprochegoal_op - s.player)*4)
            else : 
                return SoccerAction(acceleration = s.balleamelioree - s.player)
        else :
            return SoccerAction(acceleration = s.deplacement(s.goal))
        
        
class Gardien1(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Gardien")
        
    def compute_strategy(self, state, id_team, id_player):
        s = SuperState(state, id_team, id_player)
        
        if s.test_posball:
            if s.can_shoot:
                return SoccerAction(shoot = (s.coequipierprochegoal_op - s.player)*4)
            if s.has_ball(s.coequipierproche):
                return SoccerAction(acceleration = s.deplacement(s.goal))
            if s.getDistanceTo(s.ball) >= s.coequipierDistanceTo(s.ball):
                return SoccerAction(acceleration = s.deplacement(s.goal))
            else : 
                return SoccerAction(acceleration = s.balleamelioree - s.player)
        else :
            return SoccerAction(acceleration = s.deplacement(s.goal))
        

        
                    
