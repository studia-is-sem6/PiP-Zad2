from entities import Sheep

# ent = Sheep("Sheep", [10, 10], 0.5)
#
# print(ent)
# print(repr(ent))
#
# ent.move()
#
# print(ent)
# print(repr(ent))

from entities import Herd

herd = Herd(15, 10, 0.5)

for sheep in herd:
    print(sheep)

# herd.herd.pop()
herd.herd.remove(herd.herd[4])

for sheep in herd:
    print(sheep)