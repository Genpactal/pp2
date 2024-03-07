import os 

a = input()

if os.path.exists(a):
    os.remove(a)
    print("removed")
else:
    print("da takogo netu, tupoi")