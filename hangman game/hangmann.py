import random

def hangman ():

    list = ["computer ","umbrella","laptop","pakistan","python","machine","book"]
    word = random.choice(list)
    chances = 9
    guesses = ""
    valid_entry = set("abcdefghijklmnopqrstuvwxyz")

    while len(word)>0:
      main_word = ""

      for letter in word:
         if letter in guesses:
            main_word = main_word+letter
         else:
            main_word = main_word+"_"

      if main_word == word:
        print(main_word)
        print("*****************")
        print(" \" good job\"")
        print(" \"you are guesss the correct word \"")
        print("\"congratulation\" ")
        print("  \"you won!!!!\"",name) 
        print("\"do you play again!!\"")
        print("*************")
        break
      print("guess the words  ", main_word)
      guess = input()

      if guess in valid_entry:
        guesses = guesses+guess
      else:
        print("enter valid character")
        guess = input()

      if guess  not in word:
        chances = chances-1
      if chances == 9:
           print("9 chances left!!!")
           print("-------------")
      if chances == 8:
           print("8 chances left!!!")
           print("-------------")
           print("    O     ")
      if chances == 7:
           print("7 chances left!!!")
           print("-------------")
           print("     O      ")
           print("     |      ")
      if chances == 6:
           print(" 6 chances left!!!")
           print("-------------")
           print("      O      ")
           print("      |        ")
           print("       \\      ")
      if chances == 5:
           print("5 chances left!!!")
           print("-------------")
           print("    O      ")
           print("    |        ")
           print("   / \\        ")
      if chances == 4:
           print("4 chances left!!!")
           print("-------------")
           print("  O /     ")
           print("  |        ")
           print(" / \\      ")
      if chances == 3:
          print("3 chances left!!!")
          print("-------------")
          print(" \\ O /     ")
          print("    |        ")
          print("   / \\    ")
      if chances == 2:
          print("2 chances left!!!")
          print("-------------")
          print(" \\ O /   |  ")
          print("    |        ")
          print("   / \\       ")
      if chances == 1:
          print("\"only 1 chance left!!! hangman on his last brearth\"",name)
          print("\'let be thinking carefully!!!\"")
          print("-------------")
      if chances == 0:
          print("          |      ")
          print(" ' \\ O /_|  ")
          print("      |        ")
          print("     / \\       ")
      
          print(" \"you loose\"")
          print("\"you let a good man die\"")
          print("-------------")
          print("     O _|  ")
          print("    /|\\        ")
          print("    / \\        ")   
          print("\"better luck next time\"",name) 
          print("\"the correct word is\"",word)
          break
name = input ("ENTER YOUR NAME ->")
print("WELCOME",name,"!")
print("try to guess the word in less than 10 attempts")
print("\"lets start the hangman game\"")
print("***********************")
hangman()