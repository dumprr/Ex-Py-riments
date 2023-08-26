import random
import time

characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()" # List of random characters to form password with.
length = 16 # Change the number "16" to desired length.

print("\n\n\n\nWelcome to KEWLPASSGEN by Dumprr\n--\nPassword Generator made in Python. It's fully open source.\nIf you want a different result, you can change the \"length\" and \"characters\" variable.")
print("Starting in 1 second...")
time.sleep(1)

pw = ''
print("------------")
print("Generating...")
print("------------")

for x in range(length): # Repeats this code (length) times.
    pw += random.choice(characters) # Adds one random character from the "Characters" list (known as characters) to the "Password" string (known as pw)



print("\nDone!\nYour Password:\n")
print(pw)
print("\n")