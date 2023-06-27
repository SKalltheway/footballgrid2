import random
import random

def generate_team_grid():
    teams = ["Team A", "Team B", "Team C"]  # Replace with the actual team names
    random.shuffle(teams)  # Randomize the team order
    
    grid = []
    players = ["Player 1", "Player 2", "Player 3", "Player 4", "Player 5", "Player 6", "Player 7", "Player 8", "Player 9"]  # Replace with actual player names
    
    # Generate the grid
    for i in range(3):
        row = []
        for j in range(3):
            team = teams[i]
            player = random.choice(players)
            row.append(f"{team}: {player}")
            players.remove(player)  # Remove the selected player from the list
        grid.append(row)
    
    # Print the grid
    for row in grid:
        print(" | ".join(row))

# Generate and display the team grid with players
generate_team_grid()
