import unittest
from regex_url_parsing import PythonUri

class  UriTest(unittest.TestCase):
    """Tests for Python URI"""
    def setUp(self):
    	self.p_uri = PythonUri()
    def test_authority(self):
        """Test for Authority"""
        self.p_uri.url = "http://www.google.com"
        self.assertEqual(self.p_uri.get_authority(), "Authority : www.google.com")
        self.p_uri.url = "http://www.google.com"
        self.assertEqual(self.p_uri.get_authority(), "Authority : www.google.com")
        self.p_uri.url = "http://google.com"
        self.assertEqual(self.p_uri.get_authority(), "Authority : google.com")
        self.p_uri.url = "http://www.google.co.in"
        self.assertEqual(self.p_uri.get_authority(), "Authority : www.google.co.in")
        self.p_uri.url = "http://www.google.googler.com"
        self.assertEqual(self.p_uri.get_authority(), "Authority : www.google.googler.com")
        self.p_uri.url = "http://123.123.123.123"
        self.assertEqual(self.p_uri.get_authority(), "Authority : 123.123.123.123")
        self.p_uri.url = "123.123.123.123"
        self.assertEqual(self.p_uri.get_authority(), "Authority : 123.123.123.123")
    def test_scheme(self):
        """Test for Scheme"""
        self.p_uri.url = "http://www.google.com"
        self.assertEqual(self.p_uri.get_scheme(), "Scheme : http")
        self.p_uri.url = "https://www.google.com"
        self.assertEqual(self.p_uri.get_scheme(), "Scheme : https")
        self.p_uri.url = "://google.com"
        self.assertEqual(self.p_uri.get_scheme(), "Scheme not found.")
        self.p_uri.url = "ftp://www.google.co.in"
        self.assertEqual(self.p_uri.get_scheme(), "Scheme : ftp")
        self.p_uri.url = "www.google.googler.com"
        self.assertEqual(self.p_uri.get_scheme(), "Scheme not found.")
        self.p_uri.url = "http://123.123.123.123"
        self.assertEqual(self.p_uri.get_scheme(), "Scheme : http")
        self.p_uri.url = "123.123.123.123"
        self.assertEqual(self.p_uri.get_scheme(), "Scheme not found.")
    def test_domain(self):
        """Test for domain"""
        self.p_uri.url = "http://www.google.com"
        self.assertEqual(self.p_uri.get_domain(), "Domain : google.com")
        self.p_uri.url = "http://www.google.com"
        self.assertEqual(self.p_uri.get_domain(), "Domain : google.com")
        self.p_uri.url = "http://google.com"
        self.assertEqual(self.p_uri.get_domain(), "Domain : google.com")
        self.p_uri.url = "http://www.google.co.in"
        self.assertEqual(self.p_uri.get_domain(), "Domain : google.co.in")
        self.p_uri.url = "http://www.google.googler.com"
        self.assertEqual(self.p_uri.get_domain(), "Domain : googler.com")
        self.p_uri.url = "http://123.123.123.123"
        self.assertEqual(self.p_uri.get_domain(), "Domain not found.")
        self.p_uri.url = "123.123.123.123"
        self.assertEqual(self.p_uri.get_domain(), "Domain not found.")

if __name__ == '__main__':
    unittest.main()
