from settings import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self,pos,groups,collision_sprites):
        super().__init__(groups)
        self.image=pygame.image.load(join("../images","enemies","bat","0.png")).convert_alpha()
        self.rect=self.image.get_rect(center=pos)
        self.hitbox=self.rect.inflate(-60,0)
