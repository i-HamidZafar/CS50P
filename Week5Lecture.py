# ---Unit Tests

# calculator.py
# ---------------
  def main():
      x = int(input("What's x? "))
      print("x squared is", square(x))
  
  def square(of):
      return of ** 2
  if __name__ == "__main__":
      main()

test_calculator.py
# ---------------
  from calculator import square
  
  def main():
      test_square()
  
  def test_square():
      if square(2) != 4:
          print("2 squared wasn't 4")
      if square(3) != 9:
          print("3 square wasn't 9")
  
  if __name__ == "__main__":
      main()
# ----------------------using assert instead 
  from calculator import square
  
  def main():
      test_square()
  
  def test_square():
      assert square(2) == 4
      assert square(3) == 9
  
  if __name__ == "__main__":
      main()
# --------------------- but with more use friendly output
  from calculator import square
  
  def main():
      test_square()
  
  def test_square():
      try: 
          assert square(2) == 4
      except AssertionError:
          print("2 Square wasn't 4")
      try:
          assert square(3) == 9
      except AssertionError:
          print("3 Square wasn't 9")
  
  if __name__ == "__main__":
      main()

# --------------------- Bad testing
from calculator import square

def main():
    test_square()

def test_square():
    try: 
        assert square(2) == 4
    except AssertionError:
        print("2 Square wasn't 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 Square wasn't 9")
    try: 
        assert square(-2) == 4
    except AssertionError:
        print("-2 Square wasn't 4")
    try:
        assert square(-3) == 9
    except AssertionError:
        print("-3 Square wasn't 9")
    try:
        assert square(0) == 0
    except AssertionError:
        print("0 Square wasn't 0")
if __name__ == "__main__":
    main()
# ---------------------------
# Pytest tests units {pytest file.py or python -m pytest file.py}
from calculator import square

def test_square():
    assert square(2) == 4
    assert square(-2) == 4
    assert square(3) == 9
    assert square(-3) == 9
    assert square(0) == 0

# -------------------------better design tests each unit(function)'s tests individual 
from calculator import square

def test_positive():
    assert square(2) == 4
    assert square(-2) == 4
    
def test_negative():
    assert square(3) == 9
    assert square(-3) == 9

def test_zero():
     assert square(0) == 0

# hello.py
  # ------------------------can't be test as the print has side effect rather than return a value
def main():
    name = input("What's your name? ")
    hello(name)
def hello(to = "world"):
    print(f"hello, {to}")

if __name__ == "__main__":
    main()
# -------------------- testable
def main():
  name = input("What's your name? ")
  print(hello(name))
def hello(to = "world"):
  return f"hello,{to}"

if "__name__" == "__main__"
#test_hello.py
from hello import hello

def test_default():
    assert hello() == "hello, world"
def test_arguments():
    assert hello("David") == "hello, David"
    assert hello("Ron") == "hello, Ron"
  
# test/test_hello.py {testing a package} python -m pytest package_name
  # create __init__.py in test package before testing so it treats the folder as package
from hello import hello
def test_default():
    assert hello() == "hello, world"

def test_args():
    assert hello("David") == "hello, David"
