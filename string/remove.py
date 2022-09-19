# prefix will remove from the beginnig of the string
s="hello python"
print(s.removesuffix("python"))
print(s.removeprefix("hello"))
# this method is case sensitive
 s=www. website.com
print(s.removesuffix("www."))
# prefix -> will remove from the beginning of the string
# suffix -> will remove it from the end of the string

s = "Hello Python"
# If you want to remove Python from this string you can use 
# remove suffix method
print(s.removesuffix("Python"))

print(s.removeprefix("Hello"))
# This method is case sensitive

# From the given website string, 
# print only the domain name of the website

web_site = "Techtorial.com"
domain_name = web_site.removeprefix("www.").removesuffix(".com")

print(domain_name)

str = "hello world"
print(str.removeprefix("el"))

str2 ="Encapsulation is good for data hiding"
print("Result of the suffix",str2.removesuffix("gni"))
print("Result of strip",str2.strip("gni"))
#  "Encapsulation is good for data hiding"
#  "Encapsulation is good for data hid"
#  "Encapsulation is good for data hidi"

