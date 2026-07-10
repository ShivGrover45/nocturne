from settings import *
class Tiles(pygame.sprite.Sprite):
    def __init__(self,pos,groups,size):
        super().__init__(groups)
        self.image=pygame.Surface(size)
        self.image.fill("black")
        self.rect=self.image.get_rect(center=pos)