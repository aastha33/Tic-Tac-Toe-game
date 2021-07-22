from main import scores_list_0, scores_list_x, winners_list_x, winners_list_0
player_details = open("C:/Users/Dell/Documents/player-win.txt", "w")

for i in range(0, len(scores_list_x)):
    player_details.write(f"{winners_list_x[i]} wins the game with a score of {scores_list_x[i]}.")
    player_details.write("\n")

for i in range(0, len(scores_list_0)):
    player_details.write(f"{winners_list_0[i]} wins the game with a score of {scores_list_0[i]}.")
    player_details.write("\n")

sum_1 = 0
sum_2 = 0
for i in scores_list_x[0:]:
    sum_1 += i
player_details.write(f"The final score of x is: {str(sum_1)}")
player_details.write("\n")

for i in scores_list_0[0:]:
    sum_2 += i
player_details.write(f"The final score of 0 is: {str(sum_2)}")
player_details.write("\n")
player_details.close()
