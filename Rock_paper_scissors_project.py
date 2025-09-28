'''
Now i want to create Rock-paper-scissors Game 
Rock = -1 
Paper = 1 
Scissors = 0 

'''
while True:   # লুপের শুরু
    print("🎮 New Game Started!")

    import random 



    name = input("Enter you name : ")
    # lets create this game 
    rounds = int(input("Enter how many time you want to play : "))
    you_win = 0 
    Comp_win = 0 
    draw = 0 
    invalid = 0 
    for i in range (rounds):


        choice = [-1,1,0]
        Comp = random.choice(choice)
        try :
            


            Your_choice = input("Enter your choice e (rock/paper/scissors) : ")
            refined_your_choice = Your_choice.lower()

            youdict = {"rock" : -1 , "paper" : 1 , "scissors" : 0 }
            reverse_dict = { -1 : "Rock", 1 : "Paper" , 0 : "Scissors"}


            you = youdict[refined_your_choice]

            print(f" Computer choice is {reverse_dict[Comp]}.  Your Choice is {reverse_dict[you]} \n So result is ....")

        # this match was drow 
            if(Comp == you ):
                print("This round is draw ")
                draw += 1 

        # Rock(-1) vs paper(1) => Paper(1) win 
            elif(Comp == -1 and you == 1):
                print("Congrats You are the winner ")
                you_win += 1
            elif(Comp == 1 and you == -1 ):
                print("Computer is the Wineer , Try again .")
                Comp_win += 1

        # Rock(-1) vs scissors(0)  => Rock(-1) win

            elif(Comp == -1 and you == 0 ):
                print("Computer is the Wineer , Try again . ")
                Comp_win += 1
            elif( Comp == 0 and you == -1):
                print("Congrats You are the winner ")
                you_win += 1

        # Paper(1) vs Scissors(0) => Scissors(0) win
            elif(Comp == 1 and you == 0):
                print("Congrats You are the winner ")
                you_win += 1
            elif(Comp == 0 and you == 1 ):
                print("Computer is the Wineer , Try again . ")
                Comp_win += 1
            else:
                print("You loose the chance for  giving wrong input . ")
                
        except(KeyError):
            print(" ⚠️ Invalid input! Please type rock, paper, or scissors.")
            invalid += 1


    print(f" Final result upcoming....... ")

    print(f" You win = {you_win}")

    print(f" Draw = {draw}")

    print(f" loss chance = {invalid}")

    print(f"Computer win : {Comp_win}")

    print(f" Final reult is ........")
  

    if(you_win == Comp_win):
        match_draw = (f"{name} Your score is {you_win} and computer score is {Comp_win}. So match result is  draw ")
        print(match_draw)
        with open("result.txt", "a") as f:
            f.write(f"{match_draw}")


    elif(you_win > Comp_win ):
        user_win = (f"{name} Your score is {you_win} and computer score is {Comp_win}. Congrats {name} you are the winner  ")
        print(user_win)
        with open("result.txt", "a") as f:
            f.write(f"{user_win}")


    else:
        computer_win = f"{name} Your score is {you_win} and computer score is {Comp_win}.  So computer is win , Try again "
        print(computer_win)
        with open("result.txt", "a") as f:
            f.write(f" {computer_win} \n")




    reply = input("\nDo you want to play again? (yes/no): ").lower()
    if reply != "yes":
        print("👋 Thanks for playing! Goodbye.")
        break

      