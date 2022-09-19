import numbers
from re import S
from shelve import DbfilenameShelf


a=2.36
a=a*100
quarter=25
dime =10
nickel=5
penny=1
count of q =a//25
print("we need to give back,count of q, "quarters")
reming _exchane after q =a%25
count of d =reming _exchane afer q//10
print("count of d ". "dime")
remaining exchane after d=reming _exchane after q%10
cunt of nickel=remaining exchane after d//5
print("count of nickel", "nickel")
remaining after nickel=remaining exchane after d%5
count of penny =remaining after nickel//1
print(count of penny,"penny")
