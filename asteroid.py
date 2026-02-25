import pygame
import random
from circleshape import *
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            movement1 = self.velocity.rotate(angle)
            movement2 = self.velocity.rotate(-(angle))
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = movement1 * 1.2
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2.velocity = movement2 * 1.2

    def draw(self, screen):
        self.screen = screen
        pygame.draw.circle(self.screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)
