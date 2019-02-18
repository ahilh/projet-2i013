from soccersimulator import Vector2D, SoccerState, SoccerAction
from soccersimulator import Simulation, SoccerTeam, Player, show_simu
from soccersimulator import Strategy
from soccersimulator import settings
from tools import SuperState
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
        
joueura1 = Player("Attaquant A" , GoStrategy())
joueura2 = Player("Defenseur A" , defense())
team1 = SoccerTeam ("Equipe A" , [ joueura1, joueura2])
# nombre de joueurs de l equipe
joueurb1 = Player("Attaquant B" , GoStrategy())
joueurb2 = Player("Defenseur B" , defense())
team2 = SoccerTeam ("Equipe B" , [ joueurb1, joueurb2])
# Creer un match entre 2 equipes et de duree 10 pas
match = Simulation( team1 , team2 , 1000)
# Jouer le match ( sans le visualiser )
match.start()
# Jouer le match en le visualisant
show_simu( match )
# Attention !! une fois le match joue , la fonction start () permet de faire jouer le replay
# mais pas de relancer le match !!!
# Pour regarder le replay d un match

