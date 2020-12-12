import functools
import itertools
import copy
from enum import Enum

directions = ["E","S","W","N"]

# Load file
file = open('./data/day_12.txt',mode='r')
navigations = [(elem[0], int(elem[1:])) for elem in file.read().splitlines()]
file.close()

def get_md(cur_dirs):
    return abs(cur_dirs[0]-cur_dirs[2]) + abs(cur_dirs[1]-cur_dirs[3])

def compute_manhattan_distance_part_1(navigations, index, current_direction, current_direction_nav):
    if index == len(navigations):
        return get_md(current_direction_nav)
    nav = navigations[index]
    if nav[0] in directions:
        current_direction_nav[directions.index(nav[0])] += nav[1]
    elif nav[0] in ("L", "R"):
        inc = nav[1] if nav[0] == "R" else -nav[1]
        current_direction = current_direction + inc
    elif nav[0] == "F":
        current_direction_nav[(current_direction//10)%4] += nav[1]
    return compute_manhattan_distance_part_1(navigations, index+1, current_direction, current_direction_nav)

def compute_manhattan_distance_part_2(navigations, index, current_direction, current_direction_nav, current_waypoint_nav):
    if index == len(navigations):
        return get_md(current_direction_nav)
    nav = navigations[index]
    if nav[0] in directions:
        current_waypoint_nav[directions.index(nav[0])] += nav[1]
    elif nav[0] in ("L", "R"):
        inc = nav[1] if nav[0] == "R" else -nav[1]
        current_direction = current_direction + inc
    elif nav[0] == "F":
        current_direction_nav[(current_direction//10)%4] += abs(current_waypoint_nav[0]-current_waypoint_nav[2]) * nav[1]
        current_direction_nav[((current_direction-90)//10)%4] += abs(current_waypoint_nav[1]-current_waypoint_nav[3]) * nav[1]
    print(nav, current_direction, current_direction_nav, current_waypoint_nav)
    return compute_manhattan_distance_part_2(navigations, index+1, current_direction, current_direction_nav, current_waypoint_nav)

res_part_1 = compute_manhattan_distance_part_1(navigations, 0, 0, [0, 0, 0, 0])
res_part_2 = compute_manhattan_distance_part_2(navigations, 0, 0, [0, 0, 0, 0], [10, 0, 0, 1])

print("DAY X")
print("Part I :", res_part_1)
print("Part II (WRONG) :", res_part_2)

assert res_part_1 == 1133

test_navs = [("F", 10), ("N", 3), ("F", 7), ("R", 90), ("F", 11)]
assert 25 == compute_manhattan_distance_part_1(test_navs, 0, 0, [0, 0, 0, 0])
assert 286 == compute_manhattan_distance_part_2(test_navs, 0, 0, [0, 0, 0, 0], [10, 0, 0, 1])
