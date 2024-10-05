from team import Team 

def input_teams():

    teams = list()
    print('Add your teams in the format: <team_name> <registration date> <group number>')

    while True:
        user_input = input()
        if user_input == "":
            break
        lines = user_input.split('\n')
        for line in lines:
            line = line.split()
            teams.append(Team(line[0], line[1], line[2]))
    return teams

