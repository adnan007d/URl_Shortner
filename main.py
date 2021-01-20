#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup


class TinyUrl:
    def __init__(self, url=None):
        self.url = url
        self.source = "indexpage"
        self.alias = ""

    def getShortURL(self):
        if not self.url:
            return "URL was not provided"
        self.data = {
            "url": self.url,
            "source": self.source,
            "alias": self.alias
        }
        r = requests.post('https://tinyurl.com/create.php/',
                          data=self.data)
        self.soup = BeautifulSoup(r.text, 'lxml')
        self.soup.prettify

        indent = self.soup.find_all('div', {'class': 'indent'})
        error = self.soup.find('div', {'id': 'contentcontainer'})

        if indent:
            return indent[1].b.text
        elif error:
            return error.p.b.text
        else:
            return "Something went wrong"


class Cuttly:
    def __init__(self, url=None):
        self.url = url
        self.domain = 0

    def getShortURL(self):
        if not self.url:
            return "URL was not provided"
        data = {
            "url": self.url,
            "domain": self.domain
        }

        r = requests.post('https://cutt.ly/scripts/shortenUrl.php', data=data)
        return r.text


class ShortUrl:

    def __init__(self, url):
        self.url = url

    def getShortURL(self):
        if not self.url:
            return "URL was not provided"
        data = {
            "u": self.url
        }
        r = requests.post('https://www.shorturl.at/shortener.php', data=data)
        self.soup = BeautifulSoup(r.text, 'lxml')
        self.soup.prettify

        url = self.soup.find('input', {'id': 'shortenurl'})
        if url:
            return url.get('value')
        else:
            return "Something went wrong"


print("========= URL SHORTNER =========")

url = input("Enter the URL: ")

x = TinyUrl(url)
print("Tiny URL: ", x.getShortURL())

x = Cuttly(url)
print("Cuttly URL: ", x.getShortURL())

x = ShortUrl(url)
print("Shorturl URL: ", x.getShortURL())
