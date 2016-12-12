import random
print("----------------------Welcome To Rock Paper Scissors Lizard Spock------------------")
print("0)Rock")
print("1)Spock")
print("2)Paper")
print("3)Lizard")
print("4)Scissors")
player_wins=0
comp_wins=0
ties=0
game_playing=''
while game_playing!='y':
    user_choice = int(input("Choose the number corresponding to your choice :"))
    comp_choice = random.randint(0,4)

    def num_name(guess):
        if guess==0:
            return "Rock"
        elif guess==1:
            return "Spock"
        elif guess==2:
            return "Paper"
        elif guess==3:
            return "Lizard"
        elif guess==4:
            return "Scissors"
        else:
            return "Please Enter a number from the displayed options"

    user_guess=num_name(user_choice)
    comp_guess=num_name(comp_choice)

    print("Player Choose : "+user_guess)
    print("Computer Choose : "+comp_guess)

    diff = abs(user_choice-comp_choice)

    if (diff==2 or diff==1):
        print("Player Wins")
        player_wins+=1
    elif(diff==3 or diff==4):
        print("Computer Wins")
        comp_wins+=1
    else:
        print("Game Ties")
        ties+=1
    print("\n")
    print("ScoreBoard:")
    print("Player : ",player_wins)
    print("Computer : ",comp_wins)
    print("Ties : ",ties)
    print("\n")
    game_playing=input("Do you want to play again [y/n]?").lower().startswith('y')
