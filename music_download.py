import imslp
import mwclient
import requests
site = mwclient.Site('imslp.org', path='/')

# Specify the page title of the composition that contains the MP3 file
composition_page_title = "Cello_Suite_No.1_in_G_major,_BWV_1007_(Bach,_Johann_Sebastian)"

composition_page = site.pages[composition_page_title]

composition_page_text = composition_page.text()

mp3_link = None
liscense = None
for line in composition_page_text.split('\n'):
    if line.endswith(".mp3"):
        mp3_link = line.split("=", 1)[1].strip()
    if line.startswith("|Copyright"):
        liscense = line.split("=", 1)[1].strip()
        break

if mp3_link:
    file = site.images[mp3_link]
    file.imageinfo['url'] = "http:" + file.imageinfo['url']
    print(file.imageinfo)
    mwclient.image.Image.download(file)