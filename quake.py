from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import sys

app = Ursina()

player = FirstPersonController()
player.gravity = 1
player.y = 5
player.speed = 15

class Ground():
    def __init__(self, position):
        self.xmodel = Entity(model='cube', collider='box', scale=1, position=position)

for x in range(100):
    for z in range(100):
        g = Ground(position=(x, 1, z))

def input(key):
    if key == 'q': sys.exit()

app.run()