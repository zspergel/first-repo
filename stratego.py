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
#all the lines named with the lakes
move='-'
recap=''
attackrecap=True
class piece():
    '''generic class for all pieces'''
    def __init__(self,name,strength,speed,line,spot,player):
        '''intits all variables for class'''
        self.name=name
        self.strength=strength
        self.speed=speed
        self.line=line
        self.spot=spot
        self.player=player
        #initiates all the variables for the class
    def attack(self,enemy):
        '''attacks a piece that has been moved into'''
        global recap
        global attackrecap
        if self.player==enemy.player:
            selfattack=font.render('You cant attack yourself',True,blue)
            screen.blit(selfattack,(25,65))
            pygame.display.update()
            pygame.time.wait(600)
            self.move()
            #if the piece moved into is form the same player. prints it on board
            #then updates and waits .6s
        elif enemy.name=='bomb' and self.name=='miner':
            enemy.strength-=20
        #if the enemy is the bomb reduces its strenth so miner will win
        elif enemy.name=='marshall' and self.name=='spy':
            enemy.strength-=20
        #dito for above just with marhsall and spy
        elif self.strength>=enemy.strength:
            attackrecap=True
            if enemy.name=='flag':
                screen.fill((255,255,255))
                win=font.render('you captured the flag and won the game',True,green)
                screen.blit(win,(200,200))
                pygame.display.update()
                #blits winning message to screen
                running=True
                while running:
                    for event in pygame.event.get():
                        if event.type==pygame.QUIT:
                            running=False
                            pygame.quit()
                            quit()
                    #allows you to exit code
            victory=font.render(f'You win. your {self.name} defeated a {enemy.name}',True,blue)
            screen.blit(victory,(25,65))
            pygame.display.update()
            pygame.time.wait(750)
            #if it is isn't the flag print that you won and the name of the piece you defeated
            recap=f'You lost. your {enemy.name} was defeated by a {self.name}'
            #recap for other persons turn
            for i in lines:
                if i[0]==self.line:
                    i[self.spot]='-'
            #makes your old spot a dash
            self.line=enemy.line
            self.spot=enemy.spot
            #moves you into your enemies spot
            enemy.line=0
            enemy.spot=0
            self.location()
        elif self.strength<enemy.strength:
            attackrecap=True
            loss=font.render(f'you lost. Your {self.name} was defeated by a {enemy.name}',True,blue)
            screen.blit(loss,(25,65))
            pygame.display.update()
            pygame.time.wait(750)
            #blits loss text to screen
            recap=f'You won. Your {enemy.name} defeated a {self.name}'
            for i in lines:
                if (self.line)==i[0]:
                    i[self.spot]='-'
                    self.spot=0
                    self.line=0
    def row_column(self):
        '''get user input for row and column'''
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
                if event.type==pygame.KEYDOWN and len(ro)<2:
                    if str(pygame.key.name(event.key)).isnumeric()==True:
                        ro+=pygame.key.name(event.key)
                        #adds the keys that is typed to string ro assuming the typed is a number
                if event.type==pygame.QUIT:
                    running=False
                    
                n=font.render(ro,True,blue)
                screen.blit(n,(300,25))
                pygame.display.update()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN and ro.isnumeric()==True:
                        row=int(ro)
                        running=False
                #when enter is pressed exits section
        if row>10:
            toobig=font.render('You cant select a row greater than 10',True,blue)
            screen.blit(toobig,(25,65))
            pygame.display.update()
            pygame.time.wait(600)
            turn_board()
            row_columngen()
            return
            #if the typed is bigger than 10 reruns piece selection
        selcol=font.render(f'Select column of {self.name}',True,blue)
        screen.blit(selcol,(350,25))
        pygame.display.update()
        running=True
        ro=''
        while running:
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN and len(ro)<2:
                    if str(pygame.key.name(event.key)).isnumeric()==True:
                        ro+=pygame.key.name(event.key)
                if event.type==pygame.QUIT:
                    running=False
                    
                n=font.render(ro,True,blue)
                screen.blit(n,(625,25))
                pygame.display.update()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN and ro.isnumeric()==True:
                        column=int(ro)
                        running=False
        if column>10:
            toobig=font.render('You cant select a column greater than 10',True,blue)
            screen.blit(toobig,(25,65))
            pygame.display.update()
            pygame.time.wait(600)
            turn_board()
            row_columngen()
            return
        #same as above but for the column
        turn_board()
        #reprints the board

    def move(self):
        '''lets player move'''
        attackrecap=False
        if self.name=='bomb':
            bombtxt=font.render('bombs cant move',True,blue)
            screen.blit(bombtxt,(475,25))
            pygame.display.update()
            pygame.time.wait(600)
            turn_board()
            select_piece()
            #if you select the bomb reruns selection
        if self.name=='flag':
            flagtxt=font.render('the flag cant move',True,blue)
            screen.blit(flagtxt,(475,25))
            pygame.display.update()
            pygame.time.wait(600)
            turn_board()
            select_piece()
            #same as above but for flag
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
                        if event.key==pygame.K_RETURN and ro.isnumeric()==True:
                            if len(ro)==1:
                                move=str(ro)
                                running=False
        #gets the users input and returns it as a string called move
        if move!='x' and move!='s' and move!='w' and move!='a' and move!='d':
            notmove=font.render('that is not W,A,S,D, or X. Only those are keys.',True,blue)
            screen.blit(notmove,(25,65))
            pygame.display.update()
            pygame.time.wait(600)
            self.move()
            #if the pressed key is not w,a,s,d, or x reruns the move function
        elif move=='x':
            turn_board()
            select_piece()
            #if x is pressed lets yous select new piece
        elif move=='s':
            for i in lines:
                if (self.line+1)==i[0]:
                    if i[self.spot]=='-':
                        i[self.spot]=self.strength
                        if self.name=='flag':
                            i[self.spot]='F'
                        elif self.name=='bomb':
                            i[self.spot]='B'
                        elif self.name=='spy':
                            i[self.spot]='S'
                        # prints out the correct letter for special pieces
                        for x in lines:
                          if x[0]==self.line:
                            x[self.spot]='-'
                            self.line+=1
                            return
                            #if the spot is empty moves piece
                    elif i[self.spot]==0:
                        laketxt=font.render('that is the lake',True,blue)
                        screen.blit(laketxt,(25,65))
                        pygame.display.update()
                        pygame.time.wait(600)
                        self.move()
                        #if tries to mvoe intot e lakes tells user and reruns move code
                    else:
                        for x in piecesall:
                            if x.line==i[0] and x.spot==self.spot:
                                self.attack(x)
                                #if none of the others is true attacks the piece
        elif move=='w':
            #next three scetions are all the same ust different directions
            for i in lines:
                if (self.line-1)==i[0]:
                    if i[self.spot]=='-':
                        print('no one is there')
                        i[self.spot]=self.strength
                        if self.name=='flag':
                            i[self.spot]='F'
                        elif self.name=='bomb':
                            i[self.spot]='B'
                        elif self.name=='spy':
                            i[self.spot]='S'
                        n=i[0]+1
                        for x in lines:
                          if x[0]==n:
                            x[self.spot]='-'
                            self.line-=1
                            return
                    elif i[self.spot]==0:
                        laketxt=font.render('that is the lake',True,blue)
                        screen.blit(laketxt,(25,65))
                        pygame.display.update()
                        pygame.time.wait(600)                        
                        self.move()
                    else:
                        n=i[0]+1
                        for x in piecesall:
                            if x.line==i[0] and x.spot==self.spot:
                                self.attack(x)
        elif move=='a':
            for i in lines:
                if (self.line)==i[0]:
                    if i[self.spot-1]=='-':
                        i[self.spot]='-'
                        self.spot-=1
                        i[self.spot]=self.strength
                        if self.name=='flag':
                            i[self.spot]='F'
                        elif self.name=='bomb':
                            i[self.spot]='B'
                        elif self.name=='spy':
                            i[self.spot]='S'
                    elif i[self.spot-1]==0:
                        laketxt=font.render('that is the lake',True,blue)
                        screen.blit(laketxt,(25,65))
                        pygame.display.update()
                        pygame.time.wait(600)
                        self.move()
                    else:
                        for x in piecesall:
                            n=self.spot-1
                            if x.line==self.line and x.spot==n:
                                self.attack(x)
        elif move=='d':
            for i in lines:
                if (self.line)==i[0]:
                    if i[self.spot+1]=='-':
                        i[self.spot]='-'
                        self.spot+=1
                        i[self.spot]=self.strength
                        if self.name=='flag':
                            i[self.spot]='F'
                        elif self.name=='bomb':
                            i[self.spot]='B'
                        elif self.name=='spy':
                            i[self.spot]='S'
                    elif i[self.spot+1]==0:
                        laketxt=font.render('that is the lake',True,blue)
                        screen.blit(laketxt,(25,65))
                        pygame.display.update()
                        pygame.time.wait(600)
                        self.move()
                    else:
                        for x in piecesall:
                            n=self.spot+1
                            if x.line==self.line and x.spot==n:
                                self.attack(x)
        turn_board()



        pygame.display.update()
        
    def location(self):
        '''puts the piece onto the board'''
        for i in lines:
            if self.line==i[0]:
                i[self.spot]=self.strength
                if self.name=='flag':
                    i[self.spot]='F'
                elif self.name=='bomb':
                    i[self.spot]='B'
                elif self.name=='spy':
                    i[self.spot]='S'
    #locates each piece and puts it onto board
    def select_loc(self):
        '''lets the player put the pieces onto the board'''
        global column
        self.row_column()
        if playernum==1 and row<7:
            botfour=font.render('you must put your pieces in the bottom four rows',True,blue)
            screen.blit(botfour,(25,65))
            pygame.display.update()
            pygame.time.wait(600)
            self.select_loc()
            #players can only put pieces in their first four rows
            #this and next group check for that
        if playernum==2 and row>4:
            topfour=font.render('you must put your pieces in the bottom four rows',True,blue)
            screen.blit(topfour(25,65))
            pygame.display.update()
            pygame.time.wait(600)
            self.select_loc()
        self.line=row
        column=int(column)
        self.spot=column
        for i in lines:
            if i[0]==row:
                if i[column]!='-':
                    filled=font.render('that space is filled',True,blue)
                    screen.blit(filled,(25,65))
                    pygame.display.update()
                    pygame.time.wait(600)
                    self.select_loc()
                    #if their is already a piece tells player and reruns code


