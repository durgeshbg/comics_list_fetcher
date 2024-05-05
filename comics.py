import requests
import csv
with open('list.csv', 'w') as csvfile:
    fieldnames = ['ID', 'TITLE', 'RELEASE_DATE', 'IMAGE_URL']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(0, 2510, 20):
        print(f'Fetching: {i} - {i + 20}')
        if i == 0: i = ''
        url = f'https://bifrost.marvel.com/v1/catalog/comics/?byId=1009368&byZone=marvel_site_zone&byType=character&orderBy=release_date%2Bdesc&formatType=issue%2Cdigitalcomic%2Ccollection&limit=20&offset={i}&variants=false'
        try: 
            r = requests.get(url).json()['data']['results']
            for comic in r:
                writer.writerow({
                    'ID': comic['id'],
                    'TITLE': comic['title'],
                    'RELEASE_DATE': comic['release_date'],
                    'IMAGE_URL': comic['image_url']
                })
        except Exception as e:
            print(e)
