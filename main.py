#N-Body Simulator, Edward Spence 13/11/24

import contextlib
with contextlib.redirect_stdout(None):
    import pygame
from Body import *

import matplotlib.pyplot as plt

#import astro modules
from astroquery.jplhorizons import Horizons
from astropy.time import Time
planetMasses = 1e24 * np.array([0.330, 4.87, 5.97, 0.642, 1898, 568, 86.8, 102])
t = Time("2019-11-27 17:00:00.0", scale="tdb")
objMerc = Horizons(id=1, location="@sun", epochs=t.jd, id_type='id').vectors()

def makePlanet(num):
    obj = Horizons(id=num, location="@sun", epochs=t.jd, id_type='id').vectors()
    pos = []
    for i in ['x','y','z']:
        pos.append( obj[i] )
    vel = []
    for i in ['vx','vy','vz']:
        vel.append( obj[i] )
    PLANET = Body( planetMasses[num-1], pos, vel, autoAdd=False)
    return PLANET

def solarSystem():
    Body.initializeSystem(6.6743e-11)
    for i in range(1,9):
        PLANET = makePlanet(i)
        system.append( PLANET )

#A series of functions defining different systems
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

#Plots body positions over time
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

#draw2D(t3)
