from ursina import *
import sys
app = Ursina()


window.borderless = False
window.title = 'build.py'
window.exit_button.disable()
entity_list = [Entity()]
entity_list_material = [color.white]
selected_object = Entity()
playtest_enable = False
enable_ui = {
    'add mesh': False,
    'file': False,
    'object': False,
    'move': False,
    'scale': False,
    'rotate': False,
    'color': False
}


def enable_create_ui():
    enable_ui['add mesh'] = not enable_ui['add mesh']
    enable_ui['file'] = False
    enable_ui['object'] = False


def create_cube():
    cube = Entity(
        model='cube',
        texture='white_cube',
        position=(0, 0, 0),
        collider='mesh'
    )
    entity_list.append(cube)
    entity_list_material.append(color.white)
    return cube


def create_sphere():
    sphere = Entity(
        model='sphere',
        texture='white_cube',
        position=(0, 0, 0),
        collider='mesh'
    )
    entity_list.append(sphere)
    entity_list_material.append(color.white)
    return sphere


def create_plane():
    cube = Entity(
        model='plane',
        texture='white_cube',
        position=(0, 0, 0),
        collider='box',
        scale=10
    )
    entity_list.append(cube)
    entity_list_material.append(color.white)
    return cube


def create_quad():
    sphere = Entity(
        model='quad',
        texture='white_cube',
        position=(0, 0, 0),
        collider='mesh',
        scale=10
    )
    entity_list.append(sphere)
    entity_list_material.append(color.white)
    return sphere


def create_circle():
    sphere = Entity(
        model='circle',
        texture='white_cube',
        position=(0, 0, 0),
        collider='mesh'
    )
    entity_list.append(sphere)
    entity_list_material.append(color.white)
    return sphere


def create_camera():
    sphere = Entity(
        model='Models/camera',
        color=color.dark_gray,
        position=(0, 0, 0),
        collider='mesh'
    )
    entity_list.append(sphere)
    entity_list_material.append(color.dark_gray)
    return sphere


def create_player():
    sphere = Entity(
        model='Models/player',
        color=color.white,
        position=(0, 0, 0),
        collider='mesh'
    )
    entity_list.append(sphere)
    entity_list_material.append(color.white)
    return sphere


def enable_file_ui():
    enable_ui['file'] = not enable_ui['file']
    enable_ui['add mesh'] = False
    enable_ui['object'] = False


def enable_object_adjustment():
    enable_ui['object'] = not enable_ui['object']
    enable_ui['add mesh'] = False
    enable_ui['file'] = False


def enable_move():
    enable_ui['move'] = not enable_ui['move']
    enable_ui['scale'] = False
    enable_ui['rotate'] = False


def enable_scale():
    enable_ui['scale'] = not enable_ui['scale']
    enable_ui['move'] = False
    enable_ui['rotate'] = False


def enable_rotate():
    enable_ui['rotate'] = not enable_ui['rotate']
    enable_ui['move'] = False
    enable_ui['scale'] = False


def delete_object():
    global entity_list, entity_list_material, selected_object
    for r, i in enumerate(entity_list):
        if i == selected_object:
            destroy(i)
            entity_list.pop(r)
            entity_list_material.pop(r)
    selected_object = entity_list[0]


def color_white():
    global entity_list, entity_list_material, selected_object
    for r, i in enumerate(entity_list):
        if i == selected_object:
            i.color = color.white
            entity_list_material[r] = color.white


def color_smoke():
    global entity_list, entity_list_material, selected_object
    for r, i in enumerate(entity_list):
        if i == selected_object:
            i.color = color.smoke
            entity_list_material[r] = color.smoke


def color_light_gray():
    global entity_list, entity_list_material, selected_object
    for r, i in enumerate(entity_list):
        if i == selected_object:
            i.color = color.light_gray
            entity_list_material[r] = color.light_gray


def color_gray():
    global entity_list, entity_list_material, selected_object
    for r, i in enumerate(entity_list):
        if i == selected_object:
            i.color = color.gray
            entity_list_material[r] = color.gray


def color_dark_gray():
    global entity_list, entity_list_material, selected_object
    for r, i in enumerate(entity_list):
        if i == selected_object:
            i.color = color.dark_gray
            entity_list_material[r] = color.dark_gray


def color_black():
    global entity_list, entity_list_material, selected_object
    for r, i in enumerate(entity_list):
        if i == selected_object:
            i.color = color.black
            entity_list_material[r] = color.black


def color_red():
    global entity_list, entity_list_material, selected_object
    for r, i in enumerate(entity_list):
        if i == selected_object:
            i.color = color.red
            entity_list_material[r] = color.red


def color_orange():
    global entity_list, entity_list_material, selected_object
    for r, i in enumerate(entity_list):
        if i == selected_object:
            i.color = color.orange
            entity_list_material[r] = color.orange


def color_yellow():
    global entity_list, entity_list_material, selected_object
    for r, i in enumerate(entity_list):
        if i == selected_object:
            i.color = color.yellow
            entity_list_material[r] = color.yellow


def color_lime():
    global entity_list, entity_list_material, selected_object
    for r, i in enumerate(entity_list):
        if i == selected_object:
            i.color = color.lime
            entity_list_material[r] = color.lime


def color_green():
    global entity_list, entity_list_material, selected_object
    for r, i in enumerate(entity_list):
        if i == selected_object:
            i.color = color.green
            entity_list_material[r] = color.green


