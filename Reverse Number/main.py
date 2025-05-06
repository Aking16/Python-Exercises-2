n1 = 125
rev = 0

for _ in str(n1):
    digit = n1 % 10
    rev = rev * 10 + digit
    n1 //= 10

print(rev)