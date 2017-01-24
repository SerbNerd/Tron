#Tron.py
#Custom Tron game with new jump mechanic - explained on help page

import time as tym
from pygame import*
from math import*
from random import*
from pprint import*

screen=display.set_mode((1280,800))     #set screen size

class game:     #class for game
    def __init__(self):
        #all information for the game
        self.win = 0            #number keeps track of who won
        self.over = False       #flag to see when game is over
        self.one = [330,400]    #sets initial player positions
        self.two = [950,400]
        self.oned = 2           #keeps track of player directions starting with 1 is up, moving clockwise
        self.twod = 4
        self.start = True       #keeps track if game just started - used to update stuff in first loop
        self.path1 = []         #keeps track of path made
        self.path2 = []
        self.status1 = "alive"  #keeps track of status of each player
        self.status2 = "alive"
        self.jump1 = False      #keeps track if player is currently in jump
        self.jump2 = False
        self.jumpLeft1 = 3      #keeps track of how many jumps left
        self.jumpLeft2 = 3
        self.jumpCount1 = 0     #keeps track of how long jump is, jump is 5 pixels wide to make it challenging but not impossible
        self.jumpCount2 = 0

    def update(self):   #main update loop, runs all functions and then draws if game isnt over
        if self.over == False:
            if self.start: screen.blit(gameScreen,(0,0)) #if first loop put up background
            self.move()     #move
            self.draw()     #draw
            self.checkCollisions() #checkcollisions to look for end

    def move(self):
        self.start = False #immedielty after moving game is old so it didnt just start
        self.path1.append((self.one[0],self.one[1])) #adds current locations to paths
        self.path2.append((self.two[0],self.two[1]))
        if self.jumpCount1 == 0: #takes player out of jump if the counter is done
            self.jump1 = False
        if self.jump1:              #if jumping, lowers counter
            self.jumpCount1-=1
        if self.jumpCount2 == 0:
            self.jump2 = False
        if self.jump2:
            self.jumpCount2-=1

        if wClick:                  #if button is clicked, changes direction
            if self.oned != 3:      #ensures you do not go directly opp to kill yourself
                self.oned = 1
        if dClick:
            if self.oned != 4:
                self.oned = 2
        if sClick:
            if self.oned != 1:
                self.oned = 3
        if aClick:
            if self.oned != 2:
                self.oned = 4
        if spaceClick:          
            if self.jumpLeft1 >0:   #only jump if player has available jumps
                self.jumpLeft1-=1   #lowers count if used
                self.jump1 = True   #sets player to jumping when used
                self.jumpCount1 = 5 #sets counter to jump for 5 spots
                if self.jumpLeft1 == 0: #based on which jump used, it colours it to show player how mnay he has left
                    draw.rect(screen,(0,0,0),boost13,0)
                if self.jumpLeft1 == 1:
                    draw.rect(screen,(0,0,0),boost12,0)
                if self.jumpLeft1 == 2:
                    draw.rect(screen,(0,0,0),boost11,0)

        if upClick:    #same as first player just differnt buttons
            if self.twod != 3:
                self.twod = 1
        if rightClick:
            if self.twod != 4:
                self.twod = 2
        if downClick:
            if self.twod != 1:
                self.twod = 3
        if leftClick:
            if self.twod != 2:
                self.twod = 4
        if enterClick:   
            if self.jumpLeft2 >0:
                self.jump2 = True
                self.jumpCount2 = 5
                self.jumpLeft2-=1
                if self.jumpLeft2 == 0:
                    draw.rect(screen,(0,0,0),boost23,0)
                if self.jumpLeft2 == 1:
                    draw.rect(screen,(0,0,0),boost22,0)
                if self.jumpLeft2 == 2:
                    draw.rect(screen,(0,0,0),boost21,0)
        
        if self.oned == 1:
            self.one = [self.one[0],self.one[1]-1]
        elif self.oned == 2:
            self.one = [self.one[0]+1,self.one[1]]
        elif self.oned == 3:
            self.one = [self.one[0],self.one[1]+1]
        elif self.oned == 4:
            self.one = [self.one[0]-1,self.one[1]]

        if self.twod == 1:
            self.two = [self.two[0],self.two[1]-1]
        elif self.twod == 2:
            self.two = [self.two[0]+1,self.two[1]]
        elif self.twod == 3:
            self.two = [self.two[0],self.two[1]+1]
        elif self.twod == 4:
            self.two = [self.two[0]-1,self.two[1]]

    def draw(self):
        if self.jump1: #draws colour per player for current spot, only different colour used when jumping to show it
            draw.rect(screen,(100,80,220),(self.one[0],self.one[1],1,1),1)
        else:
            draw.rect(screen,(1,216,253),(self.one[0],self.one[1],1,1),1)
        if self.jump2:
            draw.rect(screen,(100,80,220),(self.two[0],self.two[1],1,1),1)
        else:
            draw.rect(screen,(251,230,1),(self.two[0],self.two[1],1,1),1)

    def checkCollisions(self):
        for points in self.path2: #checks if any position is touching anything either player previously was on
            if self.jump1 == False:
                if points == (self.one[0],self.one[1]):
                    self.status1 = "dead" #keeps track of which player diees to know of which one died, or if both
            if self.jump2 == False:
                if points == (self.two[0],self.two[1]):
                    self.status2 = "dead"
            
        for points in self.path1:
            if self.jump2 == False:
                if points == (self.two[0],self.two[1]):
                    self.status2 = "dead"
            if self.jump1 == False:
                if points == (self.one[0],self.one[1]):
                    self.status1 = "dead"

        if self.one[0] < 226: #checks if anyone hitting boundary
            self.status1 = "dead"
        if self.one[0] > 1054:
            self.status1 = "dead"
        if self.one[1] < 227:
            self.status1 = "dead"
        if self.one[1] > 580:
            self.status1 = "dead"
            
        if self.two[0] <= 226:
            self.status2 = "dead"
        if self.two[0] >= 1054:
            self.status2 = "dead"
        if self.two[1] <= 227:
            self.status2 = "dead"
        if self.two[1] >= 580:
            self.status2 = "dead"

        if self.status1 == "dead":
            self.over = True    #ends game
            self.win+=2         #adds value of winning player to total so win var is value of which player won or 3 if it is tie
        if self.status2 == "dead":
            self.over = True
            self.win+=1      

    def reset(self): #resets all game info to ensure all ready for next game
        self.over = False
        self.one = [330,400]
        self.two = [950,400]
        self.oned = 2
        self.twod = 4
        self.start = True
        self.path1 = []
        self.path2 = []
        self.status1 = "alive"
        self.status2 = "alive"
        self.jump1 = False
        self.jump2 = False
        self.jumpCount1 = 0
        self.jumpCount2 = 0
        self.jumpLeft1 = 3
        self.jumpLeft2 = 3
        self.win = 0
        
