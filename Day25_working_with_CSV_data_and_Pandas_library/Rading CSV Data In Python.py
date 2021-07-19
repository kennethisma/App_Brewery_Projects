
# with open("weather_data.csv", mode='r') as data_file:
#     data = csv_file.readlines()

# My solution #

# import csv

# with open("weather_data.csv", mode='r') as data_file:
#     data = csv.reader(data_file)
#     tempatures = []
#     for row in data:
#         for temp in row:
#             if temp.isnumeric():
#                 tempatures.append(int(temp))

# Angela's soluton #
# with open("weather_data.csv", mode='r') as data_file:
#     data = csv.reader(data_file)
#     tempatures = []
#     for row in data:
#         if row[1] != "temp":
#             tempatures.append(int(row[1]))

import pandas
data = pandas.read_csv("weather_data.csv")
print(data["temp"])
