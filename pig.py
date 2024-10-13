import random
import argparse

class Die:
    """Class representing a six-sided die."""
    def __init__(self):
        self.sides = 6

    def roll(self):
        """Roll the die and return a number between 1 and 6."""
        return random.randint(1, self.sides)


class Player:
    """Class representing a player in the Pig game."""
    def __init__(self, name):
        self.name = name
        self.score = 0

    def add_score(self, points):
        """Add points to the player's total score."""
        self.score += points

    def reset_score(self):
        """Reset the player's score to 0."""
        self.score = 0

    def __str__(self):
        """Return a string representation of the player's score."""
        return f"{self.name}: {self.score} points"


class PigGame:
    """Class representing the Pig game."""
    def __init__(self, num_players):
        self.die = Die()
        self.players = [Player(f"Player {i+1}") for i in range(num_players)]
        self.current_player = self.players[0]
        self.turn_score = 0

    def switch_turn(self):
        """Switch to the next player's turn and reset the turn score."""
        self.turn_score = 0
        current_index = self.players.index(self.current_player)
        next_index = (current_index + 1) % len(self.players)
        self.current_player = self.players[next_index]

    def play_turn(self):
        """Handle a player's turn, allowing them to roll or hold"""
        while True:
            print(f"\n{self.current_player}'s turn! Current score: {self.current_player.score}")
            decision = input ("Enter 'r' to roll or 'h' to hold: ").lower()

            if decision == 'r':
                roll = self.die.roll()
                print(f"Rolled: {roll}")
                if roll == 1:
                    print(f"{self.current_player.name} rolled a 1! No points for this turn.")
                    self.switch_turn()
                    break
                else:
                    self.turn_score += roll
                    print(f"Turn score: {self.turn_score}")
            elif decision == 'h':
                self.current_player.add_score(self.turn_score)
                print(f"{self.current_player.name}'s total score: {self.current_player.score}")
                if self.current_player.score >= 100:
                    print(f"{self.current_player.name} wins!")
                    return True
                self.switch_turn()
                break

    def play_game(self):
        """Start the game and alternate turns until a player wins."""
        print("Welcome to Pig!")
        while True:
            if self.play_turn():
                break

    def reset_game(self):
        """Reset the game by resetting all players' scores."""
        for player in self.players:
            player.reset_score()
        self.current_player = self.players[0]
        print("\nStarting a new game!\n")


if __name__ == "__main__":
    # Set up argument parser for number of players
    parser = argparse.ArgumentParser(description="Play pig, the dice game.")
    parser.add_argument('--numPlayers', type=int, default=2, help="Number of players (default: 2)")
    args = parser.parse_args()

    # Seed for reproducible randomness
    random.seed(0)

    # Create and play the game with the specified number of players
    game = PigGame(args.numPlayers)
    while True:
        game.play_game()
        play_again = input("Would you like to play again? (y/n): ").lower()
        if play_again == 'y':
            game.reset_game()
        else:
            print("Thanks for playing!")
            break
    
