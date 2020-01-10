import unittest
from main import _news_scrapper
from common import config


class TestScrapper(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def test_config_object_creation(self):
        res = config()
        self.assertIsInstance(res, dict)
    
    def test_get_url_host_eluniversal(self):
        res = _news_scrapper("eluniversal")
        self.assertEqual(res, "http://www.eluniversal.com.mx")
    
    def test_get_url_host_elpais(self):
        res = _news_scrapper("elpais")
        self.assertEqual(res, "https://elpais.com")


if __name__ == '__main__':
    unittest.main()