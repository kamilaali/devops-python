num=[1,2,10,11,13,17,21,26]
sum_even=0
sum_odd=0
for number in num:
    if number%2==0:
        sum_even+=number

    else: sum_odd+=number
print("sum of all even number of the list is",sum_even)
print("sum of all even number of the list is",sum_odd)    
