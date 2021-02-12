import sys
import math


def dist(a, b):
    return (b[0] - a[0])**2 + (b[1] - a[1])**2


def minimum_distance(x, y):
    points = list(zip(x, y))
    points_y = sorted(points, key=lambda z: z[1])
    points.sort(key=lambda g: g[0])
    return min_dist(points, points_y)


def min_dist(points, points_y):
    if len(points) == 2:
        return dist(points[0], points[1])
    elif len(points) == 3:
        return min(dist(points[0], points[1]), dist(points[0], points[2]), dist(points[1], points[2]))
    ave = (len(points) + 1) // 2
    yleft = [t for t in points_y if t[0] <= points[ave - 1][0]]
    yright = [q for q in points_y if q[0] >= points[ave][0]]
    d1 = min_dist(points[0:ave], yleft)
    d2 = min_dist(points[ave:len(points)], yright)
    d = min(d1, d2)
    arr_split = [point for point in points_y if abs(point[0] - points[ave][0]) <= d]
    d_ = 2 * (10 ** 18)
    for i in range(len(arr_split) - 1):
        for j in range(i + 1, min(len(arr_split), i + 7)):
            temp = dist(arr_split[i], arr_split[j])
            if temp < d_: d_ = temp
    return min(d, d_)

list1 = (0,10,15)
list2 = (0,10,20)

print(minimum_distance(list1,list2))