import csv 
from datetime import date, datetime

open_file = open("sitka_weather_07-2018_simple.csv", "r")
csv_file = csv.reader(open_file, delimiter = ",")

header_row = next(csv_file)

print(type(header_row))

#shows the index of each row so we know where to grab from 
for index, column_header in enumerate(header_row):
    print(index,column_header)

#testing to convert date from string
mydate = datetime.strptime('2018-07-01', '%Y-%m-%d')
print(mydate)

dates = []

highs = []

for row in csv_file:
    highs.append(int(row[5]))
    the_date = datetime.strptime(row[2], '%Y-%m-%d')
    dates.append(the_date)



print(highs)
print(dates)


#importing the graph
import matplotlib.pyplot as plt
fig = plt.figure()
plt.title("Daily High Temperatures, July 2018", fontsize = 16)
plt.xlabel("Day", fontsize = 12)
plt.ylabel("Temperatures (F)", fontsize = 12)
plt.tick_params(axis="both", which="major", labelsize = 12)

#this is what is putting data into the graph
plt.plot(dates, highs, c = "red")


fig.autofmt_xdate()

plt.show()
