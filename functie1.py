import csv
file_path = "squirrel_edges.csv"

def functie1(filecsv):
    """ We willen ene lijst met de record van de csv uitkrijgen """
    records = []
    with open(filecsv, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            records.append(row)
    return records      