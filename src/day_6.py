file = open('./data/day_6.txt',mode='r')
lines = file.read().splitlines()
file.close()

part_1_score = 0
current_group_letters = []
for answer in lines:
    if len(answer) == 0:
        current_group_letters = []
    else:
        for question in answer:
            if question not in current_group_letters:
                part_1_score += 1
                current_group_letters.append(question)

part_2_score = 0
first_person_in_group = True
first_person_answer = ""
for answer in lines:
    if len(answer) == 0:
        first_person_in_group = True
        part_2_score += len(first_person_answer)
    elif first_person_in_group:
        first_person_answer = answer
        first_person_in_group = False
    else:
        for question in answer:
            if question not in first_person_answer:
                first_person_answer = first_person_answer.replace(question, '')
        for question in first_person_answer:
            if question not in answer:
                first_person_answer = first_person_answer.replace(question, '')

print("DAY VI")
print("Part I :", part_1_score)
print("Part II :", part_2_score)

assert part_1_score == 7128
assert part_2_score == 3640
