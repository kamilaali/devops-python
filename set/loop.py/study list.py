from tabnanny import check


a=[4,5,"str",True,3.4]
print(type(a))
print(a)
a[0]="new_element"
print(a)
# duplicates in list
list=[5,"str",5,"str"]
print(list)
# list length
# to learn how many element list consist of we can use len()function
# as we did in the string
print(len(list))
# what we can store in the list?
# we can store any type of data in the list
list=["str",5,"str",5,True,False,5.4,5+4j]
print(list)
# access items 
# list item are indexed and you can access them by referring to the index number 
print(list[-5])
# range of index 
# you can specify arange of indexes by specifying where to start
# and where to end the range 
# when specify arange the return value will be anew list 
# with specified items.
print(list[3:7])
# the range it work exactlyas slicing in string .
# range of negative index 
# specify negative indexes if you want to start the search
# from the end of the list
print(list[-4:-2])
# checkif item exists
# to determine if specified item is present in alist use the in keyword :
if 5 in list:
    print(5,"is in the list")
# we can use in operator for string too.

# change item value
# to change the value of specific  item refer to the index number
a[0]= "new element"
print(a)