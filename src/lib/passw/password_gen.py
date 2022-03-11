# write a class to generate passwords
import random

from pip import main


class PasswordGen:
    def __init__(self, length=8):
        self.length = length
        self.chars = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
        self.password = ""

    def generate(self):
        for i in range(self.length):
            self.password += self.chars[random.randint(0, len(self.chars) - 1)]
        return self.password
class PasswordGenTest:
    def __init__(self):
        self.password_gen = PasswordGen()
        self.password = self.password_gen.generate()
        print(self.password)