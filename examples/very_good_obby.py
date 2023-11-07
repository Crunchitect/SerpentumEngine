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
    model='cube',
    color=Color(1.0, 0.0, 0.0, 1.0),
    position=Vec3(10.9735, 0.275319, 0),
    rotation=Vec3(0, 0, 0),
    scale=Vec3(1, 1, 1),
    texture='white_cube.png',
    collider='mesh'
)

Entity(
    model='cube',
    color=Color(1.0, 0.5, 0.0, 1.0),
    position=Vec3(8.69223, 0, 0),
    rotation=Vec3(0, 0, 0),
    scale=Vec3(1, 1, 1),
    texture='white_cube.png',
    collider='mesh'
)

Entity(
    model='cube',
    color=Color(1.0, 0.843137264251709, 0.0, 1.0),
    position=Vec3(6.48968, 0, 0),
    rotation=Vec3(0, 0, 0),
    scale=Vec3(1, 1, 1),
    texture='white_cube.png',
    collider='mesh'
)

Entity(
    model='cube',
    color=Color(0.5, 1.0, 0.0, 1.0),
    position=Vec3(4.7591, 0, 0),
    rotation=Vec3(0, 0, 0),
    scale=Vec3(1, 1, 1),
    texture='white_cube.png',
    collider='mesh'
)

Entity(
    model='cube',
    color=Color(0.0, 0.5, 1.0, 1.0),
    position=Vec3(3.02851, 0, 0),
    rotation=Vec3(0, 0, 0),
    scale=Vec3(1, 1, 1),
    texture='white_cube.png',
    collider='mesh'
)

Entity(
    model='cube',
    color=Color(0.0, 0.0, 1.0, 1.0),
    position=Vec3(1.3766, -0.314651, 0),
    rotation=Vec3(0, 0, 0),
    scale=Vec3(1, 1, 1),
    texture='white_cube.png',
    collider='mesh'
)

Entity(
    model='cube',
    color=Color(0.5, 0.0, 1.0, 1.0),
    position=Vec3(0, 0, 0),
    rotation=Vec3(0, 0, 0),
    scale=Vec3(1, 1, 1),
    texture='white_cube.png',
    collider='mesh'
)

player = FirstPersonController()
player.position = Vec3(0, 0, 0)
player.rotation = Vec3(0, 0, 0)
player.scale = Vec3(1, 1, 1)

Entity(
    model='sphere',
    color=Color(1.0, 1.0, 1.0, 1.0),
    position=Vec3(0, 0, 0),
    rotation=Vec3(0, 0, 0),
    scale=Vec3(1, 1, 1),
    texture='white_cube.png',
    collider='mesh'
)


def input(key):
    if key == 'tab':
        window.fullscreen = not window.fullscreen
    if player.y < -100:
        player.y = 100


app.run()
    