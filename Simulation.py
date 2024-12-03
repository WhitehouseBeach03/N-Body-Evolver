import pkg_resources
pkg_rescources .require("numpy=='1.26.4")
import numpy as np
import copy
from Particle import Particle

earthMass = 5.97237e24     # https://en.wikipedia.org/wiki/Earth
earthRadius = 63710 * 1e3  # https://en.wikipedia.org/wiki/Earth
Earth = Particle(
    position=np.array([0, 0, 0]),
    velocity=np.array([0, 0, 0]),
    acceleration=np.array([0, 0, 0]),
    name="Earth",
    mass=earthMass
)
satPosition = earthRadius + (35786 * 1e3)
satVelocity = np.sqrt(Earth.G * Earth.mass / satPosition)  # from centrifugal force = gravitational force
Satellite = Particle(
    position=np.array([satPosition, 0, 0]),
    velocity=np.array([0, satVelocity, 0]),
    acceleration=np.array([0, 0, 0]),
    name="Satellite",
    mass=100.
)

time = 0
data = []
for i in range(200000):
    time += 6
    Earth.updateGravitationalAcceleration(Satellite)
    Satellite.updateGravitationalAcceleration(Earth)
    Earth.update(6)
    Satellite.update(6)
    if (i)%100 == 0  :
        data.append( [time, copy.deepcopy(Earth), copy.deepcopy(Satellite)] )

np.save("TwoBodyTest.npy", data, allow_pickle=True)

DataIn = np.load("TwoBodyTest.npy", allow_pickle=True)

def print_particle(particle):
    print("Particle: {}".format(particle.name))
    print("  Mass: {0:.3e}, ".format(particle.mass))
    for attribute in ["position", "velocity", "acceleration"]:
        print("  {}: {}".format(attribute, particle.__getattribute__(attribute) + 0.0))  # add 0.0 to avoid negative zeros!

print("Testing reading the file TwoBodyTest.npy that you have loaded")

float_formatter = lambda x: "%.5e" % x
np.set_printoptions(formatter={'float_kind': float_formatter})


print("Printing First Entry")
print("{}".format(int(DataIn[0][0])))  #time
print_particle(DataIn[0][1])  # Earth
print_particle(DataIn[0][2])  # Satellite

print("Printing Fifth Entry")
print("{}".format(int(DataIn[4][0])))  #time
print_particle(DataIn[4][1])  # Earth
print_particle(DataIn[4][2])  # Satellite

print("Printing Last Entry")
print("{}".format(int(DataIn[-1][0])))  #time
print_particle(DataIn[-1][1])  # Earth
print_particle(DataIn[-1][2])  # Satellite


'''
print("The Earth and Satellite's locations after {0} seconds are:".format((2000*6)))
for particle in [Earth, Satellite]:
    print("  Particle: {}".format(particle.name))
    print("    Mass: {0:.3e}, ".format(particle.mass))
    for attribute in ["position", "velocity", "acceleration"]:
        print("    {}: {}".format(attribute, particle.__getattribute__(attribute) + 0.0))  # add 0.0 to avoid negative zeros!
        
'''
