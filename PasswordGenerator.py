'''
Random Password Generator

Qualities of a good password
- 10-16 characters in length?
- Random Mix of Numbers, Letters, and Special Characters
'''
import random
import string


def randomVal():
    choice = random.randint(1, 3)
    if choice == 1:
        # returns random int
        return str(random.randint(0, 9))
    elif choice == 2:
        # return random letter
        return random.choice(string.ascii_letters)
    else:
        # return random special letter
        specList = ["@", "#", "$", "%", "&"]
        return specList[random.randint(0, 4)]


passLength = random.randint(10, 16)
print("*** Password will be " + str(passLength) + " digits long ***")
print()

password = ""

for i in range(0, passLength):
    password = password + randomVal()

print("Password Generated: " + password)