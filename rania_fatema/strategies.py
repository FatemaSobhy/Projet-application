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
        Strategy .__init__(self ,"Attaquant")
        
    
    def compute_strategy(self , state , id_team , id_player):
        s = SuperState(state, id_team, id_player)
        
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
        
        if s.milieu: # si la balle se trouve sur sa moitié de terrain
            return SoccerAction(s.deplacement(s.pos_att2)) # il reste dans sa position devant les cages adverses
        else:
            if s.getDistanceTo(s.ball) < s.coequipierDistanceTo(s.ball): # s'il est plus proche de la balleque son coéquipier 
                if s.can_shoot:
                    if s.testjoueurdevant: # si un défenseur (ou un autre joueur adverse) le bloque
                        shoot = s.coequipierproche - s.player # il envoie la balle à un de ses coéquipier
                        return SoccerAction(shoot = shoot.normalize()*3)
                    else:
                        shoot = s.goal_opponent - s.player # sinon il tente de marquer un but
                        return SoccerAction(shoot = shoot.normalize()) 
                return SoccerAction(acceleration = s.balleamelioree - s.player)
            if s.has_ball(s.coequipierproche):
                return s.attaquant_avance
            return SoccerAction(s.deplacement(s.pos_att2))
                    
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
        Strategy .__init__(self ,"Attaquant 1")
        
    def compute_strategy(self , state , id_team , id_player):
        s = SuperState(state, id_team, id_player)
        
        if s.milieu:# si la balle se trouve sur son milieu de terrain
            if s.testposballterrain2_5:
                if s.player.distance(s.balleamelioree) < PLAYER_RADIUS + BALL_RADIUS:
                    shoot= s.coequipierprochegoal_op- s.player
                    return SoccerAction(shoot=shoot.normalize()* 5)
                else:
                    acceleration = s.balleamelioree - s.player
                    return SoccerAction(acceleration = acceleration)
            else:
                return SoccerAction(acceleration = s.deplacement(s.posattaquantdanssonmilieu))

        else:
            if s.getDistanceTo(s.ball) <= s.coequipierDistanceTo(s.ball): # s'il est plus proche de la balle que son coéquipier
                if s.can_shoot:
                    if s.testjoueurdevant: 
                        shoot = s.coequipierprochegoal_op - s.player
                        return SoccerAction(shoot =shoot.normalize()*3)
                    shoot = s.goal_opponent - s.player # il tente de marquer
                    return SoccerAction(shoot = shoot.normalize()*3)
                acceleration = s.balleamelioree - s.player
                return SoccerAction(acceleration = acceleration)
            if s.has_ball(s.coequipierproche):
                return s.attaquant_avance           
        return SoccerAction(s.deplacement(s.pos_att))

