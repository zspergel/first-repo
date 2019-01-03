import random

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
        if enemy.name=='bomb' and self.name=='miner':
            enemy.strength-=20
        if self.strength>=enemy.strength:
            if enemy.name=='flag':
                print('you captured the flag and won the game')
                return
            print(f'You win. your {self.name} defeated a {enemy.name}')
            for i in lines:
                if (enemy.line-1)==i[0]:
                    i[enemy.spot]='-'
                    self.move(direc)
        if self.strength<enemy.strength:
            print(f'you lost. Your {self.name} was defeated by a {enemy.name}')
            for i in lines:
                if (self.line)==i[0]:
                    i[self.spot]='-'



    def move(self,move=''):
        global direc
        if self.name=='bomb':
            print('bombs cant move')
            return
        if self.name=='flag':
            print('the flag cant move')
            return
        if move=='':
            direc=input('move')
            move=direc
        if move=='s':
            for i in lines:
                if (self.line+1)==i[0]:
                    if i[self.spot]=='-':
                        print('no one is there')
                        i[self.spot]=self.name
                        n=i[0]-1
                        for x in lines:
                          if x[0]==n:
                            x[self.spot]='-'
                            self.line+=1
                    elif i[self.spot]==0:
                        print('that is the lake')
                        self.move()
                    else:
                        n=i[0]-1
                        print('That is an enemy')
                        for x in pieces:
                            if x.line==n and x.spot==self.spot:
                                self.attack(x)
        if move=='w':
            for i in lines:
                if (self.line-1)==i[0]:
                    if i[self.spot]=='-':
                        print('no one is there')
                        i[self.spot]=self.name
                        n=i[0]+1
                        for x in lines:
                          if x[0]==n:
                            x[self.spot]='-'
                            self.line-=1
                    elif i[self.spot]==0:
                        print('that is the lake')
                        self.move()
                    else:
                        n=i[0]+1
                        print('That is an enemy')
                        for x in pieces:
                            if x.line==n and x.spot==self.spot:
                                self.attack(x)
        if move=='a':
            for i in lines:
                if (self.line)==i[0]:
                    if i[self.spot-1]=='-':
                        print('no one is there')
                        i[self.spot]='-'
                        self.spot-=1
                        i[self.spot]=self.name
                    elif i[self.spot-1]==0:
                        print('that is a lake')
                        self.move()
                    else:
                        print('That is an enemy')
                        for x in pieces:
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
                        i[self.spot]=self.name
                    elif i[self.spot+1]==0:
                        print('that is a lake')
                        self.move()
                    else:
                        print('That is an enemy')
                        for x in pieces:
                            n=self.spot+1
                            if x.line==self.line and x.spot==n:
                                self.attack(x)
    def location(self):
        for i in lines:
            if self.line==i[0]:
                i[self.spot]=self.name
    def select_loc(self):
        row=input(f'select row for {self.name}')
        row=int(row)
        self.line=row
        column=input('select column')
        column=int(column)
        self.spot=column
        for i in lines:
            if i[0]==row:
                if i[column]!='-':
                    print('that space is filled')
                    self.select_loc()



def board():
    for i in lines:
        print(i)

def board_create():
    for i in pez:
        i.select_loc()
        i.location()
        board()





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
    row=input('select a piece. Enter the row of the piece')
    column=input('enter the column')
    for i in lines:
        if row==i[0]:
            if i[column]=='-' or i[column]=='0':
                print('that is not a piece')
                select_piece()
    for n in pieces:
        if n.line==row and n.spot==column:
            print(f'You have selected the {n.name} on {column},{row}')
            n.move()
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
'''end piece def'''
pieces=[marshall,general,colonel1,colonel2,major1,major2,major3,captain1,captain2,captain3,captain4,lieutenant1,lieutenant2,lieutenant3,lieutenant4,sergeant1,sergeant2,sergeant3,sergeant4,miner1,miner2,miner3,miner4,miner5,scout1,scout2,scout3,scout4,scuot5,scout6,scou7,scout8,bom1,bomb2,bomb3,bomb4,bomb5,flag]
pez=[scout1]

board_create()
select_piece()
board()

