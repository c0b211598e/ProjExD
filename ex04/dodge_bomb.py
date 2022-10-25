from inspect import FullArgSpec
from random import randint
import pygame as pg
import sys

def check_bound(obj_rct, scr_rct):#obj_rct:こうかとん,爆弾rct
    
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1

    return yoko, tate



def main():
    pg.display.set_caption("逃げろ!こうかとん")
    scrn_sfc = pg.display.set_mode((1600, 900))
    scrn_rct = scrn_sfc.get_rect()
    bg_sfc = pg.image.load("fig/pg_bg.jpg")
    bg_rct = bg_sfc.get_rect()

    #れんしゅう３
    tori_sfc = pg.image.load("fig/6.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 180, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900, 400

    #練習5
    bomb_sfc1 = pg.Surface((20, 20))
    bomb_sfc1.set_colorkey((0, 0, 0)) #透過
    pg.draw.circle(bomb_sfc1, (255, 0, 0), (10, 10), 10) #円を描く
    bomb_rct1 = bomb_sfc1.get_rect()
    bomb_rct1.centerx = randint(0,scrn_rct.width)
    bomb_rct1.centery = randint(0, scrn_rct.height)

    bomb_sfc2 = pg.Surface((100, 100))
    bomb_sfc2.set_colorkey((0, 0, 0)) #透過
    pg.draw.circle(bomb_sfc2, (255, 0, 0), (50, 50), 50) #円を描く
    bomb_rct2 = bomb_sfc2.get_rect()
    bomb_rct2.centerx = randint(0,scrn_rct.width)
    bomb_rct2.centery = randint(0, scrn_rct.height)

    #練習６
    vx1,vy1 = +1, +1
    vx2,vy2 = -1, -1

    clock = pg.time.Clock() #練習1
    while True:
        scrn_sfc.blit(bg_sfc, bg_rct) #背景
        
        for event in pg.event.get(): #練習2
            if event.type == pg.QUIT:
                return

        key_states = pg.key.get_pressed()
        if key_states[pg.K_UP]: tori_rct.centery -= 1
        if key_states[pg.K_DOWN]: tori_rct.centery += 1
        if key_states[pg.K_LEFT]: tori_rct.centerx -= 1
        if key_states[pg.K_RIGHT]: tori_rct.centerx += 1
        yoko, tate = check_bound(tori_rct, scrn_rct)#壁判定
        if yoko == -1: 
            if key_states[pg.K_LEFT]:
                tori_rct.centerx += 1
            if key_states[pg.K_RIGHT]:
                tori_rct.centerx -= 1

        if tate == -1: 
            if key_states[pg.K_UP]:
                tori_rct.centery += 1
            if key_states[pg.K_DOWN]:
                tori_rct.centery -= 1

        scrn_sfc.blit(tori_sfc, tori_rct)#こうかとん

        yoko, tate = check_bound(bomb_rct1, scrn_rct)#壁判定
        vx1 *= yoko
        vy1 *= tate
        yoko, tate = check_bound(bomb_rct2, scrn_rct)#壁判定
        vx2 *= yoko
        vy2 *= tate

        bomb_rct1.move_ip(vx1, vy1)
        bomb_rct2.move_ip(vx2, vy2)
        scrn_sfc.blit(bomb_sfc1, bomb_rct1)#練習5
        scrn_sfc.blit(bomb_sfc2, bomb_rct2)
        
        pg.display.update()
        clock.tick(1000)
    
   
    
if __name__=="__main__":
    pg.init() #初期化
    main() #ゲームの本体
    pg.quit() #初期化の解除
    sys.exit()