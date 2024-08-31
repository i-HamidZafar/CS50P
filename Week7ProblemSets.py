# 1. NUMB3RS
  #numb3rs.py:
  import re
  import sys
  
  
  def main():
      print(validate(input("IPv4 Address: ")))
  
  
  def validate(ip):
      if matches := re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip):
          octates = []
          octates = matches.groups()
          for i in octates:
              if 0 <= int(i) <= 255:
                  continue
              else:
                  return False
          return True
      return False
  if __name__ == "__main__":
      main()
  #test_numb3rs.py
  from numb3rs import validate
  
  def test_true():
      assert validate("192.159.1.1") == True
      assert validate("0.0.0.0") == True
  def test_false():
      assert validate("Welcome") == False
      assert validate("28.29.22.282") == False

# 2. Watch
#   watch.py
  import re
  import sys
  def main():
      print(parse(input("HTML: ")))
  
  def parse(s):
      if embed_link := re.search(r'^.*src="(https?://(www\.)?youtube\.com/.*)".*$',s):
          if watch_link := re.sub(r"https?://(www\.)?youtube\.com/embed/","https://youtu.be/", embed_link.group(1)):
              return watch_link
      return None
  
  if __name__ == "__main__":
      main()

#3.Working 9 TO 5
# working.py
  import re
  import sys
  
  
  def main():
      print(convert(input("Hours: ")))
  
  
  def convert(s):
      if matches:= re.search(r"^(\d{1,2}):?(\d{1,2})? (AM|PM) to (\d{1,2}):?(\d{1,2})? (AM|PM)$", s):
          return format_time(matches.group(1), matches.group(2), matches.group(3)) + " to " + format_time(matches.group(4), matches.group(5), matches.group(6))
      else:
           raise ValueError
  def format_time(hours, min, period):
      if not (0 <= int(hours) <= 12):
              raise ValueError
      min = min if min else 0
      if int(min) > 59 or int(min) < 0:
          raise ValueError
      if period == "AM":
              return f"{int(hours)% 12:02}:{int(min):02}"
      elif period == "PM":
          if int(hours) < 12:
              return f"{(int(hours) + 12) :02}:{int(min):02}"
          return f"{int(hours):02}:{int(min):02}"
      else:
          raise ValueError
  
  
  if __name__ == "__main__":
      main()

  # test_working.py
  from working import convert
  import pytest
  def test_valid():
      assert convert("9 PM to 4 AM") == "21:00 to 04:00"
      assert convert("2:30 AM to 4 PM") == "02:30 to 16:00"
      assert convert("12 PM to 12 AM") == "12:00 to 00:00"
  def test_invalid():
      with pytest.raises(ValueError):
          convert("cat")
      with pytest.raises(ValueError):
          convert("9PM to 4PM")
      with pytest.raises(ValueError):
          convert("9 to 5")
      with pytest.raises(ValueError):
          convert("14 PM to 13 AM")

# 4. um.py
  import re
  import sys
  
  def main():
      print(count(input("Text: ")))
  
  def count(s):
      return len(re.findall(r"\bum\b", s, re.IGNORECASE))
  
  if __name__ == "__main__":
      main()
  # test_um.py
  from um import count
  
  def test_count():
      assert count("um?") == 1
      assert count("Um, thanks for the album.") == 1
      assert count("Um, thanks, um...") == 2

  # 5. response.py
  import validator_collection
  
  email = input("What's your email address? ")
  if validator_collection.checkers.is_email(email):
      print("Valid")
  else:
      print("Invalid")



