import pygame
from pygame.locals import *
playernum=1

line1=[1,'-','-','-','-','-','-','-','-','-','-']
line2=[2,'-','-','-','-','-','-','-','-','-','-']
line3=[3,'-','-','-','-','-','-','-','-','-','-']
line4=[4,'-','-','-','-','-','-','-','-','-','-']
line5=[5,'-','-',0,0,'-','-',0,0,'-','-']
line6=[6,'-','-',0,0,'-','-',0,0,'-','-']
line7=[7,'-','-','-','-','-','-','-','-','-','-']
line8=[8,'-','-','-','-','-','-','-','-','-','-']
line9=[9,'-','-','-','-','-','-','-','-','-','-']
line10=[10,'-','-','-','-','-','-','-','-','-','-']
lines=[line1,line2,line3,line4,line5,line6,line7,line8,line9,line10]
move='-'
recap=''
attackrecap=True
class piece():
    '''generic class for all pieces'''
    def __init__(self,name,strength,speed,line,spot,player):
        self.name=name
        self.strength=strength
        self.speed=speed
        self.line=line
        self.spot=spot
        self.player=player
    def attack(self,enemy):
        global recap
        global attackrecap
        if self.player==enemy.player:
            print('You cant attack yourself')
            self.move
        if enemy.name=='bomb' and self.name=='miner':
            enemy.strength-=20
        if enemy.name=='marshall' and self.name=='spy':
            enemy.strength-=20
        if self.strength>=enemy.strength:
            attackrecap=True
            if enemy.name=='flag':
                print('you captured the flag and won the game')
                return
            victory=font.render(f'You win. your {self.name} defeated a {enemy.name}',True,blue)
            screen.blit(victory,(25,65))
            pygame.display.update()
            pygame.time.wait(750)
            recap=f'You lost. your {enemy.name} was defeated by a {self.name}'
            for i in lines:
                if i[0]==self.line:
                    i[self.spot]='-'
            self.line=enemy.line
            self.spot=enemy.spot
            enemy.line=0
            enemy.spot=0
            self.location()
        if self.strength<enemy.strength:
            attackrecap=True
            loss=font.render(f'you lost. Your {self.name} was defeated by a {enemy.name}',True,blue)
            screen.blit(loss,(25,65))
            pygame.display.update()
            pygame.time.wait(750)
            recap=f'You won. Your {enemy.name} defeated a {self.name}'
            for i in lines:
                if (self.line)==i[0]:
                    i[self.spot]='-'
                    self.spot=0
                    self.line=0
    def row_column(self):
        global row
        global column
        global recap
        recap=''
        selrow=font.render(f'Select row of {self.name}',True,blue)
        screen.blit(selrow,(25,25))
        pygame.display.update()
        running=True
        ro=''
        while running:
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN and len(ro)==0:
                    ro=pygame.key.name(event.key)
                if event.type==pygame.QUIT:
                    running=False
                    
                n=font.render(ro,True,blue)
                screen.blit(n,(300,25))
                pygame.display.update()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        if len(ro)==1 and ro.isnumeric()==True:
                            row=int(ro)
                            running=False
        selcol=font.render(f'Select column of {self.name}',True,blue)
        screen.blit(selcol,(350,25))
        pygame.display.update()
        running=True
        ro=''
        while running:
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN and len(ro)==0:
                    ro=pygame.key.name(event.key)
                if event.type==pygame.QUIT:
                    running=False
                    
                n=font.render(ro,True,blue)
                screen.blit(n,(625,25))
                pygame.display.update()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        if len(ro)==1 and ro.isnumeric()==True:
                            column=int(ro)
                            running=False
        turn_board()


    def move(self):
        attackrecap=False
        if self.name=='bomb':
            print('bombs cant move')
            piece_select()
        if self.name=='flag':
            print('the flag cant move')
            piece_select()
        if 1==1:
            turn_board()
            move=font.render('move or press x to select a different piece',True,blue)
            screen.blit(move,(25,25))
            running=True
            ro=''
            while running:
                for event in pygame.event.get():
                    if event.type==pygame.KEYDOWN and len(ro)==0:
                        ro=pygame.key.name(event.key)
                    if event.type==pygame.QUIT:
                        running=False
                        
                    n=font.render(ro,True,blue)
                    screen.blit(n,(625,25))
                    pygame.display.update()
                    if event.type==pygame.KEYDOWN:
                        if event.key==pygame.K_RETURN:
                            if len(ro)==1:
                                move=str(ro)
                                running=False
        if move=='x':
            turn_board()
            select_piece()
        if move=='s':
            for i in lines:
                if (self.line+1)==i[0]:
                    if i[self.spot]=='-':
                        print('no one is there')
                        i[self.spot]=self.strength
                        for x in lines:
                          if x[0]==self.line:
                            x[self.spot]='-'
                            self.line+=1
                            return
                    elif i[self.spot]==0:
                        print('that is the lake')
                        self.move()
                    else:
                        print('That is an enemy')
                        for x in piecesall:
                            if x.line==i[0] and x.spot==self.spot:
                                self.attack(x)
        if move=='w':
            for i in lines:
                if (self.line-1)==i[0]:
                    if i[self.spot]=='-':
                        print('no one is there')
                        i[self.spot]=self.strength
                        n=i[0]+1
                        for x in lines:
                          if x[0]==n:
                            x[self.spot]='-'
                            self.line-=1
                            return
                    elif i[self.spot]==0:
                        print('that is the lake')
                        self.move()
                    else:
                        n=i[0]+1
                        print('That is an enemy')
                        for x in piecesall:
                            if x.line==i[0] and x.spot==self.spot:
                                self.attack(x)
        if move=='a':
            for i in lines:
                if (self.line)==i[0]:
                    if i[self.spot-1]=='-':
                        print('no one is there')
                        i[self.spot]='-'
                        self.spot-=1
                        i[self.spot]=self.strength
                    elif i[self.spot-1]==0:
                        print('that is a lake')
                        self.move()
                    else:
                        print('That is an enemy')
                        for x in piecesall:
                            n=self.spot-1
                            if x.line==self.line and x.spot==n:
                                self.attack(x)
        if move=='d':
            for i in lines:
                if (self.line)==i[0]:
                    if i[self.spot+1]=='-':
                        print('no one is there')
                        i[self.spot]='-'
                        self.spot+=1
                        i[self.spot]=self.strength
                    elif i[self.spot+1]==0:
                        print('that is a lake')
                        self.move()
                    else:
                        print('That is an enemy')
                        for x in piecesall:
                            n=self.spot+1
                            if x.line==self.line and x.spot==n:
                                self.attack(x)
        turn_board()



        pygame.display.update()
        
    def location(self):
        for i in lines:
            if self.line==i[0]:
                i[self.spot]=self.strength
    def select_loc(self):
        global column
        self.row_column()
        if playernum==1 and row<7:
            print('you must put your pieces in the bottom four rows')
            self.select_loc()
        if playernum==2 and row>4:
            print('you must put your pieces in the bottom four rows')
            self.select_loc()
        self.line=row
        column=int(column)
        self.spot=column
        for i in lines:
            if i[0]==row:
                if i[column]!='-':
                    print('that space is filled')
                    self.select_loc()


