import random

rangeMin = 0
rangeMax = 100

guess = random.randint(rangeMin, rangeMax)

t = (1,2,3,4,5,6,7)

print(len(t))
# while True:
#     userGuess = input("Enter your guess number : ")
#     PlaceLowRange = "lower , In range %d ~ %d"
#     PlaceHighRange = "higher , In range %d ~ %d"
#
#     if int(userGuess) > 100 or int(userGuess) < 0:
#         print("You have to guessing a range from 0 - 100 \n")
#     else:
#         if int(userGuess) < guess:
#             rangeMin = int(userGuess)
#             print(PlaceLowRange % (rangeMin, rangeMax))
#         elif int(userGuess) > guess:
#             rangeMax = int(userGuess)
#             print(PlaceHighRange % (rangeMin, rangeMax))
#         else:
#             print("You Guess Right")
#             break
