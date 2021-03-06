#!/usr/bin/env python3
''' Even more type annotations '''
from typing import Mapping, Any, Union, TypeVar

t = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[t, None] = None) -> Union[Any, t]:
    '''Return values, add type annotations to the function'''
    if key in dct:
        return dct[key]
    else:
        return default
