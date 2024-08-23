# test_twttr.py

from twttr import shorten

def test_shorten():
    assert shorten("word") == "wrd"
    assert shorten("hello123! !!") == "hll123! !!"
    assert shorten("David MelAn") == "Dvd Mln"

# test_bank
  #bank.py:
  def main():
      greeting = input ("Greeting: ")
      value_prize = value(greeting)
      print(f"${value_prize}")
  
  def value(greeting):
      greeting = greeting.lower()
      if greeting.startswith("hello"):
          return 0
      elif greeting.startswith("h"):
          return 20
      else:
          return 100
  
  
  if __name__ == "__main__":
      main()
  # test_bank.py
  from bank import value
  
  def test_hello():
       assert value ("HELLO") == 0
       assert value("Hello") or value("hello") or value("hello, Newman")  == 0
  def test_twenty():
      assert value("hi") or value("HI") or value("Hola") or value("Hy") == 20
  def test_hundred():
      assert value("Good Day") == 100

# test_plates.py
  from plates import is_valid
  
  def test_true():
      assert is_valid("CS50") == True
      assert is_valid("ECTO88") == True
      assert is_valid("NRVOUS") == True
  
  def test_false():
      assert is_valid("CS05") == False
      assert is_valid("50") == False
      assert is_valid("CS50P2") == False
      assert is_valid("HOLLAAA50") == False
      assert is_valid("2") == False
      assert is_valid("PI3.14") == False

# test_fuel
  #fuel.py
  def main():
      fraction = input("Fuel: ")
      percent = convert(fraction)
      fuel = gauge(percent)
      print(fuel)
  
  def convert(fraction):
      x , y = str(fraction).split('/')
      x , y = int(x) , int(y)
      if y == 0:
          raise ZeroDivisionError()
      if x <= y:
          return round(x / y  * 100)
      else:
          raise ValueError()
  
  def gauge(prcnt):
      prcnt = int(prcnt)
      if prcnt >= 99 or prcnt <= 1:
          return "F" if prcnt >= 99 else "E"
      else:
          return f"{prcnt}%"
  
  if __name__ == "__main__":
      main()

  #test_fuel.py
  import pytest
  
  from fuel import convert, gauge
  def test_value_errors_convert():
      #convert value errors
      with pytest.raises(ValueError):
          convert("4.4/8.3")
      with pytest.raises(ValueError):
          convert("4.4/8")
      with pytest.raises(ValueError):
          convert("4/8.3")
      with pytest.raises(ValueError):
          convert("9/5")
      with pytest.raises(ValueError):
          convert("cat")
      with pytest.raises(ValueError):
          convert("five/six")
  
  
  def test_zero_division():
      with pytest.raises(ZeroDivisionError):
          convert("2/0")
  
  def test_conversion():
      assert convert("2/3")  == 67
      assert convert("0/2")  == 0
      assert convert("10/10")== 100
      assert convert("-2/3") == -67
  
  def test_empty():
      assert gauge(1) == "E"
      assert gauge(0) == "E"
      assert gauge(-5) == "E"
  
  def test_full():
      assert gauge(99)  == "F"
      assert gauge(100) == "F"
      assert gauge(105) == "F"
  
  def test_integers():
      assert gauge(10) == "10%"
      assert gauge(15) == "15%"
  
  
  if __name__ == "__main__":
      main()




