import requests
from bs4 import BeautifulSoup
 
def getContentPage(page):
    """
    This function parse all p, h and table content into list of strings
    """
    soup = BeautifulSoup(page.content, 'html.parser')
    p_tags = soup.find_all('p')
    h_tags = soup.find_all('h')

    data = []

    for tag in p_tags + h_tags:
        text = tag.get_text()
        if text:
            data.append(  text) 
 
    tables = soup.find_all('table') + soup.find_all('div', {'class': 'table'})
 
    for table in tables:
        table_data = []
        rows = table.find_all('tr')
        for row in rows:
            cells = row.find_all(['td', 'th'])
            row_data = []
            for cell in cells:
                cell_value = cell.get_text()
                row_data.append(cell_value)
            table_data.append(row_data)
        data.append(table_data) 

    return data

if __name__=='__main__':  
    print('get content')
    response = requests.get('https://pypi.org' , verify=False) 
    test = getContentPage(response)
    print(test)