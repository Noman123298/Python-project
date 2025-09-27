''''
1 for snake 
-1 for water
0 for gun

'''''
round =int(input("How many rounds you want to play : "))
comp_win = 0 
you_win = 0 
draw = 0 
for i in range (round):
    
    import random 
    choice = [1,-1,0]

    #Now  computer give random choice 

    computer = random.choice(choice)

    # Then you give a choice 


    youstr = input("Enter your choice : ")
    perfect_youstr = youstr.lower()
    youdict = {"snake" : 1 , "water" : -1 , "gun" : 0 }

    you = youdict[perfect_youstr]

    # Now we showing whats going on 

    result_computer_you = {1: "Snake", -1 : "Water" , 0 : "Gun"}
    print(f" Your choice is {result_computer_you[you]} Computer choice is {result_computer_you[computer]}. So the result is ")

    # computer == you => draw
    if(computer == you):
        print("Draw . play agian ")
        draw += 1 


    # Snake vs Water → Snake win
    elif (computer == 1 and you == -1):
        print("Computer win")
        comp_win += 1
         
    elif (computer == -1 and you == 1):
        print("You win")
        you_win += 1 

    # Water vs Gun → Water win
    elif (computer == -1 and you == 0):
        print("Computer win")
        comp_win += 1
    elif (computer == 0 and you == -1):
        print("You win")
        you_win += 1 

    # Gun vs Snake → Gun win
    elif (computer == 0 and you == 1):
        print("Computer win")
        comp_win += 1
    elif (computer == 1 and you == 0):
        print("You win")
        you_win += 1 

    # samething mistake 
    else:
        print("Something went wrong")


print (f" Match result is \n Draw = {draw}  \n Computer Win = {comp_win}  \n You Win = {you_win}")
