#!/usr/local/bin/python3

__author__ = 'dave'

import urllib.request
import gzip
from bs4 import BeautifulSoup

base_url = 'https://www5.mun.ca/admit/hwswsltb.P_CourseResults'
request_url = '?p_levl=01%2A04&campus=%25&faculty=%25&prof=%25&crn=%25'
term_url = '&p_term='  # Example: p_term=201402
headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate',
           'Accept-Language': 'en-US,en;q=0.5',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:35.0) Gecko/20100101 Firefox/35.0'}


def grab_url_data(url):
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req)
    # print(response.info())
    if response.info().get('Content-Encoding') == 'gzip':
        page_data = gzip.decompress(response.read())
    elif response.info().get('Content-Encoding') == 'deflate' or not response.info().get('Content-Encoding'):
        page_data = response.read()
    elif response.info().get('Content-Encoding'):
        print('Encoding type unknown')  # Probably should raise an exception
    '''else:
        page_data = response.read()'''
    return page_data


pairs = [(year, session) for year in [str(i) for i in range(2000, 2016)] for session in ['01', '02', '03']]

contents = []

for year, session in pairs:
    complete_url = base_url + request_url + term_url + year + session
    # contents.append(grab_url_data(complete_url))

for pages in contents:
    soup = BeautifulSoup(pages)
    print(soup.prettify())