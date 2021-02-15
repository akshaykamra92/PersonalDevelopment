def isPalindrome(x):
    result = (str(x)[::-1])
    if result == str(x):
        return True
    else:
        return False

x=121
print(isPalindrome(x))