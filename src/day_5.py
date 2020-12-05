def _decode(seat: str, cur_index: int, min_row: int, max_row: int) -> int:
    if len(seat)-1 == cur_index and seat[cur_index] in ["F", "L"]:
        return min_row
    if len(seat)-1 == cur_index and seat[cur_index] in ["B", "R"]:
        return max_row
    half_seat_available = (max_row - min_row) // 2 + 1
    if seat[cur_index] in ["F", "L"]:
        return _decode(seat, cur_index+1, min_row, max_row - half_seat_available)
    if seat[cur_index] in ["B", "R"]:
        return _decode(seat, cur_index+1, min_row + half_seat_available, max_row)

def decode_seat(seat: str):
    row = _decode(seat[0:7], 0, 0, 127)
    col = _decode(seat[7:11], 0, 0, 7)
    seat_id = row * 8 + col
    return (row, col, seat_id)

file = open('./data/day_5.txt',mode='r')
lines = file.read().splitlines()
file.close()

decoded_seats = [decode_seat(seat)[2] for seat in lines]
decoded_seats.sort()
max_seat_id = decoded_seats[len(decoded_seats)-1]

my_seat_number = 0
for i in range(1, len(decoded_seats)-1):
    if decoded_seats[i-1] + 1 != decoded_seats[i]:
        my_seat_number = decoded_seats[i] - 1

print("DAY V")
print("Part I :", max_seat_id)
print("Part II :", my_seat_number)

assert max_seat_id == 826
assert my_seat_number == 678
assert (44, 5, 357) == decode_seat("FBFBBFFRLR")
assert (70, 7, 567) == decode_seat("BFFFBBFRRR")
assert (14, 7, 119) == decode_seat("FFFBBBFRRR")
assert (102, 4, 820) == decode_seat("BBFFBBFRLL")
