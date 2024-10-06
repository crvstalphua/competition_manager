import team
import match
from datetime import datetime

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

            team_1 = team.Team.get_team(line[0])
            team_2 = team.Team.get_team(line[1])

            team_1.add_match(new_match)
            team_1.update_score()
            team_2.add_match(new_match)
            team_2.update_score()

def display_rankings():
    ordered_grps = dict(sorted(team.Team.get_groups().items()))
    for grps, teams in ordered_grps.items():
        print('GROUP ' + str(grps) + ' RANKING')
        ordered_teams = sorted(teams, key = lambda x: (-x.score, -x.goals, -x.alt_score, datetime.strptime(x.reg_date, "%d/%m")))
        for x in range(len(ordered_teams)):
            if x < 4:
                print('#' + str(x + 1) + ' ' + ordered_teams[x].name + ' (Qualified)')
                '''
                print('score: ' + str(ordered_teams[x].score) + ' goals: ' + str(ordered_teams[x].goals) + 
                      ' alt_score: ' + str(ordered_teams[x].alt_score) + ' date: ' + str(ordered_teams[x].reg_date))
                '''
            else:
                print('#' + str(x + 1) + ' ' + ordered_teams[x].name) 
                '''
                print('score: ' + str(ordered_teams[x].score) + ' goals: ' + str(ordered_teams[x].goals) + 
                      ' alt_score: ' + str(ordered_teams[x].alt_score) + ' date: ' + str(ordered_teams[x].reg_date))
                '''
                
        print('\n')

        





            
            
            
