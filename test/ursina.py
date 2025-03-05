

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

sky = Sky()


def crear_cubo(posicion):
    Entity(
        position=posicion,
        model='cube',
        scale=[1, 1, 1],
        color=color.green,
        collider='box'
    )


cubo_final = Entity(
    position=[10, 0, 0],
    model='cube',
    scale=[1, 1, 1],
    color=color.red,
    collider='box'
)

for i in range(10):
    crear_cubo([i, 0, 0])

player = FirstPersonController()


def update():
    if player.position.y < -10:
        player.position = [0, 10, 0]

    rayo = raycast(player.position, player.down, distance=2, ignore=[player])
    if rayo.entity == cubo_final:
        Text(text="FIN", color=color.black, scale=(1, 1), origin=(0, 0))


def input(key):  # noqa
    if key == 'escape':
        exit()
    if key == 'h':
        Text(text="HOLA", color=color.black, scale=(1, 1), origin=(0, 0))


app.run()
