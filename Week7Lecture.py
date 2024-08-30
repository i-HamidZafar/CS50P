# Regular Expression

#valid.py
  #simple initially
  
  email = input("What's your email? ").strip()
  
  if "@" in email:
      print("Valid") 
  else:
      print("Invalid")
      
  #impoving a little more but nothing much at all.
  email = input("What's your email: ")
  
  if "@" in email and "." in email:
      print("Valid")
  else:
      print("Invalid")

  #introducing a bit more logic
  email = input("What's your email: ")
  
  username, domain = email.split("@")
  
  if username and ("." in domain):
      print("Valid")
  else:
      print("Invalid")

  #narrowing it down but still not robust 
  email = input("What's your email: ")
  
  username, domain = email.split("@")
  
  if username and domain.endswith(".edu"):
      print("Valid")
  else:
      print("Invalid")

#python re library

  #re.search(patten, string, flags=0)
  #starting to use the library
  #improving the design incrementally
  import re
  email = input("What's your email? ")
  
  if re.search("@", email):
      print("Valid")
  else:
      print("Invalid")
  
  #a step forward but clearly not the correct step 
  import re
  email = input("What's your email? ")
  
  if re.search(".*@.*", email):
      print("Valid")
  else:
      print("Invalid")

  #a correct step forward
  import re
  email = input("What's your email? ")
  
  if re.search(".+@.+", email):
      print("Valid")
  else:
      print("Invalid")

  #if there is no "+" sign then !
  import re
  email = input("What's your email? ")
  
  if re.search("..*@..*", email):
      print("Valid")
  else:
      print("Invalid")

  #checking for not only username but domain name as well but is a bug
  import re
  email = input("What's your email? ")
  
  if re.search(".+@.+.edu", email): #"." in .edu needs to be intrepretted literally. 
      print("Valid")
  else:
      print("Invalid")
  
  #fixing the bug but still there is more to it.
  import re
  email = input("What's your email? ")
  
  if re.search(r".+@.+\.edu", email): # for writing "." literally have to write regex as raw string so python doesn't interpret it as usual.
      print("Valid")
  else:
      print("Invalid")

  #being just a litttlleeee more precise [$ -> end of the string , ^ -> start of the string ]
  import re
  email = input("What's your email? ")
  
  if re.search(r"^.+@.+\.edu$", email): # for writing "." literally have to write regex as raw string 
      print("Valid")
  else:
      print("Invalid")

  #being litttlleeee more specific
  import re
  email = input("What's your email? ")
  
  if re.search(r"^[^@]+@[^@]+\.edu$", email): # for writing "." literally have to write regex as raw string 
      print("Valid")
  else:
      print("Invalid")

  #improving further , being more restrictive (cryptic)
  import re
  email = input("What's your email? ")
  
  if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email): # for writing "." literally have to write regex as raw string 
      print("Valid")
  else:
      print("Invalid")

  #using the builtin shortcuts for common patterns

  #w -> word Character(alphabets number and underscore)
  #W -> not word charcter
  #s -> space characters
  #S -> not whitespace characters
  #d -> decimal digit
  #D -> not decimal digit
  import re
  email = input("What's your email? ")
  
  if re.search(r"^\w+@\w+\.(edu|org|com|dev)$", email): #grouping with ()
      print("Valid")
  else:
      print("Invalid")

  #using the flags 
  #constants that have meaning to re.search: 
  # re.IGNORECASE , re.MULTILINE , re.DOTALL
  
  import re
  email = input("What's your email? ")
  
  if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, flags=re.IGNORECASE): #ignores the case of the email, handles a subdomain too.
      print("Valid")
  else:
      print("Invalid")

  #my solution to handling the subdomains
  
  import re
  email = input("What's your email? ")
  
  if re.search(r"^\w+@(\w+\.)+edu$", email, flags=re.IGNORECASE): #ignores the case of the email
      print("Valid")
  else:
      print("Invalid")


#format.py
  #not suitable for last name, first name
  name = input("What's your name? ").strip()
  
  print(f"hello, {name}")

  #improving but fragile
  name = input("What's your name? ").strip()

  if "," in name:
      last, first = name.split(", ")
      name = f"{first} {last}"
  print(f"hello, {name}")

  #using re
  import re
  name = input("What's your name? ").strip()
  matches = re.search(r"^(.+), (.+)$", name)
  if matches:
      last, first = matches.groups()
      name = f"{first} {last}"
  print(f"hello, {name}")

  #more tigthened up (using the groupes captured from the match)
  import re
  name = input("What's your name? ").strip()
  matches = re.search(r"^(.+), (.+)$", name)
  if matches:
      name = matches.group(2) + " " + matches.group(1)
  print(f"hello, {name}")

  #more better way to go about space
  import re
  name = input("What's your name? ").strip()
  matches = re.search(r"^(.+), *(.+)$", name)
  if matches:
      name = matches.group(2) + " " + matches.group(1)
  print(f"hello, {name}")

  #using the walrus Operator (allows you to assign a value and ask a boolean question at the same time)
  import re
  name = input("What's your name? ")
  if maches := re.search(r"(.+), *(.+)", name):
      name = matches.group(2) + " " + matches.group(1)
  print(f"hello, {name}")
