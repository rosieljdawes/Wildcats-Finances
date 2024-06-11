##------- INDEPENDENT VARIABLES -------- ###

num_training_sessions = 62
num_beginners_sessions = 20
num_members = 69
grants = 3350 #incl. spon
# equipment_grant = 500 (remove completely as it should be added to the grants variable)
eys_grant = 400 # kept seperate 
membership_fee = 50
sem_1_ice_fee_cost = 65
sem_2_ice_fee_cost = 75
beginners_sem_1_ice_fee_cost = 25
beginners_sem_2_ice_fee_cost = 35



member_to_player_dropoff_rate = 31 / 69
sem1_to_sem2_dropoff_rate = 24 / 31
sem_1_beginner_to_training_rate = 2 / 69
sem_2_beginner_to_training_rate = 5 / 69
member_to_nationals_rate = 24 / 69

### -------- DEPENDENT VARIABLES -------- ###

sem_1_ice_fee_paying_members = member_to_player_dropoff_rate * num_members
sem_2_ice_fee_paying_members = sem_1_ice_fee_paying_members * sem1_to_sem2_dropoff_rate

beginners_paying_sem_1_beg_ice_fee = sem_1_beginner_to_training_rate * num_members
beginners_paying_sem_2_beg_ice_fee = sem_2_beginner_to_training_rate * num_members

num_members_paid_nationals_fees = member_to_nationals_rate * num_members

### --------- DEFINED VARIABLES ---------- ###

ice_hire = 120
num_teams = 2
buiha_league_fee_per_team = 100
buiha_aff_fee = 50
num_matches_per_team = 5
buiha_nationals_fee_per_team = 500
match_fee_cost = 20
nationals_fees = 45
initial_funds = 3200
match_beers = 25
starting_money = 0



### - PROBABILITY-DISTRIBUTED VARIABLES - ###
ref_hire = 130
# misc_costs = 100
required_num_players = 11

# --------CALCULATIONS-----------#
# Based on num_members = 69

money_in = (
    num_members
    * (
        membership_fee
        + (sem_1_ice_fee_cost * member_to_player_dropoff_rate)
        + (beginners_sem_1_ice_fee_cost * sem_1_beginner_to_training_rate)
        + (sem_2_ice_fee_cost * member_to_player_dropoff_rate)
        + (beginners_sem_2_ice_fee_cost * sem_2_beginner_to_training_rate)
        + nationals_fees * member_to_nationals_rate
    ) + grants
    + eys_grant
    + (num_matches_per_team * num_teams * match_fee_cost * required_num_players)
)

money_out = (
    ice_hire * (num_training_sessions + num_beginners_sessions)
    + num_matches_per_team * num_teams * (ref_hire + 2 * ice_hire + match_beers)
    + buiha_aff_fee
    + num_teams * (buiha_league_fee_per_team + buiha_nationals_fee_per_team)
)

# Now calculating based on money_in = money_out
num_members = (
    money_out
    - (num_matches_per_team * num_teams * match_fee_cost * required_num_players)
    - grants
    - eys_grant
) / (
    (
        membership_fee
        + (sem_1_ice_fee_cost * member_to_player_dropoff_rate)
        + (beginners_sem_1_ice_fee_cost * sem_1_beginner_to_training_rate)
        + (sem_2_ice_fee_cost * member_to_player_dropoff_rate)
        + (beginners_sem_2_ice_fee_cost * sem_2_beginner_to_training_rate)
        + nationals_fees * member_to_nationals_rate
    )
)


# --------RESULTS----------#

print(f"money_in = {money_in}")
print(f"money_out = {money_out}")
print(f"Number of members = {num_members}")



