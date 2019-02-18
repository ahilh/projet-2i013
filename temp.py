from salsa import GoStrategy, defense
from soccersimulator import Player, SoccerTeam, Simulation, show_simu

        
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

