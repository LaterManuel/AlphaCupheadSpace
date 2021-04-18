import pygame
import random
Dimensionx=960
Dimensiony=350
fondoespacial=pygame.image.load("fondo espacila.jpg")
playericon=pygame.image.load("cupheadvolador.png")
trampaimage=pygame.image.load("bolita.png")
class Trampa(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = trampaimage
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.y +=1
        self.rect.x -=1
        if self.rect.y>350:
            self.rect.y=-20
            self.rect.x=random.randrange(1200)
class jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = playericon
        self.rect = self.image.get_rect()
    def update(self):
        mouse_pos=pygame.mouse.get_pos()
        self.rect.x=mouse_pos[0]
        self.rect.y=mouse_pos[1]
class Game(object):
    def __init__(self):
        self.gameover = False
        self.score = 0 
        self.tramppos = pygame.sprite.Group()
        self.all_events = pygame.sprite.Group()
        for i in range(0,900,(25)):
            trampa= Trampa()
            trampa.rect.x=random.randrange(900)
            trampa.rect.y=random.randrange(350)
            self.tramppos.add(trampa)
            self.all_events.add(trampa)
        self.player=jugador()
        self.all_events.add(self.player)
    def procesador_eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.gameover:
                    self.__init__()
        return False
    def logica(self):
        if not self.gameover:
            self.all_events.update()
            self.tramppos.update()
            choque=pygame.sprite.spritecollide(self.player,self.tramppos,True)
            for ocurrencia in choque :
                self.score=3
            if len(self.tramppos) == 31:
                self.gameover = True
    def pantalla_frames(self,pantalla,puntaje):
        pantalla.blit(fondoespacial,[0,0])
        if self.gameover:
            pass 
        else :
            self.all_events.draw(pantalla)
            pygame.display.flip()
        
def main():
    pygame.init()
    pantalla=pygame.display.set_mode([Dimensionx,Dimensiony])
    done=False
    reloj=pygame.time.Clock()
    juego=Game()
    puntaje=1
    pygame.mouse.set_visible(0)
    while not done:
        done=juego.procesador_eventos()
        juego.logica()
        juego.pantalla_frames(pantalla,puntaje)
        puntaje+=puntaje
        reloj.tick(75)
if __name__== "__main__":
    main()