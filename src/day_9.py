import itertools

file = open('./data/day_9.txt',mode='r')
numbers = [int(line) for line in file.read().splitlines()]
file.close()

preamble_length = 25

def find_invalid_number(numbers, index, preamble):
    if len(preamble) < preamble_length:
        preamble.append(numbers[index])
        return find_invalid_number(numbers, index+1, preamble)
    else:
        sum_found = False
        for pair in itertools.permutations(preamble, 2):
            if pair[0] + pair[1] == numbers[index]:
                sum_found = True
                break
        if not sum_found:
            return numbers[index]
        else:
            preamble.pop(0)
            preamble.append(numbers[index])
            return find_invalid_number(numbers, index+1, preamble)

def find_contiguous_set(numbers, number_to_found):
    for index in range(0, len(numbers)-1):
        current_set = []
        for index_2 in range(index, len(numbers)-1):
            current_set.append(numbers[index_2])
            current_sum = sum(current_set)
            if current_sum > number_to_found:
                break
            elif current_sum == number_to_found:
                return min(current_set) + max(current_set)

part_1_result = find_invalid_number(numbers, 0, [])
part_2_result = find_contiguous_set(numbers, 556543474)

print("DAY IX")
print("Part I :", part_1_result)
print("Part II :", part_2_result)

assert part_1_result == 556543474
assert part_2_result == 76096372
