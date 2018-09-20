#Added in calculation for DST 
#Add 1 hour to times if Daylight Savings is in effect
#Daylight Savings Time begins 2AM on second Sunday of March
#Day light Saving Time ends at 2AM on the First Sunday of November
#This is according to 
#http://astropixels.com/main/daylightsaving.html
#per the law signed by president bush.

#for now im just going to hard-code DST dates relevant to 2019, but
#eventually I want to make a funciton that can find the DST for each given yer
#for any year that we have data. 
#march 10 2AM 2019
#November 3Rd 2AM 2019

# Thsi is the second version of the editor but the problem is idk if it will work
#Copy and paste your calendar of astronomical events from astropixels.com to a new .txt file
#delete lines between months, and Date/PST/EVENT headers
#save the .txt file.
import csv
#This code is very crude, just built to work, not be elegant. don't judge me too hard
import sys
prelim=raw_input("use default 2019 file? Y/N ")
if prelim=="y" or prelim=="Y":
        print "Okay."
        filename="2019PSTevents.txt"
else:
        filename=raw_input("Please paste the full file path to your reference txt file: ")

with open(filename)as originalog:
#with open('2019PSTevents.txt') as originalog:
        lines=originalog.readlines()
   
        searchterm=raw_input("What astronomical event are you looking for?")
        print searchterm
        counter=0
        moonphases=[]
        month=""
        for line in lines:
#keep track of what month you're on
            if line[0].isspace()==False:
                    month=line[:3]
#Prints the dates the astronomical event will occur                
            if searchterm in line[15:]:
                    print month+line[3:6]+" "+line[15:]
        raw_input('Press ENTER to exit')
		
def determineDST(dateString):
	#Get a date string
	#Check if date it is within DST 
	#Check if time is within DST 
	##IF DST
	#Add an hr to the time
	#If not DST
	#return the original string
