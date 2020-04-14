# Make some things in order to alow this program; using WHILE; the program
# should let the player know if he is guess higher or lower and print an 
# message informing then.
# An correct anwser will finish the program and to exit the player should 
# press 0.

import random


highest = 10
answer = random.randint(1, highest)
print("Please guess some number between one and {}: ".format(highest))
guess = int(input())
x = 8

while x != 0:
   if guess == answer:
         print("YOU WIN")
         x += 1 
         break 
   else:
      if guess == 0:
         print("GAME OVER")
         break
   if guess > answer:
      print("Lower buddy")
   if guess < answer:
      print("Higher buddy") 
   guess = int(input())

print(answer)

''' 
 answer:
   if guess > answer:
    print("guess lower")
   if guess == answer:
    print("Congratulations")
    break
    '''



