#!/usr/bin/env python3
"""Add the stuffs"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """All is well"""
    return [(i, len(i)) for i in lst]