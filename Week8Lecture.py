# Object Oriented Programming LECTURE 8

#student.py

   # working program
  name = input("Name: ")
  house = input("House: ")
  print(f"{name} from {house}")

  #introducing week 0 learnings 
  def main():
      name = get_name()
      house = get_house()
      print(f"{name} from {house}")
  
  def get_name():
      return input("Name: ")
  
  def get_house():
      return input("House: ")
  
  if __name__ == "__main__":
      main()

  #trying to return a student
  def main():
      name , house = get_student()
      print(f"{name} from {house}")
  
  def get_student():
      name = input("Name: ")
      house = input("House: ")
      return name, house
  
  if __name__ == "__main__":
      main()

  #explicitly using tuple
  def main():
      student = get_student()
      print(f"{student[0]} from {student[1]}")
  
  def get_student():
      name = input("Name: ")
      house = input("House: ")
      return (name, house)
  
  if __name__ == "__main__":
      main()

  #Immutability of tuples
  def main():
      student = get_student()
      if student[0] == "Padma":
          student[1] = "Ravenclaw"
      print(f"{student[0]} from {student[1]}")
  
  def get_student():
      name = input("Name: ")
      house = input("House: ")
      return (name, house)
  
  if __name__ == "__main__":
      main()

  #mutability of lists
  def main():
      student = get_student()
      if student[0] == "Padma":
          student[1] = "Ravenclaw"
      print(f"{student[0]} from {student[1]}")
  
  def get_student():
      name = input("Name: ")
      house = input("House: ")
      return [name, house]
  
  if __name__ == "__main__":
      main()

  #same solution (getting student) using dict
  def main():
      student = get_student()
      print(f"{student['name']} from {student['house']}")
  
  def get_student():
      return {"name": input("Name: ") , "house" : input("House: ")}
  
  if __name__ == "__main__":
      main()
    
  #mutability of dicts
  def main():
      student = get_student()
      if student["name"] == "Padma":
          student["house"] = "Ravenclaw"
      print(f"{student["name"]} from {student["house"]}")
  
  def get_student():
      return {"name": input("Name: ") , "house" : input("House: ")}
  
  if __name__ == "__main__":
      main()


# OOP
  #using classes
  class Student:
      ... #for later implementation of the class but it exists now
  
  def main():
      student = get_student()
      print(f"{student.name} from {student.house}")
  
  def get_student():
      student = Student()
      student.name = input("Name: ")
      student.house = input("House: ")
      return student
  
  if __name__ == "__main__":
      main()

  #dunder init method [using the parameterized constructor]
  class Student:
      def __init__(self, name, house): #instantiation of objects ( automatically called when the constuctor is called)
          self.name = name 
          self.house = house
       
  
  def main():
      student = get_student()
      print(f"{student.name} from {student.house}")
  
  def get_student():
      name = input("Name: ")
      house = input("House: ")
      return Student(name, house)
  
  if __name__ == "__main__":
      main()

  #tightening code up(validating object attributes)
  class Student:
      def __init__(self, name, house): 
          if not name:
              raise ValueError("Missing name")
          if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
              raise ValueError("Invalid house")
          self.name = name 
          self.house = house
       
  
  def main():
      student = get_student()
      print(f"{student.name} from {student.house}")
  
  def get_student():
      name = input("Name: ")
      house = input("House: ")
      student = Student(name, house)
      return student
  
  if __name__ == "__main__":
      main()

   #tryna print student
    class Student:
        def __init__(self, name, house): 
            if not name:
                raise ValueError("Missing name")
            if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
                raise ValueError("Invalid house")
            self.name = name 
            self.house = house
    
    def main():
        student = get_student()
        print(student)
    
    def get_student():
        name = input("Name: ")
        house = input("House: ")
        student = Student(name, house)
        return student
    
    if __name__ == "__main__":
        main()

  #printing student using  __str__()
  class Student:
      def __init__(self, name, house): 
          if not name:
              raise ValueError("Missing name")
          if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
              raise ValueError("Invalid house")
          self.name = name 
          self.house = house
  
      def __str__(self):
          return f"{self.name} from {self.house}"
  
  def main():
      student = get_student()
      print(student)
  
  def get_student():
      name = input("Name: ")
      house = input("House: ")
      student = Student(name, house)
      return student
  
  if __name__ == "__main__":
      main()


  #class methods (userdefined)
  class Student:
      def __init__(self, name, house, patronus): 
          if not name:
              raise ValueError("Missing name")
          if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
              raise ValueError("Invalid house")
          self.name = name 
          self.house = house
          self.patronus = patronus
  
      def __str__(self):
          return f"{self.name} from {self.house}"
  
      def charm(self):
          match self.patronus:
              case "Stag":
                  return "🦌"
              case "Otter":
                  return "🦦"
              case "Jack Russel terrier":
                  return "🐶"
              case _:
                  return "🧙‍♂️"
  def main():
      student = get_student()
      print("Expecto Patronum!")
      print(student.charm())
  
  def get_student():
      name = input("Name: ")
      house = input("House: ")
      patronus = input("Patronus: ")
      student = Student(name, house, patronus)
      return student
  
  if __name__ == "__main__":
      main()

  #still not robust
  class Student:
      def __init__(self, name, house): 
          if not name:
              raise ValueError("Missing name")
          if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
              raise ValueError("Invalid house")
          self.name = name 
          self.house = house
  
      def __str__(self):
          return f"{self.name} from {self.house}"
  
  def main():
      student = get_student()
      student.house = "Number Four, Privet Drive"
      print(student)
  
  def get_student():
      name = input("Name: ")
      house = input("House: ")
      student = Student(name, house)
      return student
  
  if __name__ == "__main__":
      main()

  # more robust with error checking in one place
  #using properties [note: don't collide names]
  class Student:
      def __init__(self, name, house):         
          self.name = name #assignment goes through the setter
          self.house = house 
  
      @property
      def name(self):
          return self._name
      @name.setter
      def name(self, name):
          if not name:
              raise ValueError("Missing name")
          self._name = name
      @property    
      def house(self):
          return self._house
      @house.setter
      def house(self, house):
          if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
              raise ValueError("Invalid house")
          self._house = house
      def __str__(self):
          return f"{self.name} from {self.house}"
  
  def main():
      student = get_student()
      student.house = "Number Four, Privet Drive"
      print(student)
  
  def get_student():
      name = input("Name: ")
      house = input("House: ")
      student = Student(name, house)
      return student
  
  if __name__ == "__main__":
      main()

