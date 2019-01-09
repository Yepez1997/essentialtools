# NEXT STEP IS GETTING SPECIFIC JSON VALUES 
# INDEXING RIGHT THINGS IN DICTIONARY
# KNOW WHEN TO INDEX LOOK AT OUTER PAREN lOOOOOOkKKKKKKKKK ALERT ALERT 
import urllib
import sys
import pprint
import json
import argparse
import base64
import requests



# For Python 3.0 and later
from urllib.error import HTTPError
#from urllib.error import HTTPError
#from urllib.request import urlopen
from urllib.parse import quote
from urllib.parse import urlencode


""" CHANGE BEFORE COMMIT $$$$$$$$$$$$$$ """
# A
API_KEY = "AUGVSGgOAz7bSDrOd10cUgszg0vyJXsTwgW2JdnmyzWLwKBVB2Y_kfIr0irX2APmxUqsaOxLbictlUYl7Wp8XgZNZ0LMP1rUfLEBhlcKp4dXBrXVjDD-EgLeeUHrW3Yx"



API_HOST = 'https://api.yelp.com'
SEARCH_PATH = '/v3/businesses/search'
BUSINESS_PATH = '/v3/businesses/'  # Business ID will come after slash.


DEFAULT_TERM = 'dinner'
DEFAULT_LOCATION = 'San Francisco, CA'
SEARCH_LIMIT = 3


def request(host, path, api_key, url_params=None):
    """Given your API_KEY, send a GET request to the API.
    Args:
        host (str): The domain host of the API.
        path (str): The path of the API after the domain.
        API_KEY (str): Your API Key.
        url_params (dict): An optional set of query parameters in the request.
    Returns:
        dict: The JSON response from the request.
    Raises:
        HTTPError: An error occurs from the HTTP request.
    """
    # url params and headers are always default 
    # api host -> host 
    # path -> the path we search for
    
    url_params = url_params or {}
    # host + path 
    url = '{0}{1}'.format(host, quote(path.encode('utf8')))
    headers = {
        'Authorization': 'Bearer %s' % api_key,
    }
    print(u'Querying {0} ...'.format(url))
    response = requests.request('GET', url, headers=headers, params=url_params)
    return response.json()


def search(api_key, term, location):
    """Query the Search API by a search term and location.
    Args:
        term (str): The search term passed to the API.
        location (str): The search location passed to the API.
    Returns:
        dict: The JSON response from the request.
    """

    url_params = {
        'term': term.replace(' ', '+'),
        'location': location.replace(' ', '+'),
        'limit': SEARCH_LIMIT
    }
    return request(API_HOST, SEARCH_PATH, api_key, url_params=url_params)


def get_business(api_key, business_id):
    """Query the Business API by a business ID.
    Args:
        business_id (str): The ID of the business to query.
    Returns:
        dict: The JSON response from the request.
    """
    business_path = BUSINESS_PATH + business_id

    return request(API_HOST, business_path, api_key)


# TO:DO
# create list of restraunts w/ start and end time 

def jsonsearching(obj):
    pprint.pprint(obj, indent=2)
 

def query_api(term, location):
    """Queries the API by the input values from the user.
    Args:
        term (str): The search term to query.
        location (str): The location of the business to query.
    """
    response = search(API_KEY, term, location)

    #json here and index
    # 'businesses' -> object of businesses 
    businesses = response.get('businesses')

    if not businesses:
        print(u'No businesses for {0} in {1} found.'.format(term, location))
        return



    # working with stashes 
    # takes the first i entries to search for 
    for i in range(2):
        business_id = businesses[i]['id']

        print(u'{0} businesses found, querying business info '
            'for the top result "{1}" ...'.format(
                len(businesses), business_id))
        response = get_business(API_KEY, business_id)

        print(u'Result for business "{0}" found:'.format(business_id))
        # only going to get hours ? 
        # KNOW WHEN TO INDEX LOOK AT OUTER PAREN 
        #hours = response['hours']
        days_open = response['hours'][0]['open']
        #start_times = response['hours'][0]['open'][0]['start']
        #end_times = response['hours'][0]['open'][0]['end']
        #photos = response['photos'][0] # first photo/ needs fix
        jsonsearching(days_open)

        #pprint.pprint(hours, indent=2)
        


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-q', '--term', dest='term', default=DEFAULT_TERM,
                        type=str, help='Search term (default: %(default)s)')
    parser.add_argument('-l', '--location', dest='location',
                        default=DEFAULT_LOCATION, type=str,
                        help='Search location (default: %(default)s)')

    input_values = parser.parse_args()

    try:
        query_api(input_values.term, input_values.location)
    except HTTPError as error:
        sys.exit(
            'Encountered HTTP error {0} on {1}:\n {2}\nAbort program.'.format(
                error.code,
                error.url,
                error.read(),
            )
        )


if __name__ == '__main__':
    main()



