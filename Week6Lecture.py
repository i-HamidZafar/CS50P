# FILE I/O
# names.py
# ----simple
  name = input("What's your name? ")
  print(f"hello, {name}")
# --- introducing list
  names = []
  for _ in range(3):
      names.append(input("What's your name? "))
  for name in sorted(names):
      print(f"hello, {name}")
# ---writing to files ["w" overwrites the previous content]
  name = input("What's your name? ")
  
  file = open("names.txt", "w") #returns a file handle
  file.write(name)
  file.close()
# ---appending to the file [but have to sepereate the word for reading more cleanly]
   name = input("What's your name? ")
    
    file = open("names.txt", "a") #returns a file handle
    file.write(name)
    file.close()
# appending one name per line
  name = input("What's your name: ")
  
  file = open("names.txt", "a")
  file.write(f"{name}\n")
  file.close()
# better design more pythonic (opens, and closes the closes the file by itself.)
  name = input("what's your name: ")
  
  with open("names.txt", "a") as file:
      file.write(f"{name}\n")

# READING FROM FILE
  with open("names.txt", "r") as file:
      lines = file.readlines()
  
  for line in lines:
      print(f"hello, {line.rstrip()}") #strip offs the new line added in the file
# making it more compact and elegant
  with open("names.txt", "r") as file:
      for line in file:
          print("hello,", line.rstrip())

# displaying the prompt by names
  names = []
  with open("names.txt") as file:
      for line in file:
          names.append(line.rstrip())
  for name in sorted(names, reverse = False): #true for descending sort
      print(f"hello, {name}")
# using a more compact approach for printing in sorted order
  with open("names.txt") as file:
      for line in sorted(file):
          print("hello,", line.rstrip())
_________________________________________
       
#students.py
# reading 2D file
  with open("students.csv") as file:
      students = []
      for line in file:
          row = line.rstrip().split(",")
          print(f"{row[0]} is in {row[1]}")
      
# less cryptic and unpacking the list 
  with open("students.csv") as file:
      students = []
      for line in file:
          name, house = line.rstrip().split(",")
          print(f"{name} is in {house}")

# sorting by name, not well designed

  students = []
  with open("students.csv") as file:
      for line in file:
          name, house = line.rstrip().split(",")
          students.append(f"{name} is in {house}")
  
  for student in sorted(students):
      print(student)

# using dict

  students= []
  with open("students.csv") as file:
      for line in file:
          name, house = line.rstrip().split(",")
          student = {"name": name , "house": house}
          students.append(student)
  for student in students:
      print(f"{student['name']} is in {student['house']}")

# improving it further [sorting by a "key" in a dictionary]
  def main():
      students= []
      with open("students.csv") as file:
          for line in file:
              name, house = line.rstrip().split(",")
              student = {"name": name , "house": house}
              students.append(student)
      for student in sorted(students, key= get_name, reverse=True):
          print(f"{student['name']} is in {student['house']}")
  
  def get_name(student):
      return student["name"]
  def get_house(student):
      return student["house"]
  
  if __name__ == "__main__":
      main()

# using lambda function [better]

  def main():
      students = []
  
      with open("students.csv") as file:
          for line in file:
              name , house = line.rstrip().split(",")
              student = {"name": name, "house": house}
              students.append(student)
      for student in sorted(students, key= lambda student: student["name"], reverse=True):
          print(f"{student['name']} is in {student['house']}")
  
  if __name__ =="__main__":
      main()



#uisng CSV MODULE to handle seperation, parsing of values within the file more conventiently with more effective reads

  # using csv reader
  import csv
  def main():
      students = []
  
      with open("students.csv") as file:
          reader = csv.reader(file)
          for name, home in reader:
              students.append({"name": name, "home": home})
  
  
      for student in sorted(students, key= lambda student: student["name"], reverse=True):
          print(f"{student['name']} is from {student['home']}")
  
  if __name__ =="__main__":
      main()

  #using DictReader [you can explicitly bake the information about what each column name is to use it] more robust code
  
  import csv
  def main():
      students = []
  
      with open("students.csv") as file:
          reader = csv.DictReader(file)
          for row in reader:
              students.append(row)
  
  
      for student in sorted(students, key= lambda student: student["name"], reverse=True):
          print(f"{student['name']} is from {student['home']}")
  
  if __name__ =="__main__":
      main()

# CSV WRITER
  # using simple writer
  import csv
  
  def main():
      name = input("what's your name? ")
      home = input("what's your home? ")
      with open("students.csv", "a") as file:
          writer = csv.writer(file)
          writer.writerow([name,home])
  if __name__ == "__main__":
      main()

  # using DictWriter
  import csv
  
  def main():
    name = input("what's your name? ")
    home = input("what's your home? ")
    with open("students.csv", "a", newline= "") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "home"])#coloumns ordering in the file [fieldnames]
        writer.writerow({"name": name, "home": home})
  if __name__ == "__main__":
    main()

