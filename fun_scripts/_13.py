from bs4 import BeautifulSoup
from urllib.request import urlretrieve,urlopen,Request
import random

import ssl
ssl.match_hostname = lambda cert, hostname: True

# use this image scraper from the location that 
#you want to save scraped images to
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
headers={'User-Agent':user_agent,
    'Cache-Control': 'no-cache',
    # 'Host':'p1.music.126.net',
    'Referer':'https://stackoverflow.com/questions/13303449/urllib2-httperror-http-error-403-forbidden',
    'Cookie':'usertrack=ezq0al2LJGRBPQxyAwZuAg==',
    'Connection':'keep-alive'
    } 

def make_soup(url):
    request=Request(url,None,headers)
    html = urlopen(request).read()
    return BeautifulSoup(html)

def get_images(url):
    soup = make_soup(url)
    #this makes a list of bs4 element tags
    images = [img for img in soup.findAll('img')]
    print (str(len(images)) + "images found.")
    print ('Downloading images to current working directory.')
    #compile our unicode list of image links
    image_links=[each.get('src') for each in images]
    for each in image_links:
        if each is not None and 'p1.music.126.net' in each :
            filename=each.split('/')[-1]  
            urlretrieve('http:'+each, './files/'+str(random.choices(filename,k=5)))
    return image_links

#a standard call looks like this
get_images('https://music.163.com')