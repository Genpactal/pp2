import os

path_to_folder = r"C:\\Users\\adler\\Documents\\PP-2024\\Lab6\\builtin-functions"

for i in range(65, 91):
    open(f"{chr(i)}.txt", "x")