def turn_board():
    '''puts the board on the screen with hidden pieces based on turns'''
    global playernum
    if playernum>=3:
        playernum=2
    if playernum<=0:
        playernum=1
    #error checks the player number
    screen.fill((255,255,255))
    for i in range(11):
        pygame.draw.line(screen,blue,(100+50*i,150),(100+50*i,650))
        pygame.draw.line(screen,blue,(100,150+50*i),(600,150+50*i))
    #puts lines onto screen
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
                #if the item is the lake or a dash puts onto new list
            else:
                for i in piecesall:
                    if i.line==L[0]:
                        if i.spot==Spot:
                            if i.player==playernum:
                                linelist.append(strung)
                            else:
                                linelist.append('X')
                                #checks to find them item i piecesall
                                #then if the player number is the same puts its strength otherwise puts an X
        n=0
        for i in linelist:
            linetxt=font.render(str(i),True,blue)
            screen.blit(linetxt,(115+50*n,170+50*z))
            n+=1
            #puts each line of pieces onto screen
        z+=1
        num=[1,2,3,4,5,6,7,8,9,10]
        for i in num:
            number=font.render(str(i),True,blue)
            screen.blit(number,(65+50*i,120))
        for n in num:
            number=font.render(str(n),True,blue)
            screen.blit(number,(65,120+50*n))
        #puts the row and column markers onto screen
    pygame.display.update()



