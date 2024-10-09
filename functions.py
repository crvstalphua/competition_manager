import team
import match
from datetime import datetime
import logging

def input_teams():
    print('Add your teams in the format: <team name> <registration date> <group number>: ')
    logging.info('Adding teams from input...')
    team_info = ''
    while True:
        user_input = input()
        if user_input == "":
            break
        lines = user_input.split('\n')
        for line in lines:
            full_line = line
            line = line.split()
        
            # missing 1/2 variables for team
            if len(line) != 3:
                print(f'Team missing variable: {full_line} Format: <team name> <registration date> <group number>')
                print('Please check for error and re-input all teams')
                logging.info(f'Error adding teams due to incorrect input: {full_line}')
                team.Team.delete_all_teams()
                break

            # team already in list (same name)
            if team.Team.get_team(line[0]) != None:
                print(f'Error: {full_line} - Team with {line[0]} already exists')
                print('Please check for error and re-input all teams')
                logging.info(f'Error adding teams due to team already existing: {full_line}')
                team.Team.delete_all_teams()
                break
            
            # group number not an integer
            if not line[2].isdigit():
                print(f'Error: {full_line} - Group number must be an integer not {line[2]}')
                print('Please check for error and re-input all teams')
                logging.info(f'Error adding teams due to non-integer group number: {full_line}')
                team.Team.delete_all_teams()
                break

            # incorrect datetime format
            try:
                datetime.strptime(line[1], "%d/%m")
            except:
                print(f'Error: {full_line} - Invalid datetime: {line[1]} format should be "dd/mm"')
                print('Please check for error and re-input all teams')
                logging.info(f'Error adding teams due to incorrect date format: {full_line}')
                team.Team.delete_all_teams()
                break
            
            team.Team(line[0], line[1], line[2])
            team_info += f'Added team: {line[0]}, Registration Date: {line[2]}, Group Number: {line[1]} \n'
            team.Team.update_rankings()
    print(team_info)
    logging.info(f'Adding process completed \n{team_info}')


def input_matches():
    print('Add your matches in the format: <team 1 name> <team 2 name> <team 1 goals scored> <team 2 goals scored>: ')
    logging.info('Adding matches from input...')
    match_info = ''
    while True:
        user_input = input()
        if user_input == "":
            break
        lines = user_input.split('\n')
        for line in lines:
            full_line = line
            line = line.split()

            # missing variables for match
            if len(line) != 4:
                print(f'Match missing variable: {full_line} Format: <team 1 name> <team 2 name> <team 1 goals scored> <team 2 goals scored>')
                print('Please check for error and re-input all matches')
                logging.info(f'Error adding matches due to incorrect input: {full_line}')
                match.Match.delete_all_matches()
                break

            # team does not currently exist
            if team.Team.get_team(line[0]) == None:
                print(f'Error: {full_line} - Team {line[0]} does not exist')
                print('Please check for error and re-input all matches')
                logging.info(f'Error adding matches due to team not existing: {full_line}')
                match.Match.delete_all_matches()
                break
            elif team.Team.get_team(line[1]) == None:
                print(f'Error: {full_line} - Team {line[1]} does not exist')
                print('Please check for error and re-input all matches')
                logging.info(f'Error adding matches due to team not existing: {full_line}')
                match.Match.delete_all_matches()
                break

            # match already exists
            if match.Match.get_match(line[0], line[1]):
                print(f'Error: {full_line} - Match between {line[0]} and {line[1]} already exists')
                print('Please check for error and re-input all matches')
                logging.info(f'Error adding matches due to match already existing: {full_line}')
                match.Match.delete_all_matches()
                break

            # goals not integer
            if not line[2].isdigit():
                print(f'Error: {full_line} - Goals scored should be an integer not {line[2]}')
                print('Please check for error and re-input all matches')
                logging.info(f'Error adding matches due to non-integer group number: {full_line}')
                match.Match.delete_all_matches()
                break
            elif not line[3].isdigit():
                print(f'Error: {full_line} - Goals scored should be an integer not {line[3]}')
                print('Please check for error and re-input all matches')
                logging.info(f'Error adding matches due to non-integer group number: {full_line}')
                match.Match.delete_all_matches()
                break

            team_1 = team.Team.get_team(line[0])
            team_2 = team.Team.get_team(line[1])

            # teams do not belong to the same group
            if team_1.grp_num != team_2.grp_num:
                print(f'Error: {full_line} - Match cannot be added as {line[0]} and {line[1]} are not from the same group')
                print('Please check for error and re-input all matches')
                logging.info(f'Error adding matches due to non-matching groups: {full_line}')

            new_match = match.Match(line[0], line[1], int(line[2]), int(line[3]))
            match_info += f'Added match: {line[0]} ({line[2]}) vs {line[1]} ({line[3]}) \n'

            team_1.add_match(new_match)
            team_2.add_match(new_match)
            team.Team.update_rankings()
    print(match_info)
    logging.info(f'Adding matches complete \n{match_info}')

