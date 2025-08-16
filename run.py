import pygame
from random import randint

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
                bullet.y + bullet.radius >= self.y and
                bullet.y - bullet.radius <= self.y + self.height)


    def is_off_screen(self):
        return self.x + self.width < 0

class Game:

    def __init__(self,width= 600, height= 300 ):
        pygame.init()
        pygame.display.set_caption("game name")
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)

        # game objects
        self.player = Player(10, self.height // 2)
        self.bullets = []
        self.targets = []

        # game parameters
        self.score = 0
        self.target_speed = 1
        self.shot_delay = 0
        self.target_spawn_timer = 0
        self.target_spawn_delay = 150

    def keyboard_input_handlers(self):
        keys = pygame.key.get_pressed()

        self.player.keyboard_player_handler(self.height)

        if self.shot_delay > 0:
            self.shot_delay -= 1

        if keys[pygame.K_SPACE] and self.shot_delay == 0:
            bullet = Bullet(self.player.x + self.player.width, self.player.y + self.player.height // 2)
            self.bullets.append(bullet)
            self.shot_delay = 15

    def spawn_target(self):
        if self.target_spawn_timer <= 0:
            y = randint(0,self.height -50)
            target = Target(self.width, y, self.target_speed)
            self.targets.append(target)
            self.target_spawn_timer = self.target_spawn_delay
        else:
            self.target_spawn_timer -= 1

    def update_bullets(self):
        for bullet in self.bullets[:]:
            bullet.update()
            if bullet.is_off_screen(self.width):
                self.bullets.remove(bullet)

    def update_target(self):
        for target in self.targets[:]:
            target.update()
            if target.is_off_screen():
                self.targets.remove(target)

    def check_collisions(self):
        for bullet in self.bullets[:]:
            for target in self.targets[:]:
                if target.check_collision(bullet):
                    self.bullets.remove(bullet)
                    self.targets.remove(target)
                    self.score += 10
                    if self.score % 30 == 0:
                        self.target_speed += 0.5
                        if self.target_spawn_delay > 30:
                            self.target_spawn_delay -= 5
                    break

    def draw_ui(self):
        score_text = self.font.render(f"Score: {self.score}", True, (0, 0, 0))
        speed_text = self.font.render(f"Speed: {self.target_speed:.1f}", True, (0, 0, 0))
        self.screen.blit(score_text, (10, 10))
        self.screen.blit(speed_text, (10,50))

    def draw(self):
        self.screen.fill((255, 255, 255))

        self.player.draw(self.screen)
        for bullet in self.bullets:
            bullet.draw(self.screen)

        for target in self.targets:
            target.draw(self.screen)

        self.draw_ui()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.keyboard_input_handlers()
            self.spawn_target()
            self.update_bullets()
            self.update_target()
            self.check_collisions()

            self.draw()

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()


if __name__ == "__main__":
    start = Game()
    start.run()
