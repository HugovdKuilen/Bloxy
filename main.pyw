import pygame

BACKGROUND = (0, 0, 0)
PLAYER = (14, 215, 237) #0ed7ed
END = (66, 245, 75)     #42f54b
LAVA = (245, 87, 66)    #f55742
WALL = (0, 0, 0)        #000000
FPS = (255, 255, 255)
def load_image(name):
    image = pygame.image.load(name)
    return image
def getarrayimage(path, amount):
    tempamount = 0
    temparray = []
    temparray2 = []
    for x in range(amount):
        try:
            temparray.append(load_image(str(path)+"sprite_"+str(tempamount)+".png"))
        except:
            try:
                temparray.append(load_image(str(path)+"sprite_0"+str(tempamount)+".png"))
            except:
                try:
                    temparray.append(load_image(str(path)+"2019-09-03 15-52-41_"+str(tempamount)+".jpg"))
                except:
                    try:
                        temparray.append(load_image(str(path)+"2019-09-03 15-52-41_0"+str(tempamount)+".jpg"))
                    except:
                        temparray.append(load_image(str(path)+"2019-09-03 15-52-41_00"+str(tempamount)+".jpg"))
                    
        tempamount += 1
    return temparray
def gameoveranim(exclude=None):
    anim = getarrayimage("deathanim/", 32)
    go = True
    global allblocks
    global drawblocks
    for pl in players:
        if exclude != None:
            if pl != exclude:
                if go == True:
                    temp = Animation(pl.px, pl.py, pl.pw, pl.ph, screen, anim, 0.2, False, lambda: gameover())
                    allblocks.append(temp)
                    drawblocks.append(temp)
                else:
                    temp = Animation(pl.px, pl.py, pl.pw, pl.ph, screen, anim, 0.2, False)
                    allblocks.append(temp)
                    drawblocks.append(temp)
                go = False
        drawblocks.remove(pl)
def winanim():
    anim = getarrayimage("levelcompleteanim/", 9)
    go = True
    global allblocks
    global drawblocks
    for pl in players:
        if go == True:
            temp = Animation(pl.px, pl.py, pl.pw, pl.ph, screen, anim, 0.1, False, lambda: nextlevel())
            allblocks.append(temp)
            drawblocks.append(temp)
        else:
            temp = Animation(pl.px, pl.py, pl.pw, pl.ph, screen, anim, 0.1, False)
            allblocks.append(temp)
            drawblocks.append(temp)
        go = False
        
class Animation():
    #pg.transform.scale(IMAGE, (50, 30))
    def iscollidingwith(self, sprite):
        return self.rect.colliderect(sprite.rect)
    def __init__(self, tx, ty, tw, th, screen, images, animspeed, repeat, oncomplete=None):
        self.px = tx
        self.py = ty
        self.pw = tw
        self.ph = th
        self.screen = screen
        self.aspeed = animspeed
        self.images = images
        # assuming both images are 64x64 pixels
        self.index = 0
        self.image = self.images[self.index]
        self.image = pygame.transform.scale(self.image, (self.pw, self.ph))
        self.rect = pygame.Rect(self.px, self.py, self.pw, self.ph)
        self.repeat = repeat
        self.oncomplete = oncomplete
    def Draw(self):
        self.rect.x = self.px
        self.rect.y = self.py
        self.index += self.aspeed
        if int(self.index) >= len(self.images):
            if self.repeat == True:
                self.index = 0
            else:
                if self.oncomplete != None:
                    self.oncomplete()
                del self
        self.image = self.images[int(self.index)]
        self.image = pygame.transform.scale(self.image, (self.pw, self.ph))
        self.screen.blit(self.image, (self.px, self.py))
def nextlevel():
    global alllevels
    global currentlevel
    unloadlevel()
    loadlevel(alllevels[alllevels.index(currentlevel)+1])
def gameover():
    global dodraw
    dodraw = False
    unloadlevel()
    loadlevel(currentlevel)
    dodraw = True
def percentage(part, whole):
    return 100 * float(part)/float(whole)
