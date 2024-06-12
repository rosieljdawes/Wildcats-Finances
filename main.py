num_training_sessions = 48
num_beginners_sessions = 20
num_members = 40
grant = 2350
spon = 1000
eys_grant = 400
membership_fee = 50
sem_1_ice_fee_cost = 65
s1ifc = sem_1_ice_fee_cost
sem_2_ice_fee_cost = 75
s2ifc = sem_2_ice_fee_cost
beginners_session_fee = 5
buiha_nationals_fee_per_team = 500
buiha_league_fee_per_team = 100
match_fee_cost = 20
nationals_fees = 45
required_num_players = 11
num_matches_per_team = 5
num_teams = 2

sem_1_ice_fee_paying_members = 31
sem_2_ice_fee_paying_members = 24

num_beginners = 15
num_members_paid_nationals_fees = 25

ice_hire = 120
ref_hire = 130
match_beers = 25
num_matches = num_teams * num_matches_per_team

sem_1_ice_fee = sem_1_ice_fee_paying_members * sem_1_ice_fee_cost
sem_2_ice_fee = sem_2_ice_fee_paying_members * sem_2_ice_fee_cost
players_ice_fees_income = sem_1_ice_fee + sem_2_ice_fee
beginners_income = num_beginners * beginners_session_fee * (num_beginners_sessions - 6)
annual_ice_fees_income = players_ice_fees_income + beginners_income
nationals_income = num_members_paid_nationals_fees * nationals_fees
membership_income = num_members * membership_fee
match_fees_income = (required_num_players * match_fee_cost) * num_matches
training_cost = num_training_sessions * ice_hire
beginners_costs = num_beginners_sessions * ice_hire
match_costs = ((ice_hire * 2) + ref_hire + match_beers) * num_matches
buiha_costs = buiha_league_fee_per_team * num_teams
nationals_costs = buiha_nationals_fee_per_team * num_teams

money_in = (
    grant 
    + eys_grant
    + spon 
    + membership_income 
    + nationals_income
    + annual_ice_fees_income
    + match_fees_income
)

money_out = (
    training_cost 
    + beginners_costs
    + match_costs
    + nationals_costs
    + buiha_costs
)



# Print the result
print(f"Beginners Income: £{beginners_income}")
print(f"Beginners Cost: £{beginners_costs}") 
print(f"Training Income: £{players_ice_fees_income}")
print(f"Training Cost: £{training_cost}")
print(f"Membership Income: £{membership_income}")  
print(f"Money In: £{money_in}")
print(f"Money out: £{money_out}")
