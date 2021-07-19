import pandas

############ My Solution ###################
squirrel_data = {
    "Primary Fur Color": ["gray", "red", "black"],
    "Count": []

}

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

colors_column = data["Primary Fur Color"].to_list()

squirrel_data["Count"].append(colors_column.count("Gray"))
squirrel_data["Count"].append(colors_column.count("Cinnamon"))
squirrel_data["Count"].append(colors_column.count("Black"))

squirrel_count = pandas.DataFrame(squirrel_data)

squirrel_count.to_csv("squirrel_count_data.csv")

################ Angela's Solution ##########################

# Central Park Squirrel Data Analysis
# import pandas

# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
# red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
# print(grey_squirrels_count)
# print(red_squirrels_count)
# print(black_squirrels_count)

# data_dict = {
#     "Fur Color": ["Gray", "Cinnamon", "Black"],
#     "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
# }

# df = pandas.DataFrame(data_dict)
# df.to_csv("squirrel_count.csv")
