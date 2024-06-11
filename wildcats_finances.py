### ------- INDEPENDENT VARIABLES -------- ###

num_training_sessions = 48
num_beginners_sessions = 20
num_members = 40
grant = 2350
spon = 1000
membership_fee = 50
sem_1_ice_fee_cost = 65
s1ifc = sem_1_ice_fee_cost
sem_2_ice_fee_cost = 75
s2ifc = sem_2_ice_fee_cost
beginners_session_fee = 5
buiha_nationals_fee_per_team = 500
match_fee_cost = 20
nationals_fees = 45

sem_1_ice_fee_paying_members = 31
sem_2_ice_fee_paying_members = 24

num_beginners = 15
num_members_paid_nationals_fees = 25

ice_hire = 120
num_teams = 2
buiha_league_fee_per_team = 100
buiha_aff_fee = 50
match_beers = 25
num_matches_per_team = 5
nationals_cost = buiha_nationals_fee_per_team * num_teams
initial_funds = 3200

ref_hire = 130  # 90-140
required_num_players = 11

### ----------- MATHS ----------- ###
num_matches = num_teams * num_matches_per_team
membership_income = num_members * membership_fee
sem_1_ice_fee = sem_1_ice_fee_paying_members * sem_1_ice_fee_cost
sem_2_ice_fee = sem_2_ice_fee_paying_members * sem_2_ice_fee_cost
players_ice_fees = sem_1_ice_fee + sem_2_ice_fee
beginners_income = num_beginners * beginners_session_fee * (num_beginners_sessions - 6)
annual_ice_fees = players_ice_fees + beginners_income
match_fees_income = (required_num_players * match_fee_cost) * num_matches
training_cost = num_training_sessions * ice_hire
beginners_costs = num_beginners_sessions * ice_hire
buiha_costs = buiha_aff_fee + (buiha_league_fee_per_team * num_teams)
match_cost = (ref_hire + match_beers + (ice_hire * 2)) * num_matches
nationals_income = nationals_fees * num_members_paid_nationals_fees
starting_money = 4000

#--------EQUATION------------#
money_in = (
    membership_income
    + grant
    + spon
    + annual_ice_fees
    + match_fees_income
    + nationals_income
    + beginners_income
)
money_out = (
    training_cost 
    + match_cost 
    + beginners_costs 
    + buiha_costs 
    + nationals_cost
)

leftover_money = starting_money + money_in - money_out
extra_money = leftover_money - starting_money

# Print the result

print(f"Money In: {money_in}")  
print(f"Money Out: {money_out}")  
print(f"Leftover Money: {leftover_money}")
print(f"Extra Money: {extra_money}")
print("---------------------")
print("Money In:")
print(f"Membership Income: {membership_income}")
print(f"Grant: {grant}")
print(f"Spon: {spon}")
print(f"Annual Ice Fee Income: {annual_ice_fees}")
print(f"Match Fees Income: {match_fees_income}")
print(f"Nationals Income: {nationals_income}")
print("---------------------")
print("Money Out:")
print(f"Training Cost: {training_cost}")
print(f"Match Cost: {match_cost}")
print(f"Beginners Cost: {beginners_costs}")
print(f"BUIHA Costs: {buiha_costs}")
print(f"Nationals Cost: {nationals_cost}")
