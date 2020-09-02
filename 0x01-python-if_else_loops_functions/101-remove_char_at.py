#!/usr/bin/python3
def remove_char_at(str, n):
    a = str
    if n >= 0 and n < len(str):
        a = str.replace(str[n], '')
    return a
