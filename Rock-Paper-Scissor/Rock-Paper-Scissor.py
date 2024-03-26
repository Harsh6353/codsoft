import random

choice = ['rock','paper','scissor']
def check(comp, user):
    if comp == user:
        return 0    #0 is for draw
    if (comp == 'rock' and user == 'scissor') or (comp == 'paper' and user == 'rock') or (comp == 'scissor' and user == 'paper'):
        return -1   #-1 for user lose
    return 1        #1 for user win

uscore = 0   # User score
cscore = 0   # Computer score
playing = True

while playing:
    comp = random.choice(choice)
    user = input("Choose rock, Paper or Scissor: ")
    
    # Input validation
    while user not in choice:
        print("Invalid choice or spelling")
        user = input("Choose rock, Paper or Scissor: ")

    score = check(comp, user)

    print(f"YOU: {user}")
    print(f"COMPUTER: {comp}")

    if score == 0:
        print("It's a Draw")
    elif score == -1:
        print("You Lose")
        cscore += 1
    else:
        print("You Win")
        uscore += 1

    print(f"User Score: {uscore}")
    print(f"Comp Score: {cscore}")
    
    
    play_again = input("Do you want to play again(y/n)? ").lower()
    if play_again =="n":
        playing = False

print("Thanks for playing..")