# deep.py
#   ----------------
  def main():
    ans = input("What's the answer to life, the universe, and everything? ").lower().strip()

    match ans:
          case "forty-two" | "42" | "forty two":
              print("Yes")
          case _:
              print("No")
  
  main()

# bank.py
#   ----------------
  def main():
    greeting = input("Greeting: ").strip().lower()
  
    if greeting.find('hello') != -1:
        print("$0")
    elif greeting[0] == 'h':
        print("$20")
    else:
        print("$100")
  main()
  
 # extensions.py
 #  ----------------
  def main():
    file_name = input("File name: ").strip().lower()
    extension = file_name.split('.')[-1]
    print(find_type(extension))

  def find_type(extension):
      match extension:
          case "png" | "gif":
              return "image/" +extension
          case "jpg" | "jpeg":
              return "image/jpeg"
          case "pdf":
              return "application/pdf"
          case "txt":
              return "text/plain"
          case "zip":
              return "application/zip"
          case _:
              return "application/octet-stream"
  
  main()

# interpreter.py
#   ----------------
  def main():
    exp = input("Expression: ").split()
    x , op , z = int(exp[0]) , exp[1] , int(exp[2])
    match op:
        case "+":
            print(float(x + z), end="")
        case "-":
            print(float(x - z), end="")
        case "/":
            print(float(x / z))
        case "*":
            print(float(x * z), end="")
        case _:
            print("Byee.....")
  main()

# meal.py
#   ----------------
  def main():
    time = input("What time is it? ")
    hours , min = time.split(":")
    hours, min = int(hours), int(min)

    match hours:
        case 7:
            print("Breakfast time")
        case 12:
            print("Lunch time")
        case 8 | 13 | 19:
            if hours == 8 and min == 0:
                print("Breakfast time")
            elif hours == 13 and min == 0:
                print("Lunch time")
            elif hours == 19 and min == 0:
                print("Dinner time")
        case 18:
            print("Dinner time")
  def convert(time):
      hours , min = time.split(":")
      hours , min = int(hours), int(min)
  
      return (hours + (min / 60))
  
  if __name__ == "__main__":
      main()
  # ----------------
