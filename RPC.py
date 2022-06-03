import random
hands = ["R", "P", "S"]


r = "Rock"
p = "Paper"
s = "Scissor"


def game():
    computerPick = random.choice(hands)
    pickStatus = False

    while pickStatus == False:
        playerPick = input(
            "Pick hand: [R = Rock], [P = Paper], [S = Scissor] \n").upper()

        if checkComputer(computerPick) == checkPlayer(playerPick):
            pickStatus = True
            print("You played (%s) : CPU played (%s)" %
                (checkComputer(computerPick), checkPlayer(playerPick)))
            print("Draw!")
            game()

        elif checkComputer(computerPick) == r and checkPlayer(playerPick) == s:
            pickStatus = True
            print("You played (%s) : CPU played (%s)" %
                (checkComputer(computerPick), checkPlayer(playerPick)))
            print("CPU win!")

        elif checkPlayer(playerPick) == r and checkComputer(computerPick) == s:
            pickStatus = True
            print("You played (%s) : CPU played (%s)" %
                (checkComputer(computerPick), checkPlayer(playerPick)))
            print("You win!")

        elif checkComputer(computerPick) == p and checkPlayer(playerPick) == r:
            pickStatus = True
            print("You played (%s) : CPU played (%s)" %
                (checkComputer(computerPick), checkPlayer(playerPick)))
            print("CPU win!")

        elif checkPlayer(playerPick) == p and checkComputer(computerPick) == r:
            pickStatus = True
            print("You played (%s) : CPU played (%s)" %
                (checkComputer(computerPick), checkPlayer(playerPick)))
            print("You win!")

        elif checkComputer(computerPick) == s and checkPlayer(playerPick) == p:
            pickStatus = True
            print("You played (%s) : CPU played (%s)" %
                (checkComputer(computerPick), checkPlayer(playerPick)))
            print("CPU win!")

        elif checkPlayer(playerPick) == s and checkComputer(computerPick) == p:
            pickStatus = True
            print("You played (%s) : CPU played (%s)" %
                (checkComputer(computerPick), checkPlayer(playerPick)))
            print("You win!")

        else:
            print("Please pick a valid option and try again")


def checkPlayer(player):
    if player == "R":
        return r
    if player == "P":
        return p
    if player == "S":
        return s


def checkComputer(computer):
    if computer == 'R':
        return r
    if computer == "P":
        return p
    if computer == "S":
        return s


game()
