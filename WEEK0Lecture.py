# Hello, World:
  print("Hello, world")

# Input:
  name = input("What is your name: ")
  print("Hello,")
  print(name)
  # -----------------
  name = input("What is your name: ")
  print("Hello, " + name)
  # -----------------
  name = input("What is your name: ")
  print("Hello,",  name)
  # -----------------//endline
  name = input("What is your name: ")
  print("Hello, ", end='')
  print(name)
  # -----------------//seperate arguments
  name = input("What is your name: ")
  print("Hello,",  name, sep = "??")
  # -----------------//escape sequences
  print("Hi, \"John Doe\"")

  print('Printing " using \'')
  
  # -----------------//formated string
  name = input("What is your name? ")
  print(f"Hello, {name}")

# String methods:
#   ----------------//Remove whitespaces [from and and right of string]
  name = input("What is your name? ")
  name = name.strip()  
  print(f"Hello, {name}")

  # ----------------//Strip and capitalize (only firstcharacter of the string)
  name = input("What is your name? ")
  name = name.strip().capitalize()
  print(f"Hello, {name}")

  # ----------------//Strip and capitalize (only first character of each word)
  name = input("What is your name? ")
  name = name.strip().title()
  print(f"Hello, {name}")

  # ----------------//Cleaned
  name = input("What is your name? ").strip().capitalize()
  print(f"Hello, {name}")

  # ---------------//removes space from left, right and middle of the string and capitalize the characters of each word in the string [not from lecture]
  name = input("What is your name? ").strip().title()
  name = name.split()
  res =""
  for n in name:
      res += n.strip() + " "
  
  print(f"Final string: {res} ")

  # ---------------//First Name Last Name using Split()
  first , last = input("what is your name? ").strip().title().split()
  print(f"First Name: {first}")

# Integer:
#   ----------------//calculator.py [type conversion]
  x , y = input("What's x? ") , input("What's x? ")
  sum = int(x) + int(y)
  print(f"Sum : {sum}")
  # ----------------
  x , y = int(input("What's x? ")) , int(input("What's x? "))

  print(f"Sum : {x + y}")

# Float:
#   ----------------
  x , y = float(input("What's x? ")) , float(input("What's x? "))

  print(f"Sum : {x + y}")
  # ----------------//rounding
  x , y = float(input("What's x? ")) , float(input("What's x? "))

  sum = round(x + y,1)
  print(f"Sum : {sum}")

  # ----------------//number formating
  x , y = float(input("What's x? ")) , float(input("What's x? "))

  sum = round(x + y,2)
  print(f"Sum : {sum:,}")

  # ---------------//Division

  x , y = float(input("What's x? ")) , float(input("What's x? "))

  div  = x / y
  print(f"Div : {div}")

  # --------------//Rounded Division
  x , y = float(input("What's x? ")) , float(input("What's x? "))

  div  = round(x / y,2 )
  print(f"Div : {div}")

  # --------------//Rounded Division with fstring [formated string]
  x , y = float(input("What's x? ")) , float(input("What's x? "))

  div  = x / y
  print(f"Div : {div:.2f}")

  # -------------// Rounded division with user input of digits after decimal point
  x , y = float(input("What's x? ")) , float(input("What's x? "))
  n = input("Enter number of digits you want to rround to : ")
  div  = x / y
  print(f"Div : {div:.{n}f}")

# Functions:
#   ------------// hello ()
  def hello():
    print("Hello,")
  
  name = input("What is your name? ")
  hello()
  print(name)
  
  # ----------// hello (to)
  def hello(to):
    print(f"Hello, {to}")


  name = input("What is your name? ")
  hello(name) 

  # ----------// hello (to) default value for parameter /// won't run 
  hello() 
  name = input("What is your name? ")
  hello(name) 


  def hello(to = "World"):
    print(f"Hello, {to}")

  # ---------//using main function

  def main():    
    name = input("What is your name? ")
    hello(name) 

  def hello(to = "world"):
      print(f"Hello, {to}")
  
  main()


  # --------// scope (doesn't run)
  def main():   
    name = input("What is your name? ")
    hello() 

  def hello():
      print("Hello,", name)
  
  main()

  # ---------//final hello.py

  def main():    
    name = input("What is your name? ")
    hello(name) 

  def hello(to = "world"):
      print(f"Hello, {to}")
  
  main()


  # ---------//calculator.py (simple square)
  def main():
    x = int(input("what's x?"))
    print("x squared is:", square(x))
  
  def square(n):
      return n * n
  
  main()

  # ---------//calculator.py (square by raising to the power 2)
  def main():
    x = int(input("what's x?"))
    print("x squared is:", square(x))
  
  def square(n):
      return n ** 2
  
  main()

  # ---------//calculator.py (using pow())
  def main():
    x = int(input("what's x?"))
    print("x squared is:", square(x))
  
  def square(n):
      return pow(n, 2)
  
  main()

  # ---------//Calculator.py
  def main():
    x = int(input("what's x? "))
    pw= int(input("power? "))
    print("x squared is:", square(x))
    print(f"x ^ {pw} is: {pw_fun(x,pw)}")

  def square(n):
      return n ** 2
  
  def pw_fun(x,n):
      return x ** n
  
  main()
  
  

  
