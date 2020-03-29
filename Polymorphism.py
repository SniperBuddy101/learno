class Pencil:
    def draw(self):
        print("-" * 5 + ">")


p1 = Pencil()


def draw(iterable):
    for i in iterable:
        i.draw()


p2 = Pencil()

draw([p1, p2])
