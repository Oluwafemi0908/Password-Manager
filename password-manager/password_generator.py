# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
           'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password_length = 15
print("Welcome to the PyPassword Generator!")


class PasswordGenerator:
    def __init__(self):
        self.nr_letters = random.randint(1, password_length-4)
        self.r_length = password_length - self.nr_letters
        self.nr_symbols = random.randint(1, self.r_length-2)
        self.r_length -= self.nr_symbols
        self.nr_numbers = self.r_length
        self.password_contains = []
        self.password = ''
        self.password_list = []
        self.password_letters = []
        self.password_symbols = []
        self.password_numbers = []

    def create_password(self):

        self.password_letters = [random.choice(letters) for letter in range(1, self.nr_letters + 1)]

        self.password_symbols = [random.choice(symbols) for symbol in range(1, self.nr_symbols + 1)]

        self.password_numbers = [random.choice(numbers) for number in range(1, self.nr_numbers + 1)]

        self.password_contains = self.password_letters + self.password_numbers + self.password_symbols

        for char in range(1, password_length + 1):
            character = random.choice(self.password_contains)
            self.password_list.append(character)
            self.password_contains.remove(character)

        self.password = "".join(self.password_list)
        return self.password

# p = PasswordGenerator()
# print(p.create_password())
