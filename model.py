import pygame, random

class gameState():
    def __init__(self, window_length, window_width):
        self.window_length = window_length
        self.window_width = window_width
        self.brickPos =  [self.window_length//2, self.window_width//2]
        self.brickVelocity = [5, 30]
        self.acceleration = 4
        self.fps = pygame.time.Clock()
        self.brickColor = (0,0,0)
        self.keyPressed = None
        self.rectTop1 = -25
        self.rectTop2 = -275
        self.event = None
        pygame.init()
        pygame.mixer.init()
        self.gap1, self.gap2 = self.getRandomGap()
        self.color = self.getRandomColor()
        self.obstacleTop1 = self.rectTop1-random.randint(30,90)
        self.obstacleLeft1 = self.gap1+random.randint(0,100)
        self.obstacleTop2 = self.rectTop2+random.randint(30,90)
        self.obstacleLeft2 = self.gap2+random.randint(0,100)
        self.obstacleTop3 = 500
        self.obstacleLeft3 = self.gap1+random.randint(0,100)
        self.obstacleTop4 = self.rectTop2-random.randint(30,90)
        self.obstacleLeft4 = self.gap2-random.randint(0,100)
        self.current = "top1"
        self.score = 0
        self.gameRect1 = pygame.Rect(0, self.rectTop1, self.gap1, 25)
        self.gameRect2 = pygame.Rect(self.gap1+100, self.rectTop1, 300-(self.gap1+100), 25)
        self.gameRect3 = pygame.Rect(0, self.rectTop2, self.gap2, 25)
        self.gameRect4 = pygame.Rect(self.gap2+100, self.rectTop2, 300-(self.gap2+100), 25)
        self.gameRect5 = pygame.Rect(self.obstacleLeft1, self.obstacleTop1, 15,15)
        self.gameRect6 = pygame.Rect(self.obstacleLeft2, self.obstacleTop2, 15,15)
        self.gameRect7 = pygame.Rect(self.obstacleLeft3, self.obstacleTop3, 15, 15)       
        self.gameRect8 = pygame.Rect(self.obstacleLeft4, self.obstacleTop4,15, 15)
        self.gameOver = False
        
    def collision(self):
        self.gameOver = True
        
    def getRandomGap(self):
        return random.randint(40,180), random.randint(40,180)
       
    def getRandomColor(self):
        color = random.randint(0,3)
        if color == 0:
            return(255, 0 , 0)
        elif color == 1:
            return (0, 255, 0)
        elif color == 2:
            return (0, 0, 255)
        else:
            return (160, 32, 240)
            
    def updatePositionAndScore(self):
        self.setUpObstacles()
        self.moveBrickOrObstacles()
        self.regenerateObstacle()
        self.detectCollision()
        self.updateScore()
        
    def updateScore(self):
        if self.brickPos[1] <= self.rectTop1 and self.current == "top1":
            self.score += 1
            self.current = "top2"    
        if self.brickPos[1] <= self.rectTop2 and self.current == "top2":
            self.score += 1
            self.current = "top1"
        
    def setUpObstacles(self):
        self.gameRect1 = pygame.Rect(0, self.rectTop1, self.gap1, 25)
        self.gameRect2 = pygame.Rect(self.gap1+100, self.rectTop1, 300-(self.gap1+100), 25)
        self.gameRect3 = pygame.Rect(0, self.rectTop2, self.gap2, 25)
        self.gameRect4 = pygame.Rect(self.gap2+100, self.rectTop2, 300-(self.gap2+100), 25)
        self.gameRect5 = pygame.Rect(self.obstacleLeft1, self.obstacleTop1, 15,15)
        self.gameRect6 = pygame.Rect(self.obstacleLeft2, self.obstacleTop2, 15,15)
        self.gameRect7 = pygame.Rect(self.obstacleLeft3, self.obstacleTop3, 15, 15)       
        self.gameRect8 = pygame.Rect(self.obstacleLeft4, self.obstacleTop4,15, 15)
            
    def detectCollision(self):
        self.detectSquareCollision(self.gameRect5)
        self.detectSquareCollision(self.gameRect6)
        self.detectSquareCollision(self.gameRect7)
        self.detectSquareCollision(self.gameRect8)
        self.detectLeftRectangleCollision(self.gameRect1)
        self.detectLeftRectangleCollision(self.gameRect3)
        self.detectRightRectangleCollision(self.gameRect2)
        self.detectRightRectangleCollision(self.gameRect4)
        if self.brickPos[1] > 500:
            self.collision()
        
        
    def regenerateObstacle(self):
        if self.rectTop1 >= 500:
            self.rectTop1 = self.rectTop2 - 275
            self.gap1 = random.randint(40, 180)
            self.obstacleTop1 = self.rectTop1-random.randint(30,90)
            self.obstacleLeft1 = self.gap1+random.randint(0,100)
            self.obstacleTop3 = self.rectTop1+random.randint(30,90)
            self.obstacleLeft3 = self.gap1+random.randint(0,100)
            
        if self.rectTop2 >= 500:
            self.rectTop2 = self.rectTop1 - 275
            self.gap2 = random.randint(40, 180)
            self.obstacleTop2 = self.rectTop2+random.randint(30,90)
            self.obstacleLeft2 = self.gap2+random.randint(0,100)
            self.obstacleTop4 = self.rectTop2-random.randint(30,90)
            self.obstacleLeft4 = self.gap2+random.randint(0,100)
            
    def detectLeftRectangleCollision(self, gameRect):
        if(self.brickPos[0]-10 <= gameRect.right and self.brickPos[1]-10 <= gameRect.bottom and self.brickPos[1]-10 >= gameRect.top):
            self.collision()
        if(self.brickPos[1]+10 >= gameRect.top and self.brickPos[1]+10 <= gameRect.bottom and self.brickPos[0]-10 <= gameRect.right):
            self.collision()
            
    def detectRightRectangleCollision(self, gameRect):
        if(self.brickPos[0]+10 >= gameRect.left and self.brickPos[1]-10 <= gameRect.bottom and self.brickPos[1]-10 >= gameRect.top):
            self.collision()
        if(self.brickPos[1]+10 >= gameRect.top and self.brickPos[1]+10 <= gameRect.bottom and self.brickPos[0]+10 >= gameRect.left):
            self.collision()
        
        
    def detectSquareCollision(self, gameRect):
        if(self.brickPos[0]-10 <= gameRect.right and self.brickPos[0]-10 >= gameRect.left and self.brickPos[1]-10 >= gameRect.top and self.brickPos[1]-10 <= gameRect.bottom):
            self.collision()
        if(self.brickPos[0]+10 <= gameRect.right and self.brickPos[0]+10 >= gameRect.left and self.brickPos[1]+10 >= gameRect.top and self.brickPos[1]+10 <= gameRect.bottom):
            self.collision()
        if(self.brickPos[0]-10 <= gameRect.right and self.brickPos[0]-10 >= gameRect.left and self.brickPos[1]+10 >= gameRect.top and self.brickPos[1]+10 <= gameRect.bottom):
            self.collision()
        if(self.brickPos[0]+10 <= gameRect.right and self.brickPos[0]+10 >= gameRect.left and self.brickPos[1]-10 >= gameRect.top and self.brickPos[1]-10 <= gameRect.bottom):
            self.collision()    
        
    
    def moveBrickOrObstacles(self):
        self.brickVelocity[1] = self.brickVelocity[1]- self.acceleration
        if self.keyPressed == "left":
            if(self.brickPos[0]-10 >= 0):
                self.brickPos[0] = self.brickPos[0]-self.brickVelocity[0]
            else:
                self.brickVelocity[1] = -10
            if self.brickPos[1] > 250:           
                self.brickPos[1] = self.brickPos[1]-self.brickVelocity[1]
            else:
                self.moveObstacles()
            
        if self.keyPressed == "right":
            if(self.brickPos[0]+10 <= 300):
                self.brickPos[0] = self.brickPos[0]+self.brickVelocity[0]
            else:
                self.brickVelocity[1] = -10
            if self.brickPos[1] > 250:
                self.brickPos[1] = self.brickPos[1]-self.brickVelocity[1]
            else:
                self.moveObstacles()
        

    def moveObstacles(self):
            if self.brickVelocity[1] > 0:
                self.rectTop1 = self.rectTop1+self.brickVelocity[1]
                self.rectTop2 = self.rectTop2+self.brickVelocity[1]
                self.obstacleTop1 = self.obstacleTop1+self.brickVelocity[1]
                self.obstacleTop2 = self.obstacleTop2+self.brickVelocity[1]
                self.obstacleTop3 = self.obstacleTop3+self.brickVelocity[1]
                self.obstacleTop4 = self.obstacleTop4+self.brickVelocity[1]
            #if the brick is falling down the obstacles are stationary and the brick is moving
            else:
                self.brickPos[1] = self.brickPos[1]-self.brickVelocity[1]
            
		