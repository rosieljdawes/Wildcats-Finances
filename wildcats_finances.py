# equation:

# x in = x_membership + x_grant + x_spon + x_icefees + x_matchfees
# x out = x_training + x_matches + x_beginners + x_BUIHAFEES
# ----------------------------------------------
# x in:
# x_membership = n_members * x_membershipfee
# x_icefees = ((n_members * 39.5%) * x_icefees) + (n_beginners * x_beginners_icefees)
# x_matchfees = (n_players (av. 11) * £20) * n_matchess
# x out:
# x_trainings = n_training sessions * x_ice hire
# x_matches = (x_refhire + (x_icehire * 2)) * n_matches
# x_beginners = n_sessions * x_icehire
#---------------------------------------------------------------------
# variables:
members = 71
icefee_paying_members = members * 0.395 # according to this year's stats
players = 11 # average from this year
membership_fee = 50
ice_fee_per_year = 140 # per year
beginners_ice_fee = 25
beginners = 4 # guess?
n_of_matches = 10
training_sessions = 40
ice_hire = 120
ref_hire = 130 # 90-140
beginners_sessions = 20
teams = 2
buiha_fee = 100
grant = 2350
spon = 0

#--------------------------------------------------------------------

membership = members * membership_fee
buiha_fees = buiha_fee * teams
ice_fees = ((members * 0.395) * ice_fee_per_year) + (beginners * beginners_ice_fee)
match_fees = (players * 20) * n_of_matches
trainings = training_sessions * ice_hire
matches = (ref_hire + (ice_hire * 2)) * n_of_matches
beginners_costs = beginners_sessions * ice_hire


x_in = membership + grant + spon + ice_fees + match_fees
x_out = trainings + matches + beginners_costs + buiha_fees


print(int(x_in - x_out))





