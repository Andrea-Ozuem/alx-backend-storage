#!/usr/bin/env python3
'''Create a Cache class. In the __init__ method, store an instance of the
Redis client as a private variable named _redis (using redis.Redis())
and flush the instance using flushdb.

Create a store method that takes a data argument and returns a string.
The method should generate a random key (e.g. using uuid), store the
input data in Redis using the random key and return the key.
'''

import redis
from uuid import uuid4
from typing import Union


class Cache:
    '''Cache class'''
    def __init__(self) -> None:
        '''constructor for Cache Class'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[int, str, float, bytes]) -> str:
        '''generate a random key, use it to fill a value in the
        database, and return a string'''
        key: str = str(uuid4())
        self._redis.set(key, data)
        return key
