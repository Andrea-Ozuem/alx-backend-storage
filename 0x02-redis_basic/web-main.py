#!/usr/bin/env python3
""" Main file """

import redis
page = __import__('web').get_page


r = redis.Redis()
url = 'http://slowwly.robertomurray.co.uk'
for i in range(3):
    print(r.get('count:{}'.format(url)))
    print(page(url))
