#N-Body Simulator, Edward Spence 13/11/24

import contextlib
with contextlib.redirect_stdout(None):
    import pygame
from Body import *

import matplotlib.pyplot as plt

#4-Body symetical system
def t1():
    #system=[]
    q = Body(10, [250, 100, 0], [0.04, 0, 0] )
    w = Body(15, [100, 250, 0], [0, -0.02, 0])
    e = Body(10, [250, 400, 0], [-0.04, 0, 0])
    e = Body(15, [400, 250, 0], [0, 0.02, 0])

def t2():
    #Body.initializeSystem(0.025)
    Body(40, [250, 200], [0.06, 0], 5)
    Body(40, [250, 300], [-0.06, 0], 5)

#Orbit 2d
def t3():
    Body(400, [250, 250], [0.03, 0], 50)
    Body(40, [250, 150], [-0.3, 0], 5)

#Orbit 3d
def t4():
    Body(400, [250, 250, 0], [0, 0, 0.03], 50)
    Body(40, [250, 150, 0], [0, 0, -0.3], 5)

#print(Body.conserved())

#Displays the bodies in motion
def draw2D(syst):

    syst()
    
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    running = True
    screen.fill("purple")
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if(pygame.time.get_ticks()%1000==0):
            print(Body.conserved())
            #print('lol')
            
        screen.fill(pygame.Color(255,0,255,255))

        for body in system:
            pos2D = body.pos[0:2]
            pygame.draw.circle( screen, pygame.Color(255, 200, 100), pos2D, body.radius )

        Body.evolve()
        pygame.display.flip()
        
    pygame.quit()

def plot2D(syst, steps):
    syst()
    positions = []
    for body in system:
        positions.append( [ [body.pos[0]] , [body.pos[1]] ] )

    for i in range(steps):
        Body.evolve()
        for bodynum in range(len(system)):
            B = system[bodynum]
            positions[bodynum][0].append(B.pos[0])
            positions[bodynum][1].append(B.pos[1])
            
    for bodynum in range(len(system)):
        bodyXPlot = positions[bodynum][0]
        bodyYPlot = positions[bodynum][1]
        plt.plot(bodyXPlot, bodyYPlot)

    plt.show()

draw2D(t1)
#system = []
#plot2D(t1, 10000)

def r():
    q = [1,2,3]
    w = [4,5,6]
    plt.plot(q,w)
    plt.plot(w,q)
    plt.show()

#pygame.time.get_ticks()%