def board():
    screen.fill((255,255,255))
    for i in range(11):
        pygame.draw.line(screen,blue,(100+50*i,100),(100+50*i,600))
        pygame.draw.line(screen,blue,(100,100+50*i),(600,100+50*i))
    z=0
    
    for line in lines:
        n=0
        for i in line:
            linetxt=font.render(str(i),True,blue)
            screen.blit(linetxt,(65+50*n,120+50*z))
            n+=1
        z+=1
        pygame.display.update()
def turn_board():
    global playernum
    if playernum>=3:
        playernum=2
    if playernum<=0:
        playernum=1
    screen.fill((255,255,255))
    for i in range(11):
        pygame.draw.line(screen,blue,(100+50*i,100),(100+50*i,600))
        pygame.draw.line(screen,blue,(100,100+50*i),(600,100+50*i))
    n=0
    z=0
    for L in lines:
        linelist=[]
        Spot=-1
        for i in L:
            strung=str(i)
            Spot+=1
            if strung=='0' or strung=='-':
                linelist.append(strung)
            else:
                for i in piecesall:
                    if i.line==L[0]:
                        if i.spot==Spot:
                            if i.player==playernum:
                                linelist.append(strung)
                            else:
                                linelist.append('X')
        n=0
        for i in linelist:
            linetxt=font.render(str(i),True,blue)
            screen.blit(linetxt,(115+50*n,120+50*z))
            n+=1
        z+=1
    pygame.display.update()



