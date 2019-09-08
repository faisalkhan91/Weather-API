#!/usr/local/bin/python3

#############################################################################################
#                               Program by Mohammed Faisal Khan                             #
#                               Email: faisalkhan91@outlook.com                             #
#                               Date: 09/03/2019                                            #
#############################################################################################

# Importing system module

import urllib.request
import json
import sys


def winddir (deg):

	if deg < 22.5 or deg > 337.5:
		return "N"
	elif deg >= 22.5 and deg < 67.5:
		return "NE"
	elif deg >= 67.5 and deg < 112.5:
		return "E"
	elif deg >= 112.5 and deg < 157.5:
		return "SE"
	elif deg >= 157.5 and deg < 202.5:
		return "S"
	elif deg >= 202.5 and deg < 247.5:
		return "SW"
	elif deg >= 247.5 and deg < 292.5:
		return "W"
	elif deg >= 292.5 and deg < 337.5:
		return "NW"


if len(sys.argv[1]) == 5 and sys.argv[1].isdigit():

	url = "http://api.openweathermap.org/data/2.5/weather?zip=" + sys.argv[1] + ",us&mode=json&units=metric&APPID=b0d45b8cc18faf92d77e9825fd5aae74"

	try:
		urlobject = urllib.request.urlopen(url)
	except:
		print("Error connecting to server")
		sys.exit()

	if urlobject.getcode() != 200:
		print("Error - return code is: ", urlobject.getcode())
	else:
		response = urlobject.read()
		response = response.decode("utf-8")

		respdict = json.loads(response)
		print("Current weather conditions for", respdict["name"])
		print("Temperature =", respdict["main"]["temp"], "degrees C")
		print("Humidity =", respdict["main"]["humidity"], "%")
		print("Skies are", respdict["weather"][0]["description"])
		print("The wind is blowing at", respdict["wind"]["speed"], "m/s from the", winddir(respdict["wind"]["deg"]))
		# print(respdict)
else:
	print("Error - invalid zip code entered.")

#############################################################################################
#                                       End of Program                                      #
#                                       Copyright 2019                                      #
#############################################################################################
