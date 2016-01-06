__author__ = 'sambhav'

import json
import museapi as mus

def getData(val):

   mus.getDetails(val)
   with open("dummy.json") as f:
   	res = json.load(f)
   return res