def color_turquoise():
    global entity_list, entity_list_material, selected_object
    for r, i in enumerate(entity_list):
        if i == selected_object:
            i.color = color.turquoise
            entity_list_material[r] = color.turquoise


def color_cyan():
    global entity_list, entity_list_material, selected_object
    for r, i in enumerate(entity_list):
        if i == selected_object:
            i.color = color.cyan
            entity_list_material[r] = color.cyan


def color_azure():
    global entity_list, entity_list_material, selected_object
    for r, i in enumerate(entity_list):
        if i == selected_object:
            i.color = color.azure
            entity_list_material[r] = color.azure


def color_blue():
    global entity_list, entity_list_material, selected_object
    for r, i in enumerate(entity_list):
        if i == selected_object:
            i.color = color.blue
            entity_list_material[r] = color.blue


def color_violet():
    global entity_list, entity_list_material, selected_object
    for r, i in enumerate(entity_list):
        if i == selected_object:
            i.color = color.violet
            entity_list_material[r] = color.violet


def color_magenta():
    global entity_list, entity_list_material, selected_object
    for r, i in enumerate(entity_list):
        if i == selected_object:
            i.color = color.magenta
            entity_list_material[r] = color.magenta


def color_pink():
    global entity_list, entity_list_material, selected_object
    for r, i in enumerate(entity_list):
        if i == selected_object:
            i.color = color.pink
            entity_list_material[r] = color.pink


def color_brown():
    global entity_list, entity_list_material, selected_object
    for r, i in enumerate(entity_list):
        if i == selected_object:
            i.color = color.brown
            entity_list_material[r] = color.brown


def color_olive():
    global entity_list, entity_list_material, selected_object
    for r, i in enumerate(entity_list):
        if i == selected_object:
            i.color = color.olive
            entity_list_material[r] = color.olive


def color_peach():
    global entity_list, entity_list_material, selected_object
    for r, i in enumerate(entity_list):
        if i == selected_object:
            i.color = color.peach
            entity_list_material[r] = color.peach


def color_gold():
    global entity_list, entity_list_material, selected_object
    for r, i in enumerate(entity_list):
        if i == selected_object:
            i.color = color.gold
            entity_list_material[r] = color.gold


def color_salmon():
    global entity_list, entity_list_material, selected_object
    for r, i in enumerate(entity_list):
        if i == selected_object:
            i.color = color.salmon
            entity_list_material[r] = color.salmon


