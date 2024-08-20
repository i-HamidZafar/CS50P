# hello.py
#   ---------------//Syntax Error [unterminated string literal] 
  print("Hello, world)

# number.py
#   ---------------//prone to ValueError
  x = int(input("What's x?"))
  print(f"x is {x}")

  # --------------- Handles ValueError
  try:
    x = int(input("What's x?"))
    print(f"x is {x}")
  except ValueError:
      print("x is not an integer")
  # --------------- Better but Prone to NameError [x not define in case of catch of ValueError]
  try:
    x = int(input("What's x?"))
  except ValueError:
      print("x is not an integer")

  print(f"x is {x}")
  # --------------- else block in try except (executed when the except block is not executed.)
  try:
    x = int(input("What's x?"))
  except ValueError:
      print("x is not an integer")
  else:
      print(f"x is {x}")

  # --------------- input validation
  while True:
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x is not an integer")
    else:
        break
      
  print(f"x is {x}")

  # --------------- without else block
  while True:
    try:
        x = int(input("What's x? "))
        break
    except ValueError:
        print("x is not an integer")

  print(f"x is {x}")


  # --------------- abstracting with the function
  def main():
    x = get_int()
    print(f"x is {x}")

  def get_int(): 
      while True:
          try:
              x = int(input("What's x? "))
          except ValueError:
              print("x is not an integer")
          else:
              return x
  
  main()

  # ---------------- shortened
  def main():
    x = get_int()
    print(f"x is {x}")

  def get_int(): 
      while True:
          try:
              return int(input("What's x? "))
          except ValueError:
              print("x is not an integer")
  
  main()

  # --------------- catching the error but passing to handle it further
  def main():
    x = get_int()
    print(f"x is {x}")

  def get_int(): 
      while True:
          try:
              return int(input("What's x? "))
          except ValueError:
              pass
  
  main()

  # -------------- more compact

  def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

  def get_int(prompt): 
      while True:
          try:
              return int(input(prompt))
          except ValueError:
              pass
  
  main()


  
