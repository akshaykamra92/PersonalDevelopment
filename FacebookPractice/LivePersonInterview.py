x = 123321
old = x
new = 0
while x > 0:
    new = new*10 + x % 10
    x = x // 10

if new == old:
    print('Pallindrome')
else:
    print('NOT')

