import re 

file = open('./data/day_16.txt',mode='r')
problem = file.read()
file.close()

def parse_problem_str(problem: str):
    rule_re   = re.compile(r'(.*): (\d+)-(\d+) or (\d+)-(\d+)')
    ticket_re = re.compile(r'\d+,?')

    rules = []
    tickets = []

    for line in problem.splitlines():
        match = re.match(rule_re, line)
        if match:
            rules.append((int(match[2]), int(match[3]), int(match[4]), int(match[5]), match[1]))
        if re.match(ticket_re, line):
            tickets.append([int(num) for num in line.split(",")])
            pass

    return (rules, tickets[0], tickets[1::])

def get_num_valid_rules(rules, num):
    valid_rules = []
    for rule in rules:
        if (num >= rule[0] and num <= rule[1]) or (num >= rule[2] and num <= rule[3]):
            valid_rules.append(rule)
    return valid_rules

def get_ticket_error_rate(rules, ticket):
    error_rate = 0
    for num in ticket:
        if len(get_num_valid_rules(rules, num)) == 0:
            error_rate += num
    return error_rate

def is_rule_order_found(rules, rules_order):
    if len(rules_order) != len(rules):
        return True
    for rules_set in rules_order.values():
        if len(rules_set) != 1:
            return True
    return False

def find_rule_order(rules, tickets):
    rules_order = {}
    while is_rule_order_found(rules, rules_order):
        blocked_rules = []
        for rule in rules_order.values():
            if len(rule) == 1:
                blocked_rules.append(rule[0])

        for ticket in tickets:
            for index, num in enumerate(ticket):
                valid_rules = get_num_valid_rules(rules, num)
                if index not in rules_order:
                    rules_order[index] = valid_rules
                elif valid_rules != [] and len(rules_order[index]) != 1:
                    rules_order[index] = [item for item in valid_rules if (item not in blocked_rules) and (item in rules_order[index])]

    return rules_order

rules, my_ticket, tickets = parse_problem_str(problem)

valid_tickets = []
part_1_error_rate = 0
for ticket in tickets:
    error_rate = get_ticket_error_rate(rules, ticket)
    if error_rate == 0:
        valid_tickets.append(ticket)
    else:
        part_1_error_rate += error_rate

all_tickets = valid_tickets
all_tickets.append(my_ticket)
rules_order = find_rule_order(rules, all_tickets)
part_2_res = 1
for index, rule in rules_order.items():
    if rule[0][4].startswith("departure"):
        part_2_res *= my_ticket[index]

print("DAY XVI")
print("Part I :", part_1_error_rate)
print("Part II :", part_2_res)

assert 29759 == part_1_error_rate
assert 1307550234719 == part_2_res
