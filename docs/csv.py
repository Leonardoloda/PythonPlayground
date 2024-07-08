# Same logic can be used to open a csv file
with open("files/weather_data.csv") as weather_date:
    weather_data = weather_date.readlines()

    # But processing the values takes a bit more of logic
    header = weather_data[0:1][0].strip().split(",")
    body_rows = weather_data[1:]

    body = []

    for row in body_rows:
        body.append(row.strip().split(","))

    print(header)
    print(body)

# Instead you can use the csv module
import csv

with open("./files/weather_data.csv") as weather_date:
    # Now the module handles all the file parsing
    data = csv.reader(weather_data)
    next(data)

    temperatures = []

    for row in data:
        print(row)
        temperatures.append(int(row[1]))

    print(f"temperatures {temperatures}")
