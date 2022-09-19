# write aprogram that will take agiven amount of money and return number of dollar in quarters ,
# dime ,nickel,and penney that make up that given amount
# example place inter your plance $2.36
import re
from tkinter import CENTER
a=2.36

quarter=25
dime =10
nickel=5
penny=1
dollar =a*100
count_of_q =dollar//25
print("we need to give back ", count_of_q, "quarters")
remaing_exchange_afterq = dollar%25 
count_of_dime =remaing_exchange_afterq//10
print("count_of dime ", count_of_dime, "dimes")
remaing_exchange_afterd=remaing_exchange_afterq%10
count_of_nickel=remaing_exchange_afterd//5
print("count of nickel", count_of_nickel, "nickel")
remaing_exchange_after_nickel=remaing_exchange_afterd%5

count_of_pennies=remaing_exchange_after_nickel//1
print("count of pennies",count_of_pennies, "pennies")
