import random
again = ["yes","no"]
choices = ["snake","water","gun"]
def game():
    while True:
        print("Welocme to Snake Water Gun Game")
        print("Rules \ni) Snake vs Water --> Snake Wins \nii) Snake vs Gun --> Gun wins \niii) Water vs Gun --> Water Wins")
        print("Let's Play")
        userScore = 0
        compScore = 0
        rounds = int(input("Enter number of Rounds You Want to Play : "))
        for i in range(rounds):
            while True:
                userChoice = input("Enter Your Choice \n(snake, water, gun)\n").lower()
                if userChoice in choices:
                    break
                print("Invalid choice. Try again.")
            
            compChoice = random.choice(choices)
            print(f"Your Choice is {userChoice}\nComputer Choice is {compChoice}")

            if userChoice == compChoice:
                print("It's A Tie")    
            elif (userChoice == "snake" and compChoice == "water") or (userChoice == "water" and compChoice == "gun") or (userChoice == "gun" and compChoice == "snake"):
                print("You Win this Time")
                userScore+=1
            else:
                print("You Lose this Time")
                compScore+=1
            print(f"Your Score : {userScore} || Computer Score : {compScore}")
            print("-" * 40)
        print("Final Scores")
        print(f"Your Score : {userScore} || Computer Score : {compScore}")

        if userScore > compScore:
            print("Congratulations! You won the game!")
        elif userScore < compScore:
            print("Computer won the game! Better luck next time.")
        else:
            print("It's a tie overall!")

        while True:
            userAgain = input("Do You Want to Play Again(yes/no) : ").lower()
            if userAgain in again:
                break
            print("Enter again (yes/no).")

        if userAgain == "no":
            print("Okay Bye!")
            break

while True:
    playGame = input("Do You Want to Play Game (yes/no) : ").lower()
    if playGame in again:
        break
    print("Enter yes or no")

if playGame == "yes":
    game()
else:
    print("As You Want")
