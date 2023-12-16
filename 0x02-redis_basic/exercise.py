#!/usr/bin/env python3
"""Module for using the redis Nosql"""
import redis
import uuid
from typing import Union


class Cache:
    def __init__(self):
        """initialize redis"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store  bytes int and float"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
