import random

print ("H A N G M A N")

word_list = ["python", "java", "kotlin", "javascript"]
rand_word = random.choice(word_list)
hidden_word = "-" * (len(rand_word))
hidden_list = list(hidden_word)
words_attempted= []

def game():
    num = 8 # number of tries
    
    while num > 0:
        print("")
        tring = "".join(hidden_list)
        print(tring)
        if tring == rand_word:
            print("You guessed the word!\nYou survived!")
            break
    
        letter = input("Input a letter: ")

        if len(letter) != 1:
            print("You should input a single letter")
        elif letter.islower() == False:
            print("It is not an ASCII lowercase letter")
        elif letter in words_attempted:
            print("You already typed this letter")
        elif letter.lower() in rand_word:
            for j in range(len(rand_word)):           
                if letter == rand_word[j]:
                    hidden_list[j] = letter             
        else:
            print("No such letter in the word")
            num -= 1  
        words_attempted.append(letter)
    if num == 0:
        print("You are hanged!")
        

while True:
    start_end = input('Type "play" to play the game, "exit" to quit: ')
    if start_end == "play":
        game()
    elif start_end == "exit":
        break
    else:
        print(" ")