from random import randint

# available weapons => store this in an array
choices = ["Rock", "Paper", "Scissors"]
player = False
gameOver = False
start = False


# game lives
if start == False:
   computerLives = 3
   playerLives = 3

# Show Player how to start the game
print("type anything to get get started!")
start = input()

# Check to see if player has started the game
while start != False:


# ********************* The Computer Choice was left visible for testing purposes. This allows the user to see the outcome of the game if they win or lose.


    # checks to see if the player input is empty
    while player is False:
        # make the computer pick one item at random
        computer = choices[randint(0, 2)]

        # check to see if any player hasn't lost yet
        if gameOver == False:

            # show the computer's choice in the terminal window
            print("\nComputer chooses: ", computer)

            print("Player has", playerLives, "lives.")
            print("Computer has", computerLives, "lives.")
            print("Choose your weapon!")
            player = input("Rock, Paper, or Scissor?\n")
            print("Player chooses:", player)

        # initiate Game Over sequence
        if gameOver == True:
            player = input()

        # check to see if you picked the same thing
        if (player == computer):
            print("Tie! Live to shoot another day\n")

        # Various Player and computer choices and their outcomes
        elif player == "Rock":
            if computer == "Paper":
                # computer won
                playerLives = playerLives - 1
                print("You lose", computer, "covers", player)
                if playerLives == 0:
                    gameOver = True
                    print("You Lose! Try again if you can handle it!\n Type 'Quit' to end game or 'Reset' to play agin.")
            if  computer == "Scissors":
                computerLives = computerLives - 1
                print("You win!", player, "smashes", computer)
                if computerLives == 0:
                    gameOver = True
                    print("You Win! Your are the BOMB.COM! \n Type 'Quit' to end game or 'Reset' to play agin.")

        elif player == "Paper":
            if computer == "Scissors":
                playerLives = playerLives - 1
                print("You lose", computer, "covers", player)
                if playerLives == 0:
                    print("You Lose! Try again if you can handle it!\n Type 'Quit' to end game or 'Reset' to play agin.")
                    gameOver = True
            if  computer == "Rock":
                computerLives = computerLives - 1
                print("You win!", computer, "covers", player)
                if computerLives == 0:
                    gameOver = True
                    print("You Win! Your are the BOMB.COM! \n Type 'Quit' to end game or 'Reset' to play agin.")

        elif player == "Scissors":
            if computer == "Rock":
                playerLives = playerLives - 1
                print("You lose", computer, "covers", player)
                if playerLives == 0:
                    gameOver = True
                    print("You Lose! Try again if you can handle it!\n Type 'Quit' to end game or 'Reset' to play agin.")
            if  computer == "Paper":
                computerLives = computerLives - 1
                print("You win!", player, "cuts", computer)
                if computerLives == 0:
                    gameOver = True
                    print("You Win! Your are the BOMB.COM! \n Type 'Quit' to end game or 'Reset' to play agin.")

        # See if the player wants to quit
        elif player == "Quit":
            exit()

        # See if the player has reset the game
        elif player == "Reset":
            computerLives = 3
            playerLives = 3
            gameOver = False

        # User input was invalid
        else:
            print("Not a valid option. Check again, and check your spelling!\n")

    # Reset the player to False and randomize the computer choice agaiin.
    player = False
    computer = choices[randint(0, 2)]
