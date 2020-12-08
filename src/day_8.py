import copy

file = open('./data/day_8.txt',mode='r')
lines = file.read().splitlines()
file.close()

program = []
for line in lines:
    program.append((line.split()[0], int(line.split()[1])))

def run(program, index, accumulator, executed_indexes):
    if index in executed_indexes:
        return (accumulator, False)
    if index >= len(program):
        return (accumulator, True)
    operation = program[index]
    executed_indexes.append(index)
    if operation[0] == "nop":
        return run(program, index+1, accumulator, executed_indexes)
    elif operation[0] == "jmp":
        return run(program, index+operation[1], accumulator, executed_indexes)
    elif operation[0] == "acc":
        return run(program, index+1, accumulator+operation[1], executed_indexes)
    raise "Not handled operation"

res_part1 = run(program, 0, 0, [])

good_program_accumulator = 0
for index, elem in enumerate(program):
    new_program = copy.deepcopy(program)
    if elem[0] == "jmp" or elem[0] == "nop":
        new_program[index] = ("nop" if elem[0] == "jmp" else "jmp", elem[1])
        res = run(new_program, 0, 0, [])
        if res[1]:
            good_program_accumulator = res[0]
            break

print("DAY VIII")
print("Part I :", res_part1[0])
print("Part II :", good_program_accumulator)

assert res_part1 == (1915, False)
assert good_program_accumulator == 944
