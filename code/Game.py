import pygame
from code.Menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(600, 480))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()

            pass
            # Check for events
            #for event in pg.event.get():
            #    if event.type == pg.QUIT:
            #        print("Quit event detected")
            #        pg.quit()
            #        quit()



