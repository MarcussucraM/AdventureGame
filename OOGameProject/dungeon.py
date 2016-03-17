#Game Project for Object Oriented class
#Written by Marcus Kruzel
#Group Members: Thomas Jones, Sean Harris, Patrick Mehan, Casius Carter
#Written in Python v2.7.6

import pygame, sys, levels 
from pygame.locals import *

########################CONSTANTS############################
FPS = 60
WIDTH = 768
HEIGHT = 768

#colors
WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)
YELLOW = (255,255,0)
BROWN = (51,25,0)
GREY = (128,128,128)
GREEN = (0,100,0)
PINK = (255,105,180)

#global variables

#make this super high if you're a noob
global LIVES
LIVES = 1

#change this if you want to jump to a specific level
global LEVEL
LEVEL = 0
#################IN GAME OBJECTS##################################
'''
Block, inherits from pygame's Sprite class which allows us to
have an image which we can put any texture on and a bounding
rectangle which makes collision detection much easier.
All of the game objects inherit from this class.
'''
class Block(pygame.sprite.Sprite):
    def __init__(self,width,height,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width,height])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
class Wall(Block):
    def __init__(self,width,height,x,y):
        Block.__init__(self,width,height,x,y)
        self.image = pygame.image.load('GameImages/wall.png')
        self.image = pygame.transform.scale(self.image, (width,height))
              
class Lava(Block):
    def __init__(self,width,height,x,y):
        Block.__init__(self,width,height,x,y)
        self.image = pygame.image.load('GameImages/lava.png')
        self.image = pygame.transform.scale(self.image, (width,height))
        
class Key(Block):
    def __init__(self,width,height,x,y):
        Block.__init__(self,width,height,x,y)
        self.image = pygame.image.load('GameImages/key.png')
        self.image = pygame.transform.scale(self.image, (width,height))
        
class One_Up(Block):
    def __init__(self,width,height,x,y):
        Block.__init__(self,width,height,x,y)
        self.image = pygame.image.load('GameImages/heart.png')
        self.image = pygame.transform.scale(self.image, (width,height))
        
class Door(Block):
    def __init__(self,width,height,x,y):
        Block.__init__(self,width,height,x,y)
        self.image = pygame.image.load('GameImages/door.png')
        self.image = pygame.transform.scale(self.image, (width,height))
                
class MoveBlock(Block):
    def __init__(self,width,height,x,y):
        Block.__init__(self,width,height,x,y)
        #load image from gameimages directory
        self.image = pygame.image.load('GameImages/Box2.png')
        #size it to correct size
        self.image = pygame.transform.scale(self.image, (width,height))
        
        self.speed = 0
        self.velX = 0
        self.velY = 0
        
###################MONSTERS#########################################
'''
Monster - Base class for all the monsters in the game
each one has a strategy for movement and a base speed of 5

There are two different types of monsters in the game, and thus
there are also two different movement strategies
VerticalBounceMonster - Uses the BounceUpDown strategy which is 
self explanatory and,
HorizontalBounceMonster - Which uses the BounceLeftRight strategy
To move they call their inherited move method and then call
the strategies move method.
'''  
class Monster(Block):
    def __init__(self,width,height,x,y):
        #monster start location
        Block.__init__(self,width,height,x,y)
        self.strategy = None
        self.speed = 5
        self.velX = 0
        self.velY = 0
            
    def move(self):
        pass
        