class ColorButtons:
    white_text = Text(
        text='White',
        position=(-.58 + .15, 0.41),
        z=-1,
        font='Models/JetBrainsMono-Medium.ttf',
        enabled=False
    )
    white_button = Button(
        text=white_text,
        scale=(0.3, .1),
        position=(-.5 + .15, 0.4),
        enabled=False,
        on_click=color_white
    )
    smoke_text = Text(
        text='Smoke',
        position=(-.58 + .15, 0.31),
        z=-1,
        font='Models/JetBrainsMono-Medium.ttf',
        enabled=False
    )
    smoke_button = Button(
        text=smoke_text,
        scale=(0.3, .1),
        position=(-.5 + .15, 0.3),
        enabled=False,
        on_click=color_smoke
    )
    light_gray_text = Text(
        text='Light Gray',
        position=(-.58 + .15, 0.21),
        z=-1,
        font='Models/JetBrainsMono-Medium.ttf',
        enabled=False
    )
    light_gray_button = Button(
        text=light_gray_text,
        scale=(0.3, .1),
        position=(-.5 + .15, 0.2),
        enabled=False,
        on_click=color_light_gray
    )
    gray_text = Text(
        text='Gray',
        position=(-.58 + .15, 0.11),
        z=-1,
        font='Models/JetBrainsMono-Medium.ttf',
        enabled=False
    )
    gray_button = Button(
        text=gray_text,
        scale=(0.3, .1),
        position=(-.5 + .15, 0.1),
        enabled=False,
        on_click=color_gray
    )
    dark_gray_text = Text(
        text='Dark Gray',
        position=(-.58 + .15, 0.01),
        z=-1,
        font='Models/JetBrainsMono-Medium.ttf',
        enabled=False
    )
    dark_gray_button = Button(
        text=dark_gray_text,
        scale=(0.3, .1),
        position=(-.5 + .15, 0),
        enabled=False,
        on_click=color_dark_gray
    )
    black_text = Text(
        text='Black',
        position=(-.58 + .15, -0.09),
        z=-1,
        font='Models/JetBrainsMono-Medium.ttf',
        enabled=False
    )
    black_button = Button(
        text=black_text,
        scale=(0.3, .1),
        position=(-.5 + .15, -0.1),
        enabled=False,
        on_click=color_black
    )
    red_text = Text(
        text='Red',
        position=(-.58 + .15, -0.19),
        z=-1,
        font='Models/JetBrainsMono-Medium.ttf',
        enabled=False
    )
    red_button = Button(
        text=red_text,
        scale=(0.3, .1),
        position=(-.5 + .15, -0.2),
        enabled=False,
        on_click=color_red
    )
    orange_text = Text(
        text='Orange',
        position=(-.58 + .15, -0.29),
        z=-1,
        font='Models/JetBrainsMono-Medium.ttf',
        enabled=False
    )
    orange_button = Button(
        text=orange_text,
        scale=(0.3, .1),
        position=(-.5 + .15, -0.3),
        enabled=False,
        on_click=color_orange
    )
    yellow_text = Text(
        text='Yellow',
        position=(-.58 + .15, -0.39),
        z=-1,
        font='Models/JetBrainsMono-Medium.ttf',
        enabled=False
    )
    yellow_button = Button(
        text=yellow_text,
        scale=(0.3, .1),
        position=(-.5 + .15, -0.4),
        enabled=False,
        on_click=color_yellow
    )
    lime_text = Text(
        text='Lime',
        position=(-.58 + .5, 0.41),
        z=-1,
        font='Models/JetBrainsMono-Medium.ttf',
        enabled=False
    )
    lime_button = Button(
        text=lime_text,
        scale=(0.3, .1),
        position=(-.5 + .5, 0.4),
        enabled=False,
        on_click=color_lime
    )
    green_text = Text(
        text='Green',
        position=(-.58 + .5, .31),
        z=-1,
        font='Models/JetBrainsMono-Medium.ttf',
        enabled=False
    )
    green_button = Button(
        text=green_text,
        scale=(0.3, .1),
        position=(-.5 + .5, .3),
        enabled=False,
        on_click=color_green
    )
    turquoise_text = Text(
        text='Turquoise',
        position=(-.58 + .5, .21),
        z=-1,
        font='Models/JetBrainsMono-Medium.ttf',
        enabled=False
    )
    turquoise_button = Button(
        text=turquoise_text,
        scale=(0.3, .1),
        position=(-.5 + .5, .2),
        enabled=False,
        on_click=color_turquoise
    )
    cyan_text = Text(
        text='Cyan',
        position=(-.58 + .5, .11),
        z=-1,
        font='Models/JetBrainsMono-Medium.ttf',
        enabled=False
    )
    cyan_button = Button(
        text=cyan_text,
        scale=(0.3, .1),
        position=(-.5 + .5, .1),
        enabled=False,
        on_click=color_cyan
    )
    azure_text = Text(
        text='Azure',
        position=(-.58 + .5, .01),
        z=-1,
        font='Models/JetBrainsMono-Medium.ttf',
        enabled=False
    )
    azure_button = Button(
        text=azure_text,
        scale=(0.3, .1),
        position=(-.5 + .5, 0),
        enabled=False,
        on_click=color_azure
    )
    blue_text = Text(
        text='Blue',
        position=(-.58 + .5, -.09),
        z=-1,
        font='Models/JetBrainsMono-Medium.ttf',
        enabled=False
    )
    blue_button = Button(
        text=azure_text,
        scale=(0.3, .1),
        position=(-.5 + .5, -.1),
        enabled=False,
        on_click=color_blue
    )
    violet_text = Text(
        text='Violet',
        position=(-.58 + .5, -.19),
        z=-1,
        font='Models/JetBrainsMono-Medium.ttf',
        enabled=False
    )
    violet_button = Button(
        text=violet_text,
        scale=(0.3, .1),
        position=(-.5 + .5, -.2),
        enabled=False,
        on_click=color_violet
    )
    magenta_text = Text(
        text='Magenta',
        position=(-.58 + .5, -.29),
        z=-1,
        font='Models/JetBrainsMono-Medium.ttf',
        enabled=False
    )
    magenta_button = Button(
        text=magenta_text,
        scale=(0.3, .1),
        position=(-.5 + .5, -.3),
        enabled=False,
        on_click=color_magenta
    )
    pink_text = Text(
        text='Pink',
        position=(-.58 + .5, -.39),
        z=-1,
        font='Models/JetBrainsMono-Medium.ttf',
        enabled=False
    )
    pink_button = Button(
        text=pink_text,
        scale=(0.3, .1),
        position=(-.5 + .5, -.4),
        enabled=False,
        on_click=color_pink
    )
    brown_text = Text(
        text='Brown',
        position=(-.58 + .85, .41),
        z=-1,
        font='Models/JetBrainsMono-Medium.ttf',
        enabled=False
    )
    brown_button = Button(
        text=brown_text,
        scale=(0.3, .1),
        position=(-.5 + .85, .4),
        enabled=False,
        on_click=color_brown
    )
    olive_text = Text(
        text='Olive',
        position=(-.58 + .85, .31),
        z=-1,
        font='Models/JetBrainsMono-Medium.ttf',
        enabled=False
    )
    olive_button = Button(
        text=olive_text,
        scale=(0.3, .1),
        position=(-.5 + .85, .3),
        enabled=False,
        on_click=color_olive
    )
    peach_text = Text(
        text='Peach',
        position=(-.58 + .85, .21),
        z=-1,
        font='Models/JetBrainsMono-Medium.ttf',
        enabled=False
    )
    peach_button = Button(
        text=peach_text,
        scale=(0.3, .1),
        position=(-.5 + .85, .2),
        enabled=False,
        on_click=color_peach
    )
    gold_text = Text(
        text='Gold',
        position=(-.58 + .85, .11),
        z=-1,
        font='Models/JetBrainsMono-Medium.ttf',
        enabled=False
    )
    gold_button = Button(
        text=gold_text,
        scale=(0.3, .1),
        position=(-.5 + .85, .1),
        enabled=False,
        on_click=color_gold
    )
    salmon_text = Text(
        text='Salmon',
        position=(-.58 + .85, .01),
        z=-1,
        font='Models/JetBrainsMono-Medium.ttf',
        enabled=False
    )
    salmon_button = Button(
        text=peach_text,
        scale=(0.3, .1),
        position=(-.5 + .85, -.0),
        enabled=False,
        on_click=color_salmon
    )