def board_create():
    '''creates the board with player selecting piece locations'''
    global playernum
    if playernum==1:
        for i in pieces1:
            i.select_loc()
            i.location()
            turn_board()
            #for each piece gets the user location
            #puts the piece on board
            #prints the board onto the screen
        playernum+=1
        turn_board()
        if playernum==2:
            for i in pieces2:
                i.select_loc()
                i.location()
                turn_board()
        #process is repeated
        playernum-=1
        turn_board()





def select_piece():
    '''selects the location for piece to attack'''
    global playernum
    row_columngen()
    for i in lines:
        if row==i[0]:
            if i[column]=='x':
                print('solved')
            if i[column]=='-' or i[column]==0 or i[column]=='X':
                notpiece=font.render('that is not a piece',True,blue)
                screen.blit(notpiece,(25,65))
                pygame.display.update()
                pygame.time.wait(750)
                turn_board()
                select_piece()
                #if the selected piece is not a piece then tells player
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
                #finds the name of piece and tells player
                #then mlets the player move the piece and prints new board
    elif playernum==2:
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
                #same as above
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
scout1=piece('scout',2,1,0,0,1)
scout2=piece('scout',2,1,0,0,1)
scout3=piece('scout',2,1,0,0,1)
scout4=piece('scout',2,1,0,0,1)
scout5=piece('scout',2,1,0,0,1)
scout6=piece('scout',2,1,0,0,1)
scout7=piece('scout',2,1,0,0,1)
scout8=piece('scout',2,1,0,0,1)
bomb1=piece('bomb',20,1,0,0,1)
bomb2=piece('bomb',20,1,0,0,1)
bomb3=piece('bomb',20,1,0,0,1)
bomb4=piece('bomb',20,1,0,0,1)
bomb5=piece('bomb',20,1,0,0,1)
flag=piece('flag',0,1,0,0,1)
spy=piece('spy',1,1,0,0,1)
'''end piece def'''
#######list of all teh peices in the game
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
xscout1=piece('scout',2,1,0,0,2)
xscout2=piece('scout',2,1,0,0,2)
xscout3=piece('scout',2,1,0,0,2)
xscout4=piece('scout',2,1,0,0,2)
xscout5=piece('scout',2,1,0,0,2)
xscout6=piece('scout',2,1,0,0,2)
xscout7=piece('scout',2,1,0,0,2)
xscout8=piece('scout',2,1,0,0,2)
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
#lists of pieces

