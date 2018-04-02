from urllib.request import urlopen
from urllib.error import URLError, HTTPError
from init_db import init_db, Job
from bs4 import BeautifulSoup


def scrape_html(url):
    """
    Get html DOMs in str from the url
    :param url: url in str (e.g. https://www.google.com)
    :return: html DOMs in string
    """

    if not isinstance(url, str):
        raise TypeError('Invalid arg: url must be str: {}'.format(str(type(url))))

    try:
        with urlopen(url) as response:
            html = response.read().decode('utf-8', 'ignore')
            return html
    except HTTPError as e:
        print('The server couldn\'t fulfill the request.')
        raise HTTPError(url=url, code=e.code, msg=e.msg, hdrs=e.hdrs, fp=e.fp)
    except URLError as e:
        print('We failed to reach a server.')
        raise URLError(e.reason)


def parse_info_from_html(html_str):
    """
    Takes html DOMs in string format as arg
    Returns the list of Job(uid=..., title=...)
    :param html_str:
    :return: [Job(uid=..., title=...)...]
    """

    def _get_uid(_soup, target_tag, keyword, pos):
        return [tag['href'].split('/')[pos]
                for tag in _soup.find_all(target_tag, href=True)
                if keyword in str(tag)]

    def _get_job_title(_soup, target_tag, target_class):
        return [tag.text
                for tag in _soup.find_all(target_tag, {'class': target_class})]

    soup = BeautifulSoup(html_str, 'html.parser')
    uid_list = _get_uid(soup, target_tag='a', keyword='/en/jobs', pos=3)
    title_list = _get_job_title(soup, target_tag='div', target_class='job-card-title')

    if len(uid_list) != len(title_list):
        raise ValueError('Failed to extract uid & titles '
                         ': uid_list & title_lst must have the same length '
                         'uid:{} / title: {}'.format(uid_list, title_list))

    job_data = [Job(uid=uid_list[idx], title=title_list[idx]) for idx in range(len(uid_list))]
    return job_data


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
