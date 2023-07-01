import random
import csv as csv
import pandas as pd

DATA_PATH = 'all_NFL_players_ever.csv'



def generate_player_grid():
    teams_x_data = ["CARDINALS", "FALCONS", "RAVENS", "BILLS", "PANTHERS","BENGALS", "BROWNS", "BEARS", "COWBOYS", "BRONCOS", "LIONS", "PACKERS", "TEXANS", "COLTS", "CHIEFS", "CHARGERS", "RAMS", "JAGUARS", "DOLPHINS", "VIKINGS", "PATRIOTS", "SAINTS", "GIANTS", "JETS", "RAIDERS", "EAGLES", "49ERS", "SEAHAWKS", "STEELERS", "BUCCANEERS", "TITANS", "COMMANDERS"]
    teams_y_data = ["CARDINALS", "FALCONS", "RAVENS", "BILLS", "PANTHERS","BENGALS", "BROWNS", "BEARS", "COWBOYS", "BRONCOS", "LIONS", "PACKERS", "TEXANS", "COLTS", "CHIEFS", "CHARGERS", "RAMS", "JAGUARS", "DOLPHINS", "VIKINGS", "PATRIOTS", "SAINTS", "GIANTS", "JETS", "RAIDERS", "EAGLES", "49ERS", "SEAHAWKS", "STEELERS", "BUCCANEERS", "TITANS", "COMMANDERS"]

    team_map = dict({'Ari' : 'CARDINALS', 'Atl' : 'FALCONS', 'Bal' : 'RAVENS', 'Buf': 'BILLS', 'Car': 'PANTHERS', 'Cin': 'BENGALS', 'Cle' : 'BROWNS', 'Chi': 'BEARS', 'Dal': 'COWBOYS', 'Den':'BRONCOS', 'Det': 'LIONS', 'GB': 'PACKERS', 'Hou': 'TEXANS', 'Ind': 'COLTS', 'KC': 'CHIEFS', 'LAC': 'CHARGERS', 'SD': 'CHARGERS', 'LAR':'RAMS', 'Stl':'RAMS', 'LA': 'RAMS', 'Jax': 'JAGUARS', 'Mia':'DOLPHINS', 'Min': 'VIKINGS', 'NE': 'PATRIOTS', 'NO': 'SAINTS', 'NYG': 'GIANTS', 'NYJ': 'JETS', 'LV': 'RAIDERS', 'Oak': 'RAIDERS', 'Phi': 'EAGLES', 'SF': '49ERS', 'Sea': 'SEAHAWKS', 'Pit': 'STEELERS', 'TB': 'BUCCANEERS', 'Ten':'TITANS', 'Was': 'COMMANDERS'  })
    choice_dict = dict({'1': [0,0], '2': [1,0], '3': [2,0], '4': [0,1], '5': [1,1], '6': [2,1], '7': [0,2], '8': [1,2], '9': [2,2]})
    correct_players = dict({'1': 'X', '2': 'X', '3': 'X', '4': 'X', '5':'X', '6': 'X', '7': 'X', '8': 'X', '9': 'X'})
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
    num_correct = 0
    correct_guesses = []
    while guesses_remaining > 0:
        player_name = ''
        print("Press 1 for ", teams_x[0], " and ", teams_y[0])
        print("Press 2 for ", teams_x[1], " and ", teams_y[0])
        print("Press 3 for ", teams_x[2], " and ", teams_y[0])
        print("Press 4 for ", teams_x[0], " and ", teams_y[1])
        print("Press 5 for ", teams_x[1], " and ", teams_y[1])
        print("Press 6 for ", teams_x[2], " and ", teams_y[1])
        print("Press 7 for ", teams_x[0], " and ", teams_y[2])
        print("Press 8 for ", teams_x[1], " and ", teams_y[2])
        print("Press 9 for ", teams_x[2], " and ", teams_y[2])
        print("You have ", guesses_remaining, " guesses remaining")
        user_choice = input()
        while user_choice in correct_guesses:
            print("Correct Player Already Guessed in this Square, please select another square")
            user_choice = input()
        player = input(f"Enter player for {teams_x[choice_dict.get(user_choice)[0]]} and {teams_y[choice_dict.get(user_choice)[1]]}: ")
        for index, row in df.iterrows():   
            if player == row[0]:
                player_name = player
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
                if all(var in team_names for var in [teams_x[choice_dict.get(user_choice)[0]],teams_y[choice_dict.get(user_choice)[1]] ]):
                    print('Correct!')
                    temp_player_dict = dict({user_choice: player_name})
                    correct_guesses.insert(num_correct, user_choice)
                    correct_players.update(temp_player_dict)
                    num_correct = num_correct + 1
                    guesses_remaining = guesses_remaining - 1
                else:
                    print('Incorrect :(')
                    guesses_remaining = guesses_remaining - 1
        if not player_name:
            print('Player Not Found, please try again')
        
    row1 = [correct_players.get('1'), correct_players.get('4'), correct_players.get('7')]
    row2 = [correct_players.get('2'), correct_players.get('5'), correct_players.get('8')] 
    row3 = [correct_players.get('3'), correct_players.get('6'), correct_players.get('9')]
    grid.append(row1)
    grid.append(row2)
    grid.append(row3)

    #Print the grid
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
