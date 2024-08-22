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

  
