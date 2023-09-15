import functie1
import functie2
#import functie3

import csv


def main(file_path):
    records = functie1.functie1(file_path)
    average = functie2.functie2(records)
    return average

file_path = "D:\Users\Marilene\Documents\DS5 week2\DS5Week2\squirrel_edges.csv"
print(main(file_path))