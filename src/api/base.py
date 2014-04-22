'''
Created on Mar 9, 2014

@author: drmaas
'''

import requests

class Base(object):

    def __init__(self, baseurl, user='', passwd=''):
        self.__baseurl = baseurl
        self.__user = user
        self.__passwd = passwd 
        
    def get(self, path, params = {}):
        url = self.__baseurl + path
        r = requests.get(url, params=params, auth=(self.__user,self.__passwd))
        if r is not None:
            result = r.json()
        else:
            result = {}
        return result
    
    def post(self, path, params={}, headers={}):
        url = self.__baseurl + path
        r = requests.post(url, data=params, headers=headers)
        if r is not None:
            result = r.json()
        else:
            result = {}
        return result