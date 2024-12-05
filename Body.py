import math
import numpy as np

system = []

class Body:

    """
    The Body class stores the relevant infomation for a body and contains the method for evolving the system

    """

    def __init__(self, mass, pos, vel, radius=10, autoAdd=True):

        self.mass = mass
        self.radius = radius

        if len(pos)<3 :
            pos.append(0)
        if len(vel)<3 :
            vel.append(0)
        
        self.pos = np.array(pos)
        self.vel  = np.array(vel)
        self.acc = np.array([0, 0, 0])

        if autoAdd :
            self.add()

    def add(self):
        system.append(self)

    def __str__(self):
        posPrint = f"Position: {self.pos[0]} X, {self.pos[1]} Y"
        velPrint = f"Velocity: {self.vel[0]} X, {self.vel[1]} Y"

        return posPrint+"\n"+velPrint

    def momentum(self):
        #calculates and returns momentum of the body
        return self.mass * self.vel

    def energy(self):
        #calculates and returns total energy of body
        k=0
        u=0

    @staticmethod
    def initializeSystem(gravConst):
        global G
        system = []
        G = gravConst

    #First numerical method to evolve the system forward one time step
    @staticmethod
    def evolve():
        #calulate new acceleration for body 1
        for body1 in system:
            body1.acc = np.array([0, 0, 0])
            for body2 in system:
                if(body1==body2):
                    continue
                rVec = body2.pos - body1.pos
                rMag = np.linalg.norm( rVec )

                if  rMag >=  body2.radius+ body1.radius :
                    newAcc = rVec * ( G*body2.mass ) / (rMag**3)
                else:
                    #newAcc = rVec * ( G * body2.mass / body2.radius**3 )
                    newAcc = np.array([0,0,0])
                    #print("intersect")
                body1.acc = body1.acc + newAcc

        #Update vel and pos vectors
        for body in system:
            body.vel = body.vel + body.acc
            body.pos = body.pos + body.vel

    @staticmethod
    def conserved():
        totalP = np.array([0,0,0])
        for body in system:
            totalP = totalP + body.momentum()
        PMag = np.linalg.norm(totalP)
        return f"Total momentum is {totalP},  Magnitutde {PMag}"

Body.initializeSystem(0.025)

