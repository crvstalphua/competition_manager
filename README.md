# Competition Manager

This application allows users to keep track of the results from a competition. Users will be able to add and edit teams and match details, their rankings and qualifications in the competition can then be displayed.

Teams can be added, with their name, registration date and competition group number (such that groups in the same team go against each other). Matches can be added, involving two teams and their respective scores.

## Requirements
- Python 3.6 or higher
- If on Linux, Tkinter to be installed with:  ```sudo apt-get install python3-tk```

## To Run Application:
1. Clone the responsitory and navigate to your directory
    ```
    git clone https://github.com/crvstalphua/competition_manager.git
    cd competition manager
    ```

2. Run the application with ```python main.py``` or ```python3 main.py``` if you have multiple versions of python

## Usage Notes
- Multiple teams and matches can be added in one input
- Only one team and match can be edited in one go

## Some Assumptions Made
- Team names cannot be edited as they are used to identify the teams
- If any team/match input is invalid in the multi-line input, it will be skipped. This application allows for teams and matches to be added at any point, not just in the first round
- Each team can only go against another team once (e.g. Team1 vs Team2 is the same as Team2 vs Team1)
- Teams can only go against other teams from the same group
- If there are less than four teams in a group, all teams are considered to have qualified
