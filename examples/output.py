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


EditorCamera()


def input(key):
    if key == 'tab':
        window.fullscreen = not window.fullscreen


app.run()
    