import random
from string import digits, ascii_letters
import pyperclip


characters = ascii_letters + digits + "!@#$%^&*()_+"
list_of_chars = [x for x in characters]

def pass_gen(length):
    random.shuffle(list_of_chars)
    print(list_of_chars)
    pass_list = random.choices(list_of_chars, k=length)
    return ''.join(pass_list)


if __name__ == "__main__":
    if input("wanna create a random pass ? Y/N > ").lower() == 'y':
        length = int(input("How long you want it to be ? "))
        password = pass_gen(length)
        pyperclip.copy(password)
        print(f'Your password is "{password}" and been copied \
to you clipboard.')
        

