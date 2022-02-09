#!/usr/bin/env python3
''' Duck typing first '''
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''Correct duck-typed annotations'''
    if lst:
        return lst[0]
    else:
        return None
