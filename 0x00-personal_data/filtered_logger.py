#!/usr/bin/env python3
""" Task 0: Regex-ing """

import re


def filter_datum(fields, redaction, message, separator):
    """ a function  that returns the log message obfuscated """
    pattern = f'({"|".join(fields)}){separator}[^{separator}]*'
    replacement = f'\\1{separator}{redaction}'
    return re.sub(pattern, replacement, message)
