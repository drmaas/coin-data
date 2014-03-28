'''
Created on Mar 9, 2014

@author: drmaas
'''

import requests

class Base(object):

    def __init__(self, baseurl):
        self.baseurl = baseurl
        
    def get(self, path):
        url = self.baseurl + path
        print url
        r = requests.get(url)
        if r is not None:
            result = r.json()
        else:
            result = {}
            
        print result
        return result
        
    
    