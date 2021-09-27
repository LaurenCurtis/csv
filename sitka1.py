import csv 

open_file = open("sitka_weather_07-2018_simple.csv", "r")
csv_file = csv.reader(open_file, delimiter = ",")

header_row = next(csv_file)

print(type(header_row))

#shows the index of each row so we know where to grab from 
for index, column_header in enumerate(header_row):
    print(index,column_header)

highs = []

for row in csv_file:
    highs.append(int(row[5]))

print(highs)

#importing the graph
import matplotlib.pyplot as plt

plt.title("Daily High Temperatures, July 2018", fontsize = 16)
plt.xlabel("", fontsize = 12)
plt.ylabel("Temperatures (F)", fontsize = 12)
plt.tick_params(axis="both", which="major", labelsize = 12)

#this is what is putting data into the graph
plt.plot(highs, c = "red")

plt.show()
