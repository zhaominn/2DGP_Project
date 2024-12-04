world = [[] for _ in range(4)]

collision_pairs={}
# collision_pairs={ key: [[],[]], key: [[],[]]...}

def add_collision_pair(group,a,b):
    if group not in collision_pairs:
        # 초기화
        #print(f'Added new groub{group}')
        collision_pairs[group]=[[],[]]
    if a:
        collision_pairs[group][0].append(a)
    if b:
        collision_pairs[group][1].append(b)

def handle_collisions():
    for group, pairs in collision_pairs.items():
        for a in pairs[0]:
            for b in pairs[1]:
                if collide(a, b):
                    a.handle_collision(group)
                    b.handle_collision(group)

def add_object(o, depth = 0):
    world[depth].append(o)

def add_objects(ol, depth = 0):
    world[depth] += ol

def update():
    for layer in world:
        for o in layer:
            o.update()

def render():
    for layer in world:
        for o in layer:
            o.draw()

def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return

    #raise ValueError('Cannot delete non existing object')

def clear():
    global world
    for layer in world:
        layer.clear()


def collide(a, b):
    la, ba, ra, ta = a.get_bb()
    lb, bb, rb, tb = b.get_bb()
    if la > rb: return False
    if ra < lb: return False
    if ta < bb: return False
    if ba > tb: return False
    return True

def collide_bb(a, b):
    la, ba, ra, ta = a
    lb, bb, rb, tb = b
    if la > rb: return False
    if ra < lb: return False
    if ta < bb: return False
    if ba > tb: return False
    return True