def display_rankings():
    logging.info(f'Displaying rankings...')
    for grps, teams in team.Team.get_groups().items():
        print(f'GROUP {str(grps)} RANKING')
        for x in range(len(teams)):
            if  x < 4:
                print(f'#{str(teams[x].rank)} {teams[x].name} (Qualified)')
                
                print('score: ' + str(teams[x].score) + ' goals: ' + str(teams[x].goals) + 
                      ' alt_score: ' + str(teams[x].alt_score) + ' date: ' + str(teams[x].reg_date))
            else:
                print(f'#{str(teams[x].rank)} {teams[x].name}')
                
                print('score: ' + str(teams[x].score) + ' goals: ' + str(teams[x].goals) + 
                      ' alt_score: ' + str(teams[x].alt_score) + ' date: ' + str(teams[x].reg_date))
                
        print('\n')

def display_team():
    print('Enter name of team to retrieve details: ')
    logging.info('Retrieving team details...')
    while True:
        user_input = input()
        try: 
            response = team.Team.get_team_details(user_input)
            print(response)
            logging.info(f'Team details retrieved: \n{response}')
            break
        except:
            logging.info(f'Team could not be found: {user_input}')
            print('No such team found, please check for errors and re-enter team name')

def edit_match():
    print('Enter new match information: ')
    logging.info('Editing match details...')
    while True:
        user_input = input()
        full_line = user_input
        line = user_input.split()

        # missing variables for match
        if len(line) != 4:
            print(f'Match missing variable: {full_line} Format: <team 1 name> <team 2 name> <team 1 goals scored> <team 2 goals scored>')
            print('Please check for error and re-input match')
            logging.info(f'Error editing match due to incorrect input: {full_line}')
            continue

        # match does not exist
        if not match.Match.get_match(line[0], line[1]):
            print(f'Error: {full_line} - Match between {line[0]} and {line[1]} does not exist')
            print('Please check for error and re-input match')
            logging.info(f'Error editing match due to incorrect input: {full_line}')
            continue

        # goals not integer
        if not line[2].isdigit():
            print(f'Error: {full_line} - Goals scored should be an integer not {line[2]}')
            print('Please check for error and re-input match')
            logging.info(f'Error editing match due to incorrect input: {full_line}')
            continue
        elif not line[3].isdigit():
            print(f'Error: {full_line} - Goals scored should be an integer not {line[3]}')
            print('Please check for error and re-input match')
            logging.info(f'Error editing match due to incorrect input: {full_line}')
            continue

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
            print(f'Match Updated: {old_details} to {new_details}')
            logging.info(f'Match updated from {old_details} to {new_details}')
            break
        except:
            logging.info(f'Match could not be found: {line}')
            print('No such match found, please check for errors and re-enter match')


def edit_team():
    print('Enter new team information (note that team name is not editable): <team name> <registration date> <group number>')
    logging.info(f'Editing team details...')
    while True:
        user_input = input()
        full_line = user_input
        line = user_input.split()

        # missing 1/2 variables for team
        if len(line) != 3:
            print(f'Team missing variable: {full_line} Format: <team name> <registration date> <group number>')
            print('Please check for error and re-input team')
            logging.info(f'Error editing team due to incorrect input: {full_line}')
            continue

        # team not in list (same name)
        if team.Team.get_team(line[0]) == None:
            print(f'Error: {full_line} - Team {line[0]} does not exist')
            print('Please check for error and re-input team')
            logging.info(f'Error editing team due to incorrect input: {full_line}')
            continue
            
        # group number not an integer
        if not line[2].isdigit():
            print(f'Error: {full_line} - Group number must be an integer not {line[2]}')
            print('Please check for error and re-input team')
            logging.info(f'Error editing team due to incorrect input: {full_line}')
            continue

        # incorrect datetime format
        try:
            datetime.strptime(line[1], "%d/%m")
        except:
            print(f'Error: {full_line} - Invalid datetime: {line[1]} format should be "dd/mm"')
            print('Please check for error and re-input team')
            logging.info(f'Error editing team due to incorrect input: {full_line}')
            continue

        try: 
            team_to_edit = team.Team.get_team(line[0])
            old_details = f'{team_to_edit.name} {team_to_edit.reg_date} {str(team_to_edit.grp_num)}'
            team_to_edit.edit_team(line[0], line[1], line[2])
            new_details = f'{team_to_edit.name} {team_to_edit.reg_date} {str(team_to_edit.grp_num)}'

            team.Team.update_rankings()
            print(f'Team Updated: {old_details} to {new_details}')
            logging.info(f'Team updated from {old_details} to {new_details}')
            break
        except:
            logging.info(f'Team could not be found: {line[0]}')
            print('No such team found, please check for errors and re-enter team')

def clear():
    print('Enter "clear" if you want to delete all data:')
    logging.info(f'Clearing all data...')

    while True:
        user_input = input()
        if user_input == 'clear':
            team.Team.delete_all_teams()
            match.Match.delete_all_matches()
            team.Team.update_rankings()
            print('Data cleared')
            logging.info('Data successfully cleared')
            break
        else:
            logging.info(f'Error clearing data')
            print('Error. Re-enter "clear" to remove all data.')
            continue
        

            
            