def show_color():
    global selected_object, enable_ui
    enable_ui['color'] = not enable_ui['color']
    ColorButtons.white_text.enabled = enable_ui['color']
    ColorButtons.white_button.enabled = enable_ui['color']
    ColorButtons.smoke_text.enabled = enable_ui['color']
    ColorButtons.smoke_button.enabled = enable_ui['color']
    ColorButtons.light_gray_text.enabled = enable_ui['color']
    ColorButtons.light_gray_button.enabled = enable_ui['color']
    ColorButtons.gray_text.enabled = enable_ui['color']
    ColorButtons.gray_button.enabled = enable_ui['color']
    ColorButtons.dark_gray_text.enabled = enable_ui['color']
    ColorButtons.dark_gray_button.enabled = enable_ui['color']
    ColorButtons.black_text.enabled = enable_ui['color']
    ColorButtons.black_button.enabled = enable_ui['color']
    ColorButtons.red_text.enabled = enable_ui['color']
    ColorButtons.red_button.enabled = enable_ui['color']
    ColorButtons.orange_text.enabled = enable_ui['color']
    ColorButtons.orange_button.enabled = enable_ui['color']
    ColorButtons.yellow_text.enabled = enable_ui['color']
    ColorButtons.yellow_button.enabled = enable_ui['color']
    ColorButtons.lime_text.enabled = enable_ui['color']
    ColorButtons.lime_button.enabled = enable_ui['color']
    ColorButtons.green_text.enabled = enable_ui['color']
    ColorButtons.green_button.enabled = enable_ui['color']
    ColorButtons.turquoise_text.enabled = enable_ui['color']
    ColorButtons.turquoise_button.enabled = enable_ui['color']
    ColorButtons.cyan_text.enabled = enable_ui['color']
    ColorButtons.cyan_button.enabled = enable_ui['color']
    ColorButtons.azure_text.enabled = enable_ui['color']
    ColorButtons.azure_button.enabled = enable_ui['color']
    ColorButtons.blue_text.enabled = enable_ui['color']
    ColorButtons.blue_button.enabled = enable_ui['color']
    ColorButtons.violet_text.enabled = enable_ui['color']
    ColorButtons.violet_button.enabled = enable_ui['color']
    ColorButtons.magenta_text.enabled = enable_ui['color']
    ColorButtons.magenta_button.enabled = enable_ui['color']
    ColorButtons.pink_text.enabled = enable_ui['color']
    ColorButtons.pink_button.enabled = enable_ui['color']
    ColorButtons.brown_text.enabled = enable_ui['color']
    ColorButtons.brown_button.enabled = enable_ui['color']
    ColorButtons.olive_text.enabled = enable_ui['color']
    ColorButtons.olive_button.enabled = enable_ui['color']
    ColorButtons.peach_text.enabled = enable_ui['color']
    ColorButtons.peach_button.enabled = enable_ui['color']
    ColorButtons.gold_text.enabled = enable_ui['color']
    ColorButtons.gold_button.enabled = enable_ui['color']
    ColorButtons.salmon_text.enabled = enable_ui['color']
    ColorButtons.salmon_button.enabled = enable_ui['color']


def new_file_func():
    global entity_list, entity_list_material
    for i in entity_list:
        destroy(i)
    entity_list = [Entity()]
    entity_list_material = [color.white]


def save_func():
    no_cam = True
    player_cam = False
    code = """from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()
window.borderless = False
    
    """
    for i in entity_list:
        print(i.model)
        if str(i.model).replace('render/scene/entity/', '') == 'Models/camera':
            no_cam = False
            player_cam = False
            code += f"""
camera.position = {i.position},
camera.rotation = {i.rotation}
"""
        elif str(i.model).replace('render/scene/entity/', '') == 'Models/player':
            no_cam = False
            player_cam = True
            code += f"""
player = FirstPersonController()
player.position = {i.position}
player.rotation = {i.rotation}
player.scale = {i.scale}
"""
        else:
            code += f"""
Entity(
    model='{str(i.model).replace('render/scene/entity/', '')}',
    color={i.color},
    position={i.position},
    rotation={i.rotation},
    scale={i.scale},
    texture='{i.texture}',
    collider='mesh'
)
"""
    if no_cam:
        code += """

EditorCamera()


def input(key):
    if key == 'tab':
        window.fullscreen = not window.fullscreen


app.run()
    """
    elif not player_cam:
        code += """

def input(key):
    if key == 'tab':
        window.fullscreen = not window.fullscreen


app.run()
"""
    else:
        code += """

def input(key):
    if key == 'tab':
        window.fullscreen = not window.fullscreen
    if player.y < -100:
        player.y = y


app.run()
"""
    with open("examples/output.py", "w") as file:
        file.write(code)