def unloadlevel():
    global allblocks
    global blocks
    global drawblocks
    global ends
    global players
    for stuff in allblocks:
        del stuff
        
    blocks = []
    drawblocks = []
    allblocks = []
    ends = []
    players = []
def loadlevel(level):
    global canwinanim
    canwinanim = True
    global currentlevel
    currentlevel = level
    maxamount = 0
    curramount = 0
    for row in level:
        for col in row:
            maxamount += 1
    global blocks
    global drawblocks
    global allblocks
    global ends
    global players
    global dodraw
    blocks = []
    drawblocks = []
    allblocks = []
    ends = []
    players = []
    global cangameover
    cangameover = True
    #except:
     #   blocks = []
      #  drawblocks = []
       # allblocks = []
        #ends = []
        #players = []
        
    x = y = 0
    oid = 0
    warps = 0
    if level == tutoriallevel:
        temp = Text(15, 5, str(leveltext["tutorialtext1"]), screen)
        allblocks.append(temp)
        drawblocks.append(temp)
    for row in level:
        for col in row:
            if col == "W":
                 boi = Object(x, y, 50, 50, screen)
                 drawblocks.append(boi)
                 allblocks.append(boi)
                 blocks.append(boi)
            if col == "L":
                 en = Lava(x, y, 50, 50, screen)
                 drawblocks.append(en)
                 allblocks.append(en)
            if col == "S":
                global p
                p = Player(x, y, 50, 50, screen)
                drawblocks.append(p)
                allblocks.append(p)
                blocks.append(p)
                players.append(p)
            if col == " ":
                temp = End(x, y, 50, 50, screen)
                allblocks.append(temp)
                drawblocks.append(temp)
                ends.append(temp)
            curramount += 1
            if dodraw == True:
                screen.fill((0, 0, 0))
                fps = font.render("Loading "+str(int(percentage(curramount, maxamount)))+"%", True, FPS)
                screen.blit(fps, (5, 5))
                pygame.display.flip()
            x += 50
        y += 50
        x = 0
class Player():
    def __init__(self, tx, ty, tw, th, screen):
        self.px = tx
        self.py = ty
        self.rx = self.px
        self.ry = self.py
        
        self.pw = tw
        self.ph = th
        self.cx = 0
        self.cy = 0
        self.screen = screen
        self.rect = pygame.Rect(self.px, self.py, self.pw, self.ph)
        self.temprect = pygame.Rect(self.px, self.py, self.pw, self.ph)
    def iscollidingwith(self, sprite):
        return self.rect.colliderect(sprite.rect)
    def Draw(self):
        p.rect.x = p.px
        p.rect.y = p.py
        pygame.draw.rect(self.screen, PLAYER, [self.rect.x, self.rect.y, self.rect.w, self.rect.h], 0)
        #pygame.draw.rect(self.screen, (255, 0, 0), [self.temprect.x, self.temprect.y, self.temprect.w, self.temprect.h], 5)
    def move2(self, direction):
        global players
        if direction == "right":
            tempp = Player(self.px+50, self.py, self.pw, self.ph, self.screen)
            drawblocks.append(tempp)
            allblocks.append(tempp)
            blocks.append(tempp)
            players.append(tempp)
        if direction == "down":
            tempp = Player(self.px, self.py+50, self.pw, self.ph, self.screen)
            drawblocks.append(tempp)
            allblocks.append(tempp)
            blocks.append(tempp)
            players.append(tempp)
        if direction == "left":
            tempp = Player(self.px-50, self.py, self.pw, self.ph, self.screen)
            drawblocks.append(tempp)
            allblocks.append(tempp)
            blocks.append(tempp)
            players.append(tempp)
        if direction == "up":
            tempp = Player(self.px, self.py-50, self.pw, self.ph, self.screen)
            drawblocks.append(tempp)
            allblocks.append(tempp)
            blocks.append(tempp)
            players.append(tempp)
    def move(self, direction):
        execute = True
        self.temprect = pygame.Rect(self.rect.x, self.rect.y, self.rect.w, self.rect.h)
        if direction == "right":
            self.temprect.x += 50
            for wall in blocks:
                if self.temprect.colliderect(wall.rect):
                    #print("collision with ", str(wall))
                    execute = False
        if direction == "up":
            self.temprect.y -= 50
            for wall in blocks:
                if self.temprect.colliderect(wall.rect):
                    #print("collision with ", str(wall))
                    execute = False
        if direction == "down":
            self.temprect.y += 50
            for wall in blocks:
                if self.temprect.colliderect(wall.rect):
                    #print("collision with ", str(wall))
                    execute = False
        if direction == "left":
            self.temprect.x -= 50
            for wall in blocks:
                if self.temprect.colliderect(wall.rect):
                    #print("collision with ", str(wall))
                    execute = False
        if execute == True:
            self.move2(direction)
            
