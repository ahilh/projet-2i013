#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 18:27:34 2019

@author: 3412857
"""

from soccersimulator import Simulation, show_simu
from salsa import get_team

# Check teams with 1 player and 2 players
team1 = get_team(1)
team2 = get_team(2)

# Create a match
simu = Simulation (team1, team2)

# Simulate and display the match
show_simu (simu)