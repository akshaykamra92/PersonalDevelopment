# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.

numbers = []
x = int(input("Enter First Number "))
y = int(input("Enter Second Number "))
mrange = int(input("Enter max range "))

curr = x
sec = y
while curr < mrange:
    numbers.append(curr)
    curr = curr+x

while sec < mrange:
    numbers.append(sec)
    sec = sec+y

print(numbers)
print(len(numbers))
print(set(numbers))
print(sum(set(numbers)))


