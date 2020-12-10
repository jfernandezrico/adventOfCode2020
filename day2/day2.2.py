class Password2:

    def __init__(self, line):
        lineSplit = line.split()
        self.__set_password_policy(lineSplit[0])
        self.__set_letter_policy(lineSplit[1])
        self.__set_password(lineSplit[2])
        
    def __set_password_policy(self, password_policy_str):
        first_second_positions = password_policy_str.split('-')
        self.first_position = int(first_second_positions[0])
        self.second_position = int(first_second_positions[1])

    def __set_letter_policy(self, letter_policy):
        self.letter_policy = letter_policy[0]

    def __set_password(self, password):
        self.password = password

    def is_valid(self):
        return (self.__is_valid_position(self.first_position) ^ self.__is_valid_position(self.second_position))

    def __is_valid_position(self, position):
        return (position > 0 and len(self.password) >= position and self.password[position - 1] == self.letter_policy)


f = open("puzzle.txt", "r")
result = sum(1 for line in f if Password2(line).is_valid())
f.close()
print(result)