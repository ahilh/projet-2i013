#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 17:07:59 2019

@author: 3412857
"""
from soccersimulator import Vector2D, SoccerState, SoccerAction
from soccersimulator import Simulation, SoccerTeam, Player, show_simu
from soccersimulator import Strategy
from soccersimulator import settings
import math
#from tools import *

class SuperState ( object ):
    def __init__ ( self , state , id_team , id_player ):
        self.state = state
        self.id_team = id_team
        self.id_player = id_player
    
    @property
    def __getattr__(self, attr):
        return getattr(self.state.position)
    
    @property
    def ball ( self ):
        return self.state.ball.position

    @property
    def player ( self ):
        return self.state.player_state(self.id_team,self.id_player).position

    @property
    def goal ( self ): # position du goal
        if (self.id_team == 2):
            return Vector2D(0.,settings.GAME_HEIGHT/2)
        else:
            return Vector2D(settings.GAME_WIDTH,settings.GAME_HEIGHT/2)
        
    @property
    def mygoal ( self ): # position du goal
        if (self.id_team == 1):
            return Vector2D(0.,settings.GAME_HEIGHT/2)
        else:
            return Vector2D(settings.GAME_WIDTH,settings.GAME_HEIGHT/2)
            
    @property
    def dist_ball(self): # position de la balle par rapport joueur
        return self.ball.distance(self.player)

    @property
    def gotoball(self): #joueur vas vers la balle
        return SoccerAction(acceleration=self.ball - self.player)
        
    @property
    def shoot_to_goal(self):#shoot la balle vers le goal a vitesse non controlé
        return SoccerAction(acceleration=None, shoot=self.goal - self.player)

    @property
    def ConditionToShoot(self):
        if self.dist_ball < settings.PLAYER_RADIUS + settings.BALL_RADIUS:
            return True
        else:
            return False
    	
    @property
    def listOpponent(self): # donne la liste des joueur qui ne sont pas dans notre team
        return [self.state.player_state(id_team,id_player).position 
            for (id_team, id_player) in self.state.players 
            if id_team != self.id_team]
        
    @property
    def listplayer(self): # donne la liste des joueur qui ne sont pas dans notre team
        return [self.state.player_state(id_team,id_player).position 
            for (id_team, id_player) in self.state.players 
            if id_team == self.id_team and id_player!=self.id_player]
        
    @property
    def nearestOpponentDistance(self): # joueur adverse le plus proche
        Opponent = self.listOpponent
        return min([(self.player.distance(player),player) for player in Opponent])[0]
        
    @property
    def nearestOpponentPosition(self): # joueur adverse le plus proche
        Opponent = self.listOpponent
        return min([(self.player.distance(player),player) for player in Opponent])[1]

    @property
    def nearest_player_distance(self): # joueur adverse le plus proche
        liste = self.listplayer
        return min([(self.player.distance(player),player) for player in liste])[0]
    
    @property
    def nearest_player_position(self): # joueur adverse le plus proche
        liste = self.listplayer
        return min([(self.player.distance(player),player) for player in liste])[1]
    
    @property
    def slow_shoot_to_goal(self):
        speed = self.goal - self.player
        return SoccerAction(acceleration=None, shoot=speed.normalize()*0.2)
    
    @property
    def fast_shoot_to_goal(self): 
        speed = self.goal - self.player
        return SoccerAction(acceleration=None, shoot=speed.normalize()*2.5)
    
    @property
    def fast_shoot_to_near_player(self): 
        speed = self.nearest_player_position-self.player
        print(speed)
        return SoccerAction(acceleration=None, shoot=speed.normalize()*2.5)    
    
    @property
    def ball_zone_defense_player(self): #zone de defense
        if (self.id_team == 1 and self.ball.x<=settings.GAME_WIDTH/4.) :
            return True
        elif(self.id_team == 1 and self.ball.x>settings.GAME_WIDTH/4.):
            return False
        if (self.id_team == 2 and self.ball.x<settings.GAME_WIDTH*3./4) :
            return False
        elif(self.id_team == 2 and self.ball.x>=settings.GAME_WIDTH*3./4):
            return True 
        

    @property
    def zone_attack_opponent(self): #zone de defense
        x= self.nearestOpponentPosition.x
        gw=settings.GAME_WIDTH
        if(self.id_team == 1 and x<=gw*2/4.) or (self.id_team == 2 and x>=gw*2/4.) :
            return True
        else:
            return False
