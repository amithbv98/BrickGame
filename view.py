import pygame,math
from pygame.locals import *
class gameView:
    def __init__(self, model):
        self.model = model
        self.surface = pygame.display.set_mode((self.model.window_length, self.model.window_width))
        pygame.display.set_caption('Amazing Brick')
        self.fps = pygame.time.Clock()
        self.tempX = 0
        self.tempY = 0
		
    def updateView(self):
        if self.model.gameOver:
            theta = 0
            if self.tempY+10 <= 500:
                self.tempX = self.model.brickPos[0]
                self.tempY = self.model.brickPos[1]
            while self.tempY+10 <= 500:
                theta += 5
                self.surface.fill((255,255,255))
                xCh = 10-10*math.cos(theta)
                yCh = 10*math.sin(theta)
                pygame.draw.polygon(self.surface, self.model.brickColor, ((self.tempX-10+xCh, self.tempY-yCh), (self.tempX+yCh, self.tempY-10+xCh), (self.tempX+10-xCh, self.tempY+yCh), (self.tempX-yCh, self.tempY+10-xCh)))
                self.drawRectangles()
                self.tempY = self.tempY + 5
                pygame.display.update()
                self.fps.tick(50)
            self.displayGameOverMessage()
            
                
        else:
            self.surface.fill((255,255,255))
            pygame.draw.polygon(self.surface, self.model.brickColor, ((self.model.brickPos[0]-10, self.model.brickPos[1]), (self.model.brickPos[0], self.model.brickPos[1]-10), (self.model.brickPos[0]+10, self.model.brickPos[1]), (self.model.brickPos[0], self.model.brickPos[1]+10)))
            self.drawRectangles()
            self.updateScore()
            
    def displayGameOverMessage(self):
        self.surface.fill((255,255,255))
        font = pygame.font.SysFont("Comic Sans MS", 50)
        point = font.render("Game Over", 1, (0, 0, 0))
        self.surface.blit(point, (30,100))
        font = pygame.font.SysFont("Comic Sans MS", 40)
        point = font.render(str(self.model.score), 1, (0,0,0))
        self.surface.blit(point, (130, 200))
        restart_button = pygame.image.load('res\\images\\restart.jpg')
        restart_button = pygame.transform.scale(restart_button, (50, 50))
        rect = restart_button.get_rect()
        rect = rect.move(120, 300)
        if self.model.event.type == pygame.MOUSEBUTTONDOWN:
            mousex, mousey = self.model.event.pos
            print("{}".format(rect))
            if rect.collidepoint( (mousex, mousey) ):
                self.model.__init__(300, 500)
                self.tempY = 0
        self.surface.blit(restart_button, (120, 300))
        pygame.display.update()
            
    def drawRectangles(self):
        pygame.draw.rect(self.surface, self.model.color, self.model.gameRect1)
        pygame.draw.rect(self.surface, self.model.color, self.model.gameRect2)
        pygame.draw.rect(self.surface, self.model.color, self.model.gameRect3)
        pygame.draw.rect(self.surface, self.model.color, self.model.gameRect4)
        pygame.draw.rect(self.surface, self.model.color, self.model.gameRect5)
        pygame.draw.rect(self.surface, self.model.color, self.model.gameRect7)
        pygame.draw.rect(self.surface, self.model.color, self.model.gameRect6)
        pygame.draw.rect(self.surface, self.model.color, self.model.gameRect8)
          
    def updateScore(self):
        font = pygame.font.SysFont("Comic Sans MS", 20)
        point = font.render(str(self.model.score), 1, (0, 0, 0))
        self.surface.blit(point, (270,10))
        pygame.display.update()