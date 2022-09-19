#Veera wants lose 10 pounds in one month. 
# There are multiple conditions to lose 10 pounds in a month 
# Veera needs to walk 10000 steps daily  OR needs to run at least 4 miles a day. 
# and Addition to those , Veera needs eat less than 1500 calories daily. 
# We should create a program to calculate if Veera can loose weight or not.

walking_steps = 7000
running_distance= 0.2
daily_calory = 1200

can_loose_weigth = (walking_steps >= 10000 or running_distance>= 4) and daily_calory <1500

print("Veera can lose weight", can_loose_weigth)