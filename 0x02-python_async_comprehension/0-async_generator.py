#!/usr/bin/python3
"""Async generator"""

from random import uniform
import asyncio


async def async_generator():
    for i in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
