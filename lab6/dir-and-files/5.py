import os
import time

a = input().split()

with open(r"C:\\Users\\adler\\Documents\\PP-2024\\Lab6\\dir-and-files\\newfile.text", "x") as f:
    f.write(" ".join(a))

time.sleep(5)

os.remove(r"C:\\Users\\adler\\Documents\\PP-2024\\Lab6\\dir-and-files\\newfile.text")