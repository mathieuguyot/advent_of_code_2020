import itertools

file = open('./data/day_10.txt',mode='r')
numbers = [int(line) for line in file.read().splitlines()]
file.close()

numbers.append(0)
numbers.append(max(numbers)+3)
numbers.sort()

def part_1_solver(numbers) -> int:
    jolt_diff_1 = 0
    jolt_diff_3 = 0
    for index in range(1, len(numbers)):
        if numbers[index] - numbers[index-1] == 1:
            jolt_diff_1 += 1
        if numbers[index] - numbers[index-1] == 3:
            jolt_diff_3 += 1
    return jolt_diff_1 * jolt_diff_3

def combinaison_number(numbers, cur_index, cache) -> int:
    combinaisons = 0
    if cur_index in cache: # Cached case
        return cache[cur_index]
    for index in range(cur_index+1, len(numbers)): # General case
        if numbers[index] - numbers[cur_index] <= 3:
            combinaisons += combinaison_number(numbers, index, cache)
        else:
            break
    if cur_index == len(numbers)-1: # Leaf case
        combinaisons = 1
    cache[cur_index] = combinaisons # Update cache with computed value
    return combinaisons

part_1_result = part_1_solver(numbers)
part_2_result = combinaison_number(numbers, 0, {})

print("DAY X")
print("Part I :", part_1_result)
print("Part II :", part_2_result)

assert part_1_result == 3000
assert part_2_result == 193434623148032