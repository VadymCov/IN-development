
import pygame

class Player: # Responsible for creating figures and managing the figures that the player controls

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

        # self.shot_delay = 0
        # self.bullets = []

    def update(self):
        self.x += self.speed

    def is_of_screen(self, width):
        return self.x > width

    def draw(self, screen):
        pygame.draw.circle(screen,(255, 0, 0),(self.x, self.y), self.radius)


    # def keyboard_bullet_handler(self,  player_x, player_y):
    #     keys = pygame.key.get_pressed()
    #
    #     if self.shot_delay > 0:
    #         self.shot_delay -= 1
    #
    #     if keys[pygame.K_SPACE] and self.shot_delay == 0:
    #         bullet = Bullet(
    #             player_x + 20,
    #             player_y + 10
    #         )
    #         self.bullets.append(bullet)
    #         self.shot_delay = 15




        # for bull in bullet.bullets[:]:
        #
        #     bull.x += bull.speed
        #     if bull.x >= width:
        #         bull.speed *= -1
        #     if (bull.x <= player.x + player.width and
        #             bull.y >= player.y and
        #             bull.y + bull.radius <= player.y + player.height
        #     ):
        #         bull.speed *= -1
        #     elif (
        #             bull.x + bull.radius >= target.x  and
        #             bull.y >= target.y and
        #             bull.y + bull.radius <= target.y + target.height
        #     ):
        #         print("boow")
        #         target.width -= 0.1
        #         target.height -= 0.1
        #         bullet.bullets.remove(bull)
        #         continue
        #     elif bull.x < player.x:
        #         bullet.bullets.remove(bull)
        #         continue




class Target:
    def __init__(self, width, height):
        self.x = width
        self.y = height
        self.width = 50
        self.height = 50
        self.speed = 0.01


    def draw(self, screen, bullet):
        if self.x > 0:
            self.x -= self.speed

        pygame.draw.rect(screen, (255, 0, 0),
                         (self.x, self.y, self.width, self.height))

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
