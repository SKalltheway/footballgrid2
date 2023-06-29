import random
import csv as csv
import pandas as pd

DATA_PATH = 'all_NFL_players_ever.csv'

def generate_player_grid():
    teams_x_data = ["CARDINALS", "FALCONS", "RAVENS", "BILLS", "PANTHERS","BENGALS", "BROWNS", "BEARS", "COWBOYS", "BRONCOS", "LIONS", "PACKERS", "TEXANS", "COLTS", "CHIEFS", "CHARGERS", "RAMS", "JAGUARS", "DOLPHINS", "VIKINGS", "PATRIOTS", "SAINTS", "GIANTS", "JETS", "RAIDERS", "EAGLES", "49ERS", "SEAHAWKS", "STEELERS", "BUCCANEERS", "TITANS", "COMMANDERS"]
    teams_y_data = ["CARDINALS", "FALCONS", "RAVENS", "BILLS", "PANTHERS","BENGALS", "BROWNS", "BEARS", "COWBOYS", "BRONCOS", "LIONS", "PACKERS", "TEXANS", "COLTS", "CHIEFS", "CHARGERS", "RAMS", "JAGUARS", "DOLPHINS", "VIKINGS", "PATRIOTS", "SAINTS", "GIANTS", "JETS", "RAIDERS", "EAGLES", "49ERS", "SEAHAWKS", "STEELERS", "BUCCANEERS", "TITANS", "COMMANDERS"]

    team_map = dict({'Ari' : 'CARDINALS', 'Atl' : 'FALCONS', 'Bal' : 'RAVENS', 'Buf': 'BILLS', 'Car': 'PANTHERS', 'Cin': 'BENGALS', 'Cle' : 'BROWNS', 'Chi': 'BEARS', 'Dal': 'COWBOYS', 'Den':'BRONCOS', 'Det': 'LIONS', 'GB': 'PACKERS', 'Hou': 'TEXANS', 'Ind': 'COLTS', 'KC': 'CHIEFS', 'LAC': 'CHARGERS', 'SD': 'CHARGERS', 'LAR':'RAMS', 'Stl':'RAMS', 'LA': 'RAMS', 'Jax': 'JAGUARS', 'Mia':'DOLPHINS', 'Min': 'VIKINGS', 'NE': 'PATRIOTS', 'NO': 'SAINTS', 'NYG': 'GIANTS', 'NYJ': 'JETS', 'LV': 'RAIDERS', 'Oak': 'RAIDERS', 'Phi': 'EAGLES', 'SF': '49ERS', 'Sea': 'SEAHWAKS', 'Pit': 'STEELERS', 'TB': 'BUCCANEERS', 'Ten':'TITANS', 'Was': 'COMMANDERS'  })

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
    guesses_remaining = 9
    
    # Generate the grid
    for i in range(3):
        row1 = []
        for j in range(3):
            print("Guesses Remaining:",  guesses_remaining)
            player = input(f"Enter player for {teams_x[i]} and {teams_y[j]}: ")
            for index, row in df.iterrows():   
                if player == row[0]:
                    player_teams_with_years = row[3].split()
                    player_teams = [item for item in player_teams_with_years if not (item.isdigit() or len(item) > 4 )]
                    y = 0
                    while y<len(player_teams):
                        player_teams[y] = player_teams[y].translate({ord(","): None})
                        y = y + 1
                    x = 0
                    team_names = []
                    while x<len(player_teams):
                        team_names.insert(x, team_map.get(player_teams[x]))
                        x=x+1
            if all(var in team_names for var in [teams_x[i], teams_y[j]]):
                print('Correct!')
                row1.append(player)
            else:
                print('Incorrect :(')
                player = 'X'
                row1.append(player)
            guesses_remaining = guesses_remaining - 1
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