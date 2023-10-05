#!/usr/bin/env python3
"""Add the stuffs"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """computes and return the sum of two floats"""
    return lambda x: x * multiplier
