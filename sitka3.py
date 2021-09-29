import csv 
from datetime import date, datetime

open_file = open("sitka_weather_2018_simple.csv", "r")
csv_file = csv.reader(open_file, delimiter = ",")

header_row = next(csv_file)

print(type(header_row))

#shows the index of each row so we know where to grab from 
for index, column_header in enumerate(header_row):
    print(index,column_header)

#testing to convert date from string
'''mydate = datetime.strptime('2018-07-01', '%Y-%m-%d')
print(mydate)'''

dates = []
highs = []
lows = []

#reading in 
for row in csv_file:
    highs.append(int(row[5]))
    the_date = datetime.strptime(row[2], '%Y-%m-%d')
    dates.append(the_date)
    lows.append(int(row[6]))



#importing the graph
import matplotlib.pyplot as plt
fig = plt.figure()
plt.title("Daily Temperatures, 2018", fontsize = 16)
plt.xlabel("Day", fontsize = 12)
plt.ylabel("Temperatures (F)", fontsize = 12)
plt.tick_params(axis="both", which="major", labelsize = 12)

#this is what is putting data into the graph
plt.plot(dates, highs, c = "red", alpha = .5)
plt.plot(dates, lows, c = "blue", alpha = .5)
plt.fill_between(dates, highs, lows, facecolor = 'blue', alpha = .1)


fig.autofmt_xdate()

plt.show()

plt.subplot(2,1,1)
plt.plot(dates,highs, c = 'red')
plt.title("Highs")

plt.subplot(2,1,2)
plt.plot(dates, lows, c = 'blue')
plt.title("Lows")

plt.suptitle("Highs and Lows of Sitka, Alaska")
plt.show()