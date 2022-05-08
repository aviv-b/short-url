import math


ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
BASE = 62

""" 
@Encode example:
param num: 
       999
    calculation: 
       999 % 62 -> 7 -> ALPHABET[7]=7
       999 / 62 = 16 -> 16 % 62 = 16 ->  ALPHABET[16]=g
   return: 
       g7   

@Decode example:
    param value: 
        g7
    calculation: 
        ALPHABET[g]*62^1 + ALPHABET[7]*62^0
        16*62^1 + 7*62^0 = 999
    return:
        999   
        
@Usage examples:
    print(encode(100000000))    # 6LAze
    print(decode('6LAze'))      # 100000000
"""
       
def encode(num: int) -> str:
    """Pass a number(base 10) and return encoded value in base62, 
    :param num: int
    :return: str
    """
    str = ""
    while num > 0:
        str = ALPHABET[num % BASE] + str
        """ Divide as an int """
        num //= BASE 
    return str 


def decode(value: str) -> int:
    """Pass a string in base 62 and return a number in base 10, 
    :param encode: str
    :return: int
    """
    num = 0
    size = len(value)-1
    for ch in value:
        """ find will return -1 when value not found. """ 
        ind = ALPHABET.find(ch)
        if ind == -1: 
            return ind
        """ g7 -> A[g]*62^1 +  A[7]*62^0 """
        num  +=  ind * int(math.pow(BASE,size))
        size -= 1
    return num   





