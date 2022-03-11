data = [
    ['A', 1, 101, 1],
    ['B', 1, 110, 1],
    ['C', 1, 110, 2],
    ['D', 1, 150, 2],
    ['A', 0, 140, 2],
    ['E', 1, 160,2],
    ['E', 0, 162,2],
    ['A', 1, 165,3],
    ['D', 0, 180,3],
    ['A', 0, 185,3],
    ['B', 0, 110, 3]
]

visits = {}
hours = {}


def maxHour(us,eve,tm,hr):
    if eve == 1:
        visits[us] = [tm,hr]
        hours.setdefault(hr, []).append(us)
    if eve == 0:
        initial = visits[us][1]
        diff = hr-initial
        i = diff
        while i > 0:
            hours.setdefault(initial+i, []).append(us)
            i -= 1
    # print('The highest hour is ', max(hours, key=hours.get))



for line in data:
    user, event, time, hour = line
    maxHour(user,event,time,hour)