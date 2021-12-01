import requests
import csv
csvfile = input('csv filename: ')

'''
Use this script to scrape comments from an Omeka site.
'''


comments = []
for commentid in range(862,1515):
    comment_request = requests.get('https://digitalcollections.union.edu/api/comments/', params={'id':{commentid}})
    if comment_request.status_code != 404:
        comment_request_json = requests.get('https://digitalcollections.union.edu/api/comments/', params={'id':{commentid}}).json()
        commrow = []
        commrow.extend((comment_request_json['@id'],comment_request_json['o-module-comment:path'],comment_request_json['o:name'],comment_request_json['o-module-comment:body'],comment_request_json['o:created']))
        comments.append(commrow)


    csv_header = ['commid','siteid','name','body','commcreate']

    with open(csvfile, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(csv_header)
        writer.writerows(comments)

