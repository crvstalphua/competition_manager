import team
import match
from datetime import datetime
import logging
import tkinter as tk

def switch_frames(frame_1, frame_2):
    frame_1.pack_forget()
    frame_2.pack(fill='both')


def input_teams(event, text, log):
    print('Add your teams in the format: <team name> <registration date> <group number>: ')
    logging.info('Adding teams from input...')

    # get text input
    input = text.get('1.0', 'end').strip()
    teams = input.split('\n')
    team_info = ''

    text.delete('1.0', 'end')
    log.delete('1.0', 'end')

    for line in teams:
            full_line = line
            line = line.split()
            error = ''
        
            # missing 1/2 variables for team
            if len(line) != 3:
                error = f'Team missing variable: {full_line} Format: <team name> <registration date> <group number>'
                logging.info(f'Error adding teams due to incorrect input: {full_line}')
                
            # team already in list (same name)
            elif team.Team.get_team(line[0]) != None:
                error = f'Error: {full_line} - Team with {line[0]} already exists'
                logging.info(f'Error adding teams due to team already existing: {full_line}')
                
            # group number not an integer
            elif not line[2].isdigit():
                error = f'Error: {full_line} - Group number must be an integer not {line[2]}'
                logging.info(f'Error adding teams due to non-integer group number: {full_line}')

            # incorrect datetime format
            if len(line) == 3:
                try:
                    datetime.strptime(line[1], "%d/%m")
                except:
                    error = f'Error: {full_line} - Invalid datetime: {line[1]} format should be "dd/mm"'
                    logging.info(f'Error adding teams due to incorrect date format: {full_line}')
            
            if error:
                team_info += error + '\n'
                print(f'{error}\n')
            if not error:
                team.Team(line[0], line[1], line[2])
                team_info += f'Added team: {line[0]}, Registration Date: {line[1]}, Group Number: {line[2]} \n'
                team.Team.update_rankings()
    
    print(team_info)
    logging.info(f'Adding process completed \n{team_info}')
    log.insert(tk.END, team_info)

def input_matches(event, text, log):
    print('Add your matches in the format: <team 1 name> <team 2 name> <team 1 goals scored> <team 2 goals scored>: ')
    logging.info('Adding matches from input...')

    # get text input
    input = text.get('1.0', 'end').strip()
    matches = input.split('\n')
    match_info = ''

    text.delete('1.0', 'end')
    log.delete('1.0', 'end')
    
    for line in matches:
            full_line = line
            line = line.split()
            error = ''

            # missing variables for match
            if len(line) != 4:
                error = f'Match missing variable: {full_line} Format: <team 1 name> <team 2 name> <team 1 goals scored> <team 2 goals scored>'
                logging.info(f'Error adding matches due to incorrect input: {full_line}')

            # team does not currently exist
            elif team.Team.get_team(line[0]) == None:
                error = f'Error: {full_line} - Team {line[0]} does not exist'
                logging.info(f'Error adding matches due to team not existing: {full_line}')

            elif team.Team.get_team(line[1]) == None:
                error = f'Error: {full_line} - Team {line[1]} does not exist'
                logging.info(f'Error adding matches due to team not existing: {full_line}')

            # match already exists
            elif match.Match.get_match(line[0], line[1]):
                error = f'Error: {full_line} - Match between {line[0]} and {line[1]} already exists'
                logging.info(f'Error adding matches due to match already existing: {full_line}')

            # goals not integer
            elif not line[2].isdigit():
                error = f'Error: {full_line} - Goals scored should be an integer not {line[2]}'
                logging.info(f'Error adding matches due to non-integer group number: {full_line}')

            elif not line[3].isdigit():
                error = f'Error: {full_line} - Goals scored should be an integer not {line[3]}'
                logging.info(f'Error adding matches due to non-integer group number: {full_line}')

            # teams do not belong to the same group
            elif team.Team.get_team(line[0]).grp_num != team.Team.get_team(line[1]).grp_num:
                error = f'Error: {full_line} - Match cannot be added as {line[0]} and {line[1]} are not from the same group'
                logging.info(f'Error adding matches due to non-matching groups: {full_line}')

            if error:
                match_info += error + '\n'
                print(f'{error} \n')

            if not error:
                new_match = match.Match(line[0], line[1], int(line[2]), int(line[3]))
                match_info += f'Added match: {line[0]} ({line[2]}) vs {line[1]} ({line[3]}) \n'

                team_1 = team.Team.get_team(line[0])
                team_2 = team.Team.get_team(line[1])

                team_1.add_match(new_match)
                team_2.add_match(new_match)
                team.Team.update_rankings()

    print(match_info)
    logging.info(f'Adding matches complete \n{match_info}')
    log.insert(tk.END, match_info)

