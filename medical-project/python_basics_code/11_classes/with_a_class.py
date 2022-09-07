import datetime


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

    def __str__(self):
        return f'{self.first_name} {self.last_name}, the cricket player from {self.team}'

    def __lt__(self, other):
        my_score = self.get_average_score()
        other_score = other.get_average_score()
        return my_score < other_score

virat = CricketPlayer('virat', 'kohli', 'india', 1988)
virat.add_score(37)
virat.add_score(23)
virat.add_score(85)

print(virat)
print(virat.get_age())
print(virat.get_average_score())

david = CricketPlayer('david','warner','australia', 1985)
david.add_score(37)
david.add_score(23)
david.add_score(85)

print(david)
print(david.get_average_score())
print(virat<david)

