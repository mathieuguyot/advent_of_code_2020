import re
from typing import Dict

class Password:
    def __init__(self, fields: Dict[str, str]):
        self.fields = fields

    def are_fields_presents(self) -> bool:
        for key in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]:
            if key not in self.fields:
                return False
        return True

    def is_valid(self) -> bool:
        if not self.are_fields_presents():
            return False
        if int(self.fields["byr"]) < 1920 or int(self.fields["byr"]) > 2002:
            return False
        if int(self.fields["iyr"]) < 2010 or int(self.fields["iyr"]) > 2020:
            return False
        if int(self.fields["eyr"]) < 2020 or int(self.fields["eyr"]) > 2030:
            return False
        hgt_regex = re.compile(r'(\d+)(cm|in)')
        match = hgt_regex.match(self.fields["hgt"])
        if match is None:
            return False
        elif match[2] == "cm" and (int(match[1]) < 150 or int(match[1]) > 193):
            return False
        elif match[2] == "in" and (int(match[1]) < 59 or int(match[1]) > 76):
            return False
        hcl_regex = re.compile(r'#[0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f]')
        match = hcl_regex.match(self.fields["hcl"])
        if match is None:
            return False
        if self.fields["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            return False
        pid_regex = re.compile(r'^[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]$')
        match = pid_regex.match(self.fields["pid"])
        if match is None:
            return False
        return True

assert True == Password({"ecl":"gry", "pid":"860033327", "eyr":"2020", "hcl":"#fffffd", "byr":"1937", "iyr":"2017", "cid":"147", "hgt":"183cm"}).are_fields_presents()
assert False == Password({"iyr":"2013", "ecl":"amb", "cid":"350", "eyr":"2023", "pid":"028048884", "hcl":"#cfa07d", "byr":"1929"}).are_fields_presents()
assert True == Password({"hcl":"#ae17e1", "iyr":"2013", "eyr":"2024", "ecl":"brn", "pid":"760753108", "byr":"1931", "hgt":"179cm"}).are_fields_presents()
assert False == Password({"hcl":"#cfa07d", "eyr":"2025", "pid":"166559648", "iyr":"2011", "ecl":"brn", "hgt":"59in"}).are_fields_presents()

assert False == Password({"eyr":"1972", "cid":"100", "hcl":"#18171d", "ecl":"amb", "hgt":"170", "pid":"186cm", "iyr":"2018", "byr":"1926"}).is_valid()
assert False == Password({"iyr":"2019", "hcl":"#602927", "eyr":"1967", "hgt":"170cm", "ecl":"grn", "pid":"012533040", "byr":"1946"}).is_valid()
assert False == Password({"hcl":"dab227", "iyr":"2012", "ecl":"brn", "hgt":"182cm", "pid":"021572410", "eyr":"2020", "byr":"1992", "cid":"277"}).is_valid()
assert False == Password({"hgt":"59cm", "ecl":"zzz", "eyr":"2038", "hcl":"74454a", "iyr":"2023", "pid":"3556412378", "byr":"2007"}).is_valid()

assert True == Password({"pid":"087499704", "hgt":"74in", "ecl":"grn", "iyr":"2012", "eyr":"2030", "byr":"1980", "hcl":"#623a2f"}).is_valid()
assert True == Password({"eyr":"2029", "ecl":"blu", "cid":"129", "byr":"1989", "iyr":"2014", "pid":"896056539", "hcl":"#a97842", "hgt":"165cm"}).is_valid()
assert True == Password({"hcl":"#888785", "hgt":"164cm", "byr":"2001", "iyr":"2015", "cid":"88", "pid":"545766238", "ecl":"hzl", "eyr":"2022"}).is_valid()
assert True == Password({"iyr":"2010", "hgt":"158cm", "hcl":"#b6652a", "ecl":"blu", "byr":"1944", "eyr":"2021", "pid":"093154719"}).is_valid()

file = open('./data/day_4.txt',mode='r')
lines = file.read().splitlines()
file.close()

pwd_regex = re.compile(r'(.+):(.+)')
keys: Dict[str, str] = {}
field_ok_password_count = 0
valid_password_count = 0
for line in lines:
    if len(line) == 0:
        pwd = Password(keys)
        field_ok_password_count += 1 if pwd.are_fields_presents() else 0
        valid_password_count += 1 if pwd.is_valid() else 0
        keys = {}
    else:
        for field in line.split(" "):
            match = pwd_regex.match(field)
            if match is not None:
                keys[match[1]] = match[2]

print("DAY IV")
print("Part I :", field_ok_password_count)
print("Part II :", valid_password_count)

assert field_ok_password_count == 192
assert valid_password_count == 101