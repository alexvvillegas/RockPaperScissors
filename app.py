P1 = input("PLAYER ONE: Rock, Paper, or Scissors?")
P2 = input("PLAYER TWO: Rock, Paper, or Scissors?")

if P1 == "Rock":
    if P2 == "Paper":
        print("P2 WINS!")
    elif P2 == "Scissors":
        print("P1 WINS!")
    elif P2 == "Rock":
        print("DRAW!")

if P1 == "Paper":
    if P2 == "Rock":
        print("P1 WINS!")
    elif P2 == "Paper":
        print("DRAW!")
    elif P2 == "Scissor":
        print("P2 WINS!")

if P1 == "Scissors":
    if P2 == "Rock":
        print("P2 WINS!")
    elif P2 == "Paper":
        print("P1 WINS!")
    elif P2 == "Scissors":
        print("DRAW!")
        
    






