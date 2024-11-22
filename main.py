#N-Body Simulator, Edward Spence 13/11/24

import contextlib
with contextlib.redirect_stdout(None):
    import pygame
from Body import *

import matplotlib.pyplot as plt

def t1():
    q = Body(10, [250, 100, 0], [0.04, 0, 0] )
    w = Body(15, [100, 250, 0], [0, -0.02, 0])
    e = Body(10, [250, 400, 0], [-0.04, 0, 0])
    e = Body(15, [400, 250, 0], [0, 0.02, 0])

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
    print("done")
    
    
plot2D(t1,10)


#pygame.time.get_ticks()%
