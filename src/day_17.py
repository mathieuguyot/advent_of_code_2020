import copy
import itertools

cube_active   = "#"
cube_inactive = "."

def parse_state(state_str: str):
    state = {}
    for x, line in enumerate(state_str.splitlines()):
        for y, elem in enumerate(line):
            state[(x,y,0,0)] = True if elem == cube_active else False
    return state

def get_neighbors_number(state, x, y, z, w):
    neighbors_number = 0
    for x_off in [0, 1, -1]:
        for y_off in [0, 1, -1]:
            for z_off in [0, 1, -1]:
                for w_off in [0, 1, -1]:
                    pos = (x + x_off, y + y_off, z + z_off, w + w_off)
                    if (x_off != 0 or y_off != 0 or z_off != 0 or w_off != 0) and pos in state:
                        neighbors_number += 1 if state[pos] else 0
    return neighbors_number

def cycle(state, use_4_dim, cycle, len_size):
    new_state = copy.deepcopy(state)
    offset = len_size + (cycle+1) * 2
    w_range = [0] if not use_4_dim else range(-offset, offset)
    for x in range(-offset, offset):
        for y in range(-offset, offset):
            for z in range(-offset, offset):
                for w in w_range:
                    neighbors_nb = get_neighbors_number(state, x, y, z, w)
                    pos = (x,y,z,w)
                    if pos in state and state[pos] and neighbors_nb not in [2, 3]:
                        new_state[pos] = False
                    elif (pos not in state or not state[pos]) and neighbors_nb == 3:
                        new_state[pos] = True
    return new_state

def count_active_cubes(state):
    active_nb = 0
    for val in state.values():
        if val:
            active_nb += 1
    return active_nb

test_state = parse_state(".#.\n..#\n###")
assert get_neighbors_number(test_state, 2, 1, 0, 0) == 3

file = open('./data/day_17.txt',mode='r')
state_str = file.read()
file.close()

state = parse_state(state_str)
state_4dm = parse_state(state_str)
test_4dm_state = copy.deepcopy(test_state)
for i in range(0,6):
    test_4dm_state = cycle(test_4dm_state, True, i, 3)
    test_state = cycle(test_state, False, i, 3)
    state = cycle(state, False, i, 8)
    state_4dm = cycle(state_4dm, True, i, 8)

assert count_active_cubes(test_4dm_state) == 848
assert count_active_cubes(test_state) == 112

part_1_res = count_active_cubes(state)
part_2_res = count_active_cubes(state_4dm)

print("DAY XVII")
print("Part I :", part_1_res)
print("Part II :", part_2_res)

assert part_1_res == 273
assert part_2_res == 1504