def board_create():
    global playernum
    if playernum==1:
        for i in pieces1:
            i.select_loc()
            i.location()
            turn_board()
        playernum+=1
        turn_board()
        if playernum==2:
            for i in pieces2:
                i.select_loc()
                i.location()
                turn_board()
        playernum-=1
        turn_board()




class scout(piece):
    def __init__(self,name,strength,speed,line,spot,player):
        piece.__init__(self,name,strength,speed,line,spot,player)
    def move(self):
        fail=0
        move=input('move')
        if move=='w':
            jumped=input('what spot do you want to jump to')
            jumped=int(jumped)
            for i in lines:
                if i[0]==self.line:
                    for z in range(jumped):
                        if i[self.spot+z-jumped]!='-':
                            print("you cant jump through pieces/lakes")
                            fail+=1
                    if fail==0:
                        i[self.spot]='-'
                        self.line-=jumped
                        for x in lines:
                            if self.line==x[0]:
                                x[self.spot]=self.name
                    else:
                        self.jump()
        if move=='s':
            jumped=input('what spot do you want to jump to')
            jumped=int(jumped)
            for i in lines:
                if i[0]==self.line:
                    for z in range(jumped):
                        if i[self.spot-z+jumped]!='-':
                            print("you cant jump through pieces/lakes")
                            fail+=1
                    if fail==0:
                        i[self.spot]='-'
                        self.line+=jumped
                        for x in lines:
                            if self.line==x[0]:
                                x[self.spot]=self.name
                    else:
                        self.jump()
def select_piece():
    global playernum
    row_columngen()
    for i in lines:
        if row==i[0]:
            if i[column]=='-' or i[column]=='0' or i[column]=='X':
                print('not a piece')
                notpiece=font.render('that is not a piece',True,blue)
                screen.blit(notpiece,(25,65))
                pygame.display.update()
                pygame.time.wait(750)
                turn_board()
                select_piece()
    if playernum==1:
        for n in pieces1:
            if n.line==row and n.spot==column:
                selected=font.render(f'You have selected the {n.name} on {column},{row}',True,blue)
                turn_board()
                screen.blit(selected,(25,25))
                pygame.display.update()
                pygame.time.wait(1000)
                n.move()
                turn_board()
                playernum+=1
    if playernum==2:
        for n in pieces2:
            if n.line==row and n.spot==column:
                selected=font.render(f'You have selected the {n.name} on {column},{row}',True,blue)
                turn_board()
                screen.blit(selected,(25,25))
                pygame.display.update()
                pygame.time.wait(1000)
                n.move()
                turn_board()
                playernum-=1

'''begin piece def'''
marshall=piece('marshall',10,1,0,0,1)
general=piece('general',9,1,0,0,1)
colonel1=piece('colonel',8,1,0,0,1)
colonel2=piece('colonel',8,1,0,0,1)
major1=piece('major',7,1,0,0,1)
major2=piece('major',7,1,0,0,1)
major3=piece('major',7,1,0,0,1)
captain1=piece('captain',6,1,0,0,1)
captain2=piece('captain',6,1,0,0,1)
captain3=piece('captain',6,1,0,0,1)
captain4=piece('captain',6,1,0,0,1)
lieutenant1=piece('lieutenant',5,1,0,0,1)
lieutenant2=piece('lieutenant',5,1,0,0,1)
lieutenant3=piece('lieutenant',5,1,0,0,1)
lieutenant4=piece('lieutenant',5,1,0,0,1)
sergeant1=piece('sergeant',4,1,0,0,1)
sergeant2=piece('sergeant',4,1,0,0,1)
sergeant3=piece('sergeant',4,1,0,0,1)
sergeant4=piece('sergeant',4,1,0,0,1)
miner1=piece('miner',3,1,0,0,1)
miner2=piece('miner',3,1,0,0,1)
miner3=piece('miner',3,1,0,0,1)
miner4=piece('miner',3,1,0,0,1)
miner5=piece('miner',3,1,0,0,1)
scout1=scout('scout',2,1,0,0,1)
scout2=scout('scout',2,1,0,0,1)
scout3=scout('scout',2,1,0,0,1)
scout4=scout('scout',2,1,0,0,1)
scout5=scout('scout',2,1,0,0,1)
scout6=scout('scout',2,1,0,0,1)
scout7=scout('scout',2,1,0,0,1)
scout8=scout('scout',2,1,0,0,1)
bomb1=piece('bomb',20,1,0,0,1)
bomb2=piece('bomb',20,1,0,0,1)
bomb3=piece('bomb',20,1,0,0,1)
bomb4=piece('bomb',20,1,0,0,1)
bomb5=piece('bomb',20,1,0,0,1)
flag=piece('flag',0,1,0,0,1)
spy=piece('spy',1,1,0,0,1)
'''end piece def'''

