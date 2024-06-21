# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))


import pandas
data = pandas.read_csv("weather_data.csv")
print(type(data))
print(type(data["temp"]))

# you can specify the name of column and retrieve data
# print(data["temp"])

# DataFrame data converting
data_dict = data.to_dict()
print(data_dict)

# Series data converting
temp_list = data["temp"].to_list()
print(temp_list)


# Get Data in Columns
# print(data["temp"].mean())
# print(data["temp"].max())
# print(data["condition"])
# print(data.condition)


# Get Data in Rows - Filtering the column by condition to get a particular row
# print(data[data.day == "Monday"])
# print(data[data["temp"] == data["temp"].max()])

monday = data[data.day == "Monday"]
monday_temp = monday.temp[0]
monday_temp_f = monday_temp * 9/5 + 32
print(monday_temp_f)


# Create a datafram from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")



