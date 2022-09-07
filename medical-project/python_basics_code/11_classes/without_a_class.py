import datetime


def get_age(player):
    now = datetime.datetime.now()
    return now.year - player['birth_year']

def get_average_score(player):
    return sum(player['scores'])/len(player['scores'])


virat = {
   'first_name': 'virat',
   'last_name': 'kohli',
   'scores': [],
   'birth_year': 1988
}


virat['scores'].append(80)
virat['scores'].append(100)
virat['scores'].append(0)


print(get_age(virat))
print(get_average_score(virat))

david = {
   'first_name': 'david',
   'last_name': 'warner',
   'scores': [],
   'birth_year': 1986
}

david['scores'].append(35)
david['scores'].append(120)
david['scores'].append(12)

print(get_age(david))
print(get_average_score(david))