def palindrome_check(x):

    return x == x[::-1]

x = input()

if palindrome_check(x):
    print("YEAH, IT'S a Palindrome:3")
else:
    print("NAH, Give me another one -_-")