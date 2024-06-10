import os

#This is for tracking what's already been asked per row.
used_questions = []

def print_welcome(max_rows):
    print_line()
    print("             W E L C O M E        T O     S M A R T       H A N D S")
    print_line()
    print("\nWelcome to the smart hands team!\nA smart hands employee assists customers with their servers in datacenters.")
    print("\nThis datacenter has " + str(max_rows) + " rows.\n\n*Each row has servers inside cabinets. \n*The servers will have their indicator light on if they have an issue to attend.")
    print("\nIndicators look like this: [o]")
    print("\nWatch out for messes, missing raised floor tiles, cable disasters, and untidy cabinets! \nAnd as always provide good customer service and have a healthy respect for the servers.")
    print_line()
    input("Lets get started. Press any key.")
 

#Inputs the player step# which indexes the dict in current_row. Prints a map.
# [*]
# [*]
# [*] %
# [o]
# [o]
# [o]
# o = Waiting for player. * = Completed. % = player.
# Your current score is 55
def tracking_map(player_step, player_score, current_row):
    print("\nYour Current Row:")
    print("___________________\n")
    #list of cabinets
    cabinets = list(current_row.keys()) 
    for i, cabinet in enumerate(cabinets):
        cabinet_status = " "  
        if current_row[cabinet] == 1:
            cabinet_status = "o"
        else:
            cabinet_status = "*"
        
        if i == player_step:
            print(f"        [{cabinet_status}] %")
        else:
            print(f"        [{cabinet_status}]")
        
    print("___________________")
    print("o = Open Issue. * = No Issues. % = player.")
    print(f"Your current score is {player_score}")
        
#End conditions and outputs based on score compared to the maximum score.
def print_end(player_condition, player_score, goal_score):
    percentage_score = (player_score / goal_score) * 100
    if player_condition == "Fail":
        print("\nI'm sorry, you've been let go. We will escort you out of the datacenter.")
        print("Goal Score: " + str(goal_score))
        print("Your Score: " + str(player_score))
        print(":(\n")
        print("__________________________________________________________________________")
    else:
        #make some score conditions for low, mid, excellent.
        if percentage_score < 60:
            print("\nYou did ok. You have a lot to learn. See you tomorrow.\n")
        elif percentage_score < 75:
            print("\nYou did pretty good! Some room for improvement, but otherwise you're a great addition to the smart hands team.")
        elif percentage_score < 90:
            print("\nYou did great! You're an excellent addition to the smarthands team!!!")
        else:
            print_line()
            print("C O N G R A T U L A T I O N S !!! \nYou're going an amazing job here. Your work is complete.")
            print_line()
        print("Your score was: " + str(player_score))
        if player_score < goal_score:
            print("You were " + str(goal_score - player_score) + " points away from the goal score of " + str(goal_score) +".")
        else:
            print_line()
            print("You have earned at or above the ***G O A L  S C O R E***\n THANK YOU FOR PLAYING.")
            print("Goal Score: " + str(goal_score))
            print_line()
    exit()

def calc_score(player_score,amount):
    total = player_score + amount
    return(total)

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def print_line():
    print("---------------------------------------------------------------------------------------")