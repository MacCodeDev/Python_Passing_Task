import requests
import xml.etree.ElementTree as TreeElement

def get_songs_artists():
    response = requests.get('https://www.w3schools.com/xml/cd_catalog.xml')

    if response.status_code == 200:
        root = TreeElement.fromstring(response.content)
        songs_artists = [(cd.find('ARTIST').text, cd.find('TITLE').text) for cd in root.findall('CD')]
        return songs_artists
    else:
        print(f"Failed to download data, status code: {response.status_code}")
        return None
    
songs_artists = get_songs_artists()
print(songs_artists)