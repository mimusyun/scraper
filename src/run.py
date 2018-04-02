from urllib.request import urlopen
from init_db import init_db


def scrape_html(url):
    """
    Get html DOMs in str from the url
    :param url:
    :return:
    """
    with urlopen(url) as response:
        html = response.read().decode('utf-8', 'ignore')
        return html


def main():

    db_uri = 'postgres://test:testpass@db:5432/heyjobs'
    target_url = 'https://www.heyjobs.de/en/jobs-in-berlin'

    # initialize db
    init_db(db_uri)

    # scrape html in url
    html_str = scrape_html(target_url)

    # parse uid & title from html
    # insert data into db


if __name__ == '__main__':
    main()
