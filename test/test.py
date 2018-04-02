import prepare_utest
import unittest
from run import scrape_html, URLError


class TestScrapeHtml(unittest.TestCase):

    def test_return_something0(self):
        scraped_html = scrape_html("https://www.google.de")
        self.assertEqual(len(scraped_html) > 0, True)

    def test_return_something1(self):
        scraped_html = scrape_html("https://www.heyjobs.de/en/jobs-in-berlin")
        self.assertEqual(len(scraped_html) > 0, True)

    def test_invalid_url0(self):
        self.assertRaises(URLError, scrape_html, "htp://this.is.wrong")

    def test_invalid_arg_type(self):
        self.assertRaises(TypeError, scrape_html, 12345)


if __name__ == '__main__':
    unittest.main()
