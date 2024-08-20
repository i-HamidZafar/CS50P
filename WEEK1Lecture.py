# CONDITIONALS

# compare.py
#   --------------
  #not well designed [repitive]
  x = int(input("What's x? "))
  y = int(input("What's y? "))
  
  if x < y:
      print("x is less than y")
  if x > y:
      print("x is greater than y")
  if x == y:
      print("x is equal to y")

  # --------------with if elif 
  x = int(input("What's x? "))
  y = int(input("What's y? "))
  
  if x < y:
      print("x is less than y")
  elif x > y:
      print("x is greater than y")
  elif x == y:
      print("x is equal to y")

  # --------------with if elif else
  x = int(input("What's x? "))
  y = int(input("What's y? "))
  
  if x < y:
      print("x is less than y")
  elif x > y:
      print("x is greater than y")
  else:
      print("x is equal to y")

 # --------------equal or not [bad]
  x = int(input("What's x? "))
  y = int(input("What's y? "))
  
  if x < y or x > y:
      print("x is not equal to y")
  else: 
      print("x is equal to y")

  # --------------equal or not 
  x = int(input("What's x? "))
  y = int(input("What's y? "))
  
  if x != y:
      print("x is not equal to y")
  else: 
      print("x is equal to y")

# Grade.py
#   --------------
  score = int ( input("Score? ") )

  if score >= 90 and score <= 100:
      print("Grade :A")
  elif score >= 80 and score < 90:
      print("Grade: B")
  elif score >= 70 and score < 80:
      print("Grade: C")
  elif score >= 60 and score < 70:
      print("Grade:D")
  else:
      print("Grade: F")

  # -------------- Ranging
  score = int ( input("Score? ") )

  if 90<= score <= 100:
      print("Grade :A")
  elif 80<= score < 90:
      print("Grade: B")
  elif 70<= score < 80:
      print("Grade: C")
  elif 60<= score < 70:
      print("Grade:D")
  else:
    print("Grade: F")

  # -------------- asking less questions
  score = int ( input("Score? ") )

  if score >= 90:
      print("Grade :A")
  elif score >=80:
      print("Grade: B")
  elif score >= 70:
      print("Grade: C")
  elif score >= 60:
      print("Grade:D")
  else:
    print("Grade: F")

# parity.py
#   --------------
  num = int( input ("Num: ") )
  
  if num % 2 == 0:
      print("Even")
  else:
      print("Odd")

  # -------------- Creating function
  def main():
    num = int( input("Num: ") )

    if is_even(num):
        print("Even")
    else:  
          print("Odd")
  
  def is_even(num):
      if num % 2 == 0:
          return True
      else:
          return False
  main()

  # ---------------  Pythonic way to do it with functions  
  def main():
    num = int( input("Num: ") )

    if is_even(num):
        print("Even")
    else:  
        print("Odd")
  
  def is_even(num):
      return True if num % 2 == 0 else False
  main()

  # ---------------  most elegent 
  def main():
    num = int( input("Num: ") )

    if is_even(num):
        print("Even")
    else:  
        print("Odd")
  
  def is_even(num):
      return num % 2 == 0
  main()

# house.py
#   -------------- nayy
  name = input("What's your name? ")

  if name == "Harry" or name == "Ron" or name == "Hermione":
      print("Gryffindor")
  elif name == "Ron" or name == "Hermione":
      print("Gryffindor")
  elif name == "Hermione":
      print("Gryffindor")
  elif name == "Draco":
      print("Slytherin")
  else:
      print("Who?")

  # -------------- better
  name = input("What's your name? ")

  if name == "Harry" or name == "Ron" or name == "Hermione":
      print("Gryffindor")
  elif name == "Draco":
      print("Slytherin")
  else:
      print("Who?")

  # -------------- using case [match]

  name = input("What's your name? ")

  match name:
      case "Harry":
          print("Gryffindor")
      case "Ron":
          print("Gryffindor")
      case "Hermione":
          print("Gryffindor")
      case "Draco":
          print("Slytherin")

  # -------------- using case [match] handling other names

  name = input("What's your name? ")

  match name:
      case "Harry":
          print("Gryffindor")
      case "Ron":
          print("Gryffindor")
      case "Hermione":
          print("Gryffindor")
      case "Draco":
          print("Slytherin")
      case _:
          print("Who?")

# -------------- using match statement handling other names

  name = input("What's your name? ")

  match name:
      case "Harry":
          print("Gryffindor")
      case "Ron":
          print("Gryffindor")
      case "Hermione":
          print("Gryffindor")
      case "Draco":
          print("Slytherin")
      case _:
          print("Who?")

  # ------------- more readable
  
  name = input("What's your name? ")

  match name:
      case "Harry" | "Hermione" | "Ron":
          print("Gryffindor")
      case "Draco":
          print("Slytherin")
      case _:
          print("Who?")



  
  
