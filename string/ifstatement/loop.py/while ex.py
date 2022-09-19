# you have 40$in your phone account
#after each call you will be charge 5$
#print how much call yoy can make and
#print how much money left in the account after each call

num =40
call_cost=5
while num<=40:
   num=num-5
   print(num)# You have $40 in the your phone account. 
# After each call you will be charged $5.
# print --> How much call you can make and 
# print how much money left in the account after each call. 


acct, each_call = 40, 5
call_number = 1
while acct >= each_call:
    print(f"{call_number}th call is made")
    call_number +=1
    acct = acct - each_call
    print(f"After the call I have ${acct} left")









