# 1- indoor.py:
  def main():
    prompt()

  def prompt():
    user_prompt = input("").strip().lower()
    print(user_prompt)
  
  main()

# 2- playback.py
  def main():
    slow_speed()

  def slow_speed():
      user_prompt = input().replace(" ", "...").strip(" .")
      print(user_prompt)
  
  main()
  
# 3- faces.py 
  def main():
    user_input = input()
    user_input = convert(user_input)
    print(user_input)

  def convert(input):
      input = input.replace(":)", "🙂").replace(":(", "🙁")
      return input
  
  main()

# 4- einstein.py
  def main():
    mass = int(input("m: "))
    e = cal_e(mass)
    print(f"E: {e}")

  def cal_e(m):
      return m * 300000000 ** 2
  
  main()

# 5- tip.py
  def main():
    user_input = input()
    user_input = convert(user_input)
    print(user_input)

  def convert(input):
      input = input.replace(":)", "🙂").replace(":(", "🙁")
      return input
  
  main()
  

  

  


