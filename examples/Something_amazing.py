from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()
window.borderless = False


Entity(
    model='plane',
    color=Color(0.0, 1.0, 0.0, 1.0),
    position=Vec3(2.2963, -3.7963, 0),
    rotation=Vec3(0, 0, 0),
    scale=Vec3(16.2963, 10, 10),
    texture='white_cube.png',
    collider='mesh'
)

player = FirstPersonController()
player.position = Vec3(0, -1, -2.4)
player.rotation = Vec3(0, 0, 0)
player.scale = Vec3(1, 1, 1)

Entity(
    model='cube',
    color=Color(0.6470588445663452, 0.16470588743686676, 0.16470588743686676, 1.0),
    position=Vec3(-15.7407, 0, -20.4259),
    rotation=Vec3(0, 0, 0),
    scale=Vec3(1, 1, 1),
    texture='white_cube.png',
    collider='mesh'
)

Entity(
    model='cube',
    color=Color(0.9803921580314636, 0.501960813999176, 0.4470588266849518, 1.0),
    position=Vec3(-13.6852, 0, 0),
    rotation=Vec3(0, 0, 0),
    scale=Vec3(1, 1, 1),
    texture='white_cube.png',
    collider='mesh'
)

Entity(
    model='cube',
    color=Color(1.0, 1.0, 1.0, 1.0),
    position=Vec3(0, 4.48148, 14.5556),
    rotation=Vec3(0, 0, 0),
    scale=Vec3(1, 1, 1),
    texture='white_cube.png',
    collider='mesh'
)

Entity(
    model='cube',
    color=Color(1.0, 1.0, 1.0, 1.0),
    position=Vec3(0, -4.90741, 0),
    rotation=Vec3(0, 0, 0),
    scale=Vec3(1, 1, 1),
    texture='white_cube.png',
    collider='mesh'
)

Entity(
    model='cube',
    color=Color(0.6470588445663452, 0.16470588743686676, 0.16470588743686676, 1.0),
    position=Vec3(-16.9074, 0, 0),
    rotation=Vec3(0, 0, 0),
    scale=Vec3(1, 1, 1),
    texture='white_cube.png',
    collider='mesh'
)

Entity(
    model='cube',
    color=Color(1.0, 1.0, 1.0, 1.0),
    position=Vec3(0, -5.44444, 0),
    rotation=Vec3(0, 0, 0),
    scale=Vec3(1, 1, 1),
    texture='white_cube.png',
    collider='mesh'
)

Entity(
    model='cube',
    color=Color(0.501960813999176, 0.501960813999176, 0.0, 1.0),
    position=Vec3(-9.96296, 0, 0),
    rotation=Vec3(0, 0, 0),
    scale=Vec3(1, 1, 1),
    texture='white_cube.png',
    collider='mesh'
)

Entity(
    model='cube',
    color=Color(1.0, 1.0, 1.0, 1.0),
    position=Vec3(-6.25926, 0, 0),
    rotation=Vec3(0, 0, 0),
    scale=Vec3(1, 1, 1),
    texture='white_cube.png',
    collider='mesh'
)

Entity(
    model='cube',
    color=Color(0.0, 1.0, 1.0, 1.0),
    position=Vec3(-6.38889, 0, 0),
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
    