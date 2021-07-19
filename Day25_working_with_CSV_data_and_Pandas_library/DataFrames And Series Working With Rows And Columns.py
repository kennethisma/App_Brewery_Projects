import pandas
data = pandas.read_csv("weather_data.csv")

data_dict = data.to_dict()


data_list = data["temp"].to_list()


# My solution #

# lenght_list = len(data_list)
# temp_sumed = 0
# for n in data_list:
#     temp_sumed += n
# average = round(temp_sumed / lenght_list)
# print(average)

# Angelas's solution #

# average = sum(data_list) / lenght_list
# print(average)

# print(data["temp"].mean())  # Mean method gets the average of a Series object
# print(data["temp"].max())  # Max method gets the max number of a Series object


# Get Data in columns

# print(data["condition"])
# print(data.condition)

# Get data in row

# print(data[data["temp"] == data["temp"].max()])  The condition inside the brackets is going to search the row that has that condition
# # ---Other way---#
# print(data(data.temp == data.temp.max()))
# ------------------------------------- #
monday = data[data.day == "Monday"]
print(monday)
temp_farenheit = (monday.temp * 9/5) + 32
print(temp_farenheit)

# Create a Dataframe from scratch

# data_dict = {
#     "students": ["Angela", "Kenneth", "Fabis"],
#     "scores": [74, 85, 100]
# }

# data = pandas.DataFrame(data_dict)

# data.to_csv("new_data.csv")
