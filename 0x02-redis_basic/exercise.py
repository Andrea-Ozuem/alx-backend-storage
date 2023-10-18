#!/usr/bin/env python3
'''Create a Cache class. In the __init__ method, store an instance of the
Redis client as a private variable named _redis (using redis.Redis())
and flush the instance using flushdb.

Create a store method that takes a data argument and returns a string.
The method should generate a random key (e.g. using uuid), store the
input data in Redis using the random key and return the key.
'''

from functools import wraps
import redis
from uuid import uuid4
from typing import Callable, Union, Optional, Any


def count_calls(method: Callable) -> Callable:
    '''decorator for Cache.store'''
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Callable:
        '''increments the count for that key every time the method
        is called'''
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    '''Cache class'''
    def __init__(self) -> None:
        '''constructor for Cache Class'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[int, str, float, bytes]) -> str:
        '''generate a random key, use it to fill a value in the
        database, and return a string'''
        key: str = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Any:
        '''take a key string argument and an optional Callable argument named
        fn. This callable will be used to convert the data back to the desired
        format'''
        val_byte = self._redis.get(key)
        if fn:
            return fn(val_byte)
        return val_byte

    def get_int(self, val: bytes) -> int:
        '''Callable that returns int rep of a byte'''
        return int(val)

    def get_str(self, val: bytes) -> str:
        '''Returns str rep of key'''
        return val.decode('utf-8')
