from units import Missile
from world import level_input
_missiles = []
_canvas = None




def initialise(canvas):
    global _canvas
    _canvas = canvas

def fire(owner):
    m = Missile(_canvas, owner)
    _missiles.append(m)

def update():
    start = len(_missiles)-1
    for i in range(start, -1, -1):
        if _missiles[i].is_destroyed():
            del _missiles[i]
        else:
            _missiles[i].update()

def check_missiles_collision(tank):
    for missile in _missiles:
        if missile.get_owner() == tank:
            continue
        if missile.intersects(tank):
            missile.destroy()
            tank.damage(10*level_input)
            return