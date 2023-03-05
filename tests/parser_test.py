from src.parser import getUrls
from src.parser import getContentPage
import requests 
import unittest
 

class TestGetUrls(unittest.TestCase):

    def test_get_list(self):
        urls = getUrls.getUrls('https://pypi.org' ) 
        self.assertNotEqual(urls, [])

class TestGetContentPage(unittest.TestCase):

    def test_get_list(self):
        response = requests.get('https://pypi.org' , verify=False) 
        self.assertNotEqual(getContentPage.getContentPage(response), [])


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
