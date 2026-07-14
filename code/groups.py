from settings import *
class AllSprites(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface=pygame.display.get_surface()
        self.offset=pygame.Vector2()
    def draw(self,target_pos):
        self.offset.x=-target_pos[0]
        #offset for the y axis
        self.offset.y=-target_pos[1]
        for sprite in self :
            self.display_surface.blit(sprite.image, sprite.rect.center+self.offset)