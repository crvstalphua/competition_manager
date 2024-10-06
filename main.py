from functions import input_teams, input_matches, display_rankings, display_team, edit_match, edit_team, clear
import team

def main():
    input_teams()
    input_matches()
    display_rankings()
    display_team()
    edit_match()
    edit_team()
    display_rankings()
    clear()
    display_rankings()

    
if __name__ == '__main__':
    main()