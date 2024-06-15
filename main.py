from utils import model_2024
import matplotlib.pyplot as plt
import numpy


# --------------------DICTIONARIES---------------------#
num_members = 50
fixed_variables = {
    "Ice hire": 120,
    "BUIHA league fee per team": 100,
    "BUIHA affiliation fee": 50,
    "BUIHA nationals fee per team": 500,
    "Match beers": 25,
    "Number of matches per team": 5,
}

modifiable_variables = {
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


# -----FOR LOOP-----#
num_members_list = []
profit_list = []
for num_members in range(40, 150):
    for i in range(5):
        dropoff_rates = {
        "Member to player dropoff rate": int(numpy.random.normal(31, 5)) / int(numpy.random.normal(69, 5)),
        "Semester 1 to semester 2 dropoff rate": int(numpy.random.normal(24, 5)) / int(numpy.random.normal(31, 5)),
        "Semester 1 beginner to training rate": int(numpy.random.normal(2, 2)) / int(numpy.random.normal(69, 5)),
        "Semester 2 beginner to training rate": int(numpy.random.normal(5, 3)) / int(numpy.random.normal(69, 5)),
        "Member to nationals rate": int(numpy.random.normal(24, 5)) / int(numpy.random.normal(69, 5)),
        }

        random_variables = {
        "Grants": int(numpy.random.normal(3700, 200)),
        "Number of players in a match": int(numpy.random.normal(12, 2)),
        "Ref hire": int(numpy.random.normal(115, 10)),
        "Number of training sessions": int(numpy.random.normal(62, 3)),
        }

        profit = model_2024(
            num_members,
            fixed_variables,
            modifiable_variables,
            random_variables,
            dropoff_rates,
        )
        num_members_list.append(num_members)
        profit_list.append(profit)
    

# ------PLOT GRAPH------#

plt.plot(num_members_list, profit_list, '.')
plt.title("How number of members affects club profits")
plt.xlabel("Number of members")
plt.ylabel("Profit")
plt.show()
