# თამაში: Hangman

# Hangman არის სიტყვების გამოცნობის თამაში.
# პროგრამა ირჩევს შემთხვევით სიტყვას წინასწარ განსაზღვრული სიიდან და აჩვენებს მას ქვედა ტირეების გამოყენებით (რამდენი ასოცაა სიტყვაში, იმდენი ქვედა ტირე), რომელიც წარმოადგენს ფარულ ასოებს. 
# მომხმარებლებს სთხოვენ გამოიცნონ ასო და პროგრამა ამოწმებს არის თუ არა ასო სიტყვაში. 
# ვლინდება სწორად გამოცნობილი ასოები და თამაში გრძელდება მანამ, სანამ მომხმარებელი არ გამოიცნობს სიტყვას ან არ ამოიწურება მცდელობები.

import random
import string

# სიტყვების წინასწარ განსაზღვრული სია
def words():
    word_list = ["Berlin", "Hamburg", "Munich", "Frankfurt", "Bremen", "Dresden", "Bonn"]
    return random.choice(word_list)

# სიტყვებში ასოების გამოტანა ქვედა ტირეების საშუალებით
def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

# ასოების გამოცნობა და მცდელობების დათვლა

def hangman():
    word = words().lower()
# მომხმარებლის მცდელობების რაოდენობა = სიტყვაში არსებული ასოების რაოდენობა + 2
    attempts = len(word) + 2
    guessed_letters = []

    print("Hi there!You are playing in the game called - Hangman! Try to guess the word!")
    print("Here is a Hint: It's a city in Germany and contains {} letters ".format(len(word)))
    print(display_word(word, guessed_letters))
   
    while attempts > 0:
        guess = input("Enter a letter or the whole word: ").lower()

# მომხმარებლის მიერ ჩაწერილი სიტყვის/ასოების ვალიდაცია       
        if guess not in string.ascii_lowercase and guess != word:
            print("The word isn't correct or you are entering numbers or other symbols! Try again)")
            continue
        if guess == word:
            print("Congratulations! You guessed the word: {}".format(word))
            return      
        if len(guess) == 1:
            if guess in guessed_letters:
                print("You already guessed that letter.")
            elif guess in word:
                guessed_letters.append(guess)
                print("Correct!")
            else:
                attempts -= 1
                print("Incorrect. You have {} attempts left.".format(attempts))
        else:
            if guess == word:
                print("Congratulations! You guessed the word: {}".format(word))
                return
            else:
                attempts -= 1
                print("Incorrect guess. You have {} attempts left.".format(attempts))

        display = display_word(word, guessed_letters)
        print(display)

    print("Sorry, you ran out of attempts. The word was: {}".format(word))
hangman()