import numpy as np
from trafficSimulator import *
sim = Simulation()






n = 15
l = 200
a = 10
b = 50
c = 20
d = 5
e = 80
f = 40

SOUTH_RIGHT = (a, b)
SOUTH_LEFT = (-a, b)
NORTH_RIGHT = (-a, -b)
NORTH_LEFT = (a, -b)

SOUTH_RIGHT_START = (a, l+b)
SOUTH_LEFT_START = (-a, l+b)
NORTH_RIGHT_START = (-a, -l-b)
NORTH_LEFT_START = (a, -l-b)

SOUTH_MIDDLE = (0, b-c)
NORTH_MIDDLE = (0, -b+c)

SOUTH_RIGHT_IN = (d, b-c+d)
SOUTH_RIGHT_OUT = (-d, b-c-d)
SOUTH_RIGHT_MIDDLE = (-a, b-2*c)
NORTH_RIGHT_MIDDLE = (-a, -b+2*c)
NORTH_RIGHT_OUT = (-d, -b+c+d)
NORTH_RIGHT_IN = (d, -b+c-d)

SOUTH_LEFT_IN = (-d, b-c+d)
SOUTH_LEFT_OUT = (d, b-c-d)
SOUTH_LEFT_MIDDLE = (a, b-2*c)
NORTH_LEFT_MIDDLE = (a, -b+2*c)
NORTH_LEFT_OUT = (d, -b+c+d)
NORTH_LEFT_IN = (-d, -b+c-d)

SOUTH_RIGHT_TURN = (f, b-c-c/2)
SOUTH_RIGHT_MERGE = (e, 5)

SOUTH_LEFT_TURN = (-f, b-c-c/2)
SOUTH_LEFT_MERGE = (-e, 5)

NORTH_RIGHT_TURN = (f, -b+c+c/2)
NORTH_RIGHT_MERGE = (e, -5)

NORTH_LEFT_TURN = (-f, -b+c+c/2)
NORTH_LEFT_MERGE = (-e, -5)

sim.create_roads([
    ((10,10),(20,70)),
    ((20,70),(67,75)),
    ((67,75),(63,100)),
    ((67, 75),(75, 40)),
    ((75, 40), (80, 16)),
    ((80, 16), (10, 10)),
    ((80, 16), (90, 18)),
    ((90, 18), (120, 23))

])

def road(a): return range(a, a+n)

sim.create_gen({
    'vehicle_rate': 90,
    'vehicles': [
        [5, {'path': [0,1]}],
        [5, {'path': [1,2]}],
        [5, {'path': [0,1,2]}],
        [5, {'path': [0,1,3]}],
        [5, {'path': [0,1,3,4]}],
        [5, {'path': [1,3]}],
        [5, {'path': [1,3,4]}],
        [5, {'path': [5]}],
        [5, {'path': [6,7]}]

       
    ]
})
# Start simulation
win = Window(sim)
win.zoom = 6
win.run(steps_per_update=5)