import random

givenNumber = random.randint(1, 99)
secretNumber = random.randint(1, 99)

validInput = ["higher", "lower", "equal"]

print("I just chose a secret number between 1 and 100.")

while True:
    userInput = input(f"Is the secret number higher, lower, or equal to {givenNumber}? - ")
    if userInput in validInput:
        break
    else:
        print("Ungültige Eingabe. Bitte 'higher', 'lower' oder 'equal' eingeben.")

if userInput == "higher":
    if secretNumber > givenNumber:
        print(f"Correct! {secretNumber} is higher than {givenNumber}.")
    else:
        print(f"Wrong! {secretNumber} is not higher than {givenNumber}.")

elif userInput == "lower":
    if secretNumber < givenNumber:
        print(f"Correct! {secretNumber} is lower than {givenNumber}.")
    else:
        print(f"Wrong! {secretNumber} is not lower than {givenNumber}.")

elif userInput == "equal":
    if secretNumber == givenNumber:
        print(f"Correct! {secretNumber} is equal to {givenNumber}.")
    else:
        print(f"Wrong! {secretNumber} is not equal to {givenNumber}.")
