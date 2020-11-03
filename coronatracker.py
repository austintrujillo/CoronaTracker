import requests
import zipfile
import os
from datetime import datetime
from Tickr import Tickr

printTicker = True
file = 'Overview_Seven-Day Rolling Average COVID-19 Cases by Test Report Date_' + datetime.now().strftime('%Y-%m-%d') + '.csv'
archive = 'Utah_COVID19_data.zip'
url = 'https://coronavirus-dashboard.utah.gov/' + archive
data = []

try:
	
	# Download Archive
	open(str('./' + archive), 'wb').write(requests.get(url).content)	
	
	# Unzip Archive
	with zipfile.ZipFile(str('./' + archive), 'r') as z:
		z.extract(file)
	os.remove('./' + archive)
except:
	print('DATA NOT YET RELEASED FOR ' + datetime.now().strftime('%d %B %Y') + '. DATA IS SCHEDULED TO BE RELEASED AROUND 13:00 MOUNTAIN TIME.')
	os.remove('./' + archive)
	exit()

# Read Latest Case Count
with open(str('./' + file), 'r') as f: 
	data = f.readlines()[-1].strip('\n').split(',')
os.remove('./' + file)

if printTicker:
	try:
		tkr = Tickr()
		tkr.printText('COVID-19 REPORT',align='CENTER',bold=True)
		tkr.printSpace()
		tkr.printText(str('REPORT DATE: ' + data[0]), align='CENTER')
		tkr.printText(str('CASE COUNT: ' + data[1]), align='CENTER')
		tkr.printText(str('TOTAL CASES: ' + data[2]), align='CENTER')
		tkr.printText(str('7-DAY AVG: ' + data[3]), align='CENTER')
		tkr.printQrCode(url)
		tkr.finishTicker()
	except:
		print('ERROR PRINTING TICKER')

print(str(
	'REPORT DATE: ' + data[0] + '\n' +
	'CASE COUNT:  ' + data[1] + '\n' +
	'TOTAL CASES: ' + data[2] + '\n' +
	'7-DAY AVG:   ' + data[3]
))
