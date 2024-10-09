import team

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
    
    def get_result(self, team):
        if team.name == self.team_1:
            if self.goals_1 > self.goals_2:
                return self.goals_1, 1
            elif self.goals_1 < self.goals_2:
                return self.goals_1, -1
            else:
                return self.goals_1, 0
        elif team.name == self.team_2:
            if self.goals_2 > self.goals_1:
                return self.goals_2, 1
            elif self.goals_2 < self.goals_1:
                return self.goals_2, -1
            else:
                return self.goals_2, 0
    
    @classmethod
    def delete_match(cls, match):
        cls.__matches.remove(match)
        
    def get_match_details(self):
        return self.team_1 + ' ' + self.team_2 + ' ' + str(self.goals_1) + ' ' + str(self.goals_2)

    @classmethod
    def delete_all_matches(cls):
        matches = cls.get_matches()
        team.Team.delete_all_team_matches()
        matches.clear()