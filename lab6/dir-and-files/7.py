import time 
import os

f = open(r"C:\\Users\\adler\\Documents\\PP-2024\\Lab6\\builtin-functions\\1.py", "r")

with open(r"C:\\Users\\adler\\Documents\\PP-2024\\Lab6\\dir-and-files\\newfile.text", "x") as new:
    for x in f:
        new.write(x)

time.sleep(5)

os.remove(r"C:\\Users\\adler\\Documents\\PP-2024\\Lab6\\dir-and-files\\newfile.text")