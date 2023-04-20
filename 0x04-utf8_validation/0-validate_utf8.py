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
            # chr(value) converts int to string
            # .encode('utf-8') convert the ascii character to utf8 with b'val' as result
            utf8char = chr(num).encode('utf-8')
            decoded_utf8char = utf8char.decode('utf-8') # decode the byte-string and output the value
            if (decoded_utf8char.isprintable()): 
                # check if the decoded value is a printable character
                continue
            else:
                return False
        except UnicodeDecodeError: 
            # if a value cannot be encode or decoded throws an error
            return False
    return True
