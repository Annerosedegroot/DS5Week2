import csv
def functie1(filecsv):
    """ 
    functie geeft een lijst met de record van de csv uitkrijgen 
    arg: csv file
    Output: list met records
    """
    records = []
    with open(filecsv, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            records.append(row)
    return records      