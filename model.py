class brick:
	def __init__(self, position, velocity, acceleration):
		self.position = position
		self.velocity = velocity
		self.acceleration = acceleration
	
	def setBrickPosition(self, position):
		self.position = position
		
	def setBrickVelocity(self, velocity):
		self.velocity = velocity
		
	def setBrickAcceleration(self, acceleration):
		self.acceleration = acceleration
		
class rectObstacle:
	def __init__(self, rightPos, leftPos):
		self.rightPos = rightPos
		self.leftPos = leftPos
		
	def setRightPos(self, rightPos):
		self.rightPos = rightPos
		
	def setLeftPos(self, leftPos):
		self.leftPos = leftPos
		
class squareObstacle:
	def __init__(self, top, right):
		self.top = top
		self.right = right
		
	def setTop(self, top):
		self.top = top
		
	def setLeft(self, left):
		self.right = right 
	
