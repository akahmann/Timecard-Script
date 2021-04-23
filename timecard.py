from datetime import datetime
import re

x = datetime.now()

#get date and time
monthDayYear = x.strftime("%x")
curTime = x.strftime("%H") + ":" + x.strftime("%M") + ":" + x.strftime("%S")

f = open("timecard.txt", "r")
lineList = f.readlines()
length = len(lineList)
f.close()
#check if txt file is empty
if len(lineList) > 0:
	#check whether to login or logout
	if "LOGOUT" in lineList[length - 1]:
		print("Login - Starting work")
		f = open("timecard.txt", "a")
		f.write("\nLOGIN " + curTime)
		f.close()
	elif "LOGIN" in lineList[length - 1]:
		print("Logout - Ending work")
		f = open("timecard.txt", "a")
		f.write("\nLOGOUT " + curTime + " - ")
		#find previous time
		prevLine = lineList[length - 1]
		prevTime = re.search("\d\d:\d\d:\d\d", prevLine)
		prevTime = str(prevTime)
		prevTime = prevTime[-10:-2]
		fmt = "%H:%M:%S"
		print(curTime)
		print(prevTime)
		timeSpent = datetime.strptime(curTime, fmt) - datetime.strptime(prevTime, fmt)
		timeSpent = str(timeSpent)
		print(timeSpent)
		f.write(timeSpent)
		f.close()
		#show time spent
		print("Time spent - " + timeSpent)
#else assume they are logging in
else:
	print("Login - Starting work")
	f = open("timecard.txt", "a")
	f.write("LOGIN " + curTime)
	f.close()