import random
randomNum = random.randrange(0, 100)

while(True):
  user_choice = int(input(""))
  if randomNum == user_choice:
    print("You has guessed right number")
    exit()
  elif randomNum > user_choice:
    print("little greater")
  elif randomNum < user_choice:
    print("little smaller")
