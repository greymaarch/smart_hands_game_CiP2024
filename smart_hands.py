import random
import smart_functs as smart
import smart_questions as questions

# ---Game Facts---
#Goal score is all of the primaries available. Primaries have a max 10pts reward.
goal_score = 0
incident_chance = 2 #increase to reduce chances of an incident.
max_rows = 10
secondary_rand_chance = 5 # A random chance to get a secondary question. 1-10, 1 is low, 10 is always.

# ---Player Data---
player_score = 20
player_incorrect = 0
player_step = 0
player_condition = "Pass"
player_end = False

# --Tracking Structure---
# Statuses are Waiting (1), Complete (2), Issue (3).
current_row = {
    "0": 1,
    "1": 1,
    "2": 1,
    "3": 1,
    "4": 1,
    "5": 1,
}

#---Game Start---
smart.clear_terminal()
smart.print_welcome(max_rows)
smart.clear_terminal()

# Outer Loop.
for row in range(max_rows):
    player_end = False
    smart.used_questions.clear() #So we don't exhaust all questions. Rows start new. 
    rows_left = max_rows - row - 1

    # Update row with random value for issues or not.
    for j in range(len(current_row)):
        issue_status = random.randint(1, incident_chance) 
        if issue_status == 1:
            goal_score = goal_score + 10 #Figure out what the goal score should be.
        current_row.update({str(j): issue_status})
    
    player_step = 0
    print(str(goal_score))
    
    # inner loop 1
    while not player_end and player_step < len(current_row):
        smart.clear_terminal()
        #print(smart.used_questions) #debug

        # Check score.
        if player_score <= 0:
            player_condition = "Fail"
            smart.print_end(player_condition, player_score, goal_score)
            break

        # print map
        smart.tracking_map(player_step, player_score, current_row)
        print("")

        # Random Issue from secondary problems!
        if random.randint(1, 10) > secondary_rand_chance:
            #random secondary question function
            sec_question_score, question_asked = questions.ask_primary_question(questions.secondary_questions,questions.question_text)
            # functon should return a score that gets added or subtracted.
            updated_score = smart.calc_score(player_score, sec_question_score)
            player_score = updated_score
            #Removing repeats
            smart.used_questions.append(question_asked)
            input("\nPress any key to check for open issues.\n\n")

        # Check if cabinet is waiting
        if current_row.get(str(player_step)) == 1:
            #Primary question function.
            primary_question_score, question_asked = questions.ask_primary_question(questions.primary_questions,questions.question_text)
            # functon should return a score that gets added or subtracted.
            updated_score = smart.calc_score(player_score, primary_question_score)
            player_score = updated_score
            #Removing repeats
            smart.used_questions.append(question_asked)
        else:
            print("It looks like there are no open issues at this cabinet.")

        # Player move.
        player_step += 1
        if player_step > (len(current_row) - 1):
            player_end = True
        else:
            input("\nReady to move on?")

    # When player gets to end of row, make new random row and congratulate player.
    if rows_left > 1:
        print("\nYou've completed a row only " + str(rows_left) + " rows remain!\n")
        input("Ready to continue?")
    elif rows_left == 1:
        print("LAST ROW! Almost done.")
        input("Ready to continue?")
    else:
        pass
    smart.clear_terminal()

if player_score > 0:
    smart.print_end(player_condition, player_score, goal_score)
