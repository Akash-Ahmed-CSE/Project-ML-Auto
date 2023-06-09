
def Get_CSV():
    import csv
    with open('../data/uploaded_file.csv') as csv_file:
        # creating an object of csv reader
        # with the delimiter as ,
        csv_reader = csv.reader(csv_file, delimiter=',')

        headers = next(csv_reader)

        # Print the headers
        for header in headers:
            print(header)
        # Store the headers in a dictionary
        header_dict = {index: header for index, header in enumerate(headers)}

        # Alternatively, you can access headers dynamically using the index
        index = 0
        header_value = header_dict.get(index)  # Returns None if index is not found
        if header_value:
            print(f"Header at index {index}: {header_value}")
Get_CSV()