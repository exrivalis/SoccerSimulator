#les objets de base
from soccersimulator import Vector2D, SoccerState, SoccerAction

#objets pour un match
from soccersimulator import Simulation, SoccerTeam, Player, show_simu, SoccerTournament

#importer la strategie de base
from soccersimulator import Strategy

#toutes les constantes
from soccersimulator import settings

#module math
import math

class MyState(object):
	
	def __init__(self,state,idteam,idplayer) :
		self.state = state
		self.key = (idteam, idplayer)
	
	def my_position(self):
		return self.state.player_state(self.key[0], self.key[1]).position
	
	def ball_position(self) :
		return self.state.ball.position
		
	
	def aller(self, p) :
		return SoccerAction(p-self.my_position(), Vector2D())
	
	def shoot(self, p) :
		return SoccerAction(Vector2D(), p-self.my_position())

	def but_adv(self) :
		if self.key[0] == 1 :
			return Vector2D(150, 45)
		else :
			return Vector2D(0, 45)
	#recup joueur 
	def all_players(self) :
		return self.state.players
			
	def co_players(self) :
		
		return [ p  for p in self.all_players() if p[0] == self.key[0]]
	
	def adv_players(self) :
		
		return [ p  for p in self.all_players() if p[0] != self.key[0]]
		
	#recup adv le plus proche
	def adv_nearby(self):
		players = self.adv_players()
		pp = players[0]
		for p in players:
			if self.my_position().distance(p.player_state(p.position) < self.my_position().distance(pp.player_state.position):
				pp = p
		return pp
				
		
## Strategie aleatoire
class RandomStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Random")
    def compute_strategy(self,state,id_team,id_player):
        return SoccerAction(Vector2D.create_random(-1,1),Vector2D.create_random(-1,1))

#creation strategy
class Attaquant(Strategy):
	def __init__(self, name="attaquant"):
		Strategy.__init__(self, name)
	def compute_strategy(self, state, idteam, idplayer):
		#on cree un objet qui sera notre joueur et sur lequel on agira
		mstate = MyState(state,idteam,idplayer)
		return mstate.adv_nearby()
  		return mstate.aller(mstate.ball_position()) + mstate.shoot(mstate.but_adv())


		
class Defenseur(Strategy):
	def __init__(self, name="defenseur"):
		Strategy.__init__(self, name)
	def compute_strategy(self, state, idteam, idplayer):
		mstate = MyState(state,idteam,idplayer)
		
  		return mstate.aller(mstate.ball_position()) + mstate.shoot(mstate.but_adv())
		
		
		
