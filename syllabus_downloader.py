import urllib.request
import json
import time

links = ['https://apps.wharton.upenn.edu/syllabi/api/syllabi-list-results/?term=2020A&sections=ACCT',
         'https://apps.wharton.upenn.edu/syllabi/api/syllabi-list-results/?term=2020A&sections=REAL',
         'https://apps.wharton.upenn.edu/syllabi/api/syllabi-list-results/?term=2020A&sections=FNCE',
         ]

for link in links:
    response = urllib.request.urlopen(link)
    result = json.load(response)

    for item in result:
        if(item['syllabus_s3_direct'] is not None):
            syllabus_link = item['syllabus_s3_direct']
            section_id = item['section_id']
            if(".pdf" in syllabus_link):
                print("Retrieving " + syllabus_link)
                urllib.request.urlretrieve(syllabus_link, section_id + ".pdf" )
                time.sleep(1)