def save_as_func():
    no_cam = True
    player_cam = False
    code = """from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()
window.borderless = False

"""
    for i in entity_list:
        print(i.model)
        if str(i.model).replace('render/scene/entity/', '') == 'Models/camera':
            no_cam = False
            player_cam = False
            code += f"""
camera.position = {i.position},
camera.rotation = {i.rotation}
"""
        elif str(i.model).replace('render/scene/entity/', '') == 'Models/player':
            no_cam = False
            player_cam = True
            code += f"""
player = FirstPersonController()
player.position = {i.position}
player.rotation = {i.rotation}
player.scale = {i.scale}
"""
        else:
            code += f"""
Entity(
    model='{str(i.model).replace('render/scene/entity/', '')}',
    color={i.color},
    position={i.position},
    rotation={i.rotation},
    scale={i.scale},
    texture='{i.texture}',
    collider='mesh'
)
"""
    if no_cam:
        code += """

EditorCamera()


def input(key):
    if key == 'tab':
        window.fullscreen = not window.fullscreen


app.run()
        """
    elif not player_cam:
        code += """

def input(key):
    if key == 'tab':
        window.fullscreen = not window.fullscreen


app.run()
"""
    else:
        code += """

def input(key):
    if key == 'tab':
        window.fullscreen = not window.fullscreen
    if player.y < -100:
        player.y = 100


app.run()
    """
    input_field = InputField(default_value='___')
    input_field.next_field = None

    def submit():
        window.title = f"{input_field.text}.py"
        button.disable()
        with open(f"{input_field.text}.py", "w") as file:
            file.write(code)
        input_field.disable()

    button = Button(
        text='Submit',
        scale=(.1, .05),
        on_click=submit,
        y=-.1
    )


def playtest_func():
    global entity_list, playtest_enable
    player_detected = False
    for i in entity_list:
        if str(i.model).replace('render/scene/entity/', '') == 'Models/player':
            player_detected = True
    if player_detected:
        playtest_enable = not playtest_enable


def copy_selection():
    a = deepcopy(selected_object)
    entity_list.append(a)
    a.model = deepcopy(selected_object.model)
    entity_list_material.append(selected_object.color)


class ObjectAdjustment:
    move_text = Text(
        text='Move',
        position=(-.58 - .22, 0.41),
        z=-1,
        font='Models/JetBrainsMono-Medium.ttf'
    )
    move_button = Button(
        text=move_text,
        scale=(0.3, .1),
        position=(-.5 - .22, 0.4),
        on_click=enable_move
    )
    scale_text = Text(
        text='Scale',
        position=(-.58 - .22, 0.31),
        z=-1,
        font='Models/JetBrainsMono-Medium.ttf'
    )
    scale_button = Button(
        text=scale_text,
        scale=(0.3, .1),
        position=(-.5 - .22, 0.3),
        on_click=enable_scale
    )
    rotate_text = Text(
        text='Rotate',
        position=(-.58 - .22, 0.21),
        z=-1,
        font='Models/JetBrainsMono-Medium.ttf'
    )
    rotate_button = Button(
        text=rotate_text,
        scale=(0.3, .1),
        position=(-.5 - .22, 0.2),
        on_click=enable_rotate
    )
    delete_text = Text(
        text='Delete',
        position=(-.58 - .22, 0.11),
        z=-1,
        font='Models/JetBrainsMono-Medium.ttf'
    )
    delete_button = Button(
        text=delete_text,
        scale=(0.3, .1),
        position=(-.5 - .22, 0.1),
        on_click=delete_object
    )
    color_text = Text(
        text='Color',
        position=(-.58 - .22, 0.01),
        z=-1,
        font='Models/JetBrainsMono-Medium.ttf'
    )
    color_button = Button(
        text=color_text,
        scale=(0.3, .1),
        position=(-.5 - .22, 0.0),
        on_click=show_color
    )
    copy_selection_text = Text(
        text='Copy Selection',
        position=(-.58 - .22, -0.09),
        z=-1,
        font='Models/JetBrainsMono-Medium.ttf'
    )
    copy_selection_button = Button(
        text=color_text,
        scale=(0.3, .1),
        position=(-.5 - .22, -0.1),
        on_click=copy_selection
    )


class Files:
    save_file_text = Text(
        text='Save File',
        position=(-.58 - .24, 0.41),
        z=-1,
        font='Models/JetBrainsMono-Medium.ttf'
    )
    save_file_button = Button(
        text=save_file_text,
        scale=(0.3, .1),
        position=(-.5 - .24, 0.4),
        on_click=save_func
    )
    save_as_file_text = Text(
        text='Save File As',
        position=(-.58 - .25, 0.31),
        z=-1,
        font='Models/JetBrainsMono-Medium.ttf'
    )
    save_as_file_button = Button(
        text=save_file_text,
        scale=(0.3, .1),
        position=(-.5 - .24, 0.3),
        on_click=save_as_func
    )
    new_file_text = Text(
        text='New File',
        position=(-.58 - .25, 0.21),
        z=-1,
        font='Models/JetBrainsMono-Medium.ttf'
    )
    new_file_button = Button(
        text=new_file_text,
        scale=(0.3, .1),
        position=(-.5 - .24, 0.2),
        on_click=new_file_func
    )
    playtest_text = Text(
        text='Playtest',
        position=(-.58 - .25, 0.11),
        z=-1,
        font='Models/JetBrainsMono-Medium.ttf'
    )
    playtest_button = Button(
        text=playtest_text,
        scale=(0.3, .1),
        position=(-.5 - .24, 0.1),
        on_click=playtest_func
    )


