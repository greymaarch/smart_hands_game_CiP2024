import random
import smart_functs as smart

# These are banks of questions, some branching. It's gonna be a mess!
# Questions values: Max primary is 10pts, Max secondary is 5pts
# We want the answers to not just be correct or incorrect all the time, partial correct works but rewards some points.
# Structure:
# primary_questions = {
#    "Question 1": {
#        "What is something?": {
#            "A": 5, <-- Choosing this gives you at least 5pts
#            "B": 7,
#            "C": 3,
#            "D": 0,
#            "sub_A": {
#                "A sub question branch": { <-- a branch off of A
#                    "1a": 0,
#                    "2a": 2,
#                    "3a": 5
#                }
#            }
#        }
#    }
# }

primary_questions = {
        "HARD DISK SWAP": {
            "How do you proceed?": {
                "A. Reach out to the custonmer and ask if you are free to pull the disk with the amber light. ": 5,
                "B. Find the disk with an amber light, pull it out, then pop that new one in. ": 7,
                "C. You're unsure what to do here, so you ask your coworker for help. They show you how to complete the task. ": 2,
                "D. Power down the server to prepare for the swap. ": -10,
                "sub_A": {"Great! What next?": {
                    "1. The customer responded with yes. You put that disk in and continue with your day. ": 0, 
                    "2. The customer responded with yes. You pull out the malfunctioning disk and push the new one in and wait for the customer to conirm success. ": 5,
                    "3. The customer never responded, so you just do it anyway. You have other things to do!": -10
                    }
                    },
            }
        },
        "NETWORK_LINKS": {
            "How do you proceed?": {
                "A. You ask Dave for the details of when the port went down, and take a look at the switch side while you wait. \nHe's taking a while to respond.\n": 4,
                "B. You pull out the other network cable and swap them around. Dave sounds a little panicked but it looks like this now: \n|_______[][x]|\n": 0,
                "C. You swap out the cable with a fresh one. But it still looks like this: \n|_______[x][]|\n": 5,
                "D. You pull out the other cable in case the outage spreads to the other port.  \n|_______[][]|\n": -10,
                "sub_C": {"Great! What next?": {
                    "1. You reboot the server, sometimes things just break!": -10, 
                    "2. You go look at the switch side, it's off too. You bring the port back up in it's terminal.": 5,
                    "3. You tell Dave to contact the vendor.\n The bad stick is 'x'\nBUS-A: .x...... \nBUS-B: ........ ": 0
                    }
                    },
            }
        },
            "POWER_DOWN": {
            "How do you proceed?": {
                "A. You ask Juan to confirm, wait for the confirmation then power down. You follow up for details on when you need to unrack the server.": 10,
                "B. You ask Juan to confirm, wait for the confirmation then power down and start removing the cabling.": 3,
                "C. You call Juan and catch up. You haven't seen him put in a ticket in a while! \nHe's doing great, at the end of the call you press the power button for 8 seconds.": 2,
                "D. You run home, traffic is bad, but hopefully you can beat the recycling truck. It's been a few weeks and you keep forgetting so this is important. You're tired of throwing away things you should recycle because the bin is full.": -10,
            }
        },
            "MEMORY_TESTING": {
            "How do you proceed?": {
                "A. You wait for the go-ahead and power down, and slide the server out on it's rails. You open it up and locate the bad stick. \nIt should be swapped across the bus the bad stick is 'x'.": 5,
                "B. You power down the server, and swap it like this: \nBUS-A: ........ \nBUS-B: .x...... ": 5,
                "C. You ask her if you can call her Alex instead because it has fewer letters to type than Alexandrina. She has not replied, so you move on.": -10,
                "D. You pull the stick and swap it here: \nBUS-A: ........ \nBUS-B: ......x. ": 0,
                "sub_A": {"Great! What next?": {
                    "1. You swap all sticks across the busses. Better make sure.": -5, 
                    "2. You pop the bad stick out, then firmly reseat it. She probably just needed it reseated.": -5,
                    "3. You swap the sticks like this: \nBUS-A: ........ \nBUS-B: .x...... ": 5
                    }
                    },
            }
        },
            "POWER_BLEED": {
            "How do you proceed?": {
                "A. You have never heard of this, confused you ask a coworker what this is and they show you.": 7,
                "B. You power it off, then back on.": 0,
                "C. You power it off, remove the power and network cables, then you hold the power buttong for 30sec. Afterwhich you plug them in and power it on.": 10,
                "D. You ask the customer if they made a typo, this makes very little sense to you.": -10,
            }
        },
            "DIAGNOSTICS": {
            "How do you proceed?": {
                "A. You just reboot the server and let your boss know to tell them all the tests passed.": -5,
                "B. You go grab the crash cart and make your way over to the server.": 5,
                "C. You ask the customer what exactly they think is wrong.": 0,
                "D. You don't really have time for this, so you grab an old diag chart and send it to your boss.": -10,
                "sub_B": {"Great! What next?": {
                    "1. You plug it in and see that everything looks ok. So you tell your boss it all checks out.": 0, 
                    "2. You plug it in and reboot into the diagnostics utility, you run this for about an hour and everything is clear. You take a picture and send it to your boss.": 5,
                    "3. You plug it in and reset the BIOS settings.": -10
                    }
                    },
            }
        },
            "NEW_GPU": {
            "How do you proceed?": {
                "A. After confirmations, you power down the server, open it up and remove the old GPUs. The new ones are too big to fit in! \nSo you call the researchers and tell them.\n\n": 5,
                "B. After confirmations, you power down the server, open it up and remove the old GPUs. The new ones are too big to fit in! \nSo you just put one in.\n\n": -5,
                "C. After confirmations, you power down the server, open it up and remove the old GPUs. The new ones are too big to fit in! \nSo you return the server to it's original state and notify the customers.\n\n": 10,
                "D. After confirmations, you power down the server, open it up and remove the old GPUs. The new ones are too big to fit in! \nYou tell the researchers they need to get better at research.\n\n": -10,
            }
        },
            "RELABLE_SERVER": {
            "How do you proceed?": {
                "A. Larry rarely comes in, if ever. You tell him they've been done.": -10,
                "B. You ask Larry exactly what to relable them too.": 5,
                "C. You grab your records and search for the incorrect labels. You peel off the old ones and create new ones.": 10,
                "D. You get a marker and manually correct the labels. It was just 1 letter off, and you're running low on ink in the label maker.": 0,
            }
        },
            "CABLES_CROWDED_HEAT": {
            "How do you proceed?": {
                "A. You tell her that servers sometimes get hot.": -10,
                "B. You ask her for stats and dates on the temp changes to record in the ticket. Maybe someone was working on this.": 1,
                "C. You open the cabinet and find that the cables are a mess, overcrowding. You work with her on a maintenance window so you can recable the server for better airflow.": 10,
                "D. You open the cabinet and find that the cables are a mess, overcrowding. You power down and start reorganizing the cables to encourage better airflow. ": -10,
            }
        },
            "WRONG_PORT_SPEED": {
            "How do you proceed?": {
                "A. You ask the Network Analyst if they are sure, and to give you some logs.": 3,
                "B. You see that the link light on both ports are green. You let him know that the port is negotiating correctly.": 5,
                "C. You tell the Netowrk Analyst that this is probably a network problem and ask them to investigate this themselves.": -10,
                "D. You see that the ports are green but the port in question is infact plugged into a different switch, \nyou work with him on a maintenance window to move the cable to a faster switch.": 10,
            }
        }
    }
