import calendar
def findDSTforYear(year):
	Sundaycounter=0
	#To find the 2nd Sunday in march for a given year
	for i in range(1,15):
		ScndSundayCheck=calendar.weekday(year, 3, i)
		if ScndSundayCheck==0:
			Sundaycounter+=1
		if Sundaycounter==2:
			DSTStart=[year,3,i]
			arrayStart=''.join(str(DSTStart))
			print arrayStart
			Sundaycounter=0
			
	#To find the last sunday in november for a given year		
	for i in range(1,31):
		#we want the last sunday in the month
		#count how many sundays are in the given month for the given year?
		ScndSundayCheck=calendar.weekday(year, 11, i) 
		if ScndSundayCheck==0:
			Sundaycounter+=1
		if Sundaycounter==2:
			DSTEnd=[year,11,i]
			arrayEnd=''.join(str(DSTEnd))
			print arrayEnd
			Sundaycounter=0
	print DSTStart
	print DSTEnd
	
	return DSTStart
	return DSTEnd

	
#test statements
findDSTforYear(2018)
findDSTforYear(2019)
findDSTforYear(2020)
