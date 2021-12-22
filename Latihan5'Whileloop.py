# while condition:
      # ...

i = 1
while i <= 5:
    print('*' * i)
    i = i + 1

    # Guessing Game

secret_number = 8
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input('Guess : '))
    guess_count += 1
    if guess == secret_number:
        print("U got it !")
        break
    else:
        print("Try again !")
else:
    print("U fail !")