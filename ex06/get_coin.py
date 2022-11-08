import tkinter as tk
import tkinter.messagebox as tkm
from random import randint
import pygame as pg
import sys
import os

key_delta = {
    pg.K_UP:    [0, -1],
    pg.K_DOWN:  [0, +1],
    pg.K_LEFT:  [-1, 0],
    pg.K_RIGHT: [+1, 0],
}


SCORE = 0
class Score(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.font = pg.font.Font(None, 100)
        self.font.set_italic(1)
        self.color = "white"
        self.lastscore = -1
        self.update()
        self.rect = self.image.get_rect().move(10, 10)

    def update(self):
        """We only update the score in update() when it has changed."""
        if SCORE != self.lastscore:
            self.lastscore = SCORE
            msg = "Score: %d" % SCORE
            self.image = self.font.render(msg, 0, self.color)

def check_bound(obj_rct, scr_rct):#obj_rct:こうかとん,爆弾rct
    
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1

    return yoko, tate



def main():
    pg.display.set_caption("コインを拾えこうかとん")
    scrn_sfc = pg.display.set_mode((1600, 900))
    scrn_rct = scrn_sfc.get_rect()
    bg_sfc = pg.image.load("fig/pg_bg2.jpg")
    bg_rct = bg_sfc.get_rect()

    tori_sfc = pg.image.load("fig/6.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 180, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900, 400

    #爆弾１
    bomb_sfc1 = pg.Surface((50, 50))
    bomb_sfc1.set_colorkey((0, 0, 0)) #透過
    ch=20
    pg.draw.circle(bomb_sfc1, (255, 0, 0), (20, 20), ch) #円を描く
    bomb_rct1 = bomb_sfc1.get_rect()
    bomb_rct1.centerx = randint(0,scrn_rct.width)
    bomb_rct1.centery = randint(0, scrn_rct.height)
    
    #爆弾2
    bomb_sfc2 = pg.Surface((20, 20))
    bomb_sfc2.set_colorkey((0, 0, 0)) #透過
    pg.draw.circle(bomb_sfc2, (255, 0, 0), (10, 10), 10) #円を描く
    bomb_rct2 = bomb_sfc2.get_rect()
    bomb_rct2.centerx = randint(0,scrn_rct.width)
    bomb_rct2.centery = randint(0, scrn_rct.height)

    #コイン
    coin_sfc = pg.image.load("fig/coin01.png")
    coin_sfc = pg.transform.rotozoom(coin_sfc, 0, 0.1)
    coin_rct = coin_sfc.get_rect()
    coin_rct.centerx = randint(5, scrn_rct.width-5)
    coin_rct.centery = randint(5, scrn_rct.height-5)


    all = pg.sprite.RenderUpdates()
    Score.containers = all

    global SCORE
    if pg.font:
        all.add(Score())

    
    #練習６
    vx1,vy1 = +1, +1
    vx2,vy2 = +1, -1
    
    clock = pg.time.Clock() 

    while True:
        scrn_sfc.blit(bg_sfc, bg_rct) #背景
        
        for event in pg.event.get(): 
            if event.type == pg.QUIT:
                return
        key_states = pg.key.get_pressed()
        for key, delta in key_delta.items():
            if key_states[key]:
                tori_rct.centerx += delta[0]
                tori_rct.centery += delta[1]
                
                if check_bound(tori_rct, scrn_rct) != (+1, +1):
                    tori_rct.centerx -= delta[0]
                    tori_rct.centery -= delta[1]
        scrn_sfc.blit(tori_sfc, tori_rct) 
        
        yoko, tate = check_bound(bomb_rct1, scrn_rct)#壁判定爆弾1
        vx1 *= yoko
        vy1 *= tate

        yoko, tate = check_bound(bomb_rct2, scrn_rct)#壁判定爆弾2
        vx2 *= yoko
        vy2 *= tate

        #壁に触れると加速
        if vx2 < 0:
            vx2 -=0.0005
        if vx2 > 0:
            vx2 +=0.0005
        if vy2 < 0:
            vy2 -=0.0005
        if vy2 > 0:
            vy2 +=0.0005
    
        bomb_rct1.move_ip(vx1, vy1)
        bomb_rct2.move_ip(vx2, vy2)
        scrn_sfc.blit(bomb_sfc1, bomb_rct1)
        scrn_sfc.blit(bomb_sfc2, bomb_rct2)

        #コイン設置
        scrn_sfc.blit(coin_sfc, coin_rct)


        if tori_rct.colliderect(bomb_rct1):#こうかとん爆弾1重なったら
            tori_sfc = pg.image.load("fig/8.png")
            tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 3.0)
            tori_rct.center = tori_rct.centerx, tori_rct.centery
            scrn_sfc.blit(tori_sfc, tori_rct)#こうかとん
            pg.display.update()
            tkm.showinfo("GameOver", f"こうかとんは天に召された")

            return


        if tori_rct.colliderect(bomb_rct2):#こうかとん爆弾2重なったら
            tori_sfc = pg.image.load("fig/8.png")
            tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 3.0)
            tori_rct.center = tori_rct.centerx, tori_rct.centery
            scrn_sfc.blit(tori_sfc, tori_rct)#こうかとん
            pg.display.update()
            tkm.showinfo("GameOver", f"こうかとんは天に召された")

            return


        if tori_rct.colliderect(coin_rct):#こうかとんとコインが重なったら
            coin_rct.centerx = randint(0,scrn_rct.width)
            coin_rct.centery = randint(0, scrn_rct.height)
            SCORE = SCORE + 1
            print(SCORE)
            

        if SCORE >= 5: #コインを5回とったら
            tori_sfc = pg.image.load("fig/6.png")
            tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 3.0)
            tori_rct.center = tori_rct.centerx, tori_rct.centery
            scrn_sfc.blit(tori_sfc, tori_rct)#こうかとん
            pg.display.update()
            tkm.showinfo("GameClear", f"こうかとんはコインを拾いつくした。")
            
            return

         #時間制限      
        if pg.time.get_ticks() > 30000:#30秒たったら
            tori_sfc = pg.image.load("fig/6.png")
            tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 3.0)
            tori_rct.center = tori_rct.centerx, tori_rct.centery
            scrn_sfc.blit(tori_sfc, tori_rct)#こうかとん
            pg.display.update()
            tkm.showinfo("GameOver", f"タイムアップ!!")
            
            return


        pg.display.update()
        clock.tick(1000)
    
   
    
if __name__=="__main__":
    pg.init() #初期化
    main() #ゲームの本体
    pg.quit() #初期化の解除
    sys.exit()

    
