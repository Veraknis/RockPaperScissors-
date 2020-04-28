user1 = input("What is your name? ")
user2 = input("And your name? ")
user1_answer = input("%s, Rock, Paper or Scissors? " % user1)
user2_answer = input("%s, Rock, Paper or Scissors? " % user2)


def compare(u1, u2): # Defining the function "compare", which compares both user inputs in order to determine the winner
    if u1 == u2:
        return "It's a tie! "
    elif u1 == 'rock':
        if u2 == 'scissors':
            return "Rock wins! "
        else:
            return "Paper wins! "
    elif u1 == 'scissors':
        if u2 == 'paper':
            return "Scissors win! "
        else:
            return "Rock wins! "
    elif u1 == 'paper':
        if u2 == 'rock':
            return "Paper wins! "
        else:
            return "Scissors win! "
    else:
        return "Invalid input! You have not entered rock, paper or scissors, try again. "


print(compare(user1_answer, user2_answer))
