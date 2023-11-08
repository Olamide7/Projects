import random
from game_art import logo
from game_art import vs
from game_data import data


score = 0
choice2 = random.choice(data)
begin_game = False
while not begin_game:
    print(logo)
    choice1 = choice2
    choice2 = random.choice(data)
    while choice1 == choice2:
        choice2 = random.choice(data)

    print(f"Compare A: {choice1['name']}, {choice1['description']}, {choice1['country']}")
    print(vs)
    print(f"Compare B: {choice2['name']}, {choice2['description']}, {choice2['country']}")

    guess = input("Who has more followers? Type 'A' or 'B': ")
    count1 = choice1['follower_count']
    count2 = choice2['follower_count']
    print(count1)
    print(count2)
    if guess == 'A' and count1 > count2:
        print("You're Right!")
        score += 1
    elif guess == 'B' and count2 > count1:
        print("You're Right!")
        score += 1
    else:
        print(f"Sorry!, You lose. Final Score: {score}")
        begin_game = True
        score -= 1
        guess2 = input("Would you like to try again!?: 'yes' or 'no': ")
        if guess2 == "yes":
            begin_game = False
        else:
            begin_game = True
        
        

