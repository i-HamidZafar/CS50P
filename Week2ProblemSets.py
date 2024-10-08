# camel.py
#   ----------------
  user_input = input("camelCase: ")

  for i in range(len(user_input)):
      if user_input[i].isupper():
          user_input = user_input[:i] + "_" + user_input[i].lower() + user_input[i + 1:]
  print("snake_case:", user_input)

# coke.py
#   ----------------
  amount = 50
  change = 0
  while amount > 0:
      print("Amount Due:", amount)
      coin = int(input("Insert Coin: "))
      match coin:
          case 5 | 10 | 25:
              amount -= coin
              if amount < 0:
                  change -= amount
  
  print("Change Owed:", change)

# twttr.py
#   ----------------
  user_input = input("Input: ").strip()
  res =""
  vowels =["a","e" ,"i" ,"o" ,"u", "A" ,"E" ,"I" ,"O", "U"]
  for i in range(len(user_input)):
      if user_input[i] not in vowels:
              res += user_input[i]
  print("Output:", res)

# plates.py
#   ---------------
  def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

  def is_valid(s):
      if 2 <= len(s) <= 6:
          if s.isalpha():
                  return True
          elif s[:2].isalpha() == False or s.isalnum() == False:
                  return False
          else:
              for i in range(-2, -len(s), -1):
                   if s[i].isdigit() == False:
                      if s[i + 1] == '0' or s[0: i + 1].isalpha() == False:
                        return False
                      else:
                        return True
      return False
  
  
  main()

# nutrition.py
#   ---------------
  def main():
    item_name = input("Item").lower()
    print("Calories:",get_calories(item_name))

  def get_calories(item):
      match item:
          case "apple":
              return 130
          case "avocado" | "cantaloupe" | "honeydew melon" | "strawberries" | "tangerine":
              return 50
          case "banana":
              return 110
          case "grapefruit" | "nectarine" | "peach":
              return 60
          case "grapes" | "kiwifruit":
              return 90
          case "lemon":
              return 15
          case "lime":
              return 20
          case "orange":
              return 80
          case "pear" | "sweet cherries":
              return 100
          case "plums":
              return 70
          case "watermelon":
              return 80
          case _:
              exit()
  
  main()

