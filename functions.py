import team
import match
from datetime import datetime

def input_teams():
    print('Add your teams in the format: <team name> <registration date> <group number>: ')

    while True:
        user_input = input()
        if user_input == "":
            break
        lines = user_input.split('\n')
        for line in lines:
            line = line.split()
            team.Team(line[0], line[1], line[2])
            team.Team.update_rankings()

def input_matches():
    print('Add your matches in the format: <team 1 name> <team 2 name> <team 1 goals scored> <team 2 goals scored>: ')

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
            team_2.add_match(new_match)
            team.Team.update_rankings()

def display_rankings():
    for grps, teams in team.Team.get_groups().items():
        print('GROUP ' + str(grps) + ' RANKING')
        for x in range(len(teams)):
            if x < 4:
                print('#' + str(teams[x].rank) + ' ' + teams[x].name + ' (Qualified)')
                
                print('score: ' + str(teams[x].score) + ' goals: ' + str(teams[x].goals) + 
                      ' alt_score: ' + str(teams[x].alt_score) + ' date: ' + str(teams[x].reg_date))
                
                
            else:
                print('#' + str(teams[x].rank) + ' ' + teams[x].name) 
                
                print('score: ' + str(teams[x].score) + ' goals: ' + str(teams[x].goals) + 
                      ' alt_score: ' + str(teams[x].alt_score) + ' date: ' + str(teams[x].reg_date))
                
        print('\n')

def display_team():
    print('Enter name of team to retrieve details: ')
    while True:
        user_input = input()
        try: 
            response = team.Team.get_team_details(user_input)
            print(response)
            break
        except:
            print('No such team found, please check for errors and re-enter name')

def edit_match():
    print('Enter new match information: ')
    while True:
        user_input = input()
        line = user_input.split()
        try: 
            old_match = match.Match.get_match(line[0], line[1])
            team_1 = team.Team.get_team(line[0])
            team_2 = team.Team.get_team(line[1])
            old_details = old_match.get_match_details()

            team_1.remove_match(old_match)
            team_2.remove_match(old_match)
            match.Match.delete_match(old_match)

            new_match = match.Match(line[0], line[1], int(line[2]), int(line[3]))
            new_details = new_match.get_match_details()

            team_1.add_match(new_match)
            team_2.add_match(new_match)
            team.Team.update_rankings()
            print('Match Updated: ' + old_details + ' to ' + new_details)
            break
        except:
            print('No such match found, please check for errors and re-enter match')


def edit_team():
    print('Enter new team information (note that team name is not editable): ')
    while True:
        user_input = input()
        line = user_input.split()
        # require some form of input validation
        try: 
            team_to_edit = team.Team.get_team(line[0])
            old_details = team_to_edit.name + ' ' + team_to_edit.reg_date + ' ' + str(team_to_edit.grp_num)
            team_to_edit.edit_team(line[0], line[1], line[2])
            new_details = team_to_edit.name + ' ' + team_to_edit.reg_date + ' ' + str(team_to_edit.grp_num)

            team.Team.update_rankings()
            print('Team Updated: ' + old_details + ' to ' + new_details)
            break
        except:
            print('No such team found, please check for errors and re-enter team')

def clear():
    print('Enter "clear" if you want to delete all information:')

    while True:
        user_input = input()
        if user_input == 'clear':
            team.Team.delete_all_teams()
            match.Match.delete_all_matches()
            team.Team.update_rankings()
            print('Data cleared')
            break
        else:
            print('Error. Re-enter "clear" to remove all data.')
            continue
        

            
            
