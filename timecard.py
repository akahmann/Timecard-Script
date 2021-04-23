import datetime
import re

x = datetime.datetime.now()

#get date and time
monthDayYear = x.strftime("%x")
hour = x.strftime("%H")
minute = x.strftime("%H")

f = open("timecard.txt", "r")
lineList = f.readlines()
#check if txt file is empty
if len(lineList) > 0:
	#check whether to login or logout
	if "LOGOUT" in lineList[len(lineList) - 2]:
		f = open("timecard.txt", "a")
		f.write("LOGIN " + monthDayYear + " - " + hour + ":" + minute + "\n")
		f.close()
	elif "LOGIN" in lineList[len(lineList) - 2]:
		f = open("timecard.txt", "a")
		f.write("LOGOUT " + monthDayYear + " - " + hour + ":" + minute + "\n")
		f.close()
#els
else:
	f = open("timecard.txt", "a")
	f.write("LOGIN " + monthDayYear + " - " + hour + ":" + minute + "\n")
	f.close()
