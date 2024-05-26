#!/usr/bin/python3

"""UTF-8 Validation"""


def Get_Leading_Set_Bit(Num):
    """Returns the number of leading set bits (1) in a given number.

    Args:
        Num (int): The number to count the leading set bits in.

    Returns:
        int: The number of leading set bits.

    """
    Set_Bit = 0
    helper = 1 << 7
    while helper & Num:
        Set_Bit += 1
        helper = helper >> 1
    return Set_Bit


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): The data set to validate.

    Returns:
        bool: True if the data set is a valid UTF-8 encoding, False otherwise.

    """
    Bit_Count = 0
    for i in range(len(data)):
        if Bit_Count == 0:
            Bit_Count = Get_Leading_Set_Bit(data[i])
            '''1-byte (format: 0xxxxxxx)'''
            if Bit_Count == 0:
                continue
            '''a character in UTF-8 can be 1 to 4 bytes long'''
            if Bit_Count == 1 or Bit_Count > 4:
                return False
        else:
            '''checks if current byte has format 10xxxxxx'''
            if not (data[i] & (1 << 7) and not (data[i] & (1 << 6))):
                return False
        Bit_Count -= 1
    return Bit_Count == 0
