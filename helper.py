import urllib2
import urllib
from environment_variables import *
import json

def queryPluck(q):
    """
    """
    BASE_URL = 'https://apis.berkeley.edu/solr/fsm/select'
    url = "{base_url}?".format(base_url=BASE_URL) + urllib.urlencode({
        'q':q,
        'wt':'python',
        'app_id':FSM_APP_ID,
        'app_key':FSM_APP_KEY,
        'facet':'true',
        'facet.field':'fsmTypeOfResource',
        'facet.mincount':1
    })
    result = urllib2.urlopen(url)
    return eval(result.read())