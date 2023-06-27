import random

def generate_player_grid():
    teams_x_data = ["CARDINALS", "FALCONS", "RAVENS", "BILLS", "PANTHERS","BENGALS", "BROWNS", "BEARS", "COWBOYS", "BRONCOS", "LIONS", "PACKERS", "TEXANS", "COLTS", "CHIEFS", "CHARGERS", "RAMS", "JAGUARS", "DOLPHINS", "VIKINGS", "PATRIOTS", "SAINTS", "GIANTS", "JETS", "RAIDERS", "EAGLES", "49ERS", "SEAHAWKS", "STEELERS", "BUCCANEERS", "TITANS", "REDSKINS"]
    teams_y_data = ["CARDINALS", "FALCONS", "RAVENS", "BILLS", "PANTHERS","BENGALS", "BROWNS", "BEARS", "COWBOYS", "BRONCOS", "LIONS", "PACKERS", "TEXANS", "COLTS", "CHIEFS", "CHARGERS", "RAMS", "JAGUARS", "DOLPHINS", "VIKINGS", "PATRIOTS", "SAINTS", "GIANTS", "JETS", "RAIDERS", "EAGLES", "49ERS", "SEAHAWKS", "STEELERS", "BUCCANEERS", "TITANS", "REDSKINS"]
    

    teams_x = [random.choice(teams_x_data)]

    teams_x_data.remove(teams_x[0])
    teams_x.insert(1, random.choice(teams_x_data))
    teams_x_data.remove(teams_x[1])
    teams_x.insert(2, random.choice(teams_x_data))
    teams_x_data.remove(teams_x[2])
    
    
    teams_y_data.remove(teams_x[0])
    teams_y_data.remove(teams_x[1])
    teams_y_data.remove(teams_x[2])
    teams_y = [random.choice(teams_y_data)]
    teams_y_data.remove(teams_y[0])
    teams_y.insert(1, random.choice(teams_y_data))
    teams_y_data.remove(teams_y[1])
    teams_y.insert(2, random.choice(teams_y_data))
    teams_y_data.remove(teams_y[2])
    
    print(teams_x)
    print(teams_y)


    grid = []
    
    # Generate the grid
    for i in range(3):
        row = []
        for j in range(3):
            player = input(f"Enter player for {teams_x[i]} and {teams_y[j]}: ")
            row.append(player)
        grid.append(row)
    
    # Print the grid
    print("  |", end="")
    for team_y in teams_y:
        print(f" {team_y} |", end="")
    print()
    print("-" * (6 + 9 * len(teams_y)))
    
    for i, row in enumerate(grid):
        print(f"{teams_x[i]} |", end="")
        for player in row:
            print(f" {player} |", end="")
        print()
        print("-" * (6 + 9 * len(teams_y)))

# Generate and display the player grid
generate_player_grid()