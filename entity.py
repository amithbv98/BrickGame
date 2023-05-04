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
	def __init__(self, position, velocity, dimension, color):
		self.position = position
		self.velocity = velocity
        self.color = color
        self.dimension = dimension
		
	def setPosition(self, position):
		self.position = position
        
    def setVelocity(self, velocity):
        self.velocity = velocity
    
    def setColor(self, color):
        self.color = color
    
    def setDimension(self, dimension):
        self.dimension = dimension
				
class squareObstacle:
	def __init__(self, position, velocity, length, color):
		self.position = position
		self.velocity = velocity
		
	def setPosition(self, position):
		self.position = position
		
	def setVelocity(self, velocity):
		self.velocity = velocity

    def setColor(self, color):
        self.color = color
        
    def setLength(self, length):
        self.length = length
	
