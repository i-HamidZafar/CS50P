# emojize.py
import emoji

input = input("Input: ")
print(emoji.emojize(f'Output: {input}', language='alias'))

# figlet.py
from pyfiglet import Figlet
import sys
import random
figlet = Figlet()
if len(sys.argv) == 3:

    if sys.argv[1] not in ["--font", "-f"] or sys.argv[2] not in figlet.getFonts():
        sys.exit(1)
    else:
        user_input = input("Input: ")
        figlet.setFont(font=sys.argv[2])
        print(f"Output:\n{figlet.renderText(user_input)}")
        sys.exit(0)
elif len(sys.argv) == 1:
   user_input = input("Input: ")
   fonts = figlet.getFonts()
   font = random.randint(0,len(fonts) - 1)
   figlet.setFont(font=fonts[font])
   print(f"Output:\n{figlet.renderText(user_input)}" )
   sys.exit(0)
else:
    sys.exit(1)

# adieu.py
def main():
    names=[]
    while True:
        try:
            name = input("").strip()
            names.append(name)
        except EOFError:
            break
    format(names)
    exit(0)


def format(names):
    length = len(names)
    if length >= 3:
        print(f"Adieu, adieu, to {names[0]},", end ="")
    else:
        print(f"Adieu, adieu, to {names[0]}", end ="")
    for i in range(1, length):
        if i ==  length - 1:
            print(" and " + names[i])
        else:
            print(f" {names[i]},", end ="" )

if __name__ == "__main__":
    main()

# game.py
import random

def main():
    level = select_level()
    answer = get_answer(level)
    while True:
        guess = make_guess()
        if check_guess(guess, answer):
            return

def select_level():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                    return level
        except ValueError:
            pass

def get_answer(level):
    return random.randint(1, level)

def make_guess():
    while True:
        try:
            guess = int(input("Guess: "))
            if guess > 0:
                return guess
        except ValueError:
            pass

def check_guess(guess, ans):
    if guess == ans:
        print("Just right!")
        return True
    elif guess > ans:
        print("Too large!")
    elif guess < ans:
        print("Too small!")
    return False

if __name__ == "__main__":
    main()

# professor.py
import random


def main():
    turns = 10
    level = get_level()
    score = 0
    while turns > 0:
        x , y = generate_integer(level) , generate_integer(level)
        ans = x + y
        tries = 3

        while tries > 0:
            user_ans = input(f"{x} + {y} = ")
            if user_ans != str(ans):
                print("EEE")
                tries -= 1
            elif user_ans == str(ans):
                score += 1
                break
        if tries == 0:
            print(f"{x} + {y} = {x+y}")
        turns -= 1
    print(f"Score: {score}")




def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 0 < level < 4:
                return level
            else:
                raise ValueError("Available levels are : 1, 2, 3")
        except ValueError as e:
            print (e)




def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10,99)
    elif level == 3:
        return random.randint(100,999)
    raise ValueError("Invalid Level")


if __name__ == "__main__":
    main()


# bitcoin.py
import requests
import sys

args = len(sys.argv)
if  args == 1:
    print("Missing command-line argument ")
    sys.exit(1)
elif args == 2:
    try:
        amount = float(sys.argv[1])
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        p = response.json()
        price = p["bpi"]["USD"]["rate"]
        amount *= float(price.replace(",",""))
        print( f"${amount:,.4f}")
        sys.exit(0)
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)
    except requests.RequestException:
        pass
else:
    sys.exit(1)

