from settings import *
from player import Player
from tiles import *
from random import randint
class Game:
    def __init__(self):
        pygame.init()
        self.display_surface=pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Vampire Hunters")
        self.clock=pygame.time.Clock()
        self.running=True
        #group of sprites
        self.all_sprites=pygame.sprite.Group()
        self.collision_sprites=pygame.sprite.Group()
        #player
        self.player=Player((400,300),self.all_sprites,self.collision_sprites)
        #tiles
        for x in range(6):
            i,j=randint(0,WINDOW_WIDTH),randint(0,WINDOW_HEIGHT)
            Tiles((i,j),(self.all_sprites,self.collision_sprites),(TILE_SIZE,TILE_SIZE))

    def run(self):
        while self.running:
            #dt for handling diff refresh rates
            dt=self.clock.tick()/1000
            #event loop
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    self.running=False
            #update
            self.display_surface.fill("#D8A657")
            self.all_sprites.update(dt)
            #drawing chars
            self.all_sprites.draw(self.display_surface)
            pygame.display.update()
        pygame.quit()

if __name__=="__main__":
    game=Game()
    game.run()