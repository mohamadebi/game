import random

human_score= 0
robat_score= 0
stats = ["paper","scissor","rock"]
print("#########   start game   ##########")
name = input("whats your name ? ")
stage = input("Please specify the number of game stages: ")


print(stats)
while robat_score < int(stage) and human_score < int(stage) :

    print("""
        1.paper
        2.scissor
        3.rock
    """)
    human_choice = input("please choice one of them: ")
    robat_choice = random.choice(stats)
    print(f"{name}_choice:{human_choice}")
    print(f"robat_choice:{robat_choice}")

    if human_choice == "paper" and robat_choice == "scissor" :
        robat_score=robat_score + 1 
    elif human_choice == "paper" and robat_choice == "rock" :
        human_score=human_score + 1 
    elif human_choice == "rock" and robat_choice == "scissor" :
        human_score=human_score + 1 
    elif human_choice == "rock" and robat_choice == "paper" :
        robat_score=robat_score + 1 
    elif human_choice == "scissor" and robat_choice == "rock" :
        robat_score=robat_score + 1 
    elif human_choice == "scissor" and robat_choice == "paper" :
        human_score=human_score + 1 
    
    print(f"{name}_score:{human_score}")
    print(f"robat_score:{robat_score}")



print(f"{name}_score:{human_score}")
print(f"robat_score:{robat_score}")
if human_score > robat_score : 
    print(f"{name} WIN🎉🎉")
else:
    print("Robat WIN🎉🎉")