from settings import *
from player import Player
from enemies import Enemy
from tiles import *
from random import randint
from pytmx.util_pygame import load_pygame
from groups import AllSprites
class Game:
    def __init__(self):
        pygame.init()
        self.display_surface=pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Vampire Hunters")
        self.clock=pygame.time.Clock()
        self.running=True
        #group of sprites
        self.all_sprites=AllSprites()
        self.collision_sprites=pygame.sprite.Group()
        self.setup()
        #player
        
    def setup(self):
        map=load_pygame(join("../data","maps","world.tmx"))
       # print(map)
        
        for x,y,img in map.get_layer_by_name('Ground').tiles():
            Ground((x*TILE_SIZE,y*TILE_SIZE),self.all_sprites,img)
        #exercise for inv collision
        #for obj in map.get_layer_by_name('Collisions'):
           #Tiles((obj.x,obj.y),self.collision_sprites,pygame.Surface((obj.width,obj.height)))
        
        for obj in map.get_layer_by_name('Objects'):
            Tiles((obj.x,obj.y),(self.all_sprites,self.collision_sprites),obj.image)
        
        for obj in map.get_layer_by_name('Entities'):
            if obj.name=='Player':
                self.player=Player((obj.x,obj.y),self.all_sprites,self.collision_sprites)
            else:
                Enemy((obj.x,obj.y),self.all_sprites,self.collision_sprites)
            

        

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
            self.all_sprites.draw(self.player.rect.center)
            pygame.display.update()
        pygame.quit()

if __name__=="__main__":
    game=Game()
    game.run()