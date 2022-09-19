import code


a=2.36
a=a*100
# a = amount of the dollar that we have
quarter_value =25
dime_value= 10
nickel_value =5
penney_value =1
count_ofthe_quarter=(a//25)
print("we need to give back the custemer" ,count_ofthe_quarter ,"quarter")
count_of_remainig_after_quarter=(a%25)
count_of_dime=count_of_remainig_after_quarter//dime_value
print("count of dime",count_of_dime, "dimes")
count_of_remaining_after_dime= count_of_dime%dime_value
couunt_of_nikel=count_of_remaining_after_dime//nickel_value
print("count of nikel", couunt_of_nikel ,"nikel")
count_of_remaining_after_nikel=couunt_of_nikel%nickel_value
count_of_penny=count_of_remaining_after_nikel//penney_value
print(count_of_penny)