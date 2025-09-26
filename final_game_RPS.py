#----------------------------------------------------
# ----------Sample rock paper scissors game----------

import random

# create a fucntion for comparing player and bot choices and returning values for their scores
# the function contains the bot and player scores and condtionals to compare both choices
# else statement at the end to ensure the player inputs  within the parameters

def analyze_choices(player_choice, ai_choice):
    global ai_score
    global player_score
    if (player_choice == "paper" and ai_choice == "paper") or (player_choice == "scissors" and ai_choice == "scissors") or (player_choice == "rock" and ai_choice == "rock"):
        print("a tie")
    elif (player_choice == "rock" and ai_choice == "paper") or (player_choice == "paper" and ai_choice == "scissors") or (player_choice == "scissors" and ai_choice == "rock"):
        print("You lost")
        ai_score += 1
    elif (player_choice == "scissors" and ai_choice == "paper") or (player_choice == "rock" and ai_choice == "scissors") or (player_choice == "paper" and ai_choice == "rock"):
        print("You win")
        player_score += 1
    else:
        print("wrong input")                

#create necessary variables for the game
player_score = 0
ai_score = 0
game_choices = ["rock", "paper", "scissors"]

# create a function with a while loop to ensure the game is a best of three
# created a variable to check no of times game can be played
# game choices is sorted and the bot picks within the array(list)
def game_start():
    global no_of_plays
    no_of_plays = 0
    while no_of_plays != 3 :
        game_choices.sort()
        ai_choice = random.choice(game_choices)
        print(f'player score is {player_score} and Bot score is {ai_score}')               # to display scores
        player_choice = input("rock paper scissors....Shoot!!!!!:  ")                       
        if player_choice not in game_choices:                                              # conditions to check if player inputs are within given parameters (I didn't add an else statement cause the analyze_choices() function has an else statement to handle inputs not within the paramters)
            no_of_plays -= 1                                                               
        analyze_choices(player_choice, ai_choice)                                          # here is is
        no_of_plays += 1
        if no_of_plays == 3:                                                                # This condtionals check for no of plays which is set to be three times
            if player_score > ai_score:
                print("Congratulations, You won")
            elif player_score < ai_score:
                print("Sorry, better luck next time")
            else:
                print("there are no winners or losers")


#code for new game/rematch or game over
#create varaiable to control the while loop-player_rematch
# if user agrees to rematch, we reset the bot and player scores varaibales and set the player_rematch varaiable to end the while loop and call the game_start()  function
# if user does not want a rematch we print game over and end the while loop
# else handles any other inputs that isn't Y or N and keeps the while loop going

def rematch_question():
    global player_rematch
    player_rematch = 0
    while player_rematch <= 1:
        play_again = input("It's over, would you like to play again?? Y for Yes and N for No :     ")
        if play_again in ["Y","y"]:
            print("----new game-----  ")
            global player_score
            global ai_score
            player_score = 0
            ai_score = 0
            player_rematch += 1
            game_start()
        elif play_again in ["N","n"]:
            print("game over")
            player_rematch += 1
            break
        else:
            print("wrong input")
            continue

#call the functions
game_start()
rematch_question()













