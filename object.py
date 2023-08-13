import pygame
import settings


class Object:
    def __init__(self, volumic_mass: float, pos: pygame.Vector2, volume_shape: pygame.Vector3, color: tuple[int]) -> None:
        self.__volumic_mass = volumic_mass # In kg•m-3
        self.__volume_shape = volume_shape # In metters
        self.__volume: float = (self.__volume_shape.x * self.__volume_shape.y * self.__volume_shape.z)
        self.__mass = self.__volumic_mass * self.__volume
        self.__poids = self.__mass * settings.GRAVITY
        self.__pos = pos
        self.__color = color 
        
    def draw(self, screen: pygame.Surface):
        pass
    
    def apply_archimede_thrust(self):
        total_force: float = 0
        total_force += self.__apply_gravity()
        thrust_of_air: float = settings.AIR_VOLUMIC_MASS * self.__volume * settings.GRAVITY
        
        if self.__poids <= thrust_of_air:
            total_force -= thrust_of_air * settings.DELTA_TIME
        
        if self.__pos.y >= settings.WATER_HEIGHT:
            V_prime: float = self.__volumic_mass / settings.WATER_VOLUMIC_MASS * self.__volume
            thrust_of_water: float = settings.WATER_VOLUMIC_MASS * V_prime * settings.GRAVITY
            print(thrust_of_water, self.__poids)
            
            total_force -= thrust_of_water * settings.DELTA_TIME
            
        print(total_force)
        self.__pos.y += total_force * settings.DELTA_TIME
        
        self.__check_for_bounds()
        
    def __apply_gravity(self):
        return self.__poids * settings.DELTA_TIME
        
    def __check_for_bounds(self):
        if self.__pos.y > settings.APP_HEIGHT:
            self.__pos.y = settings.APP_HEIGHT
        if self.__pos.y < 0:
            self.__pos.y = 0
        if self.__pos.x > settings.APP_WIDTH:
            self.__pos.x = settings.APP_WIDTH
        if self.__pos.x < 0:
            self.__pos.x = 0