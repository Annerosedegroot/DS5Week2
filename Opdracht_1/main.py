import functie1
import functie2
#import functie3

import csv


def main(file_path):
    records = functie1.functie1(file_path)
    average = functie2.functie2(records)
    return average

file_path = input(r'Geef csv')
print(main(file_path))
