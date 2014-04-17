import urllib
from elementtree.ElementTree import parse

BASE_URL = 'http://www.bing.com/'
IOTD_URL = BASE_URL + 'HPImageArchive.aspx?format=json&idx=0&n=1&mkt=en-US'
SAVE_DIR = '/trash/bing'


def get_iotd():
    xml = parse(urllib.urlopen(IOTD_URL)).getroot()
    u = xml.findall('./image/url')[0]
    return "%s%s" % (BASE_URL, u.text)
