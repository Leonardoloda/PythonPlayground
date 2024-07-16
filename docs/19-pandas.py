# Pandas is a library to handle data, it can easily read csv files
import pandas

data = pandas.read_csv("files/weather_data.csv")

# Pandas basic type i a DataFrame, it contains a table with the data
print(type(data))

# You can find lots of funcitons in the documentation for the DataFrame like converting to dic
print(data.to_dict())

temperatures = data['temp']

# Each data frame is composed of a series for each column as a 1 dimensional column
print(type(temperatures))
print(temperatures)

# Same for series
temperatures_list = temperatures.to_list()

print(temperatures_list)

# Statistics can be done manually
print(sum(temperatures_list) / len(temperatures_list))

# It has a lot of built functions for statitical analysis
print(f"Average temperature: {temperatures.mean()}")

print(f"Max temperature: {temperatures.max()}")

# You can also select with the data notation since panda allows you to
conditions = data.condition

print(conditions)

# it can also be used to extract rows
monday_row = data[data.day == "Monday"]

print(monday_row)

# Or combine it to get specific rows
max_temperature = temperatures.max()

max_temperature_day = data[data.temp == max_temperature]

print(max_temperature_day)

# Since it's still a row, you can get any data
print(max_temperature_day.condition)

print(monday_row.temp.apply(lambda value: value * 9 / 5 + 32))

# You can also use it to create adtaframe from python variables
data_dict = {
    "students": ["leo", "James", "Angela"],
    "scores": [100, 10, 50]
}

pd_data = pandas.DataFrame(data_dict)
pd_data.to_csv("files/created.csv")

FUR_COLOR_COLUMN_NAME = "Primary Fur Color"

data = pandas.read_csv("files/2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240708.csv")

squirrel_colors = data[FUR_COLOR_COLUMN_NAME].values

count_per_color = data[FUR_COLOR_COLUMN_NAME].groupby(squirrel_colors).count()

count_per_color.to_csv("files/squirrel_per_color.csv")

# manually
gray_squirrel_count = data[data[FUR_COLOR_COLUMN_NAME] == "Gray"][FUR_COLOR_COLUMN_NAME].count()
red_squirrel_count = data[data[FUR_COLOR_COLUMN_NAME] == "Cinnamon"][FUR_COLOR_COLUMN_NAME].count()
black_squirrel_count = data[data[FUR_COLOR_COLUMN_NAME] == "Black"][FUR_COLOR_COLUMN_NAME].count()

squirrel_count_dict = {
    "Fur Colour": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrel_count, red_squirrel_count, black_squirrel_count],
}

count_data = pandas.DataFrame(squirrel_count_dict)
count_data.to_csv("files/squirrel_count_dict.csv")
