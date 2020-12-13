import functools
import itertools
import copy

# Load file
file = open('./data/day_13.txt',mode='r')
problem_str = file.read()
file.close()

def parse_problem_str(problem: str):
    lines = problem.splitlines()
    arrival_timestamp = int(lines[0])
    buses = []
    expected_wait_pattern = []
    wait_minutes = 0
    for elem in lines[1].split(","):
        if elem.isnumeric():
            buses.append(int(elem))
            expected_wait_pattern.append(wait_minutes)
            wait_minutes += 1
        else:
            wait_minutes += 1
    return (arrival_timestamp, buses, expected_wait_pattern)

def find_first_bus(arrival_timestamp, buses):
    buses_timestamps = []
    for bus in buses:
        factor = arrival_timestamp // bus
        if bus * factor < arrival_timestamp:
            buses_timestamps.append(bus * (factor + 1))
        else:
            buses_timestamps.append(bus * factor)
    index = buses_timestamps.index(min(buses_timestamps))
    return buses[index]*(min(buses_timestamps)-arrival_timestamp)

def find_p2_timestamp(buses, expected_wait_pattern):
    current_timestamp = 0
    current_inc = buses[0]
    index_chain_current_index = 1
    index_chain_first_ts = 0
    while True:
        iteration_good = True
        for index, elem in enumerate(expected_wait_pattern):
            if(index > index_chain_current_index):
                if index_chain_first_ts == 0:
                    index_chain_first_ts = current_timestamp
                else:
                    current_inc = current_timestamp - index_chain_first_ts
                    index_chain_first_ts = 0
                    index_chain_current_index += 1
            if (current_timestamp + elem) % buses[index] != 0:
                iteration_good = False
                break
        if iteration_good:
            return current_timestamp
        current_timestamp += current_inc

(s1_at, s1_b, s1_w) = parse_problem_str("939\n7,13,x,x,59,x,31,19")
assert 295 == find_first_bus(s1_at, s1_b)
assert 1068781 == find_p2_timestamp(s1_b, s1_w)

(s2_at, s2_b, s2_w) = parse_problem_str("0\n17,x,13,19")
assert 3417 == find_p2_timestamp(s2_b, s2_w)

(s3_at, s3_b, s3_w) = parse_problem_str("0\n67,7,59,61")
assert 754018 == find_p2_timestamp(s3_b, s3_w)

(s4_at, s4_b, s4_w) = parse_problem_str("0\n67,x,7,59,61")
assert 779210 == find_p2_timestamp(s4_b, s4_w)

(s5_at, s5_b, s5_w) = parse_problem_str("0\n67,7,x,59,61")
assert 1261476 == find_p2_timestamp(s5_b, s5_w)

(s6_at, s6_b, s6_w) = parse_problem_str("0\n1789,37,47,1889")
assert 1202161486 == find_p2_timestamp(s6_b, s6_w)

print("DAY XIII")

(arrival_timestamp, buses, expected_wait_pattern) = parse_problem_str(problem_str)
part_1_result = find_first_bus(arrival_timestamp, buses)
part_2_result = find_p2_timestamp(buses, expected_wait_pattern)

print("Part I :", part_1_result)
print("Part II :", part_2_result)

assert 3606 == part_1_result
assert 379786358533423 == part_2_result