secondary_questions = {
        "CABLES_ON_FLOOR": {
            "What is your choice?": {
                "A. Hit the EMO (Emergency Power Off) button on the wall. This is dangerous. ": -20,
                "B. Pick up the cables and walk them to the trash, these cables are certianly trash now. ": 5,
                "C. You call your manager, this is unacceptible. ": 2,
                "D. Pick up the cables and put them with the other cables. ": 0,
            }
        },
        "LOOSE_TILE" : {
            "What are you going to do about it?": {
                "A. Go get the suction cups, and put that tile back." : 5,
                "B. Walk around it. ": -5,
                "C. You're not sure if someone was working there. You go ask someone if you can put the tile back.": 2,
                "D. You drop some pocket trash in there, it's under the floor so it's fine. ": -10,
            }
        },
        "FOOD_AND_DRINK" : {
            "How do you handle this?": {
                "A. You pick it up and throw it away in the nearest safe space for liquid disposal, making a note to self to mention this to your manager." : 5,
                "B. Walk around it. ": -5,
                "C. You pick up the soda, seems fine. You're pretty thirsty.": -10,
                "D. You notify all staff and request that the offender come clean up their mess. ": 1,
            }
        },
        "COWORKER_ENCOUNTER": {
            "How to you proceed?": {
                "A. You join in, laughing, and start making up fun names for objects around you, mostly cabinets. \nYou marvel at how strong that adhesive is." : -5,
                "B. You ask your coworker not to label any equipment erroneously, and remind them to return the tool when he's done." : 5,
                "C. You let the coworker label the items in your backpack with creative names, \nbut stop them when they get the urge to stick it on customer or datacenter property." : 2,
                "D. You ignore the coworker, who at this point is giggling to themselves. You're not their boss." : 0,
            }
        },
        "LOOSE_CHILD" : {
            "How do you handle this?": {
                "A. You gently tell the child how to exit the datahall. 'This is no place for children', you say." : 2,
                "B. You engage them in a thrilling conversation about Roblox until the parent arrives, however they're the one doing all the talking." : 0,
                "C. You nicely escort the child through the secure door they somehow got through, and take them to the NOC where their parent happily informs you of 'Take your kid to work day'. \nYou ask them to pay more attention." : 5,
                "D. You ask the kid if they want to see something cool. Then proceed to do something you think is cool. " : -5,
            }
        },
        "AN_ACTUAL_MOUSE" : {
            "What is your choice?": {
                "A. You ignore the mouse." : 0,
                "B. You ignore the mouse. Later making some poorly received joke about 'losing your mouse'." : -5,
                "C. You walk around on all fours, crouching through the row trying to locate the wayward animal." : 2,
                "D. You promptly inform your management." : 5,
            }
        },
        "CRASHCART" : {
            "How do you proceed?": {
                "A. You wrap up the cables and move it to the end of the row, where they belong." : 5,
                "B. You push it to the side so it's out of your way." : 0,
                "C. You work around it, someone might need this for something." : 2,
                "D. You add more labels." : -5,
            }
        },
        "POSTIT_NOTE" : {
            "How do you handle this?": {
                "A. You transcribe the jibberish into your team chat channel and ask 'What does aoi345sudh*&6$ mean?'" : -5,
                "B. You leave it there, and let someone know." : 2,
                "C. You pull the note off the cabinet and pocket it. You'll figure it out later." : 0,
                "D. You pull the note off the cabinet and pocket it, then inform your management about the note. This is serious." : 5,
            }
        },
        "LIGHTS_OUT" : {
            "How do you proceed?": {
                "A. You make a note of this to check in with the customer about their server's status." : 5,
                "B. You ignore it and walk away." : 0,
                "C. You make a note of this and mention it to a coworker." : 2,
                "D. You power the server back on." : -10,
            }
        },
        "CABINET_OPEN" : {
            "How do you proceed?": {
                "A. You ignore it and walk away." : 0,
                "B. You send a message asking about the cabinet." : 2,
                "C. You open all the other cabinets around it. Either to be helpful for some reason, or because you just like the sound the door makes." : -5,
                "D. You close the door and latch it." : 5,
            }
        }
    }

