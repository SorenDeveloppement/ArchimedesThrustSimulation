import pygame
import settings

from object import Object


class CubeObject(Object):
    def __init__(self, volumic_mass: float, pos: pygame.Vector2, volume_shape: pygame.Vector3, color: tuple[int]) -> None:
        super().__init__(volumic_mass, pos, volume_shape, color)
        
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.line(screen, self._Object__color, (self._Object__pos.x - (self._Object__volume_shape.x / 2), self._Object__pos.y - (self._Object__volume_shape.y / 2)), (self._Object__pos.x - (self._Object__volume_shape.x / 2), self._Object__pos.y + (self._Object__volume_shape.y / 2)), 1)
        pygame.draw.line(screen, self._Object__color, (self._Object__pos.x + (self._Object__volume_shape.x / 2), self._Object__pos.y - (self._Object__volume_shape.y / 2)), (self._Object__pos.x + (self._Object__volume_shape.x / 2), self._Object__pos.y + (self._Object__volume_shape.y / 2)), 1)
        pygame.draw.line(screen, self._Object__color, (self._Object__pos.x - (self._Object__volume_shape.x / 2), self._Object__pos.y - (self._Object__volume_shape.y / 2)), (self._Object__pos.x + (self._Object__volume_shape.x / 2), self._Object__pos.y - (self._Object__volume_shape.y / 2)), 1)
        pygame.draw.line(screen, self._Object__color, (self._Object__pos.x - (self._Object__volume_shape.x / 2), self._Object__pos.y + (self._Object__volume_shape.y / 2)), (self._Object__pos.x + (self._Object__volume_shape.x / 2), self._Object__pos.y + (self._Object__volume_shape.y / 2)), 1)
        
        pygame.draw.circle(screen, settings.RED, self._Object__pos, 2, 1)
        
