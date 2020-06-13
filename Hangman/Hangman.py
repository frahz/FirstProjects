import random

print ("H A N G M A N\nThe game will be available soon.")

word_list = ["python", "java", "kotlin", "javascript"]
rand_word = random.choice(word_list)
n_dashes = "-" * (len(rand_word) - 3)
hidden_word = rand_word[0:3] + n_dashes

print(f"Guess the word {hidden_word}: ")
word = input()
print("You survived!" if word == rand_word else "You are hanged!")