import re
from graphviz import Digraph

file = open('./data/day_7.txt',mode='r')
lines = file.read().splitlines()
file.close()

bag_graph = {}
pwd_regex = re.compile(r'(\d+) (\w+ \w+) bag')
for line in lines:
    bag_name = line.split()[0] + " " + line.split()[1]
    bag_graph[bag_name] = []
    for (number, name) in re.findall(pwd_regex, line):
        bag_graph[bag_name].append((int(number), name))

def can_hold_shiny_gold_bag(bag_graph, bag_content) -> bool:
    if len(bag_content) == 0:
        return False
    for (_, name) in bag_content:
        if name == "shiny gold":
            return True
        elif can_hold_shiny_gold_bag(bag_graph, bag_graph[name]):
            return True
    return False

def get_bag_number(bag_graph, bag_content) -> int:
    bag_number = 0
    for (number, name) in bag_content:
        bag_number += number
        bag_number += number * get_bag_number(bag_graph, bag_graph[name])
    return bag_number

part_1_count = 0
for key, value in bag_graph.items():
    can_hold = can_hold_shiny_gold_bag(bag_graph, value)
    part_1_count += 1 if can_hold else 0
part_2_count = get_bag_number(bag_graph, bag_graph["shiny gold"])

print("DAY VII")
print("Part I :", part_1_count)
print("Part II :", part_2_count)

assert part_1_count == 224
assert part_2_count == 1488