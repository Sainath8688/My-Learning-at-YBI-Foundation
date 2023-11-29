import random
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_case = "abcdefghijklmnopqrstuvwxyz"
numbers = "1234567890"
symbol = "!@#$%^&*()_+:<>?|[]~`"
ans = upper_case + lower_case + numbers + symbol
length = 8
password = "".join(random.sample(ans,length))
print("Generated Password is :",password)