class Attaquant5(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Random")

    def compute_strategy(self, state, id_team, id_player):
        s = SuperState(state, id_team, id_player)
       
        if s.milieu:
            if s.can_shoot:
                return SoccerAction(shoot = s.goal_opponent - s.player)
            else:
                return SoccerAction(acceleration = s.balleamelioree - s.player)
        else:
            if s.can_shoot:
                if s.testjoueurdevant:
                    return SoccerAction(shoot = s.coequipierprochedevant - s.player)
                else:
                     return SoccerAction(shoot = s.goal_opponent - s.player)
            else:
                return SoccerAction(acceleration = s.balleamelioree - s.player)
                

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
       
             
#class Defenseur1(Strategy):
#    def __init__(self):
#        Strategy.__init__(self, "Def") 
#    def compute_strategy(self,state, id_team, id_player):
#        s = SuperState(state, id_team, id_player) 
#        cage = s.goal
#        x = s.pos_def
#        a = ((s.ball.y-cage.y)/s.ball.x - cage.x)
#        b = (GAME_HEIGHT/2) - (a * x)
#	        
#        if not s.milieu:
#            pos = Vector2D(x, a* x + b)
#            return SoccerAction(s.deplacement(pos))
#        else:
#            if s.can_shoot:
#                shoot = (s.coequipierprochegoal_op - s.player)
#                return SoccerAction(shoot = shoot.normalize()*3)
#            if not s.testopponentderriere:
#                return SoccerAction(s.deplacement(Vector2D(x, a* x + b)))
#            else:
#                deplacement= s.balleamelioree - s.player
#                return SoccerAction(acceleration = deplacement)  

class Defenseur2(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Defenseur") 
        
    def compute_strategy(self, state, id_team, id_player):
        s = SuperState(state, id_team, id_player) 
        cage = s.goal
        x = s.pos_def
        a = ((s.ball.y-cage.y)/s.ball.x - cage.x)
        b = (GAME_HEIGHT/2) - (a * x)
	        
        if not s.milieu: # si la balle n'est pas dans sa moitié de terrain
            pos = Vector2D(x, a*x + b)
            return SoccerAction(s.deplacement(pos)) # il reste sur sa ligne de défense
        else:
            if s.test_posball: # si la balle est juste devant sa ligne de défense 
                if s.can_shoot:
                    shoot = (s.coequipierprochegoal_op - s.player) # envoie la balle à son coéquipier le plus proche des cages adverses
                    return SoccerAction(shoot = shoot.normalize()*2)               
                else:
                    deplacement = s.balleamelioree - s.player
                    return SoccerAction(acceleration = deplacement)
            else:
                if not s.testopponentderriere: # s'il n'y a pas d'adversaire derrière lui
                    return s.deplacementopponentderriere
                if s.can_shoot:
                    shoot = (s.coequipierprochegoal_op - s.player)
                    return SoccerAction(shoot = shoot.normalize()*2)
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
        pos = Vector2D(x, a* x + b)

        if not s.milieu:
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
                pos = Vector2D(x, a* x + b)
                return SoccerAction(s.deplacement(pos))

class Defenseur4(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Def") 
    def compute_strategy(self,state, id_team, id_player):
        s = SuperState(state, id_team, id_player) 
        cage = s.goal
        x = s.pos_def
        a = ((s.ball.y-cage.y)/s.ball.x - cage.x)
        b = (GAME_HEIGHT/2) - (a * x)
        pos = Vector2D(x, a* x + b)
        
        
        if not s.milieu:
            return SoccerAction(s.deplacement(pos))
        
        else:
            if s.testposballterrain2_5:
                return SoccerAction(s.deplacement(pos))
            else:
                if s.can_shoot:
                    shoot = (s.coequipierprochedevant2 - s.player)
                    return SoccerAction(shoot = shoot.normalize()*4)
                
                else:
                    deplacement= s.balleamelioree -s.player
                    return SoccerAction(acceleration = deplacement)
               

#class Defenseur3(Strategy):
#    def __init__(self):
#        Strategy.__init__(self, "Def")
#    def compute_strategy(self,state, id_team, id_player):
#        s = SuperState(state, id_team, id_player)
#        cage = s.goal
#        x = s.pos_def
#        a = ((s.ball.y-cage.y)/s.ball.x - cage.x)
#        b = (GAME_HEIGHT/2) - (a * x)
#       
#        if not s.milieu:
#            pos = Vector2D(x, a* x + b)
#            return SoccerAction(s.deplacement(pos))
#        else:
#            if s.test_posball:
#                if s.can_shoot:
#                    shoot = (s.coequipierprochegoal_op - s.player)
#                    return SoccerAction(shoot = shoot.normalize()*4)    
#                else:
#                    deplacement= s.balleamelioree -s.player
#                    return SoccerAction(acceleration = deplacement)
#            else:
#                pos = Vector2D(x, a* x + b)
#                return SoccerAction(s.deplacement(pos))

        
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
        
class Gardien4(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Gardien")
        
    def compute_strategy(self, state, id_team, id_player):
        s = SuperState(state, id_team, id_player)
        
        if s.test_posball: #si la balle est derrière le défenseur
            if s.can_shoot:
                return SoccerAction(shoot = (s.coequipierprochedevant2- s.player)*4)
            if s.has_ball(s.coequipierproche):
                return SoccerAction(acceleration = s.deplacement(s.goal))
            if s.getDistanceTo(s.ball) >= s.coequipierDistanceTo(s.ball):
                return SoccerAction(acceleration = s.deplacement(s.goal))
            if not s.testopponentdevantball:
                return SoccerAction(shoot = (s.coequipierprochegoal_op - s.player)*3) # fait la passe au coéquipier le plus proche des cages adverses
            if s.has_ball(s.coequipierproche): # si c'est son coéquipier qui a la balle
                return SoccerAction(acceleration = s.deplacement(s.goal)) # il retourne dans ses cages
    
            else : 
                return SoccerAction(acceleration = s.balleamelioree - s.player)
        else :
            return SoccerAction(acceleration = s.deplacement(s.goal))# il reste dans ses cages


        
                    
