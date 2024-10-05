class Team:
    def __init__(self, name, reg_date, grp_num):
        self.name = name
        self.reg_date = reg_date
        self.grp_num = grp_num
        self.matches = list()
        self.wins = 0
        self.losses = 0
        self.draws = 0
        self.goals = 0

    def add_match(self, match):
        self.matches.append(match)
        if match.team_1 == self:
            self.goals = match.goals_1
            if match.goals_1 > match.goals_2:
                self.wins += 1
            elif match.goals_1 < match.goals_2:
                self.losses += 1
            else: 
                self.draws += 1            
        else:
            self.goals = match.goals_2
            if match.goals_2 > match.goals_1:
                self.wins += 1
            elif match.goals_2 < match.goals_1:
                self.losses += 1
            else: 
                self.draws += 1   

