

from secrets import token_bytes
from typing import Tuple
import cv2
import numpy as np

def random_key(length):
    tb = token_bytes(length)
    return int.from_bytes(tb, "big")


def encrypt(original):
    original_bytes = original.encode()
    dummy = random_key(len(original_bytes))
    original_key = int.frombytes(original_bytes, "big")
    encrypted = original_key ^ dummy
    return dummy, encrypted

def decrypt(key1, key2):
    decrypted = key1 ^ key2
    temp = decrypted.to_bytes((decrypted.but_length() + 7) // 8, "big")
    return temp.decode()

if __name__ == "__main__":

    img = cv2.imread('grokey.jpg')
    for i in img:
        print(i)
    key1, key2 =  encrypt("One time Pad")
    result = decrypt(key1, key2)
    print(result)