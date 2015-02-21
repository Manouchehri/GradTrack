#!/usr/local/bin/python3

__author__ = 'David Manouchehri (david@davidmanouchehri.com)'

import urllib.request
import gzip

base_url = 'https://www5.mun.ca/admit/hwswsltb.P_CourseResults'
request_url = '?p_levl=01%2A04&campus=%25&faculty=%25&prof=%25&crn=%25&p_term='  # Example: p_term=201402
headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate',
           'Accept-Language': 'en-US,en;q=0.5',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:35.0) Gecko/20100101 Firefox/35.0'}
start_year = 2000  # This is the earlier date possible that can be obtained online.
sessions = {'01': 'Fall',
            '02': 'Winter',
            '03': 'Spring'}

print('Memorial University course offerings scraper, written by ' + __author__ + '.')


def grab_url_data(url):
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req)
    if response.info().get('Content-Encoding') == 'gzip':
        page_data = gzip.decompress(response.read())
    elif response.info().get('Content-Encoding') == 'deflate' or not response.info().get('Content-Encoding'):
        page_data = response.read()
    elif response.info().get('Content-Encoding'):
        print('Encoding type unknown')  # Probably should raise an exception.
    return page_data

for key, season in sorted(sessions.items()):
    for year in range(start_year, start_year + 25):  # Goes up to 2024
        filename = str(year) + season + ".html"
        url = base_url + request_url + str(year) + key
        print("Trying " + url)
        contents = str(grab_url_data(url), encoding='utf8')
        if "No matches were found for your search" in contents or "404 (Page not Found)" in contents:
            print(filename + ' does not exist.')
            break
        file = open("html/" + filename, "w")  # Hardcoded path, feel free to fix.
        file.write(contents)
        file.close()
        print('Saved: ' + filename)

print('Done!')