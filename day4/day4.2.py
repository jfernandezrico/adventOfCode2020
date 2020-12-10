import re

class Passport:

    def __init__(self, dictionary):
        self.birth_year = dictionary.get("byr")
        self.issue_year = dictionary.get("iyr")
        self.expiration_year = dictionary.get("eyr")
        (self.height, self.height_measure) = self.__split_height(dictionary.get("hgt"))
        self.hair_color = dictionary.get("hcl")
        self.eye_color = dictionary.get("ecl")
        self.pid = dictionary.get("pid")

    def __split_height(self, height):
        if height is None:
            return (None, None)
        return (height[:-2], height[-2:])

    def is_valid(self):
        return (
            self.__birth_year_is_valid() and 
            self.__issue_year_is_valid() and 
            self.__expiration_year_is_valid() and 
            self.__height_is_valid() and 
            self.__hair_color_is_valid() and 
            self.__eye_color_is_valid() and 
            self.__pid_is_valid()
        )

    def __birth_year_is_valid(self):
        return (
            self.birth_year is not None and 
            self.birth_year >= '1920' and
            self.birth_year <= '2002'
        )

    def __issue_year_is_valid(self):
        return (
            self.issue_year is not None and
            self.issue_year >= '2010' and
            self.issue_year <= '2020'
        )

    def __expiration_year_is_valid(self):
        return (
            self.expiration_year is not None and
            self.expiration_year >= '2020' and
            self.expiration_year <= '2030'
        )

    def __height_is_valid(self):
        return (
            self.height is not None and
            (
                (self.height_measure == 'cm' and self.height >= '150' and self.height <= '193') or
                (self.height_measure == 'in' and self.height >= '59' and self.height <= '76')
            )
        )

    def __hair_color_is_valid(self):
        return (
            self.hair_color is not None and
            re.search('^#[\da-f]{6}$', self.hair_color) is not None
        )

    def __eye_color_is_valid(self):
        return (
            self.eye_color is not None and
            self.eye_color in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        )

    def __pid_is_valid(self):
        return (
            self.pid is not None and
            re.search('^\d{9}$', self.pid) is not None
        )

def get_passports(data, separator):
    return data.split(separator)

def get_passport_key_value_pairs(data, separators): 
    import re
    regexPattern = "|".join(map(re.escape, separators))
    return re.split(regexPattern, data)

def get_passport(key_value_pairs, key_value_spearator):
    dictionary = {}
    for key_value_pair in key_value_pairs:
        l = key_value_pair.split(key_value_spearator)
        dictionary[l[0]] = l[1]
    return Passport(dictionary)

with open("puzzle.txt", "r") as file:
    data = file.read()

passports = get_passports(data, "\n\n")

result = sum(1 for passport in passports if get_passport(get_passport_key_value_pairs(passport, ["\n", " "]), ":").is_valid())

print(result)