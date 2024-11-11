# with open("weather_data.csv") as file:
#     data = file.readlines()

# # CSV module
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1].isdigit():
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

# Pandas library
# import pandas as pd

# data = pd.read_csv("weather_data.csv")  # Pandas DataFrame
# temperatures = data["temp"]  # Pandas DataSeries
# # print(temperatures)
#
# data_dict = data.to_dict()
# # print(data_dict)
#
# temp_list = temperatures.to_list()
# # print(temp_list)
#
# # Calculate Average
# average_temp = sum(temp_list)/len(temp_list)
# print(average_temp)
# print(temperatures.mean())
#
# # Max temperature
# print(temperatures.max())
#
# # Get Data in Columns
# print(data["condition"])
# print(data.condition)  # Use column name as attribute

# Get Data in Rows
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# temp_fahr = monday.temp[0] * 9/5 + 32
# print(temp_fahr)

# # Create a DataFrame from scratch
# data_dict = {
#     "let": ["A", "B", "C"],
#     "num": [1, 2, 3],
# }
#
# data = pd.DataFrame(data_dict)
# data.to_csv("new_data.csv")

# Challenge
import pandas as pd

squirrel_data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
red = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])

squirrel_colors_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [grey, red, black]
}

squirrel_colors_data = pd.DataFrame(squirrel_colors_dict)
squirrel_colors_data.to_csv("squirrel_count.csv")
