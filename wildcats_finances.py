### ------- INDEPENDENT VARIABLES -------- ###

num_training_sessions = 40  # also a guess
num_beginners_sessions = 20  # also unsure by a bit
num_members = 69  # certain
grant = 2350  # unsure
spon = 1000  # for these purposes, set at zero
membership_fee = 50  # certain
sem_1_ice_fee_cost = 65  # certain
s1ifc = sem_1_ice_fee_cost
sem_2_ice_fee_cost = 75  # certain
s2ifc = sem_2_ice_fee_cost
beginners_sem_1_ice_fee_cost = 25  # certain
bs1ifc = beginners_sem_1_ice_fee_cost
beginners_sem_2_ice_fee_cost = 35  # certain
bs2ifc = beginners_sem_2_ice_fee_cost


member_to_player_dropoff_rate = 24 / 69  # sem_1_ice_fee_paying_members / num_members
sem1_to_sem2_dropoff_rate = (
    17 / 24
)  # sem_2_ice_fee_paying_members / sem_1_ice_fee_paying_members
sem_1_beginner_to_training_rate = 2 / 69  # bps1bif / num_members
sem_2_beginner_to_training_rate = 5 / 69  # bps2bif / num_members
player_to_nationals_rate = 24 / 69  # num_members_paid_nationals_fees / num_members

### -------- DEPENDENT VARIABLES -------- ###

sem_1_ice_fee_paying_members = member_to_player_dropoff_rate * num_members
s1ifpm = sem_1_ice_fee_paying_members
sem_2_ice_fee_paying_members = sem_1_ice_fee_paying_members * sem1_to_sem2_dropoff_rate
s2ifpm = sem_2_ice_fee_paying_members

beginners_paying_sem_1_beg_ice_fee = sem_1_beginner_to_training_rate * num_members
bps1bif = beginners_paying_sem_1_beg_ice_fee
beginners_paying_sem_2_beg_ice_fee = sem_2_beginner_to_training_rate * num_members
bps2bif = beginners_paying_sem_2_beg_ice_fee
num_members_paid_nationals_fees = player_to_nationals_rate * num_members

### --------- DEFINED VARIABLES ---------- ###

ice_hire = 120  # certain
num_teams = 2  # certain
buiha_fee = 100  # certain
buiha_aff_fee = 50  # certain
matches_per_year_per_team = 5  # certain
mpypt = matches_per_year_per_team
nationals_cost = 500 * num_teams
match_fee_cost = 20  # certain
nationals_fees = 45
initial_funds = 3200  # no idea, must check with those who know

### - PROBABILITY-DISTRIBUTED VARIABLES - ###

ref_hire = 130  # 90-140
misc_costs = 100  # very uncertain
players = 11  # average from this year- get stats


### ----------- MATHS ----------- ###

# membership_income = num_members * membership_fee
# buiha_fees = buiha_fee * num_teams
# sem_1_ice_fee = sem_1_ice_fee_paying_members * sem_1_ice_fee_cost
# sem_2_ice_fee = sem_2_ice_fee_paying_members * sem_2_ice_fee_cost
# players_ice_fees = sem_1_ice_fee + sem_2_ice_fee
# sem_1_beg_ice_fee = bps1bif * beginners_sem_1_ice_fee_cost
# sem_2_beg_ice_fee = bps2bif * beginners_sem_2_ice_fee_cost
# beginners_fees = sem_1_beg_ice_fee + sem_2_beg_ice_fee
# annual_ice_fees = players_ice_fees + beginners_fees
num_matches = num_teams * mpypt
# match_fees_income = (players * match_fee_cost) * num_matches
# training_cost = num_training_sessions * ice_hire
# beginners_costs = num_beginners_sessions * ice_hire
# buiha_costs = buiha_aff_fee + buiha_fees
# match_beers = 25 * num_matches
# match_cost = (ref_hire + (ice_hire * 2)) * num_matches + match_beers
# nationals_income = nationals_fees * num_members_paid_nationals_fees
corrective_factor = 640

# x_in =  membership_income + grant + spon + annual_ice_fees + match_fees_income + nationals_income
# x_out = training_cost + match_cost + beginners_costs + buiha_costs + misc_costs + nationals_cost

x_out = (
    ice_hire * (num_training_sessions + num_beginners_sessions)
    + num_matches * (ref_hire + 2 * ice_hire + 25)
    + buiha_aff_fee
    + num_teams * (buiha_fee + 500)
    + misc_costs
    + corrective_factor
) 

x_in = num_members * (
    membership_fee
    + sem_1_beginner_to_training_rate * beginners_sem_1_ice_fee_cost
    + sem_2_beginner_to_training_rate * beginners_sem_2_ice_fee_cost
    + nationals_fees * player_to_nationals_rate
) + (
    grant
    + spon
    + s1ifpm * sem_1_ice_fee_cost
    + s2ifpm * sem_2_ice_fee_cost
    + players * match_fee_cost * num_matches
)

