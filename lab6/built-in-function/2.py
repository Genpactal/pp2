word = str(input())

def count(word):
    a = 0
    b = 0
    for l in word:
        if l.isupper():
            a += 1
    for u in word:
        if u.islower():
            b += 1
    print(a)
    print(b)

count(word)