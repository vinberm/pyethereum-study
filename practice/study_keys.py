import os
import random
import pbkdf2
import sys

from rlp.utils import encode_hex, decode_hex
from ethereum import keys


k = hex(random.getrandbits(256))[2:].zfill(64)
print(k)

m = decode_hex(k)
print(decode_hex(k))

password = '123456'


u = encode_hex(os.urandom(16))
print(os.urandom(16))
print(u)


uuid = '-'.join((u[:8], u[8:12], u[12:16], u[16:20], u[20:]))
print(uuid)

# keystore = keys.make_keystore_json(m, password)
# print(keystore)