"""PLAYER 2 PIECES"""
xmarshall=piece('marshall',10,1,0,0,2)
xgeneral=piece('general',9,1,0,0,2)
xcolonel1=piece('colonel',8,1,0,0,2)
xcolonel2=piece('colonel',8,1,0,0,2)
xmajor1=piece('major',7,1,0,0,2)
xmajor2=piece('major',7,1,0,0,2)
xmajor3=piece('major',7,1,0,0,2)
xcaptain1=piece('captain',6,1,0,0,2)
xcaptain2=piece('captain',6,1,0,0,2)
xcaptain3=piece('captain',6,1,0,0,2)
xcaptain4=piece('captain',6,1,0,0,2)
xlieutenant1=piece('lieutenant',5,1,0,0,2)
xlieutenant2=piece('lieutenant',5,1,0,0,2)
xlieutenant3=piece('lieutenant',5,1,0,0,2)
xlieutenant4=piece('lieutenant',5,1,0,0,2)
xsergeant1=piece('sergeant',4,1,0,0,2)
xsergeant2=piece('sergeant',4,1,0,0,2)
xsergeant3=piece('sergeant',4,1,0,0,2)
xsergeant4=piece('sergeant',4,1,0,0,2)
xminer1=piece('miner',3,1,0,0,2)
xminer2=piece('miner',3,1,0,0,2)
xminer3=piece('miner',3,1,0,0,2)
xminer4=piece('miner',3,1,0,0,2)
xminer5=piece('miner',3,1,0,0,2)
xscout1=scout('scout',2,1,0,0,2)
xscout2=scout('scout',2,1,0,0,2)
xscout3=scout('scout',2,1,0,0,2)
xscout4=scout('scout',2,1,0,0,2)
xscout5=scout('scout',2,1,0,0,2)
xscout6=scout('scout',2,1,0,0,2)
xscout7=scout('scout',2,1,0,0,2)
xscout8=scout('scout',2,1,0,0,2)
xbomb1=piece('bomb',20,1,0,0,2)
xbomb2=piece('bomb',20,1,0,0,2)
xbomb3=piece('bomb',20,1,0,0,2)
xbomb4=piece('bomb',20,1,0,0,2)
xbomb5=piece('bomb',20,1,0,0,2)
xflag=piece('flag',0,1,0,0,2)
xspy=piece('spy',1,1,0,0,2)
#pieces1=[marshall,general,colonel1,colonel2,major1,major2,major3,captain1,captain2,captain3,captain4,lieutenant1,lieutenant2,lieutenant3,lieutenant4,sergeant1,sergeant2,sergeant3,sergeant4,miner1,miner2,miner3,miner4,miner5,scout1,scout2,scout3,scout4,scout5,scout6,scout7,scout8,bomb1,bomb2,bomb3,bomb4,bomb5,flag,spy]
#pieces2=[xmarshall,xgeneral,xcolonel1,xcolonel2,xmajor1,xmajor2,xmajor3,xcaptain1,xcaptain2,xcaptain3,xcaptain4,xlieutenant1,xlieutenant2,xlieutenant3,xlieutenant4,xsergeant1,xsergeant2,xsergeant3,xsergeant4,xminer1,xminer2,xminer3,xminer4,xminer5,xscout1,xscout2,xscout3,xscout4,xscout5,xscout6,xscout7,xscout8,xbomb1,xbomb2,xbomb3,xbomb4,xbomb5,xflag,xspy]
piecesall=[marshall,general,colonel1,colonel2,major1,major2,major3,captain1,captain2,captain3,captain4,lieutenant1,lieutenant2,lieutenant3,lieutenant4,sergeant1,sergeant2,sergeant3,sergeant4,miner1,miner2,miner3,miner4,miner5,scout1,scout2,scout3,scout4,scout5,scout6,scout7,scout8,bomb1,bomb2,bomb3,bomb4,bomb5,flag,spy,xmarshall,xgeneral,xcolonel1,xcolonel2,xmajor1,xmajor2,xmajor3,xcaptain1,xcaptain2,xcaptain3,xcaptain4,xlieutenant1,xlieutenant2,xlieutenant3,xlieutenant4,xsergeant1,xsergeant2,xsergeant3,xsergeant4,xminer1,xminer2,xminer3,xminer4,xminer5,xscout1,xscout2,xscout3,xscout4,xscout5,xscout6,xscout7,xscout8,xbomb1,xbomb2,xbomb3,xbomb4,xbomb5,xflag,xspy]


