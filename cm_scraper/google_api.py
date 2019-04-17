import requests
from bs4 import BeautifulSoup

GOOGLE_SEARCH_URL='http://www.google.com/search?q='
BROWSER = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'

def get_us_zip5(zip):
  """
  Query google and test if given 5-digit zipcode exists

  Returns a 3-item tuple (zip, found flag, data_url)
  """
  headers = {
    'User-Agent': BROWSER
  }
  response = requests.get(GOOGLE_SEARCH_URL + zip, headers=headers)
  soup = BeautifulSoup(response.text, "html.parser")
  ctx = soup.find(class_='kno-fb-ctx')
  data_url = None
  found = False

  if ctx:
    try:
      link = ctx.find_all('a').pop(0)
      found = True
      data_url = link.get('data-url')
      if data_url:
        data_url = "http://www.google.com" + data_url
    except Exception as ex:
      print("Failed to find data url for {} (Error: {})".format(zip, str(ex)))

  return (zip, found, data_url)


