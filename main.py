username = input("enter your user name:")

if len(username) > 12:
   print("your username can't be more than 12 characters")
elif not username.find(" ") == -1:
  print(" username cannot contain spaces!")
elif not username.isalpha():
  print("cannot contain a numbers")

else:
  print(f"welcome {username}")
  