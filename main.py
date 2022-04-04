import json
import pygame


pygame.init()
screen = pygame.display.set_mode((500, 400))
clock = pygame.time.Clock()

CHANGE_LEVEL = pygame.event.custom_type()
CHANGE_LEVEL_EVENT = pygame.event.Event(CHANGE_LEVEL)


class Square(pygame.sprite.Sprite):
    def __init__(self, pos, size, color, *groups):
        super().__init__(*groups)
        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect(center=pos)

    def update(self):
        pos = pygame.mouse.get_pos()
        left, *_ = pygame.mouse.get_pressed()
        if left and self.rect.collidepoint(pos):
            self.kill()


class SmallSquare(Square):
    def __init__(self, pos, *groups):
        super().__init__(pos, (20, 20), 'white', *groups)


class BigSquare(Square):
    def __init__(self, pos, *groups):
        super().__init__(pos, (50, 50), 'green', *groups)


def next_level(enemy_list):
    for enemy in enemy_list:
        name, pos = enemy['name'], enemy['position']
        squares[name](pos, square_group)


square_group = pygame.sprite.Group()
squares = {s.__name__: s for s in (SmallSquare, BigSquare)}
with open('levels.json', 'r') as file:
    level_dict = json.load(file)

levels = iter(sorted(level_dict.items(), key=lambda x: x[0]))
pygame.event.post(CHANGE_LEVEL_EVENT)

running = True
while running:
    clock.tick(60)
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == CHANGE_LEVEL:
            try:
                lvl_info = next(levels)
                lvl_dct = lvl_info[1]
                enemies = lvl_dct.get('enemies', [])
                next_level(enemies)
                print('Level', lvl_info[0], 'completed')
            except StopIteration:
                print('All levels completed')
                running = False

    square_group.update()
    square_group.draw(screen)
    if not square_group.sprites():
        pygame.event.post(CHANGE_LEVEL_EVENT)

    pygame.display.flip()

pygame.quit()