def question_text(question_name):
    text = {
        "HARD DISK SWAP": "You have an open issue on this server named something.biz. \nThe customer needs a failed disk to be hot swapped with the one you somehow have in your hand.\n\n",
        "CABLES_ON_FLOOR": "You almost trip on a loose tangled bundle of fiber optic cabling on the floor. What do you do?\n\n",
        "LOOSE_TILE" : "You almost fall through the floor. Someone removed a raised floor tile and didn't put it back. \n\n",
        "FOOD_AND_DRINK" : "Your foot almost knocks a half-full soda can over, right in the row.\nFood and drink are strictly prohibited in the datahall. What do you do?\n\n",
        "COWORKER_ENCOUNTER":"A coworker wanders into your row. Bored, they pick up the label maker and start labeling random objects.\n\n",
        "LOOSE_CHILD":"A random child appears.\n\n",
        "AN_ACTUAL_MOUSE":"Walking through the row you see something out of the corner of your eye. \nUpon investigation, it scurries away further under a rack.\n\n",
        "CRASHCART":"There is a crashcart in the way. It's covered with random labels that don't quite describe what you're looking at. \nIt's not plugged into anything.\n\n",
        "POSTIT_NOTE":"The cabinet you're standing at has a slightly crumpled post-it note on it, it's bright pink. On closer inspection it has random letters and numbers and symbols scrawled on it.\n\n",
        "LIGHTS_OUT":"Most servers are powered on. Except one of them.\n\n",
        "CABINET_OPEN":"This cabinet is WIDE OPEN. But there isn't anyone around.\n\n",
        "NETWORK_LINKS":"You have an open issue with a repeat customer, Dave. Dave said that one if his network links looks like it's down but he's not sure. \nYou look at it and sure enough one of the link lights is off.\n |_______[x][]|\n\n",
        "POWER_DOWN":"Sr. Systems Administrator Juan asks you to go ahead and power down his server located in this cabinet. \nIt's going to be recycled, which makes you remember that you forgot to put your recycling out on the \ncurb this morning before work.\n\n",
        "MEMORY_TESTING":"Alexandrina has requested that you help her do some memory testing. A stick is bad so she needs to figure out of the stick is bad or the slot is bad before she can call the vendor.\n\n",
        "POWER_BLEED":"A customer asks you to perform a power bleed on the server named: something.edu\n\n",
        "DIAGNOSTICS":"Your boss suggested that you run some diagnostics for a problem customer, \nthey think that everything is our fault. This should help them calm down.\n\n",
        "NEW_GPU":"A research group has acquired some new GPUs to test for their upcoming AI projects. Your issue is to replace the current GPUs in the server named something.gov\n\n",
        "RELABLE_SERVER":"The last time Larry was at the datacenter, he noticed his servers were not labeled correctly. He requests that you relabel them.\n\n",
        "CABLES_CROWDED_HEAT":"Carrie noted that her server's inlet temperature was unusually high compared to the other servers she owns in your datacenter. \nShe asks that you check this out.\n\n",
        "WRONG_PORT_SPEED":"A Network Analyst put in a ticket because they said one of their server's ports is negotiating at the wrong speed. They asked you to check.\n\n",
    }
    return(str(text.get(question_name)))

