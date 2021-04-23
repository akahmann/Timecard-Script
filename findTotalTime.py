from datetime import datetime

f = open("timecard.txt", "r")
lineList = f.readlines()
length = len(lineList)
f.close()
#check if txt file is empty
if len(lineList) > 0:
	f = open("timecard.txt", "r")
	totSeconds = 0
	totMinutes = 0
	totHours = 0
	fmt = "%H:%M:%S"
	print("Calculating please wait...")
	for i in range(1, length, 2):
		index = lineList[i]
		#if we are on the last line parse the strings differently
		if i == length - 1:
			seconds = index[-2:]
			minutes = index[-5:-3]
			hours = index[-8:-6]
		else:
			seconds = index[-3:-1]
			minutes = index[-6:-4]
			hours = index[-9:-7]
		#carry over seconds to minutes & minutes to hours
		seconds = int(seconds)
		totSeconds = totSeconds + seconds
		while totSeconds >= 60:
			totMinutes = totMinutes + 1
			totSeconds = totSeconds - 60
		minutes = int(minutes)
		totMinutes = totMinutes + minutes
		while totMinutes >= 60:
			totHours = totHours + 1
			totMinutes = totMinutes - 60
		hours = int(hours)
		totHours = totHours + hours
	totMinutes = str(totMinutes)
	totHours = str(totHours)
	total = totHours + " hours and " + totMinutes + " minutes"
	print("Total time spent on project:\n" + total)
	f.close()
else:
	print("Total time spent on project:\n0 hours and 0 minutes\nGET TO WORK!!!")