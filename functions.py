import team
import match

def input_teams():
    print('Add your teams in the format: <team name> <registration date> <group number>')

    while True:
        user_input = input()
        if user_input == "":
            break
        lines = user_input.split('\n')
        for line in lines:
            line = line.split()
            team.Team(line[0], line[1], line[2])

def input_matches():
    print('Add your matches in the format: <team 1 name> <team 2 name> <team 1 goals scored> <team 2 goals scored>')

    while True:
        user_input = input()
        if user_input == "":
            break
        lines = user_input.split('\n')
        for line in lines:
            line = line.split()
            new_match = match.Match(line[0], line[1], int(line[2]), int(line[3]))

            team.Team.get_team(line[0]).add_match(new_match)
            team.Team.get_team(line[1]).add_match(new_match)



            
            
            