def display_rankings(log):
    logging.info(f'Displaying rankings...')
    log.delete('1.0', 'end')

    output = ''
    for grps, teams in team.Team.get_groups().items():
        print(f'GROUP {str(grps)} RANKING')
        output += f'GROUP {str(grps)} RANKING \n\n'
        for x in range(len(teams)):
            if  x < 4:
                print(f'#{str(teams[x].rank)} {teams[x].name} (Qualified)')
                output += f'#{str(teams[x].rank)} {teams[x].name} (Qualified) \n'
                
                print('score: ' + str(teams[x].score) + ' goals: ' + str(teams[x].goals) + 
                      ' alt_score: ' + str(teams[x].alt_score) + ' date: ' + str(teams[x].reg_date))
            else:
                print(f'#{str(teams[x].rank)} {teams[x].name}')
                output += f'#{str(teams[x].rank)} {teams[x].name} \n'
                
                print('score: ' + str(teams[x].score) + ' goals: ' + str(teams[x].goals) + 
                      ' alt_score: ' + str(teams[x].alt_score) + ' date: ' + str(teams[x].reg_date))
                
        print('\n')
        output += '\n'
    log.insert(tk.END, output)

def display_team(event, text, log):
    print('Enter name of team to retrieve details: ')
    logging.info('Retrieving team details...')

    # get text input
    input = text.get('1.0', 'end').strip()

    text.delete('1.0', 'end')
    log.delete('1.0', 'end')

    try: 
        response = team.Team.get_team_details(input)
        print(response)    
        logging.info(f'Team details retrieved: \n{response}')
        log.insert(tk.END, f'Team details retrieved: \n{response}')            
    except:
        logging.info(f'Team could not be found: {input}')    
        print('No such team found, please check for errors and re-enter team name')   
        log.insert(tk.END, f'Team could not be found: {input}')         

def edit_match(event, text, log):
    print('Enter new match information: ')
    logging.info('Editing match details...')

    # get text input
    input = text.get('1.0', 'end').strip()
    full_line = input
    line = full_line.split()
    error = ''

    text.delete('1.0', 'end')
    log.delete('1.0', 'end')

    # missing variables for match
    if len(line) != 4:
        error = f'Match missing variable: {full_line} Format: <team 1 name> <team 2 name> <team 1 goals scored> <team 2 goals scored>'
        logging.info(f'Error editing match due to incorrect input: {full_line}')

    # match does not exist
    elif not match.Match.get_match(line[0], line[1]):
        error = f'Error: {full_line} - Match between {line[0]} and {line[1]} does not exist'
        logging.info(f'Error editing match due to incorrect input: {full_line}')

    # goals not integer
    elif not line[2].isdigit():
        error = f'Error: {full_line} - Goals scored should be an integer not {line[2]}'
        logging.info(f'Error editing match due to incorrect input: {full_line}')
    elif not line[3].isdigit():
        error = f'Error: {full_line} - Goals scored should be an integer not {line[3]}'
        logging.info(f'Error editing match due to incorrect input: {full_line}')

    if error:
        log.insert(tk.END, error)
        return
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

        log.insert(tk.END, f'Match Updated: {old_details} to {new_details}')
    except:
        logging.info(f'Match could not be found: {line}')
        print('No such match found, please check for errors and re-enter match')

def edit_team(event, text, log):
    print('Enter new team information (note that team name is not editable): <team name> <registration date> <group number>')
    logging.info(f'Editing team details...')

    # get text input
    input = text.get('1.0', 'end').strip()
    full_line = input
    line = full_line.split()
    error = ''

    text.delete('1.0', 'end')
    log.delete('1.0', 'end')

    # missing 1/2 variables for team
    if len(line) != 3:
        error = f'Team missing variable: {full_line} Format: <team name> <registration date> <group number>'
        logging.info(f'Error editing team due to incorrect input: {full_line}')

    # team not in list (same name)
    elif team.Team.get_team(line[0]) == None:
        error = f'Error: {full_line} - Team {line[0]} does not exist'
        logging.info(f'Error editing team due to incorrect input: {full_line}')
            
    # group number not an integer
    elif not line[2].isdigit():
        error = f'Error: {full_line} - Group number must be an integer not {line[2]}'
        logging.info(f'Error editing team due to incorrect input: {full_line}')

    # incorrect datetime format
    elif len(line) == 3:
        try:
            datetime.strptime(line[1], "%d/%m")
        except:
            error = f'Error: {full_line} - Invalid datetime: {line[1]} format should be "dd/mm"'
            logging.info(f'Error editing team due to incorrect input: {full_line}')
    
    if error:
        log.insert(tk.END, error)
        return

    try: 
        team_to_edit = team.Team.get_team(line[0])
        old_details = f'{team_to_edit.name} {team_to_edit.reg_date} {str(team_to_edit.grp_num)}'
        team_to_edit.edit_team(line[0], line[1], line[2])
        new_details = f'{team_to_edit.name} {team_to_edit.reg_date} {str(team_to_edit.grp_num)}'

        team.Team.update_rankings()
        print(f'Team Updated: {old_details} to {new_details}')
        logging.info(f'Team updated from {old_details} to {new_details}')
        log.insert(tk.END, f'Team Updated: {old_details} to {new_details}')

    except:
        logging.info(f'Team could not be found: {line[0]}')
        print('No such team found, please check for errors and re-enter team')

def clear():

    logging.info(f'Clearing all data...')

    team.Team.delete_all_teams()
    match.Match.delete_all_matches()
    team.Team.update_rankings()

    logging.info('Data successfully cleared')
        

            
            
