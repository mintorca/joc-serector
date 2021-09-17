#_*_ coding:utf-8 _*_
import sys,pygame
import random

cookies = ["Croissant","Cupcake","Danish","Donut","Macaroon","SugarCookie"]       

class CandyCrush(object):
    def __init__(self):#생성자
        self.TILE_LEFT_X = 35
        self.TILE_LEFT_Y = 130
        self.XBLOCK = 6
        self.YBLOCK = 6
        self.width = 450
        self.height = 720

        pygame.init()
        self.default_font = pygame.font.SysFont("Forte",30)
        self.screen = pygame.display.set_mode((self.width, self.height))        
        self.init_game()

    def init_game(self):#게임 초기화
        self.load_image()
        self.BLOCK_WD, self.BLOCK_HT = self.Tile.get_rect()[2], self.Tile.get_rect()[3] 
        self.mouse_drag = False
        self.score = 0
        self.gameover = 0
        self.counter = 60
        #이미지를 화면 크기로 변환
        self.BackGround = \
            pygame.transform.scale(self.BackGround,(self.width,self.height))
        #화면에 이미지 출력    
        self.screen.blit(self.BackGround, self.BackGround_rect)

        self.dic = {"Croissant": self.Croissant,   
                    "Cupcake": self.Cupcake,
                    "Danish": self.Danish,
                    "Donut": self.Donut,
                    "Macaroon": self.Macaroon,
                    "SugarCookie": self.SugarCookies,
                    "Tile": self.Tile}

        self.dic_N = {"Croissant": '1',   
                      "Cupcake": '2',
                      "Danish": '3',
                      "Donut": '4',
                      "Macaroon": '5',
                      "SugarCookie": '6',
                      "Tile": '7'}
        self.suffle()
        self.tilemap[3]=["Croissant","Donut","Donut","Donut","Donut","Macaroon"]
        self.tilemap[0][2],self.tilemap[1][2],self.tilemap[2][2] = \
            "SugarCookie","SugarCookie","SugarCookie"
        self.tilemap_2_number()
        self.check_chain(self.tilemap_N)
        self.check_chain(list(map(list, zip(*self.tilemap_N))))                      
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        return            

    def load_image(self):#필요한 이미지 읽기
        #배경이미지 설정
        self.BackGround = pygame.image.load("Background@2x.png")
        self.BackGround_rect = self.BackGround.get_rect()
        self.Tile = pygame.image.load("Tile@2x.png")        
        self.Croissant = pygame.image.load(cookies[0]+"@2x.png")
        self.Cupcake = pygame.image.load(cookies[1]+"@2x.png")
        self.Danish = pygame.image.load(cookies[2]+"@2x.png")
        self.Donut = pygame.image.load(cookies[3]+"@2x.png")
        self.Macaroon = pygame.image.load(cookies[4]+"@2x.png")
        self.SugarCookies = pygame.image.load(cookies[5]+"@2x.png")
        return

    def suffle(self):
        self.tilemap = [[cookies[random.randint(0,5)] \
             for e in range(self.XBLOCK)] \
             for e in range(self.YBLOCK)]
        #print(self.tilemap)
        return

    def tilemap_2_number(self):
        self.tilemap_N = [[0 for e in range(self.XBLOCK)] \
             for e in range(self.YBLOCK)]
        for i in range(self.XBLOCK):
            for j in range(self.YBLOCK):
                self.tilemap_N[i][j] = self.dic_N[self.tilemap[i][j]]                
        #print(self.tilemap_N)
        return

    def check_chain(self,map_N):
        #print(map_N)
        #print(map_N[3])
        #print(''.join(map_N[3]))
        #print(''.join(map_N[3]).find('444'))

        chain=''.join(map_N[3]).find('444')
        if chain != -1:
            self.score += 60
            for i in range(3):
                self.tilemap[3][chain+i]=cookies[random.randint(0,5)]#"Tile"
        return

    def swap(self, event):
        pg_end_x = self.TILE_LEFT_X+self.BLOCK_WD*self.XBLOCK 
        pg_end_y = self.TILE_LEFT_Y+self.BLOCK_HT*self.YBLOCK
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:            
            mouse_pos = pygame.mouse.get_pos()
            self.mouse_drag = True
            if ((mouse_pos[0] >= self.TILE_LEFT_X and mouse_pos[0] <= pg_end_x) and
                   (mouse_pos[1] >= self.TILE_LEFT_Y and mouse_pos[1] <= pg_end_y)):
                self.cur_tile_x = (int)((mouse_pos[0]-self.TILE_LEFT_X)/self.BLOCK_WD)
                self.cur_tile_y = (int)((mouse_pos[1]-self.TILE_LEFT_Y)/self.BLOCK_HT)
                #print("cur=(",self.cur_tile_x,self.cur_tile_y,")")

        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:                          
            mouse_pos = pygame.mouse.get_pos()
            if ((mouse_pos[0] >= self.TILE_LEFT_X and mouse_pos[0] <= pg_end_x) and
                   (mouse_pos[1] >= self.TILE_LEFT_Y and mouse_pos[1] <= pg_end_y)):
                self.up_tile_x = (int)((mouse_pos[0]-self.TILE_LEFT_X)/self.BLOCK_WD)
                self.up_tile_y = (int)((mouse_pos[1]-self.TILE_LEFT_Y)/self.BLOCK_HT)
                #print(" up=(",self.up_tile_x,self.up_tile_y,")")
                #[과제 2: 맞교환]
                if(self.mouse_drag == True):
                    temp = self.tilemap[self.up_tile_x][self.up_tile_y]
                    self.tilemap[self.up_tile_x][self.up_tile_y]=self.tilemap[self.cur_tile_x][self.cur_tile_y]
                    self.tilemap[self.cur_tile_x][self.cur_tile_y] = temp
                    self.mouse_drag = False
       
        if event.type == pygame.MOUSEMOTION and self.mouse_drag == True:
            mouse_pos = pygame.mouse.get_pos()
            if ((mouse_pos[0] >= self.TILE_LEFT_X and mouse_pos[0] <= pg_end_x) and
                   (mouse_pos[1] >= self.TILE_LEFT_Y and mouse_pos[1] <= pg_end_y)):
                tmp_tile_x = (int)((mouse_pos[0]-self.TILE_LEFT_X)/self.BLOCK_WD)
                tmp_tile_y = (int)((mouse_pos[1]-self.TILE_LEFT_Y)/self.BLOCK_HT)
                #[과제 1:이동 제한을 위한 if 문 추가]
                self.screen.blit(self.dic[self.tilemap[self.cur_tile_x][self.cur_tile_y]],
                (mouse_pos[0]-self.BLOCK_WD/2, mouse_pos[1]-self.BLOCK_HT/2)) 

        return                        

    def run(self):
        play_speed = pygame.time.Clock()

        while 1:#무한 루프
            for event in pygame.event.get():#이벤트 처리
                if event.type == pygame.QUIT:                   
                    sys.exit()
                if event.type == pygame.USEREVENT and self.gameover == 0:    
                    self.screen.blit(
                        self.default_font.render(
                            "Score: "+str(self.score),
                            True,
                            (64,64,64),(195,223,255)),
                            (280,self.TILE_LEFT_X))
                    self.screen.blit(
                        self.default_font.render(
                            "Time: "+str(self.counter/10),
                            True,
                            (64,64,64),(195,223,255)),
                            (40,self.TILE_LEFT_X))                            
                    self.counter -= 10
                    if self.counter == 0:
                        self.gameover = 1
                            
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.score = 0
                        self.gameover = 0
                        self.init_game()                        

            if self.gameover:
                self.screen.blit(
                    self.default_font.render(
                        "Game Over! Your score: %d" % self.score,
                        True,
                        (64,64,64),(195,223,255)),
                        (60,self.height//2))

                self.screen.blit(
                    self.default_font.render(
                        "Press space to continue",
                        True,
                        (64,64,64),(195,223,255)),
                        (80,self.height//2+40))                                
            else:    
                for i in range(self.XBLOCK):
                    for j in range(self.YBLOCK):
                        self.screen.blit(self.Tile,(self.TILE_LEFT_X+i*self.BLOCK_WD,\
                            self.TILE_LEFT_Y+j*self.BLOCK_HT))
                        self.screen.blit(self.dic[self.tilemap[i][j]],\
                            (self.TILE_LEFT_X+i*self.BLOCK_WD,\
                            self.TILE_LEFT_Y+j*self.BLOCK_HT))
                       
            self.swap(event)
            self.tilemap_2_number()
            self.check_chain(self.tilemap_N) 
            self.check_chain(list(map(list, zip(*self.tilemap_N))))                      

            pygame.display.update()#화면 갱신
            play_speed.tick(60)

if __name__ == '__main__':
    App = CandyCrush()#CandyCrush 클래스의 객체 생성
    App.run()
