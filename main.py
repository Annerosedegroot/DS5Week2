import functie1
import functie2
#import functie3

#import csv


def main(file_path):
    records = functie1(file_path)
    average = functie2(records)
    return average

file_path = "squirrel_edges.csv"
print(main(file_path))