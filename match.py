class Match:
    __matches = list()

    def __init__(self, team_1, team_2, goals_1, goals_2):
        self.team_1 = team_1
        self.team_2 = team_2
        self.goals_1 = goals_1
        self.goals_2 = goals_2
        
        Match.__matches.append(self)
    
    @classmethod
    def get_matches(cls):
        return cls.__matches
    
    @classmethod
    def get_match(cls, team_1, team_2):
        for match in cls.__matches:
            if match.team_1 == team_1 and match.team_2 == team_2:
                return match
            elif match.team_2 == team_1 and match.team_1 == team_2:
                return match
    
    def get_match_details(self):
        return self.team_1 + ' ' + self.team_2 + ' ' + str(self.goals_1) + ' ' + str(self.goals_2)