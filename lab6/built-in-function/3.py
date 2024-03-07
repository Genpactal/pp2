def checki(word1, word2):
    return word1 == word2

word1 = str(input())

word2 = ''.join(reversed(word1))

if checki(word1, word2):
    print(True)
else:
    print(False)