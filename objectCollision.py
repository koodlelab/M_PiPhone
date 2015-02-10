import pygame
from pygame.locals import*
import random
import sys
import math
pygame.init()


size = (800,600)
screen = pygame.display.set_mode(size)

def rand_circle_pos(size):
    x=random.randint(size[0]/-2, size[0]/2)
    y=random.randint(size[1]/-2, size[1]/2)
    magn = math.sqrt(x**2+y**2)

    x/=magn
    y/=magn

    speed = random.randint(1,min(size[0]/2, size[1]/2)*1000)/2000.0
    x*=speed
    y*=speed

    x+=size[0]/2.0
    y+=size[1]/2.0

    return [int(x),int(y)]


class Partical:
    def __init__(self, size):
        self.radius = random.randint(10,20)
        self.pos = [random.randint(0,size[0]),random.randint(0,size[1])]
        self.vector = [0.0,0.0]
        #self.image = pygame.image.load("rock.gif")

    def update(self,particals,size):
        for dot in particals:
            if dot!=self and math.sqrt((self.pos[0]-dot.pos[0])**2+(self.pos[1]-dot.pos[1])**2)<=(dot.radius+self.radius)*1.25:
                x=self.pos[0]-dot.pos[0]
                y=self.pos[1]-dot.pos[1]

                magn = math.sqrt(x**2+y**2)

                x/=magn
                y/=magn

                x*= max(0,(int(dot.radius+self.radius+5)-magn)*0.75)
                y*= max(0,(int(dot.radius+self.radius+5)-magn)*0.75)

                if max(0,(int(dot.radius+self.radius+5)-magn))>0:
                    self.vector[0]*=0.8
                    self.vector[1]*=0.8

                self.vector[0]-=x
                self.vector[1]-=y

        x = self.pos[0]-size[0]/2
        y = self.pos[1]-size[1]/2
        magn = float(math.sqrt(x**2+y**2))
        x/=magn
        y/=magn
        self.vector[0]+=x
        self.vector[1]+=y

    def move(self, size):
        self.pos[0]-=self.vector[0]
        self.pos[1]-=self.vector[1]

        if self.pos[0]<0 or self.pos[0]>size[0]:
            self.vector[0]*=-1
            self.pos[0]-=self.vector[0]
        if self.pos[1]<0 or self.pos[1]>size[1]:
            self.vector[1]*=-1
            self.pos[1]-=self.vector[1]

        self.vector[0]*=0.999
        self.vector[1]*=0.999

    def render(self):
        pygame.draw.circle(pygame.display.get_surface(), [100,100,255], self.pos, self.radius)

class Planet:
    def __init__(self, size):
        self.radius = 50
        self.pos = [size[0]/2, size[1]/2]

    def update(self,particals,size):
        pass

    def move(self, size):
        pass

    def render(self):
        pygame.draw.circle(pygame.display.get_surface(), [255,255,0], self.pos, self.radius)



##########################################
##########################################
##########################################

particals = []

for x in xrange(100):
    particals.append(Partical(size))

particals.append(Planet(size))

##########################################
##########################################

time = 0

while True:

    random.shuffle(particals, random.random)

    time +=1


    for dot in particals:
        dot.update(particals,size)
    for dot in particals:
        dot.move(size)
        dot.render()

    pygame.display.flip()
    screen.fill([0,0,0])

    keys = pygame.key.get_pressed()

    # === ANTI-CRASH ===
    for event in pygame.event.get():
        if event.type == QUIT or keys[K_ESCAPE]:
            pygame.quit(); sys.exit()