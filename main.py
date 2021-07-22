
import random

game_dict = {'7': " ", '8': " ", '9': " ",
             '4': " ", "5": " ", "6": " ",
             '1': " ", '2': " ", '3': " "}
sum_x = 0
sum_0 = 0
score = 0
scores_list_x = []
winners_list_x = []
scores_list_0 = []
winners_list_0 = []

key_list = []
for i in game_dict:
    key_list.append(i)


def refresh():
    for number in key_list:
        game_dict[number] = " "


def print_board(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])


print("Initially the board is - ")
print_board(game_dict)
random_choice = ['X', 'O']
turn = random.choice(random_choice)

game_is_on = True
while game_is_on:
    count = 0
    for i in range(0, len(game_dict)):
        user_move = input(f"It's {turn} turn. Choose where to place? ")
        if game_dict[user_move] == " ":
            game_dict[user_move] = turn
            count += 1
            print_board(game_dict)
        else:
            print("The place is already filled. Choose another place.")
            continue

        if count >= 5:
            if game_dict['1'] == game_dict['2'] == game_dict['3'] != " ":
                print_board(game_dict)
                print("Game Over.")
                score += 1
                print(f"{turn} won with a score of {score}.")
                break

            if game_dict['4'] == game_dict['5'] == game_dict['6'] != " ":
                print_board(game_dict)
                print("Game Over.")
                score += 1
                print(f"{turn} won with a score of {score}.")
                break

            if game_dict['7'] == game_dict['8'] == game_dict['9'] != " ":
                print_board(game_dict)
                print("Game Over.")
                score += 1
                print(f"{turn} won with a score of {score}.")
                break

            if game_dict['1'] == game_dict['4'] == game_dict['7'] != " ":
                print_board(game_dict)
                print("Game Over.")
                score += 1
                print(f"{turn} won with a score of {score}.")
                break

            if game_dict['2'] == game_dict['5'] == game_dict['8'] != " ":
                print_board(game_dict)
                print("Game Over.")
                score += 1
                print(f"{turn} won with a score of {score}.")
                break

            if game_dict['3'] == game_dict['6'] == game_dict['9'] != " ":
                print_board(game_dict)
                print("Game Over.")
                score += 1
                print(f"{turn} won with a score of {score}.")
                break

            if game_dict['1'] == game_dict['5'] == game_dict['8'] != " ":
                print_board(game_dict)
                print("Game Over.")
                score += 1
                print(f"{turn} won with a score of {score}.")
                break

            if game_dict['3'] == game_dict['5'] == game_dict['7'] != " ":
                print_board(game_dict)
                print("Game Over.")
                score += 1
                print(f"{turn} won with a score of {score}.")
                break

        if count == len(game_dict):
            print("Game Over.")
            print("It's a TIE.")

        if turn == 'X':
            turn = 'O'
        elif turn == 'O':
            turn = 'X'
    if turn == 'X':
        scores_list_x.append(score)
        winners_list_x.append(turn)
    else:
        scores_list_0.append(score)
        winners_list_0.append(turn)

    user_input = input("Do you want to continue(y/n)? ")
    if user_input.lower() == 'y':
        game_is_on = True
        refresh()
        print_board(game_dict)
        random_choice = ['X', 'O']
        turn = random.choice(random_choice)
        score = 0
    else:
        game_is_on = False
