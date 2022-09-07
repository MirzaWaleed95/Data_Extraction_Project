import datetime


class TennisPlayer:
    def __init__(self, fname, lname, birth_year, gwinner):
        self.first_name = fname
        self.last_name = lname
        self.birth_year = birth_year
        self.grand_slam_winner = gwinner
        self.aces = []

    def get_age(self):
        now = datetime.datetime.now()
        return now.year - self.birth_year

    def get_average_aces_per_match(self):
        return sum(self.aces)/len(self.aces)


class CricketPlayer:
    def __init__(self, fname, lname, team, birth_year):
        self.first_name = fname
        self.last_name = lname
        self.birth_year = birth_year
        self.team = team
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)

    def get_average_score(self):
        return sum(self.scores)/len(self.scores)

    def get_age(self):
        now = datetime.datetime.now()
        return now.year - self.birth_year


virat = CricketPlayer('virat', 'kohli', 'india', 1988)
virat.add_score(37)
virat.add_score(23)
virat.add_score(85)

print("Age of viral kohli:", virat.get_age())
print("Average score of viral kohli:", virat.get_average_score())

roger = TennisPlayer('roger','federer',1981, 20)
print("Age of roger federer:",roger.get_age())


