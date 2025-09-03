import pygame
from constants import *
import player
import asteroid
from asteroid_field import AsteroidField
from shot import Shot

def main():    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock_object = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (shots, updatable, drawable)
    asteroid.Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable, )
    player.Player.containers = (updatable, drawable)

    player1 = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill('black')

        updatable.update(dt)
        for obj in asteroids:
            if obj.collision(player1):
                print('Game Over')
                return

        for obj in drawable:
            obj.draw(screen)

        for asteroid_obj in asteroids:
            for shot in shots:
                if asteroid_obj.collision(shot):
                    asteroid_obj.split()
                    shot.kill()
        
        pygame.display.flip()
        dt = clock_object.tick(60) / 1000



if __name__ == "__main__":
    main()


