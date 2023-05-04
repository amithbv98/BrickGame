import pygame, model, view, controller, sys

class amazingBrick:
    def __init__(self):
        self.model = model.gameState(300, 500)
        self.controller = controller.eventHandler(self.model)
        self.view = view.gameView(self.model)
        self.fps = pygame.time.Clock()
		
    def startGameLoop(self):
        while True:
            for event in pygame.event.get():
                self.controller.handleEvent(event)
            self.model.updatePositionAndScore()
            self.view.updateView()
            self.fps.tick(12)