class Meshes:
    text_add_cube = Text(
            text='Create Cube',
            position=(-.58 - .2, 0.41),
            z=-1,
            font='Models/JetBrainsMono-Medium.ttf'
        )

    add_cube = Button(
        text=text_add_cube,
        on_click=create_cube,
        scale=(0.3, .1),
        position=(-.5-.2, 0.4)
    )

    text_add_sphere = Text(
            text='Create Sphere',
            position=(-.59-.2, .31),
            z=-1,
            font='Models/JetBrainsMono-Medium.ttf'
    )

    add_sphere = Button(
        text=text_add_sphere,
        on_click=create_sphere,
        scale=(0.3, .1),
        position=(-.5-.2, .3)
    )

    text_add_quad = Text(
        text='Create Quad',
        position=(-.58 - .2, 0.21),
        z=-1,
        font='Models/JetBrainsMono-Medium.ttf'
    )

    add_quad = Button(
        text=text_add_quad,
        on_click=create_quad,
        scale=(0.3, .1),
        position=(-.5 - .2, 0.2)
    )

    text_add_plane = Text(
        text='Create Plane',
        position=(-.59 - .2, .11),
        z=-1,
        font='Models/JetBrainsMono-Medium.ttf'
    )

    add_plane = Button(
        text=text_add_plane,
        on_click=create_plane,
        scale=(0.3, .1),
        position=(-.5 - .2, .1)
    )

    text_add_circle = Text(
        text='Create Circle',
        position=(-.59 - .2, .01),
        z=-1,
        font='Models/JetBrainsMono-Medium.ttf'
    )

    add_circle = Button(
        text=text_add_circle,
        on_click=create_circle,
        scale=(0.3, .1),
        position=(-.5 - .2, 0)
    )

    text_add_camera = Text(
        text='Create Camera',
        position=(-.59 - .2, -.09),
        z=-1,
        font='Models/JetBrainsMono-Medium.ttf'
    )

    add_camera = Button(
        text=text_add_camera,
        on_click=create_camera,
        scale=(0.3, .1),
        position=(-.5 - .2, -.1)
    )
    text_add_player = Text(
        text='Create Player',
        position=(-.59 - .2, -.19),
        z=-1,
        font='Models/JetBrainsMono-Medium.ttf'
    )

    add_player = Button(
        text=text_add_player,
        on_click=create_player,
        scale=(0.3, .1),
        position=(-.5 - .2, -.2)
    )


def move_x():
    init_cursor_x = mouse.x

    def final_move_x():
        final_cursor_x = mouse.x
        change_x = final_cursor_x - init_cursor_x
        change_x *= 20
        selected_object.x -= change_x
        destroy(final_move)
        MoveArrow.x.position = selected_object.position
        MoveArrow.x.x += 0.6
        MoveArrow.y.position = selected_object.position
        MoveArrow.y.y += 0.6
        MoveArrow.z.position = selected_object.position
        MoveArrow.z.z += 0.6

    final_move = Button(
        scale=2,
        on_click=final_move_x
    )


def move_y():
    init_cursor_y = mouse.y

    def final_move_y():
        final_cursor_y = mouse.y
        change_y = final_cursor_y - init_cursor_y
        change_y *= 20
        selected_object.y += change_y
        destroy(final_move)
        MoveArrow.x.position = selected_object.position
        MoveArrow.x.x += 0.6
        MoveArrow.y.position = selected_object.position
        MoveArrow.y.y += 0.6
        MoveArrow.z.position = selected_object.position
        MoveArrow.z.z += 0.6

    final_move = Button(
        scale=2,
        on_click=final_move_y
    )


def move_z():
    init_cursor_z = mouse.x

    def final_move_z():
        final_cursor_z = mouse.x
        change_z = final_cursor_z - init_cursor_z
        change_z *= 20
        selected_object.z += change_z
        destroy(final_move)
        MoveArrow.x.position = selected_object.position
        MoveArrow.y.position = selected_object.position
        MoveArrow.z.position = selected_object.position

    final_move = Button(
        scale=2,
        on_click=final_move_z
    )


class MoveArrow:
    x = Button(
        parent=scene,
        model='Models/arrow',
        rotation_x=-90,
        rotation_y=-90,
        scale=1.2,
        color=color.red,
        on_click=move_x
    )
    y = Button(
        parent=scene,
        model='Models/arrow',
        scale=1.2,
        color=color.green,
        on_click=move_y
    )
    z = Button(
        parent=scene,
        model='Models/arrow',
        rotation_z=-90,
        rotation_y=90,
        scale=1.2,
        color=color.blue,
        on_click=move_z
    )


def scale_x():
    init_cursor_x = mouse.x

    def final_move_x():
        final_cursor_x = mouse.x
        change_x = final_cursor_x - init_cursor_x
        change_x *= 20
        selected_object.scale_x += abs(change_x)
        destroy(final_move)
        ScaleArrow.x.position = selected_object.position
        ScaleArrow.x.x += 0.6
        ScaleArrow.y.position = selected_object.position
        ScaleArrow.y.y += 0.6
        ScaleArrow.z.position = selected_object.position
        ScaleArrow.z.z += 0.6

    final_move = Button(
        scale=2,
        on_click=final_move_x
    )


def scale_y():
    init_cursor_y = mouse.y

    def final_move_y():
        final_cursor_y = mouse.y
        change_y = final_cursor_y - init_cursor_y
        change_y *= 20
        selected_object.scale_y += abs(change_y)
        destroy(final_move)
        ScaleArrow.x.position = selected_object.position
        ScaleArrow.x.x += 0.6
        ScaleArrow.y.position = selected_object.position
        ScaleArrow.y.y += 0.6
        ScaleArrow.z.position = selected_object.position
        ScaleArrow.z.z += 0.6

    final_move = Button(
        scale=2,
        on_click=final_move_y
    )


