# fuel.py
#   -------------
  def main():
    fuel = get_fuel()
    print(fuel)
  def get_fuel():
      while True:
          try:
              x, y = input("Fraction: ").split("/")
              x, y = int(x) ,int(y)
              if x <= y:
                  fuel = round((x / y) * 100)
                  if fuel <= 1  or fuel >=99:
                      return "F" if fuel >= 99 else "E"
                  else:
                      return str(fuel) + "%"
          except (ZeroDivisionError, ValueError):
              pass
  main()

# taqueria.py
#   ---------------
  def main():
      menu = {"Baja Taco": 4.25, "Burrito": 7.50, "Bowl": 8.50,
              "Nachos": 11.00, "Quesadilla": 8.50, "Super Burrito": 8.50,
              "Super Quesadilla": 9.50, "Taco": 3.00, "Tortilla Salad": 8.00
      }
      invoice(menu)
  
  def invoice(menu):
      total = 0
      while True:
          try:
              item = input("Item: ").title()
              total += menu[item]
              print(f"Total: ${total:.2f}")
          except EOFError:
              print()
              break
          except KeyError:
              pass
  
  main()

# grocery.py
#   --------------
  def main():
    get_grocery_list()

  def get_grocery_list():
      grocery_list = {}
      while True:
          try:
              item = input().upper()
          except EOFError:
              print()
              display_list(grocery_list)
              return
          else:
              grocery_list[item] = grocery_list.setdefault(item, 0) + 1
  def display_list(items):
      keys = sorted(items.keys())
      for key in keys:
          print(items[key], key)
  
  main()

# outdated.py
#   ---------------
  def main():
    get_date()

def print_date(year, month, day):
    print(f"{year}-{month:02}-{day:02}")
def split_date(date, delimiter):
    month, day, year = date.replace(delimiter," ").split()
    return month , day , year
def validate_date(month, day, year):
    return 13 > month > 0 and 31 >= day > 0 and year > 0

def get_date():
    months_list =[    "January", "February", "March", "April", "May", "June", "July",
                        "August", "September", "October", "November", "December"        ]
    while True:
        input_date = input("Date: ")
        if '/' in input_date:
            month, day, year = split_date(input_date, '/')
            try:
                if validate_date(int(month), int(day), int(year)):
                    print_date(year, int(month), int(day))
                    break
            except(ValueError, IndexError):
                pass
        elif ',' in input_date:
            month, day, year = split_date(input_date, ',')
            try:
                if validate_date(months_list.index(month) + 1, int(day), int(year)):
                    print_date(year, months_list.index(month) + 1, int(day))
                    break
            except(ValueError, IndexError):
                pass

main()

