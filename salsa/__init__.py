#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 18:20:37 2019

@author: 3412857
"""

from .strategy import Attaquant, Defense
from soccersimulator import SoccerTeam

def get_team (nb_players):
    team = SoccerTeam ( name = "Salsa team" )
    if nb_players == 1:
        team.add ( "Striker" , Attaquant())
    if nb_players == 2:
        team.add ( "Striker" , Attaquant())
        team.add ( "Defense" , Defense())
    return team
