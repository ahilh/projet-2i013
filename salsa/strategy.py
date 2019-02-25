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


class Attaquant (Strategy):
    def __init__(self) :
        Strategy.__init__(self,"Go−getter ")
        
    def compute_strategy(self,state,id_team,id_player): 
        s=SuperState( state , id_team , id_player )
        if s.ConditionToShoot==True:
            return s.slow_shoot_to_goal
        if s.ball_zone_defense_player==True and s.id_team==1:
            dir = s.ball - s.player
            dir.x = settings.GAME_WIDTH/4 - s.player.x
            return SoccerAction(acceleration=dir)
        elif s.ball_zone_defense_player==True and s.id_team==2:
            dir = s.ball - s.player
            dir.x = settings.GAME_WIDTH*3./4 - s.player.x
            return SoccerAction(acceleration=dir)
        else:
            return s.gotoball


class Defense(Strategy):
    def __init__(self) :                                                  
        Strategy.__init__(self,"Defenseur")
        
    def compute_strategy(self,state,id_team,id_player): 
        s=SuperState( state , id_team , id_player )
        fastshoot = s.fast_shoot_to_near_player
        gotoball= s.gotoball
        if (s.ConditionToShoot==True) :
            if(s.zone_attack_opponent==True):
                return fastshoot
        if (s.ball_zone_defense_player== True):
            return gotoball
        else:
            dir = s.ball - s.player
            dir.x = 0
            return SoccerAction(acceleration=dir)
