from pygame import *
import pygame_menu

class GameSprite(sprite.Sprite):
    def __init__(self,player_w, player_h, player_image, player_x, player_y, player_speed):
            super().__init__()
            self.image = transform.scale(image.load(player_image),(player_w, player_h))
            self.speed = player_speed
            self.rect = self.image.get_rect()
            self.rect.x = player_x
            self.rect.y = player_y

    def  reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))  

class Player(GameSprite):

    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 700:
            self.rect.y += self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < 1110:
            self.rect.x += self.speed
        if keys_pressed[K_LEFT] and self.rect.x > 50:
            self.rect.x -= self.speed

class Enemy(GameSprite):
    direction = 'left'
    direction_2 ='up'
    def update(self,start_x,end_x):
        if self.rect.x <= start_x :
            self.direction = 'right'
        elif self.rect.x >= end_x:
            self.direction ='left'

        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

    def update_up(self,start_y,end_y):
        if self.rect.y <= start_y :
            self.direction_2 = 'down'
        elif self.rect.y >= end_y:
            self.direction_2 ='up'

        if self.direction_2 == 'down':
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

            


    

init()

win_w = 1200
win_h = 800
window = display.set_mode((win_w,win_h))
display.set_caption('Лабиринт')
display.set_icon(image.load('icon.png'))
clock = time.Clock()
background = transform.scale(image.load('background.png') ,(win_w,win_h))
background_2 = transform.scale(image.load('scooby_back.jpg'),(win_w,win_h))
mixer.init()
prize = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')
font.init()
font = font.Font(None,70)

def main():
    player = Player(50,50,'gnome.png',150,100,10)
    enemy1 = Enemy(80,70,'enemy.png',800,100,5)
    enemy2 = Enemy(85,85,'enemy_boss.png',1100,120,3)
    enemy3 = Enemy(65,65,'enemy_green.png',400,200,7)
    star = Enemy(50,50,'star_prize.png',1100,40,0)
    wall_1 = Wall(0,128,255,100,0,10,700)
    wall_2 = Wall(0,128,255,320,0,10,200)
    wall_3 = Wall(0,128,255,110,200,80,10)
    wall_4 = Wall(0,128,255,190,200,10,400)
    wall_5 = Wall(0,128,255,320,300,10,100)
    wall_6 = Wall(0,128,255,320,400,250,10)
    wall_7 = Wall(0,128,255,190,600,1000,10)
    wall_8 = Wall(0,128,255,570,260,10,150)
    wall_9 = Wall(0,128,255,690,250,10,360)
    wall_10 = Wall(0,128,255,330,120,540,10)
    wall_11 = Wall(0,128,255,870,120,10,350)
    wall_12 = Wall(0,128,255,870,470,200,10)
    wall_13 = Wall(0,128,255,1190,0,10,600)
    wall_14 = Wall(0,128,255,1050,0,10,100)
    wall_15 = Wall(0,128,255,1050,210,10,260)
    win_text = font.render('YOU WON!', True,(255,215,0) )
    lose_text = font.render('YOU LOSE',True,(155,17,30))
    mixer.music.load('backmusic.ogg')
    # mixer.music.play()
    finish = False
    while True:

        for e in event.get():
            if e.type == QUIT:
                return

        if finish != True:
            window.blit(background,(0,0))
            wall_1.draw_wall()
            wall_2.draw_wall()
            wall_3.draw_wall()
            wall_4.draw_wall()
            wall_5.draw_wall()
            wall_6.draw_wall()
            wall_7.draw_wall()
            wall_8.draw_wall()
            wall_9.draw_wall()
            wall_10.draw_wall()
            wall_11.draw_wall()
            wall_12.draw_wall()
            wall_13.draw_wall()
            wall_14.draw_wall()
            wall_15.draw_wall()
            player.reset()
            player.update()
            enemy1.reset()
            enemy1.update_up(50,25)
            enemy2.reset()
            enemy2.update(900,1100)
            enemy3.reset()
            enemy3.update(200,600)
            star.reset()
            if sprite.collide_rect(player,star):
                finish = True
                window.blit(win_text,(500,400))
                prize.play()
            if sprite.collide_rect(player,wall_15) or sprite.collide_rect(player,wall_14) or sprite.collide_rect(player,wall_13) or sprite.collide_rect(player,wall_12) or sprite.collide_rect(player,wall_11) or sprite.collide_rect(player,wall_10) or sprite.collide_rect(player,wall_9) or sprite.collide_rect(player,wall_8) or sprite.collide_rect(player,wall_7) or sprite.collide_rect(player,wall_6) or sprite.collide_rect(player,wall_5) or sprite.collide_rect(player,wall_4) or sprite.collide_rect(player,wall_3) or sprite.collide_rect(player,wall_2) or sprite.collide_rect(player,wall_1) or  sprite.collide_rect(player,enemy1) or sprite.collide_rect(player,enemy2) or sprite.collide_rect(player,enemy3):
                finish = True
                window.blit(lose_text,(500,400))
                kick.play()
                


        display.update()
        clock.tick(60)

        

def scooby_doo():
    player = Player(170,170,'scooby_doo.png',100,100,10)
    enemy1 = Enemy(180,180,'enemy_1.png',800,100,5)
    enemy2 = Enemy(185,185,'enemy_2.png',1100,120,3)
    enemy3 = Enemy(165,165,'enemy_3.png',400,200,7)
    star = Enemy(100,100,'scooby_snacks.png',1100,40,0)
    wall_1s = Wall(224,127,36,100,0,10,700)
    wall_2s = Wall(224,127,36,270,0,10,200)
    wall_3s = Wall(224,127,36,270,370,10,100)
    mixer.music.load('scooby_music.ogg')
    #mixer.music.play()
    while True:
        window.blit(background_2,(0,0))
        
        player.reset()
        player.update()
        enemy1.reset()
        enemy1.update_up(25,50)
        enemy2.reset()
        enemy2.update(900,1150)
        enemy3.reset()
        enemy3.update(200,600)
        star.reset()
        wall_1s.draw_wall()
        wall_2s.draw_wall()
        wall_3s.draw_wall()

        for e in event.get():
            if e.type == QUIT:
                return
        display.update()
        clock.tick(60)



def start_menu():
    menu = pygame_menu.Menu('Лабиринт', win_w, win_h, theme = pygame_menu.themes.THEME_GREEN)
    menu.add.button('START', main)
    menu.add.button('SCOOBY START',scooby_doo)
    menu.add.button('EXIT', pygame_menu.events.EXIT)
    menu.mainloop(window)


start_menu()
