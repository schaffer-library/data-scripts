import requests
import csv
csvfile = input('csv filename: ')

'''
Use this script to scrape data from the contentdm API. 
'''


records = []
for record in range(1,100):
    request = requests.get(f'https://cdm16694.contentdm.oclc.org/digital/bl/dmwebservices/index.php?q=dmGetItemInfo/p16202coll7/{record}/json').json()
    if 'title' in request:
        row = []
        row.extend((request['title'],request['relatig'],request['dmrecord'],request['file']))
        records.append(row)

    csv_header = ['title','collection','recordID','filename']
    with open(csvfile, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(csv_header)
        writer.writerows(records)