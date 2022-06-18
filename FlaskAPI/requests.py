# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 15:54:17 2022

@author: Hari
"""

import requests
from data_input import data_in

URL= 'http://127.0.0.1:5000/'
headers = {"Content-Type": "application/json"}
data = {"input": data_in}

r = requests.get(URL, headers=headers, json=data)

r.josn()