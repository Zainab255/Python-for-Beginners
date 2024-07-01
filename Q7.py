P = int(input("Enter the marks in Python: "))
C = int(input("Enter the marks in C Language: "))
D = int(input("Enter the marks in DBMS: "))

condition1 = (P >= 70) and (C >= 60) and (D >= 60)
condition2 = (P + C + D) >= 180

result = condition1 or condition2
print(result)
