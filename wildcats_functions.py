# --------------------DICTIONARIES---------------------#
# -----COSTS-----#
costs = {
    "Ice hire": 120,
    "BUIHA league fee per team": 100,
    "BUIHA affiliation fee": 50,
    "BUIHA nationals fee per team": 500,
    "Match beers": 25,
    "Ref hire": 130,
}

# -----CONTROLLABLE VARIABLES-----#
controllable_variables = {
    "Number of training sessions": 62,
    "Number of beginners sessions": 20,
    "Number of members": 69,
    "Grant and spon": 3350,
    "EYS grant": 400,
    "Membership fee": 50,
    "Semester 1 ice fee cost": 65,
    "Semester 2 ice fee cost": 75,
    "Beginners semester 1 ice fee cost": 25,
    "Beginners semester 2 ice fee cost": 35,
    "Nationals fees cost": 45,
    "Match fee cost": 20,
    "Initial funds": 3200,
    "Starting money": 0,
    "Number of players in a match": 11,
    "Number of matches per team": 5,
    "Number of teams": 2,
}

# -----DROP-OFF RATES-----#
dropoff_rates = {
    "Member to player dropoff rate": 31 / 69,
    "Semester 1 to semester 2 dropoff rate": 24 / 31,
    "Semester 1 beginner to training rate": 2 / 69,
    "Semester 2 beginner to training rate": 5 / 69,
    "Member to nationals rate": 24 / 69,
}


def model_2024(costs, controllable_variables, dropoff_rates):
    """takes in  3 dictionaries containing 1) costs 2) controllable variables and 3) the dropoff rates
    and returns money_in, money_out and num_members_needed (to breake even)"""

    """dropoff rates calcualations"""
    sem_1_ice_fee_paying_members = (
        dropoff_rates["Member to player dropoff rate"]
        * controllable_variables["Number of members"]
    )
    sem_2_ice_fee_paying_members = (
        sem_1_ice_fee_paying_members
        * dropoff_rates["Semester 1 to semester 2 dropoff rate"]
    )

    beginners_paying_sem_1_beg_ice_fee = (
        dropoff_rates["Semester 1 beginner to training rate"]
        * controllable_variables["Number of members"]
    )
    beginners_paying_sem_2_beg_ice_fee = (
        dropoff_rates["Semester 2 beginner to training rate"]
        * controllable_variables["Number of members"]
    )

    num_members_paid_nationals_fees = (
        dropoff_rates["Member to nationals rate"]
        * controllable_variables["Number of members"]
    )

    """money in calculations"""

    money_in = (
        controllable_variables["Number of members"]
        * (
            controllable_variables["Membership fee"]
            + (
                controllable_variables["Semester 1 ice fee cost"]
                * dropoff_rates["Member to player dropoff rate"]
            )
            + (
                controllable_variables["Beginners semester 1 ice fee cost"]
                * dropoff_rates["Semester 1 beginner to training rate"]
            )
            + (
                controllable_variables["Semester 2 ice fee cost"]
                * dropoff_rates["Member to player dropoff rate"]
            )
            + (
                controllable_variables["Beginners semester 2 ice fee cost"]
                * dropoff_rates["Semester 2 beginner to training rate"]
            )
            + controllable_variables["Nationals fees cost"]
            * dropoff_rates["Member to nationals rate"]
        )
        + controllable_variables["Grant and spon"]
        + controllable_variables["EYS grant"]
        + (
            controllable_variables["Number of matches per team"]
            * controllable_variables["Number of teams"]
            * controllable_variables["Match fee cost"]
            * controllable_variables["Number of players in a match"]
        )
    )
    print(f"Money in: £{money_in}")

    """money out calculations"""
    money_out = (
        costs["Ice hire"]
        * (
            controllable_variables["Number of training sessions"]
            + controllable_variables["Number of beginners sessions"]
        )
        + controllable_variables["Number of matches per team"]
        * controllable_variables["Number of teams"]
        * (costs["Ref hire"] + 2 * costs["Ice hire"] + costs["Match beers"])
        + costs["BUIHA affiliation fee"]
        + controllable_variables["Number of teams"]
        * (costs["BUIHA league fee per team"] + costs["BUIHA nationals fee per team"])
    )
    print(f"Money out: £{money_out}")

    """number of members needed calculations"""

    num_members = (
        money_out
        - (
            controllable_variables["Number of matches per team"]
            * controllable_variables["Number of teams"]
            * controllable_variables["Match fee cost"]
            * controllable_variables["Number of players in a match"]
        )
        - controllable_variables["Grant and spon"]
        - controllable_variables["EYS grant"]
    ) / (
        (
            controllable_variables["Membership fee"]
            + (
                controllable_variables["Semester 1 ice fee cost"]
                * dropoff_rates["Member to player dropoff rate"]
            )
            + (
                controllable_variables["Beginners semester 1 ice fee cost"]
                * dropoff_rates["Semester 1 beginner to training rate"]
            )
            + (
                controllable_variables["Semester 2 ice fee cost"]
                * dropoff_rates["Member to player dropoff rate"]
            )
            + (
                controllable_variables["Beginners semester 2 ice fee cost"]
                * dropoff_rates["Semester 2 beginner to training rate"]
            )
            + controllable_variables["Nationals fees cost"]
            * dropoff_rates["Member to nationals rate"]
        )
    )
    print(f"Number of members needed to break even: £{num_members}")


model_2024(costs, controllable_variables, dropoff_rates)
