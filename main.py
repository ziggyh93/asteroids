import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()

    print("Starting Asteroids!")
    print(f"Screen width:{SCREEN_WIDTH}")
    print(f"Screen height:{SCREEN_HEIGHT}")

    fps = pygame.time.Clock()
    dt = 0

    updateable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()

    Player.containers = (updateable_group, drawable_group)
    Asteroid.containers = (updateable_group, drawable_group, asteroids_group)
    AsteroidField.containers = (updateable_group)
    Shot.containers = (updateable_group, drawable_group, shots_group)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updateable_group.update(dt)
        for asteroid in asteroids_group:
            if asteroid.collision(player) == True:
                print("Game over!")
                sys.exit()
            for shot in shots_group:
                if shot.collision(asteroid) == True:
                    asteroid.split()
                    shot.kill()
        for thing in drawable_group:
            thing.draw(screen)
        pygame.display.flip()
        dt = fps.tick(60) / 1000

if __name__ == "__main__":
    main()
