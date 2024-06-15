
def model_2024(num_members, fixed_variables, modifiable_variables, random_variables, dropoff_rates):
    """takes in  3 dictionaries containing 1) fixed_variables 2) controllable variables and 3) the dropoff rates
    and returns money_in, money_out and num_members_needed (to breake even)"""

    """dropoff rates calcualations"""
    sem_1_ice_fee_paying_members = (
        dropoff_rates["Member to player dropoff rate"]
        * num_members
    )
    sem_2_ice_fee_paying_members = (
        sem_1_ice_fee_paying_members
        * dropoff_rates["Semester 1 to semester 2 dropoff rate"]
    )

    beginners_paying_sem_1_beg_ice_fee = (
        dropoff_rates["Semester 1 beginner to training rate"]
        * num_members
    )
    beginners_paying_sem_2_beg_ice_fee = (
        dropoff_rates["Semester 2 beginner to training rate"]
        * num_members
    )

    num_members_paid_nationals_fees = (
        dropoff_rates["Member to nationals rate"]
        * num_members
    )

    """money in calculations"""

    money_in = (
        num_members
        * (
            modifiable_variables["Membership fee"]
            + (
                modifiable_variables["Semester 1 ice fee cost"]
                * dropoff_rates["Member to player dropoff rate"]
            )
            + (
                modifiable_variables["Beginners semester 1 ice fee cost"]
                * dropoff_rates["Semester 1 beginner to training rate"]
            )
            + (
                modifiable_variables["Semester 2 ice fee cost"]
                * dropoff_rates["Member to player dropoff rate"]
            )
            + (
                modifiable_variables["Beginners semester 2 ice fee cost"]
                * dropoff_rates["Semester 2 beginner to training rate"]
            )
            + modifiable_variables["Nationals fees cost"]
            * dropoff_rates["Member to nationals rate"]
        )
        + random_variables["Grants"]
        + (
            fixed_variables["Number of matches per team"]
            * modifiable_variables["Number of teams"]
            * modifiable_variables["Match fee cost"]
            * random_variables["Number of players in a match"]
        )
    )
    #print(f"Money in: £{money_in}")

    """money out calculations"""
    money_out = (
        fixed_variables["Ice hire"]
        * (
            random_variables["Number of training sessions"]
            + modifiable_variables["Number of beginners sessions"]
        )
        + fixed_variables["Number of matches per team"]
        * modifiable_variables["Number of teams"]
        * (random_variables["Ref hire"] + 2 * fixed_variables["Ice hire"] + fixed_variables["Match beers"])
        + fixed_variables["BUIHA affiliation fee"]
        + modifiable_variables["Number of teams"]
        * (fixed_variables["BUIHA league fee per team"] + fixed_variables["BUIHA nationals fee per team"])
    )
    #print(f"Money out: £{money_out}")

    """number of members needed calculations"""

    # num_members_needed = (
    #     money_out
    #     - (
    #         fixed_variables["Number of matches per team"]
    #         * modifiable_variables["Number of teams"]
    #         * modifiable_variables["Match fee cost"]
    #         * random_variables["Number of players in a match"]
    #     )
    #     - random_variables["Grants"]
    # ) / (
    #     (
    #         modifiable_variables["Membership fee"]
    #         + (
    #             modifiable_variables["Semester 1 ice fee cost"]
    #             * dropoff_rates["Member to player dropoff rate"]
    #         )
    #         + (
    #             modifiable_variables["Beginners semester 1 ice fee cost"]
    #             * dropoff_rates["Semester 1 beginner to training rate"]
    #         )
    #         + (
    #             modifiable_variables["Semester 2 ice fee cost"]
    #             * dropoff_rates["Member to player dropoff rate"]
    #         )
    #         + (
    #             modifiable_variables["Beginners semester 2 ice fee cost"]
    #             * dropoff_rates["Semester 2 beginner to training rate"]
    #         )
    #         + modifiable_variables["Nationals fees cost"]
    #         * dropoff_rates["Member to nationals rate"]
    #     )
    # )
    #print(f"Number of members needed to break even: {num_members_needed}")

    return money_in - money_out
