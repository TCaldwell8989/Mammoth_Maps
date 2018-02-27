import csv

mammoth_data = []

with open('pbdb_data.csv', 'r') as csvfile:

    reader = csv.reader(csvfile)

    # The first row is the column types, read line, keep if needed
    columns = reader.__next__()

    # Interested in col 9, accepted_name
    # Abundance val and abundance unit 22 and 23
    # lat, long, cols 24, 25
    # State, country, in 27, 28
    # geocomment 32
    for row in reader:

        # get data of interest. Convert numeric types to floats
        # write out to new CSV file that another module can reader
        name = row[9]
        abd = row[22]
        abd_unit = row[23]
        lat = float(row[25])
        lng = float(row[24])
        state = row[27]
        county = row[28]
        comment = row[32]

        mammoth_data.append([name, abd, abd_unit, lat, lng, state, county, comment])

    with open('mammoth_data.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_NONNUMERIC)
        writer.writerow(['name', 'abd', 'abd_unit', 'lat', 'lng', 'state', 'count', 'comment'])
        writer.writerows(mammoth_data)