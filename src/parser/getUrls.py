import requests
from bs4 import BeautifulSoup
 
def getUrls(url):
    """
    This function takes a webpage as an argument and returns a list of all the URLs that are linked to from that page.
    """
    response = requests.get(url , verify=False)
    html = response.content
    soup = BeautifulSoup(html, 'html.parser')
    links = {l.get('href'):l.get_text()  for l in soup.select("a[href*=http]")  }
    return links


if __name__=='__main__': 
    print('get urls')
    urls = getUrls('https://pypi.org' )
    print(urls)