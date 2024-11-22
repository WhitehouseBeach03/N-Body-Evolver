import math
import numpy as np

class Particle:

    def __init__(
        self,
        position=np.array([0, 0, 0], dtype=float),
        velocity=np.array([0, 0, 0], dtype=float),
        acceleration=np.array([0, -10, 0], dtype=float),
        name='Ball',
        mass=1.0
    ):
        self.position = position.astype(dtype="float")
        self.velocity = velocity.astype(dtype="float")
        self.acceleration = acceleration.astype(dtype="float")
        self.name = name
        self.mass = mass
        
    def __str__(self):
        return "Particle: {0}, Mass: {1:.3e}, Position: {2}, Velocity: {3}, Acceleration: {4}".format(
            self.name, self.mass,self.position, self.velocity, self.acceleration
        )

    def update(self, deltaT):
        self.position = self.position + deltaT * self.velocity
        self.velocity = self.velocity + deltaT * self.acceleration


