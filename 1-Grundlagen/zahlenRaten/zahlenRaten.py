import random

random_num = random.randint(1, 100)

try_counter = 0

print("I chose a number between 1 and 100. Try to guess the number!")

while True:
    user_input = int(input("Enter your number: "))

    if user_input in range(1,101):
        try_counter += 1

        if user_input < random_num:
            print("Too low!")
        elif user_input > random_num:
            print("Too high!")
        else:
            print(f"Yessir! You guessed the number in {try_counter} attempts.")
            break
    else:
        print("Input invalid, try again.")
