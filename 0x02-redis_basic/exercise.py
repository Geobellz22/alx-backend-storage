#!/usr/bin/env python3
"""Module for using the redis Nosql"""
import redis
import uuid
from functools import wraps
from typing import Callable, Union

class Cache:
    def __init__(self):
        """initialize redis"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @staticmethod
    def count_calls(method: Callable) -> Callable:
        @wraps(method)
        def wrapper(self, *args, **kwargs):
            key = f"{method.__qualname__}_calls"
            self._redis.incr(key)
            return method(self, *args, **kwargs)
        return wrapper

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store  bytes int and float"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int]:
        """initialize get method"""
        data = self._redis.get(key)
        if data is None:
            return data
        return fn(data) if fn else data

    def get_str(self, key: str) -> str:
        """initialize get_str method"""
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """get_int method"""
        return self.get(key, fn=int)
