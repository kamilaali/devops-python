# Write a python program to convert minutes into a number of
# years and days.
# Test Data
# Input the number of minutes: 3456789
# Expected Output :
# 3456789 minutes is approximately 6 years and 210 days
a=3456789
hours=(a/60)
days=(hours/24)

years=(days//365)
days_left=years%365
print(days)

print(years)
