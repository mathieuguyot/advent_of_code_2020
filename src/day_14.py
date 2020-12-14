import re
import itertools

# Load file
file = open('./data/day_14.txt',mode='r')
program = file.read().splitlines()
file.close()

mem_re = re.compile(r'mem\[(\d+)\] = (\d+)')

def run_program_part_1(program, index, mask, memory):
    if index >= len(program):
        return sum(memory.values())
    if program[index].startswith("mask = "):
        mask = program[index][7:]
        mask = mask[::-1]
    else:
        match = re.match(mem_re, program[index])
        if match:
            memory_address = int(match[1])
            memory_value = "{0:b}".format(int(match[2]))[::-1]
            for digit_index in range(len(memory_value), len(mask)):
                memory_value += "0"
            memory_value_masked = ""
            for digit_index in range(0, len(memory_value)):
                if mask[digit_index] != "X":
                    memory_value_masked += mask[digit_index]
                else:
                    memory_value_masked += memory_value[digit_index]
            memory[memory_address] = int(memory_value_masked[::-1], 2)
    return run_program_part_1(program, index+1, mask, memory)

def find_all_memory_address_values(memory_mask):
    values = []
    x_count = memory_mask.count("X")
    combinaisons = list(itertools.product([0, 1], repeat=x_count))
    for comb in combinaisons:
        memory = memory_mask
        for index in range(0, x_count):
            memory = memory.replace("X", str(comb[index]), 1)
        values.append(int(memory, 2))
    return values

def run_program_part_2(program, index, mask, memory):
    if index >= len(program):
        return sum(memory.values())
    if program[index].startswith("mask = "):
        mask = program[index][7:]
        mask = mask[::-1]
    else:
        match = re.match(mem_re, program[index])
        if match:
            memory_address = "{0:b}".format(int(match[1]))[::-1]
            memory_value = int(match[2])
            for digit_index in range(len(memory_address), len(mask)):
                memory_address += "0"
            memory_address_masked = ""
            for digit_index in range(0, len(memory_address)):
                if mask[digit_index] != "0":
                    memory_address_masked += mask[digit_index]
                else:
                    memory_address_masked += memory_address[digit_index]
            for address in find_all_memory_address_values(memory_address_masked):
                memory[address] = memory_value
    return run_program_part_2(program, index+1, mask, memory)

part_1_res = run_program_part_1(program, 0, "", {})
part_2_res = run_program_part_2(program, 0, "", {})

print(part_1_res)
print(part_2_res)

assert 4886706177792 == part_1_res
assert 3348493585827 == part_2_res

assert [26, 27, 58, 59] == find_all_memory_address_values("000000000000000000000000000000X1101X")
