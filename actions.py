class Move(object):
	def __init__(self, superstate):
		self.superstate = superstate
		
	def move(self, acceleration = None):
		return SoccerAction(acceleration = acceleration)
	
	def to_ball(self):
		return self.move(self.superstate.ball_dir())
	
class Shoot(object):
	def __init__(self, superstate):
		self.superstate = superstate
	def shoot(self, direction = None):
		dist = self.superstate.player.distance(self.sueprstate.ball)
		if (dist < PLAYER_RADIUS + BALL_RADIUS :
			return SoccerAction(shoot = direction)
		else: 
			return SoccerAction()
			
	def to_goal(self, strength = None):
		return self.shoot(self.superstate.goal_dir)
		

