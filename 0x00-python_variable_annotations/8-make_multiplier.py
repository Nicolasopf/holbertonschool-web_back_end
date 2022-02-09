#!/usr/bin/env python3
''' function return a function '''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Returns a function that multiplies a float by multiplier'''

    def fun(number: float) -> float:
        '''Multiplies a float by multiplier'''
        return float(number * multiplier)
    
    return fun