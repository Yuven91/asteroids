import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MAX_RADIUS, ASTEROID_MIN_RADIUS
from logger import log_state, log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(
            screen,
            "white",
            self.position,
            self.radius,
            LINE_WIDTH
        )

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        else:
            old_radius = self.radius
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            forward1 = self.velocity.rotate(angle)
            forward2 = self.velocity.rotate(-angle)

            new_asteroid_radius = old_radius - ASTEROID_MIN_RADIUS

            new_asteroid1 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
            new_asteroid1.velocity = forward1 * 1.2
            new_asteroid2 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
            new_asteroid2.velocity = forward2 * 1.2
            self.kill()


            """
            new_asteroid1 = Asteroid(self.position.x, self.position.y, self.radius)
            
            new_asteroid1.velocity = forward * new_asteroid1.velocity
            
            new_asteroid2 = Asteroid(self.position.x, self.position.y, self.radius)
            forward = pygame.Vector2(0,1).rotate(-angle)
            new_asteroid2.velocity = forward * new_asteroid1.velocity
            """
