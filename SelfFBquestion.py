visited = {}
calculated = {}

data = [
    ['A', 1, 100],
    ['B', 1, 100],
    ['A', 7, 190],
    ['A', 4, 150],
    ['A', 4, 135],
    ['A', 2, 110],
    ['A', 3, 130],
    ['A', 5, 140],
    ['A', 6, 180],
    ['B', 2, 150]
]


def calculate(ss, st, tm):
    if (ss, st) in visited.keys():
        if visited[(ss, st)] > tm:
            visited[(ss, st)] = tm
    else:
        visited[(ss, st)] = tm
        if (ss, st - 1) in visited.keys():
            calculated.setdefault(st - 1, []).append(visited[(ss, st)] - visited[(ss, st - 1)])
            print(calculated)


for line in data:
    session, step, timestart = line
    calculate(session, step, timestart)

print(visited)
print(calculated)
