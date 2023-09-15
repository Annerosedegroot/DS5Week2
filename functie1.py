import csv
file_path = "squirrel_edges.csv"
# records = []
# with open(file_path, 'r') as file:
#     csv_reader = csv.DictReader(file)
#     for row in csv_reader:
#         records.append(row)

def functie1(file_path):
    """ We willen ene lijst met de record van de csv uitkrijgen """
    records = []
    with open(file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            records.append(row)
    return records

print(functie1(file_path))      