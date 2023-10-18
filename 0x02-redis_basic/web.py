#!/usr/bin/env python3
""" Main file """

from functools import wraps
import redis
import requests
from typing import Callable


def count_calls(method: Callable) -> Callable:
    '''decorator for Cache.store'''
    r = redis.Redis()

    @wraps(method)
    def wrapper(url) -> Callable:
        '''increments the count for that key every time the method
        is called'''
        key = 'count:{}'.format(str(url))
        r.incr(key)
        r.expire(key, 10)
        return method(url)
    return wrapper


@count_calls
def get_page(url: str) -> str:
    '''obtain the HTML content of a particular URL and returns it'''
    return requests.get(url).text
