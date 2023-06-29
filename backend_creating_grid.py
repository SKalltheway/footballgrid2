import random
import csv as csv
import pandas as pd

DATA_PATH = 'all_NFL_players_ever.csv'

def generate_player_grid():
    teams_x_data = ["CARDINALS", "FALCONS", "RAVENS", "BILLS", "PANTHERS","BENGALS", "BROWNS", "BEARS", "COWBOYS", "BRONCOS", "LIONS", "PACKERS", "TEXANS", "COLTS", "CHIEFS", "CHARGERS", "RAMS", "JAGUARS", "DOLPHINS", "VIKINGS", "PATRIOTS", "SAINTS", "GIANTS", "JETS", "RAIDERS", "EAGLES", "49ERS", "SEAHAWKS", "STEELERS", "BUCCANEERS", "TITANS", "REDSKINS"]
    teams_y_data = ["CARDINALS", "FALCONS", "RAVENS", "BILLS", "PANTHERS","BENGALS", "BROWNS", "BEARS", "COWBOYS", "BRONCOS", "LIONS", "PACKERS", "TEXANS", "COLTS", "CHIEFS", "CHARGERS", "RAMS", "JAGUARS", "DOLPHINS", "VIKINGS", "PATRIOTS", "SAINTS", "GIANTS", "JETS", "RAIDERS", "EAGLES", "49ERS", "SEAHAWKS", "STEELERS", "BUCCANEERS", "TITANS", "REDSKINS"]

    team_map = dict({'Ari' : 'CARDINALS', 'Atl' : 'FALCONS',})

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
    df = pd.read_csv(DATA_PATH)

    grid = []
    
    # Generate the grid
    for i in range(3):
        row1 = []
        for j in range(3):
            
            player = input(f"Enter player for {teams_x[i]} and {teams_y[j]}: ")
            for index, row in df.iterrows():   
                if player == row[0]:
                    print(row)
            #team_map.get()
            row1.append(player)
        grid.append(row1)
    
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