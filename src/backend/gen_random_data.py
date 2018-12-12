'''
Created on Sep 28th, 2018
Author: Miles McCall
'''

# Library Imports
import os
import sys
import random

#Functions
def write_csv(num_rows, file_name):
    print("Writing randomized entries to output csv...")
    f = open(file_name, "a")
    for i in range(num_rows):
        row_string = str(i) + "," # ID number
        row_string = row_string + str(random.randint(20,60)) + "," # Latitude
        row_string = row_string + str(random.randint(100,140)) + "," # Longitude
        row_string = row_string + str(random.choice(['Apis mellifera','Lasioglossum','Seladonia','Osmia'])) # Species Name
        row_string = row_string + "\n"
        f.write(row_string)
    print("\t--> Done.")

def main():
    # Example Command-line input:
        # python gen_random_number.py 500 500rows.csv
    num_rows = int(sys.argv[1])
    file_name = "results/" + str(sys.argv[2])
    write_csv(num_rows, file_name)

if __name__ == '__main__':
    main()
