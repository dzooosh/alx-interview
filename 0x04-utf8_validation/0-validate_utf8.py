#!/usr/bin/python3

""" UTF 8 VALIDATION """


def validUTF8(data):
    """
    checks if a given data set reps. a valid UTF-8 encoding
    args:
        data - the data to determine its validity
    Return - True if data is valid
    """
    if not isinstance(data, list):
        return False

    for num in data:
        # using try and except to check for validity
        try:
            utf8char = chr(num).encode('utf-8').decode('utf-8')
            if (utf8char.isprintable()):
                continue
            else:
                return False
        except UnicodeDecodeError:
            return False
    return True
