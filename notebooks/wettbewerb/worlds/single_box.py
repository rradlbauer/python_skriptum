import shutil
from random import random
import math

vorlage = 'wettbewerb.vorlage'
world = 'wettbewerb.wbt'


def save_world(box):
    shutil.copy(vorlage, world)
    with open(world, 'a') as w:
        w.write(box)


def create_box():
    tx = (random() + 0.1) * 0.4
    if random() < 0.5: tx = -tx
    ty = (random() + 0.1) * 0.4
    if random() < 0.5: ty = -ty
    ty = (random() - 0.5) * 0.8
    rz = random() * math.pi
    b = """
    WoodenBox {
        translation tx ty 0.05
        rotation 0 0 0 rz
        size 0.1 0.1 0.1
    }
    """
    b = b.replace('tx', str(tx))
    b = b.replace('ty', str(ty))
    b = b.replace('rz', str(rz))
   
    return b
    
    
if __name__ == '__main__':
    save_world(create_box())
    print("done")
    