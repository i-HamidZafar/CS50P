# LOOPS

# cat.py
#   ------------- Without Loop
  print("Meow")
  print("Meow")
  print("Meow")

  # ------------- while loop
  i = 3
  while i != 0:
      print("Meow")
      i = i - 1 
  # ------------- 
  i = 1 
  while i <= 3:
      print("Meow")
      i = i + 1
  # ------------- 
  i = 0
  while i < 3:
      print("Meow")
      i += 1

  # ------------- for loop [poorly]
  for i in [0, 1, 2]:
    print("Meow")

  # ------------- for loop using range instead of list of values
  for i in [0, 1, 2]:
    print("Meow")

  # ------------- when you don't care about the name of the variable
  for _ in [0, 1, 2]:
    print("Meow")

  # ------------- pythonic but not a good thing to do due to readability 
  print("Meow\n" * 3)


  # ------------- input validation
  while True:
    cnt = int(input("what's n? "))
    if cnt < 0:
        continue
    else:
        break
  
  for i in range(cnt):
      print("Meow")

  # ------------- input validation
  while True:
    cnt = int(input("what's n? "))
    if cnt < 0:
        continue
    else:
        break
  
  for i in range(cnt):
      print("Meow")

  # ------------- better
  while True:
    cnt = int( input("What's n?") )
    if cnt > 0:
        break
  for _ in range(cnt):
      print("Meow")

  # ------------- hardcoded with function
  def main():
    meow(4)

  def meow(times):
    for _ in range(times):
      print("Meow")
  main()
  # ------------- with function
  def main():
    cnt = get_num()
    meow(cnt)
  def get_num():
      while True:
          n = int(input("what's n?"))
          if n > 0:
              return n
  def meow(times):
      for _ in range(times):
          print("Meow")
  main()

  # ------------- with function [scope of n is within the function not the loop only]
  def main():
    cnt = get_num()
    meow(cnt)
  def get_num():
      while True:
          n = int(input("what's n?"))
          if n > 0:
            break;
      return n
  def meow(times):
      for _ in range(times):
          print("Meow")
  main()

# hogwarts.py
#   ------------- lists
  students = ["Harmione", "Harry", "Ron"]

  #indexing into the list  

  print(students[0])
  print(students[1])
  print(students[2])

  # ------------- itterating through list using loops
  students = ["Harmione", "Harry", "Ron"]

  for student in students:
    print(student)
  # ------------- using len() for indexing through the list

  students = ["Harmione", "Harry", "Ron"]

  for idx in range(len(students)):
      print(students[idx])

  # ------------- ranking

  students = ["Harmione", "Harry", "Ron"]

  for idx in range(len(students)):
      print(idx + 1,students[idx])

  # ------------- Dict

  student = {"Hermione": "Gryffindor",
           "Harry": "Gryffindor",
           "Ron": "Gryffindor",
           "Draco": "Gryffindor",
           }

  print(student["Ron"])
  print(student["Harry"])
  print(student["Hermione"])

  # ------------- Looping through dict [keys]

  students = {"Hermione": "Gryffindor",
           "Harry": "Gryffindor",
           "Ron": "Gryffindor",
           "Draco" : "Slytherin",
  }
  
  for student in students:
      print(student)

  # ------------- Dict key values

  students = {"Hermione": "Gryffindor",
           "Harry": "Gryffindor",
           "Ron": "Gryffindor",
           "Draco" : "Slytherin",
  }
  
  for  student in students:
      print(student, students[student], sep = ", ")

  # ------------- list of Dict

  students = [
    {"name": "Hermione", "house" : "Gryffindor", "patronous" : "Otter"},
    {"name": "Hermione", "house" : "Gryffindor", "patronous" : "Stag"},
    {"name": "Hermione", "house" : "Gryffindor", "patronous" : "Jack Russell terrier"},
    {"name": "Draco", "house" : "Slytherin", "patronous" : None},
  ]
  
  for student in students:
      print(student["name"], student["house"], student["patronous"],  sep= ", ")

# mario.py
  # ------------- without loop
  print("#")
  print("#")
  print("#")

  # ------------- loop
  for _ in range(3)
    print("#"

  # ------------- using function
  def main():
    print_column(3)
  def print_column(height):
    for _ in range(height):
        print("#")
  main()

  # ------------- using function changing the implementation
  
  def main():
    print_column(3)
  def print_column(height):
          print("#\n" * height, end ="")
  main()

  # ------------- horizontal question marks
  def main():
    print_row(4)

  def print_row(width):
      print("?" * width)
  
  main()

  # ------------ printing mario squares without nested loops
  def main():
    print_square(3)

  def print_square(size):
      for _ in range(size):
          print("#" * size)
  main()

  # ------------ 
  def main():
    print_square(3)

  def print_square(size):
      for _ in range(size):
          print_row(size)
  def print_row(width):
    print("#" * width)
  main()


  # ------------ printing mario squares with nested loops
  def main():
    print_square(3)

  def print_square(size):
      for row in range(size):
          for col in range(size):
              print("#", end="")
          print()
  main()
