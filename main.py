from functions import input_teams, input_matches, display_rankings, display_team, edit_match, edit_team, clear
import logging

logging.basicConfig(filename='comp_manager.log', level=logging.INFO, format='%(asctime)s %(message)s', filemode='w')

def main():
    input_teams()
    input_matches()
    display_rankings()
    display_team()
    edit_match()
    edit_team()
    display_rankings()
    clear()
    display_team()
    display_rankings()

    
if __name__ == '__main__':
    main()