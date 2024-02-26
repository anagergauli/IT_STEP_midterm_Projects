#           გამოიცანით რიცხვი

# ამ თამაშში პროგრამა აგენერირებს შემთხვევით რიცხვს მითითებული დიაპაზონიდან.
# მომხმარებლებს სთხოვენ გამოიცნონ რიცხვი. არასწორი რიცხვის შემთხვევაში პროგრამა მომხმარებელს აძლევს მინიშნებას (უფრო მაღალი/უფრო დაბალი).
# თამაში აკონტროლებს მცდელობების რაოდენობას და აჩვენებს შედეგს, როდესაც მომხმარებელი გამოიცნობს სწორ რიცხვს

import random

num = random.randint(1, 100)
attempts = 0

print ("Hiii ! You are playing the game  - Guess the number! Good Luck :)))")

while True:
    try:
        guess = int(input("Guess the number (from 1 to 100): "))
        attempts += 1 
    except ValueError:
        print("Enter only positive whole numbers from 0 to 100 !!!")
        continue

    if guess == num:
        print(f"Congrats!!! You guessed the number correctly: {num}")
        print(f"It took you {attempts} attempts to guess the number")
        break  
    elif guess < num:
        print("The number assumed is greater than the number you entered. Try again!")
    else:
        print("oops that's a lot.. the number assumed is less than the number you entered. Try again!")