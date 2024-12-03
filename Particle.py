import math
import numpy as np

class Particle:

    G = 6.67408E-11

    def __init__(
        self,
        position=np.array([0, 0, 0], dtype=float),
        velocity=np.array([0, 0, 0], dtype=float),
        acceleration=np.array([0, 0, 0], dtype=float),
        name='Ball',
        mass=1.0
    ):
        self.position = position.astype(dtype="float")
        self.velocity = velocity.astype(dtype="float")
        self.acceleration = acceleration.astype(dtype="float")
        self.name = name
        self.mass = mass
        
    def __str__(self):
        return "Particle: {0}, Mass: {1}, Position: {2}, Velocity: {3}, Acceleration: {4}".format(
            self.name, self.mass,self.position, self.velocity, self.acceleration
        )

    def kineticEnergy(self):
        velMag = linalg.norm(self.velocity)
        return 1/2 * self.mass * velMag

    def update(self, deltaT):
        self.position = self.position + deltaT * self.velocity
        self.velocity = self.velocity + deltaT * self.acceleration

    def updateGravitationalAcceleration(self, body):
        rVec = body.position - self.position
        rMag = np.linalg.norm(rVec)
        newAcc = rVec * ( self.G * body.mass ) / (rMag**3)
        self.acceleration = newAcc

"""
b1 = Particle(mass=100000)
b2 = Particle(position=np.array([10,0,0]), mass=100000)
b1.updateGravitationalAcceleration(b2)
b2.updateGravitationalAcceleration(b1)
print(b1.acceleration)
print(b2.acceleration)
"""
