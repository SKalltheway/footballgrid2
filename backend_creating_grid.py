import random

def generate_nfl_grid():
    grid = []
    teams = ["Team A", "Team B", "Team C", "Team D", "Team E", "Team F", "Team G", "Team H", "Team I"]  # Replace with the actual team names
    
    # Shuffle the team list
    random.shuffle(teams)
    
    # Generate the grid
    for i in range(3):
        row = []
        for j in range(3):
            # Assign a random player to each cell
            player = get_random_player()
            row.append(f"{teams[i*3+j]}: {player}")
        grid.append(row)
    
    # Print the grid
    for row in grid:
        print(" | ".join(row))

def get_random_player():
    players = ["Player 1", "Player 2", "Player 3", "Player 4", "Player 5", "Player 6", "Player 7", "Player 8", "Player 9"]  # Replace with actual player names
    return random.choice(players)

# Generate and display the NFL grid with player names
generate_nfl_grid()