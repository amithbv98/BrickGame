import pygame, sys
from pygame.locals import *
class eventHandler:
    def __init__(self,model):
        self.model = model
		
    def handleEvent(self, event):
        keys = pygame.key.get_pressed()
        self.model.event = event
        brickSound = pygame.mixer.Sound('res\\sounds\\BrickSound.wav')
        if keys[pygame.K_LEFT]:
            pygame.mixer.Sound.play(brickSound)
            self.model.brickVelocity[1] =  30
            self.model.keyPressed = "left"
        elif keys[pygame.K_RIGHT]:
            pygame.mixer.Sound.play(brickSound)
            self.model.brickVelocity[1] =  30
            self.model.keyPressed = "right"
        elif event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            

		