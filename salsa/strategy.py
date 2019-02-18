#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 18:21:40 2019

@author: 3412857
"""

from soccersimulator import Vector2D, SoccerState, SoccerAction
from soccersimulator import Simulation, SoccerTeam, Player, show_simu
from soccersimulator import Strategy
from soccersimulator import settings
from .tools import SuperState
import math


class GoStrategy (Strategy):
    def __init__(self) :
        Strategy.__init__(self,"Go−getter ")
        
    def compute_strategy(self,state,id_team,id_player): 
        s=SuperState( state , id_team , id_player )
        if s.dist_ball < settings.PLAYER_RADIUS + settings.BALL_RADIUS:
            return s.shoot_to_goal
        else:
            return s.gotoball


class defense(Strategy):
    def __init__(self) :
        Strategy.__init__(self,"Defenseur")
        
    def compute_strategy(self,state,id_team,id_player): 
        s=SuperState( state , id_team , id_player )
        if ( s.dist_ball < settings.PLAYER_RADIUS + settings.BALL_RADIUS):
            return s.shoot_to_goal
        elif (s.zone_defenseur == True):
            return s.gotoball
        else:
            return SoccerAction()