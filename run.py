import pygame
class Player:

    def __init__(self, x=0, y=0):

        self.x = x
        self.y = y
        self.width = 20
        self.height = 20
        self.speed = 3

    def keyboard_handler(self, screen_height):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            if self.y > 0:
                self.y -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            if self.y < screen_height - self.height:
                self.y += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen,
                         (255, 0, 0),
                         (self.x, self.y, self.width, self.height))

class Game:

    def __init__(self,width= 400, height= 300 ):
        pygame.init()
        pygame.display.set_caption("game name")
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode(
            (self.width, self.height)
        )
        self.clock = pygame.time.Clock()
        self.player = Player()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill((255,255,255))
            self.player.keyboard_handler(self.height)
            self.player.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()



if __name__ == "__main__":
    start = Game()
    start.run()
