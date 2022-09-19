t=(1,2,3,4,5,6)
# form this tuple remove each number if the square of the number if is smaller than20
# convert the tuple in to alist
t=list(t)
l=t.copy()
print(type(t))
for number in l:
    if number**2<20:
        t.remove(number)
t=tuple(t)
print(t)       
