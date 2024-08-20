# Libraries

# generate.py

#   random module
#   --------------import
  import random
  
  coin = random.choice(["heads", "tails"])
  print(coin)


  # ------------- from x import y
  from random import choice
  
  coin = choice(["heads", "tails"])
  print(coin)

  # ------------ randint()
  import random
  
  number = random.randint(1,10)
  print(number)


  # ----------- shuffle(x)
  import random
  
  cards = ["jack", "queen", "king"]
  random.shuffle(cards)
  for card in cards:
      print(card)

# average.py
#   statistics
#   ----------- mean
  import statistics
  print(statistics.mean([100, 90]))

# name.py
#   sys
#   -----------  sys.argv[CL Arguments] [argument vector]
  import sys
  try: 
      print("hello, my name is", sys.argv[1])
  except IndexError:
      print("Too few Arguments")
  # ---------- avoid exceptions
  import sys
  
  if len(sys.argv) < 2:
      print("Too few args")
  elif len(sys.argv) > 2:
      print("Too many args")
  else:
      print("hello, my name is", sys.argv[1])

  # ----------- multiple args
  import sys
  
  if len(sys.argv) < 2:
      sys.exit(print("Too few args"))
  for arg in sys.argv[1:]:
      print("hello, my name is", arg)

# say.py
#   cowsay package
#   -----------
  import sys
  import cowsay
  
  if len(sys.argv) == 2:
      cowsay.trex("hello," + sys.argv[1])

# itunes.py
#   APIs & JSON
#   ----------- REQUESTS library: get a response from an API
  import requests
  
  import sys
  
  if len(sys.argv) != 2:
      sys.exit()
  
  response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
  
  print(response.json())

  # ----------- Lazily printing out the content of the response using dumps()  
  import requests
  import json
  import sys
  
  if len(sys.argv) != 2:
      sys.exit()
  
  response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
  print(json.dumps(response.json(), indent = 7))

# WHY shouldn't call main() like this:
# sayings.py
  # -------------
  def main():
        hello("world")
        good_bye("world")
    
    def hello(name):
        print(f"hello, {name}")
    
    def good_bye(name):
        print(f"goodbye, {name}")
    
  main()
# -----------------------------
say.py
  import sys
  from sayings import hello
  
  if len(sys.argv) == 2:
      hello(sys.argv[1])
# -----------------------------

# use main() like this:

# sayings.py
  # ------------------------
  def main():
      hello("world")
      bye("world")
    
  def hello(name):
      print(f"hello, {name}")
  
  def bye(name):
      print(f"goodbye, {name}")
  if __name__ == "__main__":
      main()
# --------------------------
# say.py
  import sys
  from sayings import bye
  
  if len(sys.argv) == 2:
      bye(sys.argv[1])
# -----------------------------

