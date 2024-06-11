##------- INDEPENDENT VARIABLES -------- ###

num_training_sessions = 62
num_beginners_sessions = 20
num_members = 40
grant = 2350
spon = 1000
# equipment_grant = 500
eys_grant = 400
membership_fee = 50
sem_1_ice_fee_cost = 65
s1ifc = sem_1_ice_fee_cost
sem_2_ice_fee_cost = 75
s2ifc = sem_2_ice_fee_cost
beginners_fee = 10
num_beginners = 30



member_to_player_dropoff_rate = 24 / 69
sem1_to_sem2_dropoff_rate = 17 / 24
player_to_nationals_rate = 24 / 69

### -------- DEPENDENT VARIABLES -------- ###

sem_1_ice_fee_paying_members = member_to_player_dropoff_rate * num_members
s1ifpm = sem_1_ice_fee_paying_members
sem_2_ice_fee_paying_members = sem_1_ice_fee_paying_members * sem1_to_sem2_dropoff_rate
s2ifpm = sem_2_ice_fee_paying_members

beginners_income = num_beginners * beginners_fee * (num_beginners_sessions - 6)

num_members_paid_nationals_fees = player_to_nationals_rate * num_members

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
num_matches = num_teams * num_matches_per_team
match_beers = 25
starting_money = 0
### - PROBABILITY-DISTRIBUTED VARIABLES - ###
ref_hire = 130
# misc_costs = 100
required_num_players = 11

# --------CALCULATIONS-----------#

x_in_1 = (
    num_members
    * (
        membership_fee
        + (sem_1_ice_fee_cost * member_to_player_dropoff_rate)
        + (sem_2_ice_fee_cost * member_to_player_dropoff_rate)
        + nationals_fees * player_to_nationals_rate
    )
    + beginners_income
    + grant
    + spon
 #   + equipment_grant
    + eys_grant
    + (num_matches * match_fee_cost * required_num_players)
)

x_out = (
    ice_hire * (num_training_sessions + num_beginners_sessions)
    + num_matches * (ref_hire + 2 * ice_hire + match_beers)
    + buiha_aff_fee
    + num_teams * (buiha_league_fee_per_team + buiha_nationals_fee_per_team)
)

num_members = (
    x_out
    - starting_money
    - beginners_income
    - grant
    - spon
    - eys_grant
#    - equipment_grant
    - (num_matches * match_fee_cost * required_num_players)
) / (
    (
        membership_fee
        + (sem_1_ice_fee_cost * member_to_player_dropoff_rate)
        + (sem_2_ice_fee_cost * member_to_player_dropoff_rate)
        + nationals_fees * player_to_nationals_rate
    )
)


# --------RESULTS----------#

print(f"x_in = {x_in_1}")
print(f"x_out = {x_out}")
print(f"Number of members = {num_members}")
