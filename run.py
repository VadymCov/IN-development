import pygame




class Game:

    pygame.init()
    pygame.display.set_caption("game name")

    def __init__(self,width= 400, height= 300 ):

        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode(
            (self.width, self.height)
        )
    def run(self):
        y = 0
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            y += 0.1

            self.screen.fill((255,255,255))
            pygame.draw.rect(self.screen, (255,0,0,), (y, 100, 50, 50))
            pygame.display.flip()

        pygame.quit()



if __name__ == "__main__":
    start = Game()
    start.run()