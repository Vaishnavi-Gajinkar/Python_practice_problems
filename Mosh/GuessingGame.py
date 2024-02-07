# guess = int(input("Guess: "))
sn = 9
i = 1

while i <= 3:
    guessv = int(input("Guess: "))
    if guessv == sn:
        print("You guessed it right!")
        flag = 1
        break
    else:
        flag = 0
        i += 1
if flag == 0:
    print("Sorry max attempt of guesses reached!")

#-----------------------------------------------------------------------------------

secret_num = 5
guess_count = 0
guess_limit = 3

while(guess_count < guess_limit):
    guessm = int(input('Guess: '))
    guess_count += 1
    if guessm == secret_num:
        print('You won!')
        break
else:
    print(f'Sorry you failed!')