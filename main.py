#N-Body Simulator, Edward Spence 13/11/24

#imports external libraries
import contextlib
with contextlib.redirect_stdout(None):
    import pygame
import matplotlib.pyplot as plt
from astropy.coordinates import get_body_barycentric_posvel
from astropy.time import Time

#imports other project files
from Body import *

#Test astro data
t = Time("2019-11-27 17:00:00.0", scale="tdb")
pos, vel = get_body_barycentric_posvel("sun", t, ephemeris="jpl")

#4-Body symetical system
def t1():
    #system=[]
    Body(10, [250, 100, 0], [0.02, 0, 0] )
    Body(10, [100, 250, 0], [0, -0.02, 0])
    Body(10, [250, 400, 0], [-0.02, 0, 0])
    Body(10, [400, 250, 0], [0, 0.02, 0])

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

#Through the earth
def t5():
      Body(10, [250, 100], [0, 0], 10)
      Body(200, [250,250], [0,0], 50)



#Displays the bodies in motion using pygame
def draw2D(syst):

    #initiates the system of bodies
    syst()

    #initiates the pygame window
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    running = True
    screen.fill("purple")

    #runs the simulation untill it is closed
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #tests if important quantities are conserved: momentum
        if(pygame.time.get_ticks()%1000==0):
            print(Body.conserved())
            #print('lol')
            
        screen.fill(pygame.Color(255,0,255,255))

        #draws each body in the system to the screen
        for body in system:
            pos2D = body.pos[0:2]
            pygame.draw.circle( screen, pygame.Color(255, 200, 100), pos2D, body.radius )

        #evolves the system
        Body.evolve()
        
        pygame.display.flip()
    #closes the pygame window
    pygame.quit()


#draw2D(t5)


#pygame.time.get_ticks()%

'''
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
'''
