import csv 
from datetime import date, datetime

open_file = open("death_valley_2018_simple.csv", "r")
csv_file = csv.reader(open_file, delimiter = ",")

header_row = next(csv_file)

print(type(header_row))

#shows the index of each row so we know where to grab from 
for index, column_header in enumerate(header_row):
    print(index,column_header)
    if column_header == "TMAX":
        tmax = index
    elif column_header == "TMIN":
        tmin = index





dates = []
highs = []
lows = []

#reading in 
for row in csv_file:
    try:
        the_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[tmax])
        low = int(row[tmin])
    except ValueError:
        print(f"Missing data for {the_date}")
    else:
        highs.append(int(row[4]))
        dates.append(the_date)
        lows.append(int(row[5]))

print(highs)
print(lows)


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