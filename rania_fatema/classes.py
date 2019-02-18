#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 17:52:23 2019

@author: 3701014
"""


class Decorator :
    def __init__ ( self , state ):
        self . state = state
    def __getattr__ ( self , attr ):
        return getattr ( self . state , attr )

class Shoot ( Decorator ):
    def __init__ ( self , state ):
        Decorator . __init__ ( self , state )
    def shoot ( self , p ):
        return SoccerAction ( Vector2D (...))

class Passe ( Decorator ):
    def __init__ ( self , state ):
        Decorator . __init__ ( self , state )
    def passe ( self , p ):
        return SoccerAction ( Vector2D (...))
