import itertools

file = open('./data/day_1.txt',mode='r')
lines = file.read().splitlines()
file.close()

numbers = map(lambda e : int(e), lines)

first_sum = 0
second_sum = 0
for pair in itertools.permutations(numbers, 3):
    if pair[0] + pair[1] == 2020:
        first_sum = pair[0] * pair[1]
    if pair[0] + pair[1] + pair[2] == 2020:
        second_sum = pair[0] * pair[1] * pair[2]

print("DAY I")
print("DAY I", first_sum)
print("DAY II", second_sum)

assert first_sum == 713184
assert second_sum == 261244452