def scale_z():
    init_cursor_z = mouse.x

    def final_move_z():
        final_cursor_z = mouse.x
        change_z = final_cursor_z - init_cursor_z
        change_z *= 20
        selected_object.scale_z += abs(change_z)
        destroy(final_move)
        ScaleArrow.x.position = selected_object.position
        ScaleArrow.x.x += 0.6
        ScaleArrow.y.position = selected_object.position
        ScaleArrow.y.y += 0.6
        ScaleArrow.z.position = selected_object.position
        ScaleArrow.z.z += 0.6

    final_move = Button(
        scale=2,
        on_click=final_move_z
    )


class ScaleArrow:

    x = Button(
        parent=scene,
        model='Models/scale_arrow',
        rotation_x=-90,
        rotation_y=-90,
        scale=1.2,
        color=color.red,
        on_click=scale_x
    )
    y = Button(
        parent=scene,
        model='Models/scale_arrow',
        scale=1.2,
        color=color.green,
        on_click=scale_y
    )
    z = Button(
        parent=scene,
        model='Models/scale_arrow',
        rotation_z=-90,
        rotation_y=90,
        scale=1.2,
        color=color.blue,
        on_click=scale_z
    )


def rotate_x():
    print('x')
    init_cursor_x = mouse.x

    def final_move_x():
        final_cursor_x = mouse.x
        change_x = final_cursor_x - init_cursor_x
        change_x *= 20
        selected_object.rotation_x -= change_x
        destroy(final_move)
        RotateArrow.xx.position = selected_object.position
        RotateArrow.yy.position = selected_object.position
        RotateArrow.zz.position = selected_object.position

    final_move = Button(
        scale=2,
        on_click=final_move_x
    )


def rotate_y():
    print('y')
    init_cursor_y = mouse.y

    def final_move_y():
        final_cursor_y = mouse.y
        change_y = final_cursor_y - init_cursor_y
        change_y *= 20
        selected_object.rotation_y += change_y
        destroy(final_move)
        RotateArrow.xx.position = selected_object.position
        RotateArrow.yy.position = selected_object.position
        RotateArrow.zz.position = selected_object.position

    final_move = Button(
        scale=2,
        on_click=final_move_y
    )


def rotate_z():
    init_cursor_z = mouse.x
    print('z')

    def final_move_z():
        final_cursor_z = mouse.x
        change_z = final_cursor_z - init_cursor_z
        change_z *= 20
        selected_object.rotation_z += change_z
        destroy(final_move)
        RotateArrow.xx.position = selected_object.position
        RotateArrow.yy.position = selected_object.position
        RotateArrow.zz.position = selected_object.position

    final_move = Button(
        scale=2,
        on_click=final_move_z
    )


class RotateArrow:

    xx = Button(
        parent=scene,
        model='circle',
        scale=1.2,
        color=color.red,
        on_click=rotate_x,
        double_sided=True
    )
    yy = Button(
        parent=scene,
        model='circle',
        scale=1.2,
        rotation_x=-90,
        rotation_y=-90,
        color=color.green,
        on_click=rotate_y,
        double_sided=True
    )
    zz = Button(
        parent=scene,
        model='circle',
        scale=1.2,
        rotation_z=-90,
        rotation_y=90,
        color=color.blue,
        on_click=rotate_z,
        double_sided=True
    )


Button(
    text=Text(
        text='File',
        x=-.03 - .85,
        y=.01 + .48,
        z=-1,
        font='Models/JetBrainsMono-Bold.ttf'
    ),
    scale=(0.1, 0.05),
    x=-.85,
    y=.48,
    on_click=enable_file_ui
)
Button(
    text=Text(
        text='Add',
        x=-.03 - .74,
        y=.01 + .48,
        z=-1,
        font='Models/JetBrainsMono-Bold.ttf'
    ),
    scale=(0.1, 0.05),
    x=-.75,
    y=.48,
    on_click=enable_create_ui
)
Button(
    text=Text(
        text='Object',
        x=-.03 - .65,
        y=.01 + .48,
        z=-1,
        font='Models/JetBrainsMono-Bold.ttf'
    ),
    scale=(0.12, 0.05),
    x=-.64,
    y=.48,
    on_click=enable_object_adjustment
)


e_cam = EditorCamera()


def input(key):
    global selected_object, e_cam
    if key == 'tab':
        window.fullscreen = not window.fullscreen
    if key == 'alt' and key == 'f4':
        app.destroy()
        sys.exit()
    if key == 'left mouse down':
        for r, i in enumerate(entity_list):
            if i.hovered:
                i.color = color.gold
                selected_object = i
                MoveArrow.x.position = (i.x + .6, i.y, i.z)
                MoveArrow.y.position = (i.x, i.y + .6, i.z)
                MoveArrow.z.position = (i.x, i.y, i.z + .6)
            else:
                i.color = entity_list_material[r]
    if key == 'delete':
        delete_object()
    if key == 'm':
        enable_move()
    if key == 's' and not playtest_enable:
        enable_scale()
    if key == 'r':
        enable_rotate()
    if held_keys['w'] and playtest_enable:
        for i in entity_list:
            if str(i.model).replace('render/scene/entity/', '') == 'Models/player':
                i.position += i.forward * 0.1
    if held_keys['s'] and playtest_enable:
        for i in entity_list:
            if str(i.model).replace('render/scene/entity/', '') == 'Models/player':
                i.position += i.back * 0.1
    if held_keys['a'] and playtest_enable:
        for i in entity_list:
            if str(i.model).replace('render/scene/entity/', '') == 'Models/player':
                i.position += i.left * 0.1
    if held_keys['d'] and playtest_enable:
        for i in entity_list:
            if str(i.model).replace('render/scene/entity/', '') == 'Models/player':
                i.position += i.right * 0.1
    if held_keys['space'] and playtest_enable:
        for i in entity_list:
            if str(i.model).replace('render/scene/entity/', '') == 'Models/player':
                i.y += 10
    if key == 'ctrl':
        if held_keys['ctrl'] and held_keys['d']:
            copy_selection()
        if key == 'ctrl' and key == 'v':
            copy_selection()


