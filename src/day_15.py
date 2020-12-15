file = open('./data/day_15.txt',mode='r')
numbers = [int(num) for num in file.read().splitlines()[0].split(",")]
file.close()

def play(numbers, end_turn=2020):
    state = {}
    last_turn_number = -1
    for turn in range(1, end_turn+1):
        if turn <= len(numbers):
            if last_turn_number != -1:
                state[last_turn_number] = turn-1
            last_turn_number = numbers[turn-1]
        elif last_turn_number not in state:
            state[last_turn_number] = turn-1
            last_turn_number = 0
        else:
            mem = (turn-1) - state[last_turn_number]
            state[last_turn_number] = turn-1
            last_turn_number = mem
    return last_turn_number

assert play([0,3,6]) == 436
assert play([1,3,2]) == 1
assert play([2,1,3]) == 10

res_part_1 = play(numbers)
res_part_2 = play(numbers, 30000000)

print("DAY XV")
print("Part I :", res_part_1)
print("Part II :", res_part_2)

assert res_part_1 == 260
assert res_part_2 == 950
