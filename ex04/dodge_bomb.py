from random import randint
import pygame as pg
import sys



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
    bomb_sfc = pg.Surface((20, 20))
    bomb_sfc.set_colorkey((0, 0, 0)) #透過
    pg.draw.circle(bomb_sfc, (255, 0, 0), (10, 10), 50) #円を描く
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx = randint(0,scrn_rct.width)
    bomb_rct.centery = randint(0, scrn_rct.height)

    clock = pg.time.Clock() #練習1
    while True:
        scrn_sfc.blit(bg_sfc, bg_rct) #背景
        
        for event in pg.event.get(): #練習2
            if event.type == pg.QUIT:
                return

        key_states = pg.key.get_pressed()
        if key_states[pg.K_UP]: tori_rct.centery -= 1
        if key_states[pg.K_DOWN]: tori_rct.centery += 1
        if key_states[pg.K_LEFT]: tori_rct.centerx -=1
        if key_states[pg.K_RIGHT]: tori_rct.centerx +=1
        scrn_sfc.blit(tori_sfc, tori_rct)#こうかとん

        scrn_sfc.blit(bomb_sfc, bomb_rct)#練習5
        
        pg.display.update()
        clock.tick(1000)
    
   
    
if __name__=="__main__":
    pg.init() #初期化
    main() #ゲームの本体
    pg.quit() #初期化の解除
    sys.exit()