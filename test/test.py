import prepare_utest
import unittest
from run import scrape_html


class TestScrapeHtml(unittest.TestCase):

    def test_return_something0(self):
        scraped_html = scrape_html("https://www.google.de")
        self.assertEqual(len(scraped_html) > 0, True)

    def test_return_something1(self):
        scraped_html = scrape_html("https://www.heyjobs.de/en/jobs-in-berlin")
        self.assertEqual(len(scraped_html) > 0, True)


if __name__ == '__main__':
    unittest.main()
