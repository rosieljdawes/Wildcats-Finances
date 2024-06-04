# variables:
# both variables:
num_members = 71 # certain
matches_per_year_per_team = 5 # certain
mpypt = matches_per_year_per_team
# money in variables:
sem_1_ice_fee_paying_members = 26 # unsure
s1ifpm = sem_1_ice_fee_paying_members
sem_2_ice_fee_paying_members = 29 # unsure
s2ifpm = sem_2_ice_fee_paying_members
players = 11 # average from this year- get stats
membership_fee = 50 # certain
sem_1_ice_fee_cost = 65 # certain
s1ifc = sem_1_ice_fee_cost
sem_2_ice_fee_cost = 75 # certain
s2ifc = sem_2_ice_fee_cost
beginners_sem_1_ice_fee_cost = 25 # certain
bs1ifc = beginners_sem_1_ice_fee_cost
beginners_sem_2_ice_fee_cost = 35 # certain
bs2ifc = beginners_sem_2_ice_fee_cost
beginners_paying_sem_1_beg_ice_fee = 2 # unsure
bps1bif = beginners_paying_sem_1_beg_ice_fee
beginners_paying_sem_2_beg_ice_fee = 2 # unsure
bps2bif = beginners_paying_sem_2_beg_ice_fee
grant = 2350 # unsure
spon = 0 # for these purposes, set at zero
match_fee_cost = 20 # certain
# percent_of_members_pay_ice_fees = (s1ifpm + s2ifpm) / num_members
# pompif = percent_of_members_pay_ice_fees

# money out variables:
num_training_sessions = 40 # also a guess
ice_hire = 120 # certai
ref_hire = 130 # 90-140
num_beginners_sessions = 20 #also unsure by a bit
num_teams = 2 #certain
buiha_fee = 100 # certain
buiha_aff_fee = 50 # certain



#--------------------------------------------------------------------

membership_income = num_members * membership_fee
buiha_fees = buiha_fee * num_teams
sem_1_ice_fee = sem_1_ice_fee_paying_members * sem_1_ice_fee_cost
sem_2_ice_fee = sem_2_ice_fee_paying_members * sem_2_ice_fee_cost
players_ice_fees = sem_1_ice_fee + sem_2_ice_fee
sem_1_beg_ice_fee = bps1bif * beginners_sem_1_ice_fee_cost
sem_2_beg_ice_fee = bps2bif * beginners_sem_2_ice_fee_cost
beginners_fees = sem_1_beg_ice_fee + sem_2_beg_ice_fee
annual_ice_fees = players_ice_fees + beginners_fees
num_matches = num_teams * mpypt
match_fees_income = (players * match_fee_cost) * num_matches
training_cost = num_training_sessions * ice_hire
match_cost = (ref_hire + (ice_hire * 2)) * num_matches
beginners_costs = num_beginners_sessions * ice_hire
buiha_costs = buiha_aff_fee + (buiha_fee * num_teams)


x_in = membership_income + grant + spon + annual_ice_fees + match_fees_income
x_out = training_cost + match_cost + beginners_costs + buiha_costs


print(int(x_in - x_out))