running = True
myClock = time.Clock() #set up clock to keep track of framerate
game = game()      #initialize game

menupic = image.load("Images/menu.jpg").convert()      #all pics loaded
menuGame = image.load("Images/menu1.jpg").convert()
menuHelp = image.load("Images/menu2.jpg").convert()
helpMenu = image.load("Images/helpmenu.jpg").convert()
gameScreen = image.load("Images/game.jpg").convert()
p1pic = image.load("Images/p1.jpg").convert()
p2pic = image.load("Images/p2.jpg").convert()
tiepic = image.load("Images/tie.jpg").convert()

startbutton = Rect(45,405,215,60)                   #all rectangles defined that are used
helpbutton = Rect(45,542,217,60)
boost11 = Rect(70,293,85,34)
boost12 = Rect(70,346,85,34)
boost13 = Rect(70,405,85,34)
boost21 = Rect(1124,293,85,34)
boost22 = Rect(1124,346,85,34)
boost23 = Rect(1124,405,85,34)

page = "menu"       #keeps track of what is being displayed - game starts off at menu

click = False       #keeps track of all inputs, when each button is clicked the become true temp.
upClick = False
downClick = False
leftClick = False
rightClick = False
wClick = False
aClick = False
sClick = False
dClick = False
spaceClick = False
enterClick = False

while running:
    click = False  #always setting the click vars to false to ensure only the ensure action of pressing down the key counts
    upClick = False
    downClick = False
    leftClick = False
    rightClick = False
    wClick = False
    aClick = False
    sClick = False
    dClick = False
    spaceClick = False
    enterClick = False
    for evnt in event.get(): #listening to all keys plus mouse 
        if evnt.type == MOUSEBUTTONDOWN :
            if evnt.button==1:
                click = True
        if evnt.type == KEYDOWN:
            if evnt.key == K_UP:
                upClick = True
            if evnt.key == K_DOWN:
                downClick = True
            if evnt.key == K_LEFT:
                leftClick = True
            if evnt.key == K_RIGHT:
                rightClick = True
            if evnt.key == K_w:
                wClick = True
            if evnt.key == K_a:
                aClick = True
            if evnt.key == K_s:
                sClick = True
            if evnt.key == K_d:
                dClick = True
            if evnt.key == K_SPACE:
                spaceClick = True
            if evnt.key == K_KP_ENTER:
                enterClick = True
        if evnt.type==QUIT:
            running=False
            
    mx,my  = mouse.get_pos()
    mb = mouse.get_pressed()
            
    if page == "game":          #checks what part of game you are on
        mouse.set_visible(False)    #if the game starts, turn off mouse
        game.update()               #start updating the game which runs it
        if game.over == True:       #checks if game has finished
            mouse.set_visible(True) #makes mouse visible again
            if game.win == 1:       #checks who won to go to appropriate end screen
                page = "p1"
            elif game.win == 2:
                page = "p2"
            elif game.win == 3:
                page = "tie"
            game.reset()            #resets the game to ensure everything is ready for if the player plays again
            
    if page == "menu":              #game starts at menu
        screen.blit(menupic,(0,0))  #displays menupic
        if startbutton.collidepoint(mx,my): #if hovering a button, displays updated menupic to show user that
            screen.blit(menuGame,(0,0))
            if click:   #if click the buttons, changes gamemode
                page = "game"
        if helpbutton.collidepoint(mx,my):
            screen.blit(menuHelp,(0,0))
            if click:
                page = "help"

    if page == "help":
        screen.blit(helpMenu,(0,0))
        if spaceClick: #for screens with just info on them, space continues the process
            page = "menu"

    if page == "p1":
        screen.blit(p1pic,(0,0))
        if spaceClick:
            page = "menu"

    if page == "p2":
        screen.blit(p2pic,(0,0))
        if spaceClick:
            page = "menu"

    if page == "tie":
        screen.blit(tiepic,(0,0))
        if spaceClick:
            page = "menu"
                
    display.flip() #show eveyrthing drawn on screen
    myClock.tick(60)    #ensures constant clock every 60 seconds
quit()
