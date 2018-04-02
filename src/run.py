from init_db import init_db


def scrape_html(url):
    """
    Get html DOMs in str from the url
    :param url:
    :return:
    """
    pass


def main():

    db_uri = 'postgres://test:testpass@db:5432/heyjobs'
    # target_url = 'https://www.heyjobs.de/en/jobs-in-berlin'

    # initialize db
    init_db(db_uri)

    # todo
    # scrape html in url
    # parse uid & title from html
    # insert data into db


if __name__ == '__main__':
    main()
