N = int(input("Enter the number of days: "))

years = N // 365
remaining_days = N % 365
weeks = remaining_days // 7
days = remaining_days % 7

print(years)
print(weeks)
print(days)
