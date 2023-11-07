from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()
window.borderless = False
    
    
Entity(
    model='None',
    color=Color(1.0, 1.0, 1.0, 1.0),
    position=Vec3(0, 0, 0),
    rotation=Vec3(0, 0, 0),
    scale=Vec3(1, 1, 1),
    texture='None',
    collider='mesh'
)

Entity(
    model='plane',
    color=Color(1.0, 1.0, 1.0, 1.0),
    position=Vec3(0, 0, 0),
    rotation=Vec3(0, 0, 0),
    scale=Vec3(10, 10, 10),
    texture='white_cube.png',
    collider='mesh'
)

player = FirstPersonController()
player.position = Vec3(0, 0, 0)
player.rotation = Vec3(0, 0, 0)
player.scale = Vec3(1, 1, 1)


def input(key):
    if key == 'tab':
        window.fullscreen = not window.fullscreen
    if player.y < -100:
        player.y = y


app.run()
