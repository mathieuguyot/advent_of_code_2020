import re
from functools import reduce

class Password:
    def __init__(self, num_1: int, num_2: int, letter: str, password: str):
        self.num_1 = num_1
        self.num_2 = num_2
        self.letter = letter
        self.password = password

    def is_valid_part1(self):
        count_occurences = lambda cur_count, letter : 1 + cur_count if letter == self.letter else cur_count
        occurences = reduce(count_occurences, self.password, 0)
        return occurences >= self.num_1 and occurences <= self.num_2
    
    def is_valid_part2(self):
        is_first_num = self.password[self.num_1-1] == self.letter
        is_second_num = self.password[self.num_2-1] == self.letter
        return (is_first_num and not is_second_num) or (not is_first_num and is_second_num)

password = Password(1, 3, "a", "abcde")
assert password.is_valid_part1()
assert password.is_valid_part2()
password = Password(1, 3, "b", "cdefg")
assert not password.is_valid_part1()
assert not password.is_valid_part2()
password = Password(2, 9, "c", "ccccccccc")
assert password.is_valid_part1()
assert not password.is_valid_part2()

file = open('./data/day_2.txt',mode='r')
lines = file.read().splitlines()
file.close()

pwd_regex = re.compile(r'(\d+)-(\d+) (\w): (\w+)')
good_pwd_p1 = 0
good_pwd_p2 = 0
for line in lines:
    match = pwd_regex.match(line)
    if match is not None:
        pwd = Password(int(match[1]), int(match[2]), match[3], match[4])
        if pwd.is_valid_part1():
            good_pwd_p1 += 1
        if pwd.is_valid_part2():
            good_pwd_p2 += 1

print("DAY II")
print("Part I :", good_pwd_p1)
print("Part II:", good_pwd_p2)

assert good_pwd_p1 == 625
assert good_pwd_p2 == 391