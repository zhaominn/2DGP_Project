world=[[],[],[]]

def add_object(o, depth):
    world[depth].append(o)

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
    print('에러: 존재하지 않은 객체를 지운다고?')