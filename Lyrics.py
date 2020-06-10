from bs4 import BeautifulSoup
import urllib.request, urllib.error
import requests
import codecs
import re

baseUrl = "http://search.j-lyric.net/index.php?ct=2&kt="

def Search(query):
  query = query.replace(' ', '+')
  
  html = requests.get(baseUrl + query).content

  bs = BeautifulSoup(html, "html.parser")

  results = bs.select("#mnb > .bdy")

  result = []
  for r in results:
    sml = r.select(".sml")

    result.append({
      "title": r.select_one(".mid > a").string,
      "artist": sml[0].select_one("a").string,
      "lyric_start": sml[1].string,
      "link": r.select_one(".mid > a").get("href")
    })

  return result

def getLyrics(url):
  html = requests.get(url).content

  bs = BeautifulSoup(html, "html.parser")

  lyric = str(bs.select_one("#mnb > .lbdy > #Lyric"))
  lyric = re.sub(r"\<[^\>]*\>", "\n", lyric)

  sml = bs.select("#mnb > .lbdy > .sml")

  info = []
  for s in sml:
    info.append(re.sub(r"\<[^\>]*\>", "", str(s)))

  return {
    "lyric": lyric,
    "info": info
  }

if __name__ == "__main__":
  data = Search("Melty Fantasia")
  print(getLyrics(data[0]["link"]))
@Mitsuki007
 
