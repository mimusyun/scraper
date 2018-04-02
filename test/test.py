import prepare_utest
import unittest
from run import scrape_html, parse_info_from_html, URLError


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


class TestParseInfoFromHtml(unittest.TestCase):

    def test_case0(self):
        html_str = \
            '<a target="_blank" href="/en/jobs/b8e936de-f06c-41aa-ad38-d394f58d56b8">' \
            '<div data-reactid="377">' \
            '<div>' \
            '<div class="job-card-title" data-reactid="381">' \
            'This is the job title I want to scrape!!!!!!!' \
            '</div>' \
            '</div>' \
            '</div>' \
            '</a>'
        obj_data = parse_info_from_html(html_str)

        self.assertEqual(len(obj_data), 1)
        self.assertEqual(obj_data[0].uid, "b8e936de-f06c-41aa-ad38-d394f58d56b8")
        self.assertEqual(obj_data[0].title, "This is the job title I want to scrape!!!!!!!")

    def test_invalid(self):
        html_str = \
            '<a target="_blank" href="/en/jobs/b8e936de-f06c-41aa-ad38-d394f58d56b8">' \
            '<div data-reactid="377">' \
            '<div>' \
            '<div class="" data-reactid="381">' \
            'This is the job title I want to scrape!!!!!!!' \
            '</div>' \
            '</div>' \
            '</div>' \
            '</a>'

        self.assertRaises(ValueError, parse_info_from_html, html_str)


if __name__ == '__main__':
    unittest.main()
