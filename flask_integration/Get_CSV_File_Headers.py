
def Get_CSV():
    import csv
    with open('../data/uploaded_file.csv') as csv_file:
        # creating an object of csv reader
        # with the delimiter as ,
        csv_reader = csv.reader(csv_file, delimiter=',')
        headers = next(csv_reader)
        print(headers)
Get_CSV()