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

class piece():
    def __init__(self,name,strength,speed,line,spot):
        self.name=name
        self.strength=strength
        self.speed=speed
        self.line=line
        self.spot=spot
    def attack(self,enemy):
        print('hi')
        if self.strength>=enemy.strength:
          print('you won')
          for i in lines:
            if (self.line+1)==i[0]:
              i[self.spot]=self.name
              n=i[0]-1
              for x in lines:
                if x[0]==n:
                  x[self.spot]='-'
        if self.strength<enemy.strength:
          print('you lost')
          for i in lines:
            if (enemy.line+1)==i[0]:
              i[enemy.spot]=enemy.name
              n=i[0]-1
              for x in lines:
                if x[0]==n:
                  x[enemy.spot]='-'
    def move(self):
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
                        n=i[0]-1
                        print('That is an enemy')
                        for x in pieces:
                            if x.line==n and x.spot==self.spot:
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

pieces=[marshall,general,colonel1,colonel2,major1,major2,major3,captain1,captain2,captain3,captain4,lieutenant1,lieutenant2,lieutenant3,lieutenant4,sergeant1,sergeant2,sergeant3,sergeant4]
pez=[marshall,general]
def board_create():
    for i in pieces:
        i.select_loc()
        i.location()
        board()


board_create()
marshall.move()
board()

class miner(piece):
    def __init__(self,strength,speed,line,spot):
        piece__init__(self,strength,speed,line,spot)
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
#class scout(piece):

#class bomb(piece):

#class flag(piece):
'''begin piece def'''
marshall=piece('marshall',10,1,0,0)
general=piece('general',9,1,0,0)
colonel1=piece('colonel',8,1,0,0)
colonel2=piece('colonel',8,1,0,0)
major1=piece('major',7,1,0,0)
major2=piece('major',7,1,0,0)
major3=piece('major',7,1,0,0)
captain1=piece('captain',6,1,0,0)
captain2=piece('captain',6,1,0,0)
captain3=piece('captain',6,1,0,0)
captain4=piece('captain',6,1,0,0)
lieutenant1=piece('lieutenant',5,1,0,0)
lieutenant2=piece('lieutenant',5,1,0,0)
lieutenant3=piece('lieutenant',5,1,0,0)
lieutenant4=piece('lieutenant',5,1,0,0)
sergeant1=piece('sergeant',4,1,0,0)
sergeant2=piece('sergeant',4,1,0,0)
sergeant3=piece('sergeant',4,1,0,0)
sergeant4=piece('sergeant',4,1,0,0)
miner1=miner('miner',3,1,0,0)
miner2=miner('miner',3,1,0,0)
miner3=miner('miner',3,1,0,0)
miner4=miner('miner',3,1,0,0)
miner5=miner('miner',3,1,0,0)
'''end piece def'''


