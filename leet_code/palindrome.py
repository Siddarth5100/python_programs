x = 123
z = 123321

# y = str(x)

# print(x, type(x))
# print(y, type(y))

def check_palindrome(num):
    # print(num, type(num))
    no = str(num)
    if no == no[::-1]:
        return True
    else:
        return False

print(check_palindrome(z))