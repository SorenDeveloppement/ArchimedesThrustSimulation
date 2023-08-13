import pygame
import settings
from cube_object import CubeObject

pygame.init()
pygame.display.set_caption("Archimedes' Thrust Simulation by SorenDev")
screen: pygame.Surface = pygame.display.set_mode((settings.APP_WIDTH, settings.APP_HEIGHT))

object: CubeObject = CubeObject(85, pygame.Vector2(600, 400), pygame.Vector3(10, 10, 10), settings.WHITE, 5)

while True:
    settings.DELTA_TIME = pygame.time.Clock().tick(settings.FPS) / 1000.0
    
    screen.fill(settings.BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        
    # Draw water
    pygame.draw.line(screen, settings.BLUE, (0, settings.WATER_HEIGHT), (settings.APP_WIDTH, settings.WATER_HEIGHT))    
    
    # Object        
    object.apply_archimede_thrust()
    object.draw(screen)
    
    pygame.display.update()
    pygame.time.Clock().tick(settings.FPS)
