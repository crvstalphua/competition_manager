from datetime import datetime

class Team:
    __teams = list()
    __groups = dict()

    def __init__(self, name, reg_date, grp_num):
        self.name = name
        self.reg_date = reg_date
        self.grp_num = grp_num
        self.matches = list()
        self.wins = 0
        self.losses = 0
        self.draws = 0
        self.goals = 0
        self.score = 0
        self.alt_score = 0
        self.rank = 0

        Team.__teams.append(self)
        if grp_num not in Team.__groups:
            Team.__groups[grp_num] = list()
        
        Team.__groups[grp_num].append(self)

    def add_match(self, match):
        self.matches.append(match)
        goals, result = match.get_result(self)
        self.goals += goals
        if result == 0:
            self.draws += 1
        elif result == 1:
            self.wins += 1
        else:
            self.losses += 1
        self.update_score()

    def remove_match(self, match):
        self.matches.remove(match)
        goals, result = match.get_result(self)
        self.goals -= goals
        if result == 0:
            self.draws -= 1
        elif result == 1:
            self.wins -= 1
        else:
            self.losses -= 1
        self.update_score()

    # calculate and update score and alternate score of a team
    def update_score(self):
        self.score = self.wins * 3 + self.draws * 1 + self.losses * 0
        self.alt_score = self.wins * 5 + self.draws * 3 + self.losses * 1

    def edit_team(self, name, reg_date, grp_num):
        self.reg_date = reg_date
        if self.grp_num != grp_num:
            if grp_num not in Team.__groups:
                Team.__groups[grp_num] = list()
            Team.__groups[self.grp_num].remove(self)
            Team.__groups[grp_num].append(self)
            self.grp_num = grp_num

    # based on group number, sort the teams based on the the given criteria to obtain the qualification rankings
    @classmethod
    def update_rankings(cls):
        ordered_grps = dict(sorted(Team.get_groups().items()))
        for grps, teams in ordered_grps.items():
            ordered_teams = sorted(teams, key = lambda x: (-x.score, -x.goals, -x.alt_score, datetime.strptime(x.reg_date, "%d/%m")))
            cls.__groups[grps] = ordered_teams
            for x in range(len(ordered_teams)):
                    ordered_teams[x].rank = x + 1

    @classmethod
    def get_teams(cls):
        return cls.__teams
    
    @classmethod
    def get_team(cls, name):
        for team in cls.__teams:
            if team.name == name:
                return team

    @classmethod
    def get_groups(cls):
        return cls.__groups
    
    # obtain team name, registration date, group number, matches played and qualification outcome of specified team
    @classmethod
    def get_team_details(cls, name):
        team = Team.get_team(name)
        if team.rank > 4:
            outcome = 'Did not qualify'
        elif 0 < team.rank <= 4: 
            outcome = 'Qualified'
        matches = ''
        for match in team.matches:
            matches += f'- {match.get_match_details()} \n'
        return f'Team name: {team.name} \nRegistration date: {team.reg_date} \nGroup number: {str(team.grp_num)} \nMatches played: \n{matches}Outcome: {outcome}'

    @classmethod
    def delete_all_teams(cls):
        teams = cls.get_teams()
        teams.clear()
        groups = cls.get_groups()
        groups.clear()

    @classmethod
    def delete_all_team_matches(cls):
        teams = cls.get_teams()
        for t in teams:
            t.matches.clear()
            t.rank = 0
