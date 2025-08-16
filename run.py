import pygame

class Player:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.width = 20
        self.height = 20
        self.speed = 3

    def keyboard_player_handler(self, screen_height):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            if self.y > 0:
                self.y -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            if self.y < screen_height - self.height:
                self.y += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen,(255, 0, 0),(self.x, self.y, self.width, self.height))

class Bullet:
    def __init__(self, x, y ):
        self.x = x
        self.y = y
        self.radius = 3
        self.speed = 3

    def update(self):
        self.x += self.speed

    def is_off_screen(self, width):
        return self.x > width

    def draw(self, screen):
        pygame.draw.circle(screen,(255, 0, 0),(int(self.x), int(self.y)), self.radius)

class Target:
    def __init__(self, x, y, speed=1):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.speed = speed


    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0),(self.x, self.y, self.width, self.height))

    def update(self):
        self.x -= self.speed

    def check_collision(self, bullet):
        return (bullet.x + bullet.radius >= self.x and
                bullet.x - bullet.radius <= self.x + self.width and
                bullet.y + bullet.radius <= self.y and
                bullet.y - bullet.radius >= self.y + self.height)


    def is_off_screen(self):
        return self.x + self.width < 0

class Game:

    def __init__(self,width= 600, height= 300 ):
        pygame.init()
        pygame.display.set_caption("game name")
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode(
            (self.width, self.height)
        )
        self.clock = pygame.time.Clock()

        self.player = Player()
        self.bullet = Bullet()
        self.target = Target(self.width - 50, self.height // 2)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill((255,255,255))

            self.bullet.keyboard_bullet_handler(self.player.x, self.player.y)
            self.bullet.update(self.width, self.bullet, self.player, self.target)

            self.player.keyboard_player_handler(self.height)
            self.player.draw(self.screen)

            for boll in self.bullet.bullets:
                boll.draw(self.screen)

            self.target.draw(self.screen, self.bullet)



            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()



if __name__ == "__main__":
    start = Game()
    start.run()
