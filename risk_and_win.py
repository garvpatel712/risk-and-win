import random

def roll():
    value = random.randint(1,6)
    return value

print("     risk and win\n\n")
print("   rules!  \n1. every time you roll your score will increse.\n2. if you get 1 your score become 0 and you will out the game.\n3. if your score become 50 you wil win the game with highest score.\n4. the player with the higest score will win.\n5. risk your score carefully.")

start = input("would you like to play game (y-n)? ")


while (start.lower() == "y"):
    players = input("how many players want to play (2-4) ?")

    if players.isdigit():
        player = int(players)
        if 2 <= player <= 4:
            score_list = [0 for _ in range(player)]
            max_score = 50 
            current_score = 0
            
            for i in range(player):
                if max(score_list) < max_score:
                    print("player",i+1,"turn is start")
                    current_value=0
                    while True:
                        a = input("whoud you take the risk? ")
                        if a.lower() != "y":
                            print("your total score is",score_list[i])
                            break
                        else:
                            current_value = roll()
                            if current_value == 1:
                                score_list[i] = 0 
                                print("current_value is 1!you'r done.\n")
                                print("your total score is 0")
                                break
                            else:
                                score_list[i] += current_value

                                print("current value =",current_value)
                                if max(score_list) > max_score:
                                    print("your total score is 50")
                                else:
                                    print("your total score is ",score_list[i])
                else:
                    print("game over!\nplayer ",i+1,"is win the game with maximum score.")
                    break
            winner = score_list.index(max(score_list))
            print("winner is player ",winner+1)
        else:
            print("please enter the value between 2 to 4.")

        break
    else:
        print("input is invalid.\nplease enter valid input.")
print("GAME OFF!")