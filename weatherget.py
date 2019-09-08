#!/usr/local/bin/python3

#############################################################################################
#                               Program by Mohammed Faisal Khan                             #
#                               Email: faisalkhan91@outlook.com                             #
#                               Date: 09/03/2019                                            #
#############################################################################################

# Importing system module

import urllib.request
import sys

try:
	urlobject = urllib.request.urlopen("http://www.newhaven.edu")
except:
	print("Error connecting to server")
	sys.exit()

if urlobject.getcode() != 200:
	print("Error - return code is: ", urlobject.getcode())
else:
	response = urlobject.read()

	file = open("web.html", "wb")
	file.write(response)
	file.close()
	response = response.decode("utf-8")
	print(response)

#############################################################################################
#                                       End of Program                                      #
#                                       Copyright 2019                                      #
#############################################################################################
