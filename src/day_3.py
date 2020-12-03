file = open('./data/day_3.txt',mode='r')
lines = file.read().splitlines()
file.close()

def slope(lines, offset_col, offset_row):
    col_size = len(lines[0])
    cur_col = 0
    cur_row = 0
    tree_count = 0
    while cur_row < len(lines):
        if lines[cur_row][cur_col % col_size] == "#":
            tree_count += 1
        cur_col += offset_col
        cur_row += offset_row
    return tree_count

problem_1 = slope(lines, 3, 1)
problem_2 = slope(lines, 1, 1) * slope(lines, 3, 1) * slope(lines, 5, 1) * slope(lines, 7, 1) * slope(lines, 1, 2)

print("DAY III")
print("Part I :",problem_1)
print("Part II :",problem_2)

assert problem_1 == 151
assert problem_2 == 7540141059