class Object():
    #pg.transform.scale(IMAGE, (50, 30))
    def iscollidingwith(self, sprite):
        return self.rect.colliderect(sprite.rect)
    def __init__(self, tx, ty, tw, th, screen):
        self.px = tx
        self.py = ty
        self.pw = tw
        self.ph = th
        self.screen = screen
        self.rect = pygame.Rect(self.px, self.py, self.pw, self.ph)
    def Draw(self):
        self.rect.x = self.px
        self.rect.y = self.py
        pygame.draw.rect(self.screen, WALL, [self.rect.x, self.rect.y, self.rect.w, self.rect.h], 0)
class Lava():
    def iscollidingwith(self, sprite):
        return self.rect.colliderect(sprite.rect)
    def __init__(self, tx, ty, tw, th, screen):
        self.px = tx
        self.py = ty
        self.pw = tw
        self.ph = th
        self.screen = screen
        self.rect = pygame.Rect(self.px, self.py, self.pw, self.ph)

    def Draw(self):
        global cangameover
        for player in players:
            if self.iscollidingwith(player) and cangameover == True:
                gameoveranim(player)
                canwinanim = False
                cangameover = False
        self.rect.x = self.px
        self.rect.y = self.py
        pygame.draw.rect(self.screen, LAVA, [self.rect.x, self.rect.y, self.rect.w, self.rect.h], 0)
class End():
    def iscollidingwith(self, sprite):
        return self.rect.colliderect(sprite.rect)
    def __init__(self, tx, ty, tw, th, screen):
        self.px = tx
        self.py = ty
        self.pw = tw
        self.ph = th
        self.screen = screen
        self.rect = pygame.Rect(self.px, self.py, self.pw, self.ph)

    def Draw(self):
        self.rect.x = self.px
        self.rect.y = self.py
        pygame.draw.rect(self.screen, END, [self.rect.x, self.rect.y, self.rect.w, self.rect.h], 0)
class Text():
    def __init__(self, tx, ty, text, screen):
        self.px = tx
        self.py = ty
        self.screen = screen
        self.text = font.render(str(text), True, FPS)

    def Draw(self):
        self.screen.blit(self.text, (self.px, self.py))

pygame.init()
w = 700
h = 500
size = (w, h)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Box game")
done = False
clock = pygame.time.Clock()
font = pygame.font.Font(None, 30)
drawblocks = []
allblocks = []
ends = []

