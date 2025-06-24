import game_data

player_wins = 0
computer_wins = 0

def calculate_results(user, computer):
    if user == computer:
        return "It's a draw!"
    elif (user - computer) % 3 == 1:
        return game_data.win_message
    else:
        return game_data.lose_message
    