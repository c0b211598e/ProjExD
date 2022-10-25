import pygame as pg
import sys



def main():
    pg.display.set_caption("逃げろ!こうかとん")
    scrn_sfc = pg.display.set_mode((1600, 900))
    bg_sfc = pg.image.load("fig/pg_bg.jpg")
    bg_rct = bg_sfc.get_rect()

    #れんしゅう３
    tori_sfc = pg.image.load("fig/6.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 800, 400

    clock = pg.time.Clock() #練習1
    while True:
        scrn_sfc.blit(bg_sfc, bg_rct) #背景
        
        for event in pg.event.get(): #練習2
            if event.type == pg.QUIT:
                return

        scrn_sfc.blit(tori_sfc, tori_rct)#こうかとん
        
        pg.display.update()
        clock.tick(1000)
    
   
    
if __name__=="__main__":
    pg.init() #初期化
    main() #ゲームの本体
    pg.quit() #初期化の解除
    sys.exit()