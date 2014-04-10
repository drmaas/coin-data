'''
Created on Mar 9, 2014

@author: drmaas
'''

import requests

class Base(object):

    def __init__(self, baseurl, user='', passwd=''):
        self.baseurl = baseurl
        self.user = user
        self.passwd = passwd 
        
    def get(self, path, params = {}):
        url = self.baseurl + path
        r = requests.get(url, params=params, auth=(self.user,self.passwd))
        print r.url
        if r is not None:
            result = r.json()
        else:
            result = {}
            
        print result
        return result