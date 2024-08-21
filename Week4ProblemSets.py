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
