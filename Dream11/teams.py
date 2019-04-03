from itertools import permutations,combinations

class GenerateDummyTeams:

    def __init__(self, apponents, team_A, team_B, _cnumber, _lnumber):
        self.apponents = apponents
        self.team_A = team_A
        self.team_B = team_B
        self._cnumber = _cnumber
        self._lnumber = _lnumber

    def getApponents(self):
        return self.apponents

    def getCompul(self):
        return self._cnumber

    def getLeast(self):
        return self._lnumber

    def countCompulsary(self, players_iter):
        team1_count=0
        team2_count =0
        # print('\nPlayers_Set:',players_iter)
        for i, j in enumerate(list(players_iter)):
            # print(j)
            if j[1] == self.apponents[0]:
                team1_count = team1_count + 1
            else:
                team2_count = team2_count + 1
            # print(team1_count,team2_count)
        if team1_count >= self._lnumber and team2_count >= self._lnumber:
            if team2_count + team2_count == self._cnumber and len(list(dict.fromkeys(players_iter)))>=_cnumber:
                return list(dict.fromkeys(players_iter))
            else:
                return None

    def getTeamBatsman(self, team_name):
        batsman = team_name
        print('\nBatsman are:', batsman)
        return batsman

    def getTeamBowlers(self, team_name):
        bowlers = team_name
        print('\nBowlers are:', bowlers)
        return bowlers

    def getAllBatsman(self):
        batsman_team_A = self.getTeamBatsman(self, team_A)
        batsman_team_B = self.getTeamBatsman(self, team_B)
        batmans_List = batsman_team_A + batsman_team_B
        return batmans_List

    def getAllBowlers(self):
        bowlers_team_A = self.getTeamBowlers(self, team_A)
        bowlers_team_B = self.getTeamBowlers(self, team_B)
        bowlers_List = bowlers_team_A + bowlers_team_B
        return bowlers_List

    def getTeamAllRounders(self, team_name):
        allRounders = team_name
        return allRounders

    def getAllRounders(self):
        all_rounders_team_A = self.getTeamAllRounders(self, team_A)
        all_rounders_team_B = self.getTeamAllRounders(self, team_B)
        all_rounders_List = all_rounders_team_A + all_rounders_team_B
        return all_rounders_List

    def getTeamKeeper(self, team_name):
        keeper = team_name
        return keeper

    def getAllKeepers(self):
        keeper_Team_A = self.getTeamKeeper(self, team_A)
        keeper_Team_B = self.getTeamKeeper(self, team_B)
        all_keepers = keeper_Team_A + keeper_Team_B
        return all_keepers

    def getPlayerType(self, team_name, player_type):
        # print('\nPlayer Type is:', player_type)
        def batsman():
            return self.getTeamBatsman(team_name)

        def bowlers():
            return self.getTeamBowlers(team_name)

        def allRounders():
            return self.getTeamAllRounders(team_name)

        def keeper():
            return self.getTeamKeeper(team_name)

        switcher = {
            'batsman': batsman,
            'bowlers': bowlers,
            'allRounder': allRounders,
            'keeper': keeper(),

        }
        func = switcher.get(player_type, lambda: 'Invalid Player Type')
        return func()

    def generateImpSingleTeamPlayers(self, team_name, player_type):
        imp_player_List = self.getPlayerType(team_name,player_type)
        # print('\nImp Players List:',imp_player_List)
        for comb in enumerate(imp_player_List):
            print(comb)

    def generateImpBothTeamPlayers(self, team_name1, team_name2, player_type):
        player_List_A = player_List_B = []
        # print(team_name1, team_name2)
        player_List1 = self.getPlayerType(team_name1, player_type)
        for player in player_List1:
             player_List_A.append((player, apponents[0]))

        # print("\nset:", player_List_A)
        player_List2 = self.getPlayerType(team_name2, player_type)
        for player in player_List2:
            player_List_A.append((player, apponents[1]))

        print("\nset:", player_List_B)

        imp_player_List = player_List_A + player_List_B
        teamList = set(combinations(imp_player_List, self._cnumber))
        print('\nImp Players List:',imp_player_List)
        # print('\nImp Team List:')
        for i, comb in enumerate(teamList):
            matched = self.countCompulsary(comb)
            if matched:
                print(i, sorted(matched, reverse=True, key=lambda x: x[1]))
                print("\n")


if __name__ == "__main__":

    apponents = ['Ind', 'Aus']
    _cnumber = 4
    _lnumber = 2

    team_A = ['Rohit Sharma', ' Shikhar Dhawan', ' Virat Kohli(c)', ' Lokesh Rahul', ' Rishabh Pant' ]

    team_A_All = ['Rohit Sharma', ' Shikhar Dhawan', ' Virat Kohli(c)', ' Lokesh Rahul', ' Rishabh Pant',
              ' Dinesh Karthik', ' MS Dhoni', ' Krunal Pandya', ' Vijay Shankar', ' Siddarth Kaul',
              'Umesh Yadav', ' Jasprit Bumrah', ' Yuzvendra Chahal', ' Mayank Markande']


    team_B = ['Aaron Finch(c)', ' Alex Carey', ' Usman Khawaja', ' Shaun Marsh', ' D Arcy Short']

    team_B_All = ['Aaron Finch(c)', ' Alex Carey', ' Usman Khawaja', ' Shaun Marsh', ' D Arcy Short',
              ' Marcus Stoinis', ' Pat Cummins', ' Glenn Maxwell', ' Jhye Richardson', ' Kane Richardson',
              ' Nathan Coulter-Nile', ' Peter Handscomb', ' Jason Behrendorff', ' Nathan Lyon', ' Ashton Turner',
              ' Adam Zampa']

    myTeam=GenerateDummyTeams(apponents, team_A, team_B, _cnumber, _lnumber)
    # myTeam.generateImpSingleTeamPlayers(team_B , 'batsman') #for single Team
    myTeam.generateImpBothTeamPlayers(team_A,team_B,'bowlers') # for mutiple Team














