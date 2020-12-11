import functools
import itertools
import copy

# Load file
file = open('./data/day_11.txt',mode='r')
rows = file.read().splitlines()
file.close()

# Define some helpful constants
cell_floor         = "."
cell_seat_empty    = "L"
cell_seat_occupied = "#"
seats_offsets      = [(-1, -1), (+1, +1), (-1, +1), (+1, -1), (+1, 0), (-1, 0), (0, +1), (0, -1)]
seats_rows         = len(rows)
seats_cols         = len(rows[0])

# Create a map (x, y) => seat types
seats = {}
for index_row in range(0, len(rows)):
    for index_col in range(0, len(rows[0])):
        if rows[index_row][index_col] == cell_seat_empty:
            seats[(index_row, index_col)] = cell_seat_occupied

def check_adjacent_single(seats, seat_coords, offset):
    coords = (seat_coords[0] + offset[0], seat_coords[1] + offset[1]) # Checked coords
    if coords in seats and seats[coords] == cell_seat_occupied:
        return True
    return False

def check_adjacent_line(seats, seat_coords, offset):
    coords = (seat_coords[0] + offset[0], seat_coords[1] + offset[1]) # Checked coords
    while coords[0] >= 0 and coords[1] >= 0 and coords[0] < seats_rows and coords[1] < seats_cols:
        if coords in seats and seats[coords] == cell_seat_occupied:
            return True
        elif coords in seats:
            return False
        coords = (coords[0] + offset[0], coords[1] + offset[1])
    return False

def get_number_seat_adjacent(seats, seat_coords, check_adjacent_func):
    occupied_seats = 0
    for offset in seats_offsets:
         if check_adjacent_func(seats, seat_coords, offset):
             occupied_seats += 1
    return occupied_seats

def compute_next_seats_step(seats, check_adjacent_func, max_tolerated_adjacent_seats):
    updated = False
    new_seats = copy.deepcopy(seats)
    for seat_coords, seat_value in seats.items():
        occupied = get_number_seat_adjacent(seats, seat_coords, check_adjacent_func)
        if occupied >= max_tolerated_adjacent_seats and seat_value == cell_seat_occupied:
            new_seats[seat_coords] = cell_seat_empty
            updated = True
        elif occupied == 0 and seat_value == cell_seat_empty:
            new_seats[seat_coords] = cell_seat_occupied
            updated = True
    return (updated, new_seats)


seats_state_part_1 = compute_next_seats_step(seats, check_adjacent_single, 4)
seats_state_part_2 = compute_next_seats_step(seats, check_adjacent_line, 5)
while seats_state_part_1[0] or seats_state_part_2[0]:
    if seats_state_part_1[0]:
        seats_state_part_1 = compute_next_seats_step(seats_state_part_1[1], check_adjacent_single, 4)
    if seats_state_part_2[0]:
        seats_state_part_2 = compute_next_seats_step(seats_state_part_2[1], check_adjacent_line, 5)

occupied_seat_reducer = lambda sum, seat : sum + 1 if seat == cell_seat_occupied else sum
occupied_seats_part_1 = functools.reduce(occupied_seat_reducer, seats_state_part_1[1].values(), 0)
occupied_seats_part_2 = functools.reduce(occupied_seat_reducer, seats_state_part_2[1].values(), 0)

print("DAY XI")
print("Part I :", occupied_seats_part_1)
print("Part II :", occupied_seats_part_2)

assert occupied_seats_part_1 == 2126
assert occupied_seats_part_2 == 1914
