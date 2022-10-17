# import Tank class from tank.py
from tank import Tank


tanks = {
    'a': Tank("Alice"),
    'b': Tank("Bob"),
    'c': Tank("Carol")
}

#print(f"tanks= {tanks}")
alive_tanks = len(tanks)

#print(f"alive_tanks (tanks length)= {alive_tanks}")

while alive_tanks > 1:
    for tank_name in sorted(tanks.keys()):
        print(f"tank name {tanks[tank_name]}")

    first = input("Who fires? ").lower()
    second = input("Who at? ").lower()

    try:
        first_tank = tanks[first]
        second_tank = tanks[second]
    except KeyError as name:
        print(f"No such tank! {name}")
        continue

    if not first_tank.alive or not second_tank.alive:
        print(f"One of those tanks is dead!")
        continue

    print()
    print("*" * 30)

    first_tank.fire_at(second_tank)
    if not second_tank.alive:
        alive_tanks -= 1

    print("*" * 30)

for tank in tanks.values():
    if tank.alive:
        print(f"{tank.name} is the winner!")
        break

