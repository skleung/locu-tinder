import urllib2
import urllib
from environment_variables import *
import json

def searchForNearbyBuisness(locu_id, category = None):
    """
    """
    url = 'https://api.locu.com/v2/venue/search'

    values = {'api_key' : 'Michael Foord',
          'fields' : [ "name", "location", "contact" ],
          "venue_queries" : [
            {
              "locu_id": locu_id
            }
          ]
        }

    data = urllib.urlencode(values)
    req = urllib2.Request(url, data)
    result = urllib2.urlopen(req)
    venue_object = result.read()
    try:
        coordinates = venue_object['location']['geo']["coordinates"] # longitude is first
    except Exception, e:
        print 'ask for forgiveness'
        return


    venue_queries = { "location": {"geo": "$in_lat_lng_radius" : [coordinates[1], coordinates[0], 5000]}}

    if category:
        venue_queries["category"] = category

    values = {'api_key' : 'Michael Foord',
          'fields' : [ "name", "location", "contact" ],
          "venue_queries" : [venue_queries]
        }

    data = urllib.urlencode(values)

    req = urllib2.Request(url, data)
    result = urllib2.urlopen(req)
    return result.read()
