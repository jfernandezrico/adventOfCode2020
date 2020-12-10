class Password:

    def __init__(self, line):
        lineSplit = line.split()
        self.__set_password_policy(lineSplit[0].split('-'))
        self.__set_letter_policy(lineSplit[1])
        self.__set_password(lineSplit[2])
        
    def __set_password_policy(self, password_policy_str):
        self.min_contains = int(password_policy_str[0])
        self.max_contains = int(password_policy_str[1])

    def __set_letter_policy(self, letter_policy):
        self.letter_policy = letter_policy[0]

    def __set_password(self, password):
        self.password = password

    def is_valid(self):
        occurrences = self.password.count(self.letter_policy)
        return (occurrences >= self.min_contains and occurrences <= self.max_contains)


f = open("puzzle.txt", "r")
result = sum(1 for line in f if Password(line).is_valid())
f.close()
print(result)