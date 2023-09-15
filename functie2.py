
def functie2(records):
    total = sum(float(record['id2']) for record in records)
    average = total / len(records)
    return f'Average grade: {average}'
