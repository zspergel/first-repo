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
        print('hi')
        if self.strength>=enemy.strength:
          print('you won')
          for i in lines:
              if (enemy.line-1)==i[0]:
                  i[enemy.spot]='-'
                  self.move(direc)
        if self.strength<enemy.strength:
            print('you lost')
            for i in lines:
                if (self.line)==i[0]:
                    i[self.spot]='-'



    def move(self,move=''):
        global direc
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




class miner(piece):
    def __init__(self,name,strength,speed,line,spot,player):
        piece.__init__(self,name,strength,speed,line,spot,player)
    def defuse(self):
        move=input('move')
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
                        if enemy.name=='bomb':
                            print('you have defused the bomb')
                            enemy.strength-=20
                        n=i[0]-1
                        print('That is an enemy')
                        for x in pieces:
                            if x.line==n and x.spot==self.spot:
                                self.attack(x)
class scout(piece):
    def __init__(self,name,strength,speed,line,spot,player):
        piece__init__(self,name,strength,speed,line,spot,player)
    def jump(self):
        move=input('move')
        if move=='s':
            jumped=input('what spot do you want to jump to')
            jumped=int(jumped)
            self.line-=jumped
            #for i in lines:

#class bomb(piece):

#class flag(piece):
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
miner1=miner('miner',3,1,0,0,1)
miner2=miner('miner',3,1,0,0,1)
miner3=miner('miner',3,1,0,0,1)
miner4=miner('miner',3,1,0,0,1)
miner5=miner('miner',3,1,0,0,1)
'''end piece def'''
pieces=[marshall,general,colonel1,colonel2,major1,major2,major3,captain1,captain2,captain3,captain4,lieutenant1,lieutenant2,lieutenant3,lieutenant4,sergeant1,sergeant2,sergeant3,sergeant4]
pez=[marshall,general]

board_create()
marshall.move()
board()

