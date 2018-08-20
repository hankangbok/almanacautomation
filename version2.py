# Thsi is the second version of the editor but the problem is idk if it will work
#Copy and paste your calendar of astronomical events from astropixels.com to a new .txt file
#delete lines between months, and Date/PST/EVENT headers
#save the .txt file.
#This code is very crude, just built to work, not be elegant. don't judge me too hard
import csv
import sys
prelim=raw_input("use default 2019 file? Y/N ")
if prelim=="y" or prelim=="Y":
        print "Okay."
        filename="2019skyevents.txt"
else:
        filename=raw_input("Please paste the full file path to your reference txt file: ")

with open(filename)as originalog:
#with open('C:/Users/hkang/Documents/2019skyevents.txt') as originalog:
        lines=originalog.readlines()
   
        whatdo=raw_input("What astronomical event are you looking for?")
        print whatdo
        counter=0
        moonphases=[]
        month=""
        for line in lines:
#keep track of what month you're on
            if line[0].isspace()==False:
                    month=line[:3]
#Prints the dates the astronomical event will occur                
            if whatdo in line[15:]:
                    print month+line[3:6]+" "+line[15:]
                #counter+=1
        raw_input('Press ENTER to exit')
