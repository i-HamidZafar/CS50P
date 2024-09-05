# 1- Seasons of Love
  # seasons.py
  from datetime import date
  import sys, re, inflect
  
  def main():
      date_of_birth = input("Date of Birth: ")
      if validate_date_format(date_of_birth):
          minutes = count_minutes(date_of_birth)
          print(f"{minutes} minutes")
      else:
          sys.exit("Invalid date")
  
  def validate_date_format(input):
      return True if re.search(r"^\d{4}-\d{2}-\d{2}$", input) else False
  
  def count_minutes(date_of_birth):
      days = get_days(date_of_birth)
      return print_in_words(round(days * 24 * 60))
  
  def get_days(given_date):
      year, month, day = given_date.split("-")
      return (date.today() - date(int(year), int(month), int(day))).days
  
  def print_in_words(minutes):
      min_in_words = re.sub(r"\b and\b", "", inflect.engine().number_to_words(int(minutes))).capitalize()
      return min_in_words
  if __name__ == "__main__":
      main()

  #test_seasons.py
  from seasons import validate_date_format, count_minutes
  import pytest
  #date : 2024/09/03
  def test_date_formats():
      assert validate_date_format("1970-01-01") == True
      assert validate_date_format("cat") == False
      assert validate_date_format("10-1-2002") == False
      assert validate_date_format("10-10-22") == False
      assert validate_date_format("January 1, 1999") == False
      assert validate_date_format("22-01-01") == False
  
  def test_count_minutes():
      with pytest.raises(ValueError):
          count_minutes("0000-01-01")
  
      assert count_minutes("0001-01-01") == "One billion, sixty-four million, three hundred forty-eight thousand, six hundred forty"
      assert count_minutes("2024-09-02") == "One thousand, four hundred forty"

# 2- Cookie Jar
  #jar.py
  class Jar:
      def __init__(self, capacity=12):
          self.capacity = capacity
          self.size = 0
  
      def __str__(self):
          if self.size > 0:
              return f"🍪"* int(self.size)
          else:
              return ""
  
      def deposit(self, n):
          if self.size + n <= self.capacity:
              self._size = self.size + n
          else:
              raise ValueError
  
      def withdraw(self, n):
          if n > self.size:
              raise ValueError
          self._size = self.size - n
  
      @property
      def capacity(self):
          return self._capacity
      @capacity.setter
      def capacity(self, n =12):
          if n < 0:
              raise ValueError
          self._capacity = n
      @property
      def size(self):
          return self._size
      @size.setter
      def size(self, n = 0):
          if n > self.capacity:
              raise ValueError
          self._size = n
  #test_jar.py
  from jar import Jar
  import pytest
  
  def test_init():
      jar = Jar()
      assert jar.capacity == 12
      assert jar.size == 0
      with pytest.raises(ValueError):
          jar = Jar(-2)
  
  
  def test_str():
      jar = Jar()
      str(jar) == ""
      jar.deposit(1)
      assert str(jar) == "🍪"
      jar.deposit(11)
      assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
  
  
  def test_deposit():
      with pytest.raises(ValueError):
          jar = Jar()
          jar.deposit(14)
      jar = Jar()
      jar.deposit(2)
      assert jar.size == 2
      jar.deposit(10)
      assert jar.size == 12
  
  
  
  def test_withdraw():
      with pytest.raises(ValueError):
          jar = Jar()
          jar.withdraw(1)
      jar = Jar()
      jar.deposit(1)
      jar.withdraw(1)
      assert jar.size == 0

# 3- CS50 Shirtificate
  # shirtificate.py
  from fpdf import FPDF
  
  class PDF(FPDF):
      def header(self):
          self.set_font("Helvetica", "", 44)
          self.cell(192, 32,txt="CS50 Shirtificate",  align='C', ln = True)
          self.ln(20)
          self.image("shirtificate.png", 10, 60, 190)
  def main():
      name = input("Name: ")
      shirt(name)
  def shirt(tag):
      pdf = PDF()
      pdf.add_page(orientation="portrait", format="a4")
      pdf.set_text_color(255,255,255)
      pdf.set_font(size=30)
      pdf.cell(0, 120, f"{tag} took CS50", align= "C")
      pdf.output("shirtificate.pdf")
  
  if __name__ == "__main__":
      main()