#movementID for collision detector later, so it can tell them apart.
class VerticalBounceMonster(Monster):
    def __init__(self,width,height,x,y):
        Monster.__init__(self,width,height,x,y)
        self.image = pygame.image.load('GameImages/vbouncemonster.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (width,height))
        self.strategy = BounceUpDown()
        self.movementID = "bounceY"
        self.velY = 5
        
    def move(self):
        self.strategy.move(self)
        
        
class HorizontalBounceMonster(Monster):
    def __init__(self,width,height,x,y):
        Monster.__init__(self,width,height,x,y)
        self.image = pygame.image.load('GameImages/vbouncemonster.png')
        self.image = pygame.transform.scale(self.image, (width,height))
        self.strategy = BounceLeftRight()
        self.movementID = "bounceX"
        self.velX = 5
        
    def move(self):
        self.strategy.move(self)
     
#####strategies for monster movement#####           
#####STRATEGY PATTERN####################
'''
Strategies for movement, each has a move strategy
and bounce strategy, which is called when it collides
with something else
'''
class BounceLeftRight(object):                
    def move(self, monster):    
        monster.rect.x += monster.velX        
        
    def bounce(self, monster):
        if monster.velX > 0:
            monster.velX = -monster.speed
            
        elif monster.velX < 0:
            monster.velX = monster.speed
            
            
class BounceUpDown(object):
    def move(self,monster):
        monster.rect.y += monster.velY
        
    def bounce(self, monster):
        if monster.velY > 0:
            monster.velY = -monster.speed
        
        elif monster.velY < 0:
            monster.velY = monster.speed
        
           
########################################################################

######################PLAYER############################################


class Player(Block):
    def __init__(self,width,height,x,y):
        Block.__init__(self,width,height,x,y)                        
        self.speed = 3
        self.velX = 0
        self.velY = 0
              
        #number of keys currently has#
        self.keys = 0
        
        #current frame to know what image to show on screen
        self.frame = 0
        #used to delay image switching
        self.last_update = 0
        
        #set initial player image
        self.image = pygame.image.load('GameImages/characterStandingFacingDown.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (width,height))
        
        #load images for walking animations
        self.walkdown = [pygame.image.load('GameImages/wf01.png').convert_alpha(),
                         pygame.image.load('GameImages/wf02.png').convert_alpha(),
                         pygame.image.load('GameImages/wf03.png').convert_alpha(),
                         pygame.image.load('GameImages/wf04.png').convert_alpha()]

        self.walkup = [pygame.image.load('GameImages/wb01.png').convert_alpha(),
                       pygame.image.load('GameImages/wb02.png').convert_alpha(),
                       pygame.image.load('GameImages/wb03.png').convert_alpha(),
                       pygame.image.load('GameImages/wb04.png').convert_alpha()]

        self.walkleft = [pygame.image.load('GameImages/wl01.png').convert_alpha(),
                         pygame.image.load('GameImages/wl02.png').convert_alpha(),
                         pygame.image.load('GameImages/wl03.png').convert_alpha(),
                         pygame.image.load('GameImages/wl04.png').convert_alpha()]

        self.walkright = [pygame.image.load('GameImages/wr01.png').convert_alpha(),
                          pygame.image.load('GameImages/wr02.png').convert_alpha(),
                          pygame.image.load('GameImages/wr03.png').convert_alpha(),
                          pygame.image.load('GameImages/wr04.png').convert_alpha()]
        
        
        
        #scale images to correct size
        self.scaleImages(self.walkdown,width,height)                                                    
        self.scaleImages(self.walkup,width,height)
        self.scaleImages(self.walkleft,width,height)               
        self.scaleImages(self.walkright,width,height)
        
    #player movement methods, invoked by PlayerMove            
    def move_up(self):
        self.update(self.walkup)
        self.velY = -self.speed
        self.rect.y += self.velY
                
    def move_down(self):
        self.update(self.walkdown)
        self.velY = self.speed
        self.rect.y += self.velY
                
    def move_right(self):
        self.update(self.walkright)
        self.velX = self.speed
        self.rect.x += self.velX
                
    def move_left(self):
        self.update(self.walkleft)
        self.velX = -self.speed
        self.rect.x += self.velX
     
    #scales images to correct size of the bounding rectangle
    def scaleImages(self, images,width,height):
        for i in xrange(len(images)):
            images[i] = pygame.transform.scale(images[i], (width,height))
            
    #changes player image, checks the current time and
    #if it - the last update is greater than the delay time
    #then switch it out with the next image
    #makes the walking animation work.
    def update(self, images, delay = 5000/FPS):
        t = pygame.time.get_ticks()
        if t - self.last_update > delay:
            self.frame += 1
            if self.frame >= len(images): self.frame = 0
            self.image = images[self.frame]
            self.last_update = t
 

####################COMMAND PATTERN##################################
'''Client'''
class PlayerEvent(object):
    def __init__(self,player):
        self.p = player
        self.__move = PlayerMove(self.p.move_up,self.p.move_down,self.p.move_right,self.p.move_left)
        
    def event(self,key):
        if key[K_a]:
            self.__move.move_left()
        elif key[K_d]:
            self.__move.move_right()
        elif key[K_s]:
            self.__move.move_down()
        elif key[K_w]:    
            self.__move.move_up()
     
    #this is made because every new level creates a new instance of player
    #so it needs to be updated every level change.
    def updatePlayer(self,player):
        self.p = player
        self.__move = PlayerMove(self.p.move_up,self.p.move_down,self.p.move_right,self.p.move_left)

'''Invoker'''            
class PlayerMove(object):
    def __init__(self, move_up_cmd, move_down_cmd, move_right_cmd, move_left_cmd):
        self.move_up = move_up_cmd
        self.move_down = move_down_cmd
        self.move_left = move_left_cmd
        self.move_right = move_right_cmd               
            
 
#################GAME OBJECT FACTORY#####################################
###################FACTORY PATTERN#######################################
'''
Creates all objects in the game. Stores a dictionary of game objects it can
choose from when reading input from the room buildLevel method. each key
corresponds to a specific object Type
''' 
class Game_Object_Factory(object):
    def __init__(self):
        self.game_objects = {'h': HorizontalBounceMonster, 'v': VerticalBounceMonster, 'd': Door, 'k': Key, 'l': Lava, 'x': Wall, 'u': One_Up, 'm':MoveBlock,
        's':Player}
    
    def create(self,typ,width,height,x,y):
        return self.game_objects[typ](width,height,x,y)

        
        
        
###################---------ROOMS-------#################################
'''
contains main stats for every room
each room could contain different things

monster = v or h = monster spawn point
wall = x
key = k
lava = l
door = d
start = s = player spawn point
one_ups = u
moveable blocks = m
'''
class Room(object):
    monsters = None
    walls = None
    keys = None
    lava = None
    doors = None
    players = None
    one_ups = None
    moveBlocks = None
    
    #groups of things within the level
    #self,layout
    def __init__(self, layout):
        self.monsters = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.keys = pygame.sprite.Group()
        self.lava = pygame.sprite.Group()
        self.doors = pygame.sprite.Group()
        self.players = pygame.sprite.Group()
        self.one_ups = pygame.sprite.Group()
        self.moveBlocks = pygame.sprite.Group()
        
        #layout for the level, found in levels.py
        self.layout = layout
    
    #resets level incase player gets stuck
    def reset(self):
        #empty all sprites from room
        self.monsters.empty()
        self.walls.empty()
        self.keys.empty()
        self.lava.empty()
        self.doors.empty()
        self.players.empty()
        self.one_ups.empty()
        self.moveBlocks.empty()
        
        #redo them all
        self.buildLevel()    
    
            
    def buildLevel(self):
        '''this method reads the string array from the levels class
        it then pushes the character read into the game object factory
        which decides what type of object to create. To get the size of the block
        we take the width and height of the screen and divide each by either the rows
        or columns in the string array that way we get a tile that fits the screen'''
        
        #creates all the objects in a room
        gof = Game_Object_Factory()
                    
        rows = len(self.layout)        
        columns = len(self.layout[0])
        #width of block,height of block
        wob = WIDTH/columns
        hob = HEIGHT/rows
        #if you see a division against these its to make the block smaller
        #and/or center it in the middle of a tile
        

        for y in range(rows):
            for x in range(columns):
                if self.layout[y][x] == 'x':
                    self.walls.add(gof.create('x',wob,hob,x*wob,y*hob))
                elif self.layout[y][x] == 'l':
                    self.lava.add(gof.create('l',wob,hob,x*wob,y*hob))
                elif self.layout[y][x] == 'd':
                    self.doors.add(gof.create('d',wob,hob,x*wob,y*hob))
                elif self.layout[y][x] == 's':
                    self.players.add(gof.create('s',3*wob/4,3*hob/4,x*wob,y*hob))
                elif self.layout[y][x] == 'k':
                    self.keys.add(gof.create('k',wob/2,hob/2,x*wob + wob/4,y*hob + wob/4))
                elif self.layout[y][x] == 'h':
                    self.monsters.add(gof.create('h',wob,hob,x*wob,y*hob))
                elif self.layout[y][x] == 'v':
                    self.monsters.add(gof.create('v',wob,hob,x*wob,y*hob))
                elif self.layout[y][x] == 'u':
                    self.one_ups.add(gof.create('u',wob/2,hob/2,x*wob + wob/4,y*hob + wob/4))
                elif self.layout[y][x] == 'm':
                    self.moveBlocks.add(gof.create('m',wob,hob,x*wob,y*hob))
        
                

###################COLLISION DETECTOR###############################
'''
    This class contains all objects in a level/room
    it has various methods that allow a single object to check against
    other specific types of objects/blocks and then positions them and
    does various actions depending on what collides with what.
'''   
class CollisionDetector(object):    
    def __init__(self,room):
        self.room = room
        
    #updates room to check for collisions
    def updateRoom(self,room):
        self.room = room

    #inputs, type of block(thing),player direction, and player
    #if the player bumps into something, this puts it in the right spot
    #to get this to work, we need to use velocity        
    def getposition(self,thing,player):
        if player.velX > 0:
            player.rect.right = thing.rect.left - player.speed
                        
        elif player.velX < 0:
            player.rect.left = thing.rect.right + player.speed
                       
        elif player.velY > 0:
            player.rect.bottom = thing.rect.top - player.speed
                       
        elif player.velY < 0:
            player.rect.top = thing.rect.bottom + player.speed
            
            
    
    #how to move a moveable block around        
    def moveBlock(self,mb,player):
        if player.velX > 0:
            mb.velX = player.speed
            mb.rect.x += mb.velX
        elif player.velX < 0:
            mb.velX = -player.speed 
            mb.rect.x += mb.velX
        elif player.velY > 0:
            mb.velY = player.speed
            mb.rect.y += mb.velY
        elif player.velY < 0:
            mb.velY = -player.speed
            mb.rect.y += mb.velY        
        
                                
    #input, player direction, and the player
    #detects player collisions with different blocks    
    def playerDetection(self,player):
        ###uses the global variable LIVES to keep track###
        global LIVES
        
        ###walls###
        block_hit_list = pygame.sprite.spritecollide(player,self.room.walls,False)
        for block in block_hit_list:
            self.getposition(block,player)
                
        ###lava###        
        lava_hit_list = pygame.sprite.spritecollide(player,self.room.lava,False)
        for lava in lava_hit_list:
            #make sure only one lava gets counted otherwise you lose 2 lives
            if lava in lava_hit_list:
                self.room.reset()
                LIVES -= 1
                break
        
        ###keys###    
        key_hit_list = pygame.sprite.spritecollide(player,self.room.keys,False)
        for key in key_hit_list:
            player.keys += 1
            self.room.keys.remove(key)
            
            
        ###one_ups###
        one_up_hit_list = pygame.sprite.spritecollide(player,self.room.one_ups,False)
        for one_up in one_up_hit_list:
            LIVES += 1
            self.room.one_ups.remove(one_up)
            
        ###monsters###    
        monster_hit_list = pygame.sprite.spritecollide(player,self.room.monsters,False)
        for monster in monster_hit_list:
            #make sure only one monster gets counted otherwise you lose 2 lives
            if monster in monster_hit_list:
                self.room.reset()
                LIVES -= 1
                break
            
        ###doors###    
        door_hit_list = pygame.sprite.spritecollide(player,self.room.doors,False)
        for door in door_hit_list:    
            if not player.keys == 0:
                global LEVEL
                player.keys -= 1
                self.room.doors.remove(door)
                LEVEL += 1
            else:
                self.getposition(door,player)
                
                
        ###moveBlocks###
        mb_hit_list = pygame.sprite.spritecollide(player,self.room.moveBlocks,False)
        for mb in mb_hit_list:
            self.moveBlock(mb,player)
            self.getposition(mb,player)
            
    #if a moveblock runs into things, this is what happens    
    def moveBlockDetection(self, mb):
        ####walls###
        block_hit_list = pygame.sprite.spritecollide(mb,self.room.walls,False)
        for block in block_hit_list:
            self.getposition(block,mb)
        
        ###moveblocks###
        ###make sure the group doesnt only contain one sprite###
        ###otherwise the block collides with itself and funny things happen###
        moveblock_hit_list = pygame.sprite.spritecollide(mb,self.room.moveBlocks,False)
        for moveblock in moveblock_hit_list:
            if mb != moveblock:
                self.getposition(moveblock,mb)
                
        ###lava###
        lava_hit_list = pygame.sprite.spritecollide(mb,self.room.lava,False)
        for lava in lava_hit_list:
            self.room.moveBlocks.remove(mb)
            self.room.lava.remove(lava)
            
        
                            
    #if a monster hits these things, this stuff happens    
    def monsterDetection(self, monster):
        ###walls###
        block_hit_list = pygame.sprite.spritecollide(monster,self.room.walls,False)
        for block in block_hit_list:
            self.getposition(block,monster)    
            if monster.movementID == "bounceX":
                if monster.velX > 0:
                    monster.velX = -monster.speed
                elif monster.velX < 0:
                    monster.velX = monster.speed
            if monster.movementID == "bounceY":
                monster.strategy.bounce(monster)
                
        
        ###doors###        
        door_hit_list = pygame.sprite.spritecollide(monster,self.room.doors,False)
        for door in door_hit_list:
            self.getposition(door,monster)
            if monster.movementID == "bounceX":
                monster.strategy.bounce(monster)
            elif monster.movementID == "bounceY":
                monster.strategy.bounce(monster)
                
                
        ###moveblocks###
        mb_hit_list = pygame.sprite.spritecollide(monster,self.room.moveBlocks,False)
        for mb in mb_hit_list:
            self.getposition(mb,monster)
            if monster.movementID == "bounceX":
                monster.strategy.bounce(monster)
            elif monster.movementID == "bounceY":
                monster.strategy.bounce(monster)
            

####################END CONDITIONS###################################
####################OBSERVER PATTERN#################################
'''
Subject of the observer pattern, Didn't bother to make a list of
observers, because the only one will be the main game
holds state for current amount of lives left and the current level
'''
class EndConditions(object):
    def __init__(self):
        global LIVES
        global LEVEL
        self.observer = None
        
    def addObserver(self,o):
        self.observer = o
        
    def removeObserver(self,o):
        self.observer = o
        
    def notifyObserver(self):
        if LIVES <= 0:
            self.observer.end("YOU LOSE")
        elif LEVEL > 8:
            self.observer.end("YOU WIN!")
                
                
###################MAIN GAME#########################################
'''
Main class for the game, everything happens here
'''
class Game(object):
    def __init__(self):
        '''init game elements'''
        pygame.init()
        pygame.display.set_caption("TestLevels")
        self.size = (WIDTH,HEIGHT)
        self.screen = pygame.display.set_mode(self.size)
        self.flags=self.screen.get_flags()        
		
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.currentRoom = None
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('mono', HEIGHT//30, bold = True)
        self.player = None
             
        #add subject class for observer pattern#
        self.endConditions = EndConditions()
        #subscribe to subject class#
        self.endConditions.addObserver(self)
       
    def draw(self):
        '''draws everything in the room onto the screen'''
        self.currentRoom.walls.draw(self.screen)
        self.currentRoom.lava.draw(self.screen)
        self.currentRoom.doors.draw(self.screen)
        self.currentRoom.players.draw(self.screen)
        self.currentRoom.monsters.draw(self.screen)
        self.currentRoom.keys.draw(self.screen)
        self.currentRoom.one_ups.draw(self.screen)
        self.currentRoom.moveBlocks.draw(self.screen)
    
   
    def drawText(self):
        '''draws all text onto the screen'''
        
        global LIVES,LEVEL
        string = "Level:   %d   LivesLeft:  %d   Keys:  %d"%(LEVEL+1,LIVES,self.player.keys)
        surface = self.font.render((string), True, WHITE)
        self.screen.blit(surface, (0, 5))
        
    
    def updateLevel(self):
        '''updates current level'''
        
        l = levels.Levels()
        if self.i != LEVEL:
            self.currentRoom = Room(l.layouts[LEVEL])
            self.currentRoom.buildLevel()
            self.i = LEVEL
    
    
    def end(self,string):
        '''
        Player gets notified by the endCondition class every loop
        EndCondition class tells if you win or lose
        this method builds a screen that notifies you whether you win or
        lose(string) and tells you how to exit/restart the game.
        '''
        
        global LEVEL
        global LIVES
        LEVEL = 0
        
        running = True
        while running:
            string1 = string
            string2 = "PRESS ENTER TO PLAY AGAIN"
            self.screen.blit(self.background,(0,0))
                
            '''random magical numbers - just trust that this centers the
            above two strings'''
            surface = self.font.render((string1),True,WHITE)
            self.screen.blit(surface,(2*WIDTH//5,HEIGHT//2))
            surface = self.font.render((string2),True,WHITE)
            self.screen.blit(surface,(WIDTH//4,HEIGHT//2 + 30))
             
            '''events that must happen to exit screen display loop'''
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key == pygame.K_RETURN:
                        LIVES = 1
                        self.updateLevel()
                        running = False   
                    
            pygame.display.update()
    
    #this is where everything happens 
    def run(self):
        #index for level, starts at -1 but once
        #a call to updateLevel is made it increments to current level
        self.i = -1
        ################################
        
        #method call to build start screen# 
        
###########generate levels######################################
        
        #set current level
        self.updateLevel()
        for player in self.currentRoom.players:
                self.player = player;
                
        #add collision detection - knows where all elements on map are
        c_detector = CollisionDetector(self.currentRoom)
        
        #add client class for command pattern
        p_events = PlayerEvent(self.player)
        
        #start the game#
        running = True        
        while running:   
            #add player to game, updates when u change a room        
            for player in self.currentRoom.players:
                self.player = player;

##############update collision detection incase room is different
            c_detector.updateRoom(self.currentRoom)
              
#############draw things to screen##################
#############blit(the surface you want to paint, the location u want to draw at)
            self.screen.blit(self.background, (0,0))
            self.draw()
            self.drawText()                

############moveblock detection####################
            for moveblock in self.currentRoom.moveBlocks:
                c_detector.moveBlockDetection(moveblock)
                moveblock.velX = 0
                moveblock.velY = 0
               
############player controls########################
            p_events.updatePlayer(self.player)
            p_events.event(pygame.key.get_pressed())
            c_detector.playerDetection(self.player)
            #zero out the players velocity so wierd things don't happen.
            self.player.velX = 0
            self.player.velY = 0
            
#############monster movement######################            
            for monster in self.currentRoom.monsters:
                monster.move()
                c_detector.monsterDetection(monster)
                                                    
#############game events###########################                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    if event.key == pygame.K_SPACE:
                        self.currentRoom.reset()
                    elif event.key ==K_f:
                        #toggle fullscreen by pressing F key.
                        if self.flags&FULLSCREEN==False:
                            self.flags|=FULLSCREEN
                            pygame.display.set_mode(self.size, self.flags)
                        else:
                            self.flags^=FULLSCREEN
                            pygame.display.set_mode(self.size, self.flags)
                    
            #check to see if player is still alive
            self.endConditions.notifyObserver() 

            #clock tick/update display
            self.updateLevel()                    
            self.clock.tick(FPS)
            pygame.display.update()
            
    
#################################################################            

def main():
    Game().run()


if __name__=='__main__':    
    main()