def calculate_results(user, computer):
    if user == computer:
        return "It's a draw!"
    elif (user - computer) % 3 == 1:
        return "You win!"
    else:
        return "You lose!"
    