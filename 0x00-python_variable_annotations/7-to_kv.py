#!/usr/bin/env python3
"""Add the stuffs"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """computes and return the sum of two floats"""
    return k, float(v**2)