level = [
    "WWWWWWWWWWWWWW",
    "WWWWWWS  LWWWW",
    "WWWWWWW  WWWWW",
    "WWWW     WWWWW",
    "WW    WWWWWWWW",
    "WW W   WWWWWWW",
    "WWLWWW WWWWWWW",
    "WWWWW  WWWWWWW",
    "WWWW  WWWWWWWW",
    "WWWWWWWWWWWWWW",
]
template = [
    "WWWWWWWWWWWWWW",
    "WWWWWWWWWWWWWW",
    "WWWWWWWWWWWWWW",
    "WWWWWWWWWWWWWW",
    "WWWWWWWWWWWWWW",
    "WWWWWWWWWWWWWW",
    "WWWWWWWWWWWWWW",
    "WWWWWWWWWWWWWW",
    "WWWWWWWWWWWWWW",
    "WWWWWWWWWWWWWW"
]
level2 = [
    "WWWWWWWWWWWWWW",
    "WWWWWWWWWWWWWW",
    "WWW      WWWWW",
    "WWW WWLWWWWWWW",
    "WWW WLWWWWWWWW",
    "WWW      WWWWW",
    "WWW W    LWWWW",
    "WWS       WWWW",
    "WWWWWWWWWWWWWW",
    "WWWWWWWWWWWWWW"
]
tutoriallevel = [
    'WWWWWWWWWWWWWW',
    'WWWWWWWWWWWWWW',
    'WWWWWWWWWLWWWW',
    'WWWW      WWWW',
    'WWWW      WWWW',
    'WWWWS     WWWW',
    'WWWWWWW   WWWW',
    'WWWWWWWWWWWWWW',
    'WWWWWWWWWWWWWW',
    'WWWWWWWWWWWWWW'
]
testlevel = [
    'WWWWWWWWWWWWWW',
    'W           SW',
    'W            W',
    'W            W',
    'W            W',
    'W            W',
    'W            W',
    'W            W',
    'WS           W',
    'WWWWWWWWWWWWWW'
]
leveltext = {
    "tutorialtext1": "Try filling up these green squares by\nmaking one row of blue\nsquares and going up"
}
def start_game():
    unloadlevel
    global running
    running = True
    loadlevel(tutoriallevel)
currentlevel = tutoriallevel
alllevels = [tutoriallevel, level, level2, testlevel]
dodraw = True
cangameover = True
canwinanim = True
running = False
screen.fill((0, 0, 0))
loadingimg = load_image("Loading screen.png")
screen.blit(loadingimg, (0, 0))
pygame.display.flip()
titlebool = False
win = False
with open("settings.txt", "r+") as f:
    if f.read() == "title screen = true":
        titleanim = getarrayimage("titlescreen/", 300)
        titlescreen = Animation(0, 0, w, h, screen, titleanim, 0.5, True)
        allblocks.append(titlescreen)
        drawblocks.append(titlescreen)
        titlebool = True
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if running == True:
                if event.key == pygame.K_RIGHT:
                    tempamount = 0
                    for temppla in players:
                        #print("px: ", temppla.px, " py: ", temppla.py)
                        tempamount += 1
                    for x in range(tempamount):
                        players[x].move("right")
                if event.key == pygame.K_LEFT:
                    tempamount = 0
                    for temppla in players:
                        #print("px: ", temppla.px, " py: ", temppla.py)
                        tempamount += 1
                    for x in range(tempamount):
                        players[x].move("left")
                if event.key == pygame.K_UP:
                    tempamount = 0
                    for temppla in players:
                        #print("px: ", temppla.px, " py: ", temppla.py)
                        tempamount += 1
                    for x in range(tempamount):
                        players[x].move("up")
                if event.key == pygame.K_DOWN:
                    tempamount = 0
                    for temppla in players:
                        #print("px: ", temppla.px, " py: ", temppla.py)
                        tempamount += 1
                    for x in range(tempamount):
                        players[x].move("down")
            else:
                if event.key == pygame.K_SPACE:
                    start_game()
    if running == False:
        screen.fill((0,0,0))
    if dodraw == True:
        screen.fill(BACKGROUND)
        for temp in drawblocks:
            try:
                temp.Draw()
            except:
                continue
        if running == False:
            pressspace = font.render("Press space to start", True, FPS)
            if titlebool == False:
                screen.blit(pressspace, (250, 350))
            else:
                screen.blit(pressspace, (300, 350))
    win = False
    filled = 0
    if running == True:
        for end in ends:
            for player in players:
                if end.iscollidingwith(player):
                    filled += 1
        if filled == len(ends):
            win = True
        if win == True and canwinanim == True:
            winanim()
            canwinanim = False
    pygame.display.flip()
 
    clock.tick(60)
 
pygame.quit()