pieces1=[marshall,general]
pieces2=[xmarshall,xgeneral,xflag]

"""pygame code below here"""
pygame.init()
screen=pygame.display.set_mode((800,700))
"""colors"""
blue=(0,0,255)
red=(255,0,0)
green=(0,255,0)
font=pygame.font.SysFont('comisansms',30)
#inits the colors,screen, and font
def main_loop():
    '''main loop for the game'''
    global playernum
    global attackrecap
    global recap
    running=True
    screen.fill((255,255,255))
    while running:
        for event in pygame.event.get():
            if event.type==QUIT:
                running=False
        turn_board()
        board_create()
        #creates the board
        while True:
            select_piece()
            change=True
            while change==True:
                screen.fill((255,255,255))
                playerchange=font.render('Change the player. press enter to continue',True,blue)
                screen.blit(playerchange,(25,25))
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type==pygame.KEYDOWN:
                        if event.key==K_RETURN:
                            change=False
                            #puts a white screen with just above words
                            #then after enter changes the player and prints new board
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
                #error checks player number agian
def row_columngen():
        '''gets the row and column for pieces to be placed on board'''
        global row
        global column
        selrow=font.render(f'Select row of piece',True,blue)
        screen.blit(selrow,(25,25))
        pygame.display.update()
        running=True
        ro=''
        #blits first question to screen
        while running:
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN and len(ro)<2:
                    if str(pygame.key.name(event.key)).isnumeric()==True:
                        ro+=pygame.key.name(event.key)
                        #if the pressed key is a numebr adds it to 'ro'
                if event.type==pygame.QUIT:
                    running=False
                    
                n=font.render(ro,True,blue)
                screen.blit(n,(300,25))
                pygame.display.update()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN and ro.isnumeric()==True:
                        row=int(ro)
                        running=False
                #once enter is pressed saves ro to 'row'
        if row>10:
            toobig=font.render('You cant select a row greater than 10',True,blue)
            screen.blit(toobig,(25,65))
            pygame.display.update()
            pygame.time.wait(600)
            turn_board()
            row_columngen()
            return
            #if row is bigger than 10 then reruns code
        selcol=font.render(f'Select column of piece',True,blue)
        screen.blit(selcol,(350,25))
        pygame.display.update()
        running=True
        ro=''
        #explained above
        while running:
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN and len(ro)<2:
                    if str(pygame.key.name(event.key)).isnumeric()==True:
                        ro+=pygame.key.name(event.key)
                if event.type==pygame.QUIT:
                    running=False
                    
                n=font.render(ro,True,blue)
                screen.blit(n,(625,25))
                pygame.display.update()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN and ro.isnumeric()==True:
                        column=int(ro)
                        running=False
        if column>10:
            toobig=font.render('You cant select a column greater than 10',True,blue)
            screen.blit(toobig,(25,65))
            pygame.display.update()
            pygame.time.wait(600)
            turn_board()
            pygame.display.update()
            row_columngen()
            return
        
main_loop()
#deselecting pieces INCORRECT
#moving into own piece XXXXXX
#selecting other piece
#selecting nothign XXXXXXX
#selecting lake INCORRECT
#selecting not moving piece XXXXX
#miner vs bomb
#spy vs marshall
#capturing flag
#selecting too big numberXXXXX
#recapXXXXXX
