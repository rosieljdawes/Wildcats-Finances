from utils import model_2024

# --------------------DICTIONARIES---------------------#
fixed_variables = {
    "Ice hire": 120,
    "BUIHA league fee per team": 100,
    "BUIHA affiliation fee": 50,
    "BUIHA nationals fee per team": 500,
    "Match beers": 25,
    "Ref hire": 130,
    "Number of matches per team": 5,
}

modifiable_variables = {
    "Number of training sessions": 62,
    "Number of beginners sessions": 20,
    "Membership fee": 50,
    "Semester 1 ice fee cost": 65,
    "Semester 2 ice fee cost": 75,
    "Beginners semester 1 ice fee cost": 25,
    "Beginners semester 2 ice fee cost": 35,
    "Match fee cost": 20,
    "Number of teams": 2,
    "Nationals fees cost": 45,
}

random_variables = {
    "Grants": 3750,
    "Number of members": 69,
    "Number of players in a match": 11,
}

dropoff_rates = {
    "Member to player dropoff rate": 31 / 69,
    "Semester 1 to semester 2 dropoff rate": 24 / 31,
    "Semester 1 beginner to training rate": 2 / 69,
    "Semester 2 beginner to training rate": 5 / 69,
    "Member to nationals rate": 24 / 69,
}

model_2024(fixed_variables, modifiable_variables, random_variables,dropoff_rates)
