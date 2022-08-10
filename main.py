import time

import pygame
import random
import statistics


with open('log.txt', 'w+') as file:
    file.write('')


class Blik(pygame.sprite.Sprite):
    def __init__(self, screen: pygame.Surface):
        super().__init__()
        self.screen = screen
        self.velocity = 5
        self.direction = 5
        self.size = 100
        #self.pos = [random.randint(0, self.screen.get_size()[0]), random.randint(0, self.screen.get_size()[1])]
        self.pos = [0, 0]
        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.size, self.size)
        self.change = False
    def draw(self):
        if self.rect.y < 0:
            self.change = True
        elif self.rect.y > self.screen.get_size()[1]-self.size:
            self.change = False

        if self.change:
            self.rect.y += self.velocity
        else:
            self.rect.y -= self.velocity
        # if self.rect.x < 0 or self.rect.x > self.screen.get_size()[0]-self.size or self.rect.y < 0 or self.rect.y > self.screen.get_size()[1]-self.size:
        #     if self.direction < 0:
        #         self.direction = self.velocity
        #     else:
        #         n = self.velocity
        #         self.direction = 0 - n
        #     self.rect.x, self.rect.y = [random.randint(0, self.screen.get_size()[0]), random.randint(0, self.screen.get_size()[1])]
        # else:
        #     self.rect.x += self.direction #+ random.randint(1, 9)
        #     self.rect.y += self.direction #+ random.randint(1, 9)

        pygame.draw.rect(self.screen, (255, 0, 0), self.rect)


class Blop(pygame.sprite.Sprite):
    def __init__(self, screen: pygame.Surface, size_, velocity_):
        super().__init__()
        self.size = size_
        self.velocity = velocity_

        self.pos = [random.randint(0, screen.get_size()[0]-self.size), random.randint(0, screen.get_size()[1]-self.size)]
        self.screen = screen
        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.size, self.size)
        self.changeDir = False

        self.ADN = {
            'size': self.size,
            'speed': self.velocity
        }

    def draw(self):
        if self.rect.x > self.screen.get_size()[0]-self.size:
            self.changeDir = False
        elif self.rect.x < 0:
            self.changeDir = True

        if self.changeDir:
            self.rect.x += self.velocity
        else:
            self.rect.x -= self.velocity
        pygame.draw.rect(self.screen, (0, 255, 0), self.rect)


pygame.init()
game = pygame.display.set_mode((600, 600))
FPS = 40
CLOCK = pygame.time.Clock()

pygame.display.set_caption("~ Game ~")
running = True

person = [
    Blop(game, random.randint(5, 50), random.randint(1, 20)),
    Blop(game, random.randint(5, 50), random.randint(1, 20)),
    Blop(game, random.randint(5, 50), random.randint(1, 20)),
    Blop(game, random.randint(5, 50), random.randint(1, 20)),
    Blop(game, random.randint(5, 50), random.randint(1, 20)),
    Blop(game, random.randint(5, 50), random.randint(1, 20)),
    Blop(game, random.randint(5, 50), random.randint(1, 20)),
    Blop(game, random.randint(5, 50), random.randint(1, 20)),
Blop(game, random.randint(5, 50), random.randint(1, 20)),
    Blop(game, random.randint(5, 50), random.randint(1, 20)),
    Blop(game, random.randint(5, 50), random.randint(1, 20)),
    Blop(game, random.randint(5, 50), random.randint(1, 20)),
    Blop(game, random.randint(5, 50), random.randint(1, 20)),
    Blop(game, random.randint(5, 50), random.randint(1, 20)),
    Blop(game, random.randint(5, 50), random.randint(1, 20)),
    Blop(game, random.randint(5, 50), random.randint(1, 20)),
Blop(game, random.randint(5, 50), random.randint(1, 20)),
    Blop(game, random.randint(5, 50), random.randint(1, 20)),
    Blop(game, random.randint(5, 50), random.randint(1, 20)),
    Blop(game, random.randint(5, 50), random.randint(1, 20)),
    Blop(game, random.randint(5, 50), random.randint(1, 20)),
    Blop(game, random.randint(5, 50), random.randint(1, 20)),
    Blop(game, random.randint(5, 50), random.randint(1, 20)),
    Blop(game, random.randint(5, 50), random.randint(1, 20)),
    Blop(game, random.randint(5, 50), random.randint(1, 20)),
    Blop(game, random.randint(5, 50), random.randint(1, 20))
]

person2 = [

]

monster = [
    Blik(game),
    # Blik(game),
    # Blik(game),
    # Blik(game),
    # Blik(game)
]

startTime = time.time()
endTime = 0

idx = 0

while running:
    if not person:
        endTime = time.time()
        best = person2[-1]
        person.append(best)

        bad = person2[0]

        for pers in person2[:-1]:
            size = int(statistics.mean([int(statistics.mean([best.ADN['size'], pers.ADN['size']])), random.randint(5, 55-bad.ADN['size'])]))
            velocity = int(statistics.mean([int(statistics.mean([best.ADN['speed'], pers.ADN['speed']])), random.randint(1, 25-bad.ADN['speed'])]))
            bUpgrade = Blop(game, size, velocity)
            person.append(bUpgrade)

        person2 = []

        with open('log.txt', 'a+') as file:
            file.write("Time = "+str(endTime-startTime)+f" : Best = {best.ADN} : Bad = {bad.ADN}\n")

        startTime = time.time()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            # for i, p in enumerate(person):
            #     if p.rect.collidepoint(pos[0], pos[1]):
            #         person2.append(person[i])
            #         person.pop(i)

    game.fill((0, 0, 0))
    for p in person:
        p.draw()

    for i, p in enumerate(person):
        for m in monster:
            if p.rect.colliderect(m.rect):
                person2.append(person[i])
                person.pop(i)

    for m in monster:
        m.draw()

    pygame.display.update()
    pygame.display.flip()
    CLOCK.tick(FPS)
pygame.quit()
