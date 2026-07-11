from settings import *
class Tiles(pygame.sprite.Sprite):
    def __init__(self,pos,groups,surf):
        super().__init__(groups)
        self.image=surf
        self.rect=self.image.get_frect(center=pos)

class Ground(pygame.sprite.Sprite):
    def __init__(self,pos,groups,surf):
        super().__init__(groups)
        self.image=surf
        self.rect=self.image.get_frect(topleft=pos)
