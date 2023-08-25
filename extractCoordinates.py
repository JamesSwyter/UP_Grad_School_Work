import re


def extractCoordinates(dat):
    """
    Function for transforming string column 'coordinates' into two numeric columns
    :param dat: dataframe with coordinates column
    :return: new dataframe, with coordinates column separated into latitude and longitude columns
    """

    # Check that station and coordinates columns exist
    if 'station' not in dat.columns:
        return -1
    if 'coordinates' not in dat.columns:
        return -2

    # Extract latitude and longitude numbers from coordinates column
    pat = re.compile(r'^\(((?P<lat>-*\d+\.*\d*), *(?P<lon>-*\d+\.*\d*))\)$')
    lat = []
    lon = []

    for i in dat['coordinates']:
        rslt = pat.search(f'{i}')
        lat.append(float(rslt.group('lat')))
        lon.append(float(rslt.group('lon')))

    # Drop coordinates column, add in the new latitude and longitude columns
    dat = dat.drop(['coordinates'], axis=1)
    dat['lat'] = lat
    dat['lon'] = lon

    return dat
