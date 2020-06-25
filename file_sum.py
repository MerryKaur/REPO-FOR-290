# Author: Merry Kaur
# Date: 1/22/2020
# Description: Takes a text file of numbers and writes the sum of those numbers to a different text file.

def file_sum(file):
    """takes a text file list of numbers and writes the sum to a text file"""
    sums = 0
    with open(file, 'r') as infile:
        for line in infile:
            number = float(line.strip())
            sums += float(number)
            print(sums)

    with open('sum.txt', 'w') as outfile:
        sums = str(sums)
        outfile.write(sums + '\n')


#file_sum("numbers.txt")
