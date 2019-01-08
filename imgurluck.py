#! python3
## This is a command line program
## This program opens the first five imgur results after searching for the command line argument in the imgur website
## Example input: python imgurlucky.py tesla cars
## This will return the first five imgur results of a 'tesla cars' search on imgur

import sys, requests, bs4, webbrowser

try:
	fileObj = requests.get('https://imgur.com/search?q=' + ' '.join(sys.argv[1:])) ## Gets the response object of the imgur page, so we can later create a soup object
	fileObj.raise_for_status() ## Checks to see if it went all okay

	soupObj = bs4.BeautifulSoup(fileObj.text, 'html.parser') ## Creates the soup object, the program will use it to crawl

	mytags = soupObj.findAll('a', {'class': 'image-list-link'}) ## Gets all the result images links

	x = 0
	if len(mytags) != 0:       ## Checks if the result wasn't empty
		for a in mytags:
		  if x < 5:    ##  Checks if the link is one of the first five ones
		    webbrowser.open('https://imgur.com' + a['href']) ## Opens the link
		    x = x + 1
	else:
		print('Found 0 imgur results for ' + ' '.join(sys.argv[1:])) #error handling

except requests.exceptions.HTTPError:
	print("404 Error\nThe page you requested does't exist.") ##error handling
except:
	print("Something went wrong, please try again.") ##error handling