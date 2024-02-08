from itertools import permutations

def print_permutations(str):
    listOfPermutations = permutations(str)
    for perm in listOfPermutations:
        print(''.join(perm))

userInput = input()
print_permutations(userInput)
