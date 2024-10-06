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

        Team.__teams.append(self)
        if grp_num not in Team.__groups:
            Team.__groups[grp_num] = list()
        
        Team.__groups[grp_num].append(self)

    def add_match(self, match):
        self.matches.append(match)
        if match.team_1 == self.name:
            self.goals += match.goals_1
            if match.goals_1 > match.goals_2:
                self.wins += 1
            elif match.goals_1 < match.goals_2:
                self.losses += 1
            else: 
                self.draws += 1            
        else:
            self.goals += match.goals_2
            if match.goals_2 > match.goals_1:
                self.wins += 1
            elif match.goals_2 < match.goals_1:
                self.losses += 1
            else: 
                self.draws += 1   

    def update_score(self):
        self.score = self.wins * 3 + self.draws * 1 + self.losses * 0
        self.alt_score = self.wins * 5 + self.draws * 3 + self.losses * 1

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

