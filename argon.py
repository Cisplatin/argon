from structures.binnum import BinNum
from ciphers.rc4 import RC4

key = BinNum('1001001')
cipher = RC4(key)
print "Result: %s" % cipher
print cipher.encrypt(key)