pieces1=[marshall,general]
pieces2=[xmarshall,xgeneral]

"""pygame code below here"""
pygame.init()
screen=pygame.display.set_mode((800,700))
"""colors"""
blue=(0,0,255)
red=(255,0,0)
green=(0,255,0)
font=pygame.font.SysFont('comisansms',30)
def main_loop():
    global playernum
    global attackrecap
    global recap
    running=True
    screen.fill((255,255,255))
    while running:
        for event in pygame.event.get():
            if event.type==QUIT:
                running=False
            if event.type==pygame.KEYDOWN:
                n=pygame.key.name(event.key)
        for i in range(11):
            pygame.draw.line(screen,blue,(100+50*i,100),(100+50*i,600))
            pygame.draw.line(screen,blue,(100,100+50*i),(600,100+50*i))
        z=0
        
        for line in lines:
            n=0
            for i in line:
                linetxt=font.render(str(i),True,blue)
                screen.blit(linetxt,(65+50*n,120+50*z))
                n+=1
            z+=1
        board_create()
        while True:
            select_piece()
            change=True
            #pygame.time.wait(1000)
            while change==True:
                screen.fill((255,255,255))
                playerchange=font.render('Change the player. press enter to continue',True,blue)
                screen.blit(playerchange,(25,25))
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type==pygame.KEYDOWN:
                        if event.key==K_RETURN:
                            change=False
            turn_board()
            if attackrecap==True:
                rec=font.render(recap,True,blue)
                screen.blit(rec,(25,65))
                pygame.display.update()
                pygame.time.wait(750)
            if playernum>=3:
                playernum=2
            if playernum<=0:
                playernum=1
def row_columngen():
        global row
        global column
        selrow=font.render(f'Select row of piece',True,blue)
        screen.blit(selrow,(25,25))
        pygame.display.update()
        running=True
        ro=''
        while running:
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN and len(ro)==0:
                    ro=pygame.key.name(event.key)
                if event.type==pygame.QUIT:
                    running=False
                    
                n=font.render(ro,True,blue)
                screen.blit(n,(300,25))
                pygame.display.update()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        if len(ro)==1 and ro.isnumeric()==True:
                            row=int(ro)
                            running=False
        selcol=font.render(f'Select column of piece',True,blue)
        screen.blit(selcol,(350,25))
        pygame.display.update()
        running=True
        ro=''
        while running:
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN and len(ro)==0:
                    ro=pygame.key.name(event.key)
                if event.type==pygame.QUIT:
                    running=False
                    
                n=font.render(ro,True,blue)
                screen.blit(n,(625,25))
                pygame.display.update()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        if len(ro)==1 and ro.isnumeric()==True:
                            column=int(ro)
                            running=False
        
main_loop()