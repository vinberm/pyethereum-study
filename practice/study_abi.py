from ethereum.utils import big_endian_to_int, int_to_big_endian, encode_int, zpad
from ethereum import utils
import abi

function_keccak = utils.sha3('foo(uint256)')
print(function_keccak)
print(big_endian_to_int(function_keccak))

first_bytes = function_keccak[:4]
print(first_bytes)
print(big_endian_to_int(first_bytes))

# big-endian, ascii, 16->10
x = b'/\xbe'
print(big_endian_to_int(x))
print(int_to_big_endian(12222))

#zero padded
print(zpad(encode_int(big_endian_to_int(first_bytes)), 32))

#
# base, sub, c = abi.process_type(bytes)
# print(base)
# print(sub)
# print(c)