tooltip_mov = Tooltip(f'')
tooltip_scale = Tooltip(f'')
tooltip_rot = Tooltip(f'')


def update():
    global tooltip_mov, tooltip_scale, tooltip_rot
    Meshes.add_cube.enabled = enable_ui['add mesh']
    Meshes.add_sphere.enabled = enable_ui['add mesh']
    Meshes.text_add_cube.enabled = enable_ui['add mesh']
    Meshes.text_add_sphere.enabled = enable_ui['add mesh']
    Meshes.add_quad.enabled = enable_ui['add mesh']
    Meshes.add_plane.enabled = enable_ui['add mesh']
    Meshes.text_add_quad.enabled = enable_ui['add mesh']
    Meshes.text_add_plane.enabled = enable_ui['add mesh']
    Meshes.text_add_circle.enabled = enable_ui['add mesh']
    Meshes.add_camera.enabled = enable_ui['add mesh']
    Meshes.text_add_camera.enabled = enable_ui['add mesh']
    Meshes.add_circle.enabled = enable_ui['add mesh']
    Meshes.text_add_player.enabled = enable_ui['add mesh']
    Meshes.add_player.enabled = enable_ui['add mesh']
    Files.save_file_button.enabled = enable_ui['file']
    Files.save_file_text.enabled = enable_ui['file']
    Files.save_as_file_button.enabled = enable_ui['file']
    Files.save_as_file_text.enabled = enable_ui['file']
    Files.new_file_button.enabled = enable_ui['file']
    Files.new_file_text.enabled = enable_ui['file']
    Files.playtest_button.enabled = enable_ui['file']
    Files.playtest_text.enabled = enable_ui['file']
    ObjectAdjustment.move_button.enabled = enable_ui['object']
    ObjectAdjustment.scale_button.enabled = enable_ui['object']
    ObjectAdjustment.move_text.enabled = enable_ui['object']
    ObjectAdjustment.scale_text.enabled = enable_ui['object']
    ObjectAdjustment.delete_button.enabled = enable_ui['object']
    ObjectAdjustment.delete_text.enabled = enable_ui['object']
    ObjectAdjustment.rotate_button.enabled = enable_ui['object']
    ObjectAdjustment.rotate_text.enabled = enable_ui['object']
    ObjectAdjustment.color_text.enabled = enable_ui['object']
    ObjectAdjustment.color_button.enabled = enable_ui['object']
    ObjectAdjustment.copy_selection_text.enabled = enable_ui['object']
    ObjectAdjustment.copy_selection_button.enabled = enable_ui['object']
    MoveArrow.x.enabled = enable_ui['move']
    MoveArrow.y.enabled = enable_ui['move']
    MoveArrow.z.enabled = enable_ui['move']
    ScaleArrow.x.enabled = enable_ui['scale']
    ScaleArrow.y.enabled = enable_ui['scale']
    ScaleArrow.z.enabled = enable_ui['scale']
    RotateArrow.xx.enabled = enable_ui['rotate']
    RotateArrow.yy.enabled = enable_ui['rotate']
    RotateArrow.zz.enabled = enable_ui['rotate']
    destroy(tooltip_mov)
    del tooltip_mov
    tooltip_mov = Tooltip(f'{round(selected_object.x, 2)}, {round(selected_object.y, 2)}, {round(selected_object.z, 2)}'
                          )
    tooltip_mov.position = mouse.position
    tooltip_mov.enabled = enable_ui['move']
    destroy(tooltip_scale)
    del tooltip_scale
    tooltip_scale = Tooltip(
        f'{round(selected_object.scale_x, 2)}, {round(selected_object.scale_y, 2)}, {round(selected_object.scale_z, 2)}'
    )
    tooltip_scale.position = mouse.position
    tooltip_scale.enabled = enable_ui['scale']
    destroy(tooltip_rot)
    del tooltip_rot
    tooltip_rot = Tooltip(
        f'{round(selected_object.rotation_x, 2)}, {round(selected_object.rotation_y, 2)}::='.replace(
            '::=',
            f', {round(selected_object.rotation_z, 2)}'
        )
    )
    for i in entity_list:
        if str(i.model).replace('render/scene/entity/', '') == 'Models/player':
            i.collider = 'box'
            hit_info = i.intersects()
            if not hit_info.hit:
                i.y -= 0.5
    tooltip_rot.position = mouse.position
    tooltip_rot.enabled = enable_ui['rotate']
    if camera.y < -100:
        camera.y = 100


app.run()
