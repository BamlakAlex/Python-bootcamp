# challenge 1: Factorial Calculator

# Write a Python function called factorial that calculates the factorial of a given number using a while loop. The factorial of a non-negative integer n, denoted by n!, is the product of all positive integers less than or equal to n. The factorial of 0 is defined to be 1.

# The function should have the following specifications:

# Name: factorial
# Parameters:
# n (integer): The number for which the factorial needs to be calculated.
# Return:
# result (integer): The factorial of the given number.
# You should use a while loop inside the function to calculate the factorial.


def factorial(n : int):
 while n < 0 :
  return "Factorial is not defined for non negative numbers"
 while n == 0 or n == 1 :
  return 1
 while n > 1:
  return n * factorial(n-1)

Your_number= input("What is integer do you want the factorial of? ")

print(factorial (int(Your_number)))





# Task 2: Create a simple game function, that takes no parameter and initiates the guessing game
# 1. The game should generate a random number between 1 and 100.
# 2. The player should be prompted to guess the number.
# 3. The game should provide feedback to the player after each guess, indicating whether the guess was too high or too low.
# 4. The player has 5 chances to get it right and whenever they guess wrong they lose a chance.
# 5. If the player guesses the correct number within the given attempts, they should be declared the winner.
# 6. If the player runs out of attempts without guessing the correct number, they should be declared the loser.
# Hint : Learn about python break keyword





game_logo = """
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█░▄▄▄█░██░█░▄▄█░▄▄█░▄▄███▄░▄█░████░▄▄███░▄▄▀█░██░█░▄▀▄░█░▄▄▀█░▄▄█░▄▄▀.
█░█▄▀█░██░█░▄▄█▄▄▀█▄▄▀████░██░▄▄░█░▄▄███░██░█░██░█░█▄█░█░▄▄▀█░▄▄█░▀▀▄
█▄▄▄▄██▄▄▄█▄▄▄█▄▄▄█▄▄▄████▄██▄██▄█▄▄▄███▄██▄██▄▄▄█▄███▄█▄▄▄▄█▄▄▄█▄█▄▄
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
            """

total_chances = ['💖','💖','💖','💖','💖']
win_emoji = '🏆🎉'
lose_emoji = '💔😭'

from random import randint

def Game():
    chance= 5
    Correct_Number= randint(1,100)
    
    while chance > 0:
      Guess= int(input("Guess a number between 1 and 100! "))
      chance -= 1 
      
      if Guess > Correct_Number :   
        print ("Too high")
      elif chance == 0:
        print ("You lost")
        print (f"The correct number was {Correct_Number}")
        break      
      if Guess < Correct_Number:
        print ("Too Low")
      elif chance == 0:
        print ("You lost")
        print (f"The correct number was {Correct_Number}")
        break
      elif chance > 0 and Guess == Correct_Number:
        print("You are a winner")
        break   
 
        
Game()



        
       
def nested_sum(data):
    total = 0 
    
   
    for key, value in data.items():
        
       
        if isinstance(value, int):
            total += value
        
        elif isinstance(value, dict):
            total += nested_sum(value)
        
       
        elif isinstance(value, list):
            for item in value:
               
                if isinstance(item, int):
                    total += item
                elif isinstance(item, dict):
                    total += nested_sum(item)
                elif isinstance(item, list):
                    total += nested_sum({"temp": item})
    
    return total




