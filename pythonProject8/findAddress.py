import requests
import pandas as pd
import time


def findAddress(lat, lng, key=None):
    """
    Looks up and returns addresses from a set of coordinates
    :param lat: tuple of latitudes
    :param lng: tuple of longitudes
    :param key: API key, default is to use a key that has already been created
    :return: Dataframe with addresses and status codes
    """

    # Error handling for non tuple or different length entries
    if not isinstance(lat, tuple) or not isinstance(lng, tuple):
        return None
    if len(lat) is not len(lng):
        return None

    # Assign key for api call
    if key is None:
        key = 'U1jX5r2jlZtr4gfkauqMAuGwjM42TkAZ'

    # Initiate columns for the dataframe
    address_column = []
    status_column = []

    # Cycle through each coordinate in the tuples provided
    for i in range(0, len(lat)):

        lat_coord = lat[i]
        lng_coord = lng[i]

        # Prepare url to be called
        position = f'{lat_coord},{lng_coord}'
        base_url = f'https://api.tomtom.com/search/2/reverseGeocode/{position}.json?key={key}'

        # Call API
        response = requests.get(base_url)
        time.sleep(0.3)

        # Retrieve address from the api response if it was successful
        if response.status_code == 200:
            address_info = response.json()['addresses'][0]['address']['freeformAddress']
        else:
            address_info = None

        # Append status code and address to the lists
        address_column.append(address_info)
        status_column.append(response.status_code)

    # Assemble the dataframe
    df_dict = {'address': address_column, 'status_code': status_column}
    df = pd.DataFrame(df_dict)

    return df