def ask_primary_question(questions,question_text):
    # You start at 0 for this question, it gets added or removed from your overall score after the function returns.
    player_choices_a = ['A','B','C','D']
    player_choices_b = ['1','2','3']
    score = 0

    rand_question_key = random.choice(list(questions.keys()))
    while rand_question_key in smart.used_questions:
        rand_question_key = random.choice(list(questions.keys()))
    rand_question, answers = list(questions[rand_question_key].items())[0]
    print(str(question_text(rand_question_key)))
    
    for option, points in answers.items():
        if not option.startswith("sub_"):
            print(str(option))
    
    #Do a little validation
    while True:
        player_answer = input("Please enter a choice: A, B, C, or D: \n\n").strip().upper()
        if player_answer in player_choices_a:
            break
        else:
            print("Invalid choice. Please enter A, B, C, or D.")
    
    #Get Score so far
    for option, points in answers.items():
        if option.startswith(player_answer):
            score += points
            print(f"Points: {score}")
    
    sub_key = f"sub_{player_answer}"
    if sub_key in answers:
        sub_question = answers[sub_key]
        sub_text, sub_answers = list(sub_question.items())[0]

        print(f"\n{sub_text}")
        for option, points in sub_answers.items():
            print(str(option))
    
        #Do a little validation
        while True:
            player_sub_answer = input("Which one do you choose? 1, 2, or 3: ").strip()
            if player_sub_answer in player_choices_b:
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.\n")

        for option, points in sub_answers.items():
            if option.startswith(player_sub_answer):
                score += points
                print(f"Points: {score}")

    return score,rand_question_key
