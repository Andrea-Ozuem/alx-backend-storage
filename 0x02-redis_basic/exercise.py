#!/usr/bin/env python3
'Practice redies  0'

import uuid
import redis
from typing import Union


class Cache():
    '''Cache class'''

    def __init__(self):
        '''Init'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[int, str, float, bytes]) -> str:
        '''store'''
        u_id = str(uuid.uuid4())
        self._redis.set(u_id, data)
        return u_id
