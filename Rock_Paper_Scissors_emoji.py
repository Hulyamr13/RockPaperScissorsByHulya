import random

moves = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

player_score = 0
computer_score = 0

emojis = {"rock": "🪨", "paper": "📄", "scissors": "✂️", "win": "🎉", "lose": "💩", "tie": "🙃"}

while player_score < 5 and computer_score < 5:
    player_move = input("Choose rock, paper, or scissors: ").lower()

    while player_move not in moves.keys():
        player_move = input("Invalid move. Choose rock, paper, or scissors: ").lower()

    computer_move = random.choice(list(moves.keys()))

    if moves[player_move] == computer_move:
        print(f"{emojis[player_move]} {emojis['tie']} {emojis[computer_move]}")
    elif moves[computer_move] == player_move:
        print(f"{emojis[player_move]} {emojis['lose']} {emojis[computer_move]}")
        computer_score += 1
    else:
        print(f"{emojis[player_move]} {emojis['win']} {emojis[computer_move]}")
        player_score += 1

    print(f"Player score: {player_score}")
    print(f"Computer score: {computer_score}")

if player_score > computer_score:
    print(f"{emojis['win']} You win the game!")
else:
    print(f"{emojis['lose']} Computer wins the game!")

play_again = input("Play again? (y/n)").lower()
while play_again == "y":
    player_score = 0
    computer_score = 0

    while player_score < 5 and computer_score < 5:
        player_move = input("Choose rock, paper, or scissors: ").lower()
        while player_move not in moves.keys():
            player_move = input("Invalid move. Choose rock, paper, or scissors: ").lower()
        computer_move = random.choice(list(moves.keys()))

        if moves[player_move] == computer_move:
            print(f"{emojis[player_move]} {emojis['tie']} {emojis[computer_move]}")
        elif moves[computer_move] == player_move:
            print(f"{emojis[player_move]} {emojis['lose']} {emojis[computer_move]}")
            computer_score += 1
        else:
            print(f"{emojis[player_move]} {emojis['win']} {emojis[computer_move]}")
            player_score += 1

        print(f"Player score: {player_score}")
        print(f"Computer score: {computer_score}")

    if player_score > computer_score:
        print(f"{emojis['win']} You win the game!")
    else:
        print(f"{emojis['lose']} Computer wins the game!")

    play_again = input("Play again? (y/n)").lower()

print("Thanks for playing!")