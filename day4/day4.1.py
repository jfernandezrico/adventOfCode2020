def get_passports(data, separator):
    return data.split(separator)

def get_passport_key_value_pairs(data, separators): 
    import re
    regexPattern = "|".join(map(re.escape, separators))
    return re.split(regexPattern, data)

def get_keys(key_value_pairs, key_value_spearator):
    return list(map(lambda key_value_pair: key_value_pair.split(key_value_spearator)[0], key_value_pairs))

def contains_all_mandatory_keys(passport_keys, mandatory_keys):
    return all(elem in passport_keys  for elem in mandatory_keys)


with open("puzzle.txt", "r") as file:
    data = file.read()

passports = get_passports(data, "\n\n")

result = sum(1 for passport in passports if contains_all_mandatory_keys(get_keys(get_passport_key_value_pairs(passport, ["\n", " "]), ":"), ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]))

print(result)