num_members = (
    ice_hire * (num_training_sessions + num_beginners_sessions)
    + num_matches * (ref_hire + 2 * ice_hire + 25)
    + buiha_aff_fee
    + num_teams * (buiha_fee + 500)
    + misc_costs
    + corrective_factor
    - (
        grant
        + spon
        + s1ifpm * sem_1_ice_fee_cost
        + s2ifpm * sem_2_ice_fee_cost
        + players * match_fee_cost * num_matches
    )
) / (
    membership_fee
    + sem_1_beginner_to_training_rate * beginners_sem_1_ice_fee_cost
    + sem_2_beginner_to_training_rate * beginners_sem_2_ice_fee_cost
    + nationals_fees * player_to_nationals_rate
)

# Print the result
print(num_members)





#JAMES BITS

### expand x_in and x_out entirely

match_beers = 25 # define this as per match for both teams' beers so we minimise the number of numbers in the equation
buiha_league_fee_per_team = 100 # make this more explicit, was buiha_fee
buiha_nationals_fee_per_team = 500 # define this explicitly, was '500'
num_matches_per_team = 5 # make this more explicit, no need for per_year as the whole problem is per year
required_num_players = 11 # call it required_num_players instead of players, as we need 11 for a match - this can be an independent var
starting_money = 640

#expanded:
# x_out = (num_training_sessions * ice_hire) + (num_beginners_sessions * ice_hire) + num_teams * (num_matches_per_team * (match_beers + ref_hire + 2 * (ice_hire))) + (buiha_aff_fee) + num_teams * (buiha_league_fee_per_team + buiha_nationals_fee_per_team) + misc_costs
#simplified a bit
x_out = ice_hire * (num_training_sessions + num_beginners_sessions) + num_teams * ((num_matches_per_team * (match_beers + ref_hire + 2 * ice_hire)) + (buiha_league_fee_per_team + buiha_nationals_fee_per_team))  + buiha_aff_fee + misc_costs

#expanded:
# x_in = ((num_members * membership_fee) + ((sem_1_ice_fee_cost * member_to_player_dropoff_rate * num_members + beginners_sem_1_ice_fee_cost * num_members * sem_1_beginner_to_training_rate) + 
                                        #  (sem_2_ice_fee_cost * member_to_player_dropoff_rate * num_members + beginners_sem_2_ice_fee_cost * num_members * sem_2_beginner_to_training_rate)) +
                                        # (num_matches * match_fee_cost * required_num_players) + (nationals_fees * player_to_nationals_rate * num_members) + (grant + spon))
#simplified:
# x_in = num_members * (membership_fee + (sem_1_ice_fee_cost * member_to_player_dropoff_rate) + (beginners_sem_1_ice_fee_cost * sem_1_beginner_to_training_rate) + 
                    #   (sem_2_ice_fee_cost * member_to_player_dropoff_rate) + (beginners_sem_2_ice_fee_cost * sem_2_beginner_to_training_rate) + 
                    #   nationals_fees * player_to_nationals_rate
                    #   ) + grant + spon + (num_matches * match_fee_cost * required_num_players)
                                        
# so arrange for num_members:
# x_in + starting_money - x_out = 0
# x_in = x_out - starting_money
num_members = (x_out - starting_money - grant - spon - (num_matches * match_fee_cost * required_num_players)) / ((membership_fee + (sem_1_ice_fee_cost * member_to_player_dropoff_rate) + (beginners_sem_1_ice_fee_cost * sem_1_beginner_to_training_rate) + (sem_2_ice_fee_cost * member_to_player_dropoff_rate) + (beginners_sem_2_ice_fee_cost * sem_2_beginner_to_training_rate) + nationals_fees * player_to_nationals_rate))



## i think your corrective factor needs to be negative?

# x_out = ice_hire*(num_training_sessions+num_beginners_sessions)+num_matches*(ref_hire+2*ice_hire+25)+buiha_aff_fee+num_teams*(buiha_fee+500)+misc_costs + corrective_factor

# x_in=num_members*(membership_fee+sem_1_beginner_to_training_rate*beginners_sem_1_ice_fee_cost+sem_2_beginner_to_training_rate*beginners_sem_2_ice_fee_cost+nationals_fees*player_to_nationals_rate)+(grant+spon+s1ifpm*sem_1_ice_fee_cost+s2ifpm*sem_2_ice_fee_cost+players*match_fee_cost*num_matches)

# num_members = (ice_hire * (num_training_sessions + num_beginners_sessions) + num_matches * (ref_hire + 2 * ice_hire + 25) + buiha_aff_fee + num_teams * (buiha_fee + 500) + misc_costs + corrective_factor - (grant + spon + s1ifpm * sem_1_ice_fee_cost + s2ifpm * sem_2_ice_fee_cost + players * match_fee_cost * num_matches)) /
#  (membership_fee + sem_1_beginner_to_training_rate * beginners_sem_1_ice_fee_cost + sem_2_beginner_to_training_rate * beginners_sem_2_ice_fee_cost + nationals_fees * player_to_nationals_rate)

# Print the result
print(num_members)
