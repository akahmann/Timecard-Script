import datetime
import re

x = datetime.datetime.now()

#get date and time
monthDayYear = x.strftime("%x")
curTime = x.strftime("%H") + ":" + x.strftime("%M") + ":" + x.strftime("%S")

f = open("timecard.txt", "r")
lineList = f.readlines()
#check if txt file is empty
if len(lineList) > 0:
	#check whether to login or logout
	if "LOGOUT" in lineList[len(lineList) - 2]:
		print("Login - Starting work")
		f = open("timecard.txt", "a")
		f.write("LOGIN " + curTime + "\n")
		f.close()
	elif "LOGIN" in lineList[len(lineList) - 2]:
		print("Logout - Ending work")
		f = open("timecard.txt", "a")
		f.write("LOGOUT " + curTime + " - ")
		#TODO find previous time
		prevTime = "10:33:21"
		fmt = "%H:%M:%S"
		timeSpent = datetime.datetime.strptime(curTime, fmt) - datetime.datetime.strptime(prevTime, fmt)
		timeSpent = str(timeSpent)
		f.write(timeSpent + "\n")
		f.close()
		print("Time spent - " + timeSpent)
		#display
#else assume they are logging in
else:
	print("Login - Starting work")
	f = open("timecard.txt", "a")
	f.write("LOGIN " + curTime + "\n")
	f.close()

# txt = "lalala alladsf 09:20 dfdsafsd"

# y = re.search("\d\d:\d\d", txt)
# print(y)
# z = re.split("\D", y)
# print(z)