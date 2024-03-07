import os 

x = input()

print(os.access(x, os.F_OK))
print(os.access(x, os.X_OK))
print(os.access(x, os.W_OK))
print(os.access(x, os.R_OK))