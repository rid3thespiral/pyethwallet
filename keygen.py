from tinyec.ec import SubGroup, Curve
from Crypto.Random.random import randint
from web3 import Web3

#key pair generation elliptic curve
#standard ethereum parameter elliptic curve a=zero e b=seven//
p = int("FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F", 16)
n = int("FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141", 16)
x = int("79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798", 16)
y = int("483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8", 16)
h = 1
g = (x,y)

#tinyec objects curve derivation
field = SubGroup(p, g, n, h)
curve = Curve(a = 0, b = 7, field = field, name = 'secp256k1')

#private key selection using crypto libraries
private_key = randint(1, n)
#public key derivation
public_key = private_key * curve.g

#obtaining ethereum address hashing the concatenation of hexadecimals value removing the zerox part
public_key_hex = Web3.toHex(public_key.x)[2:] + Web3.toHex(public_key.y)[2:]
address = Web3.keccak(hexstr = public_key_hex).hex()
address = "0x" + address[-40:]

#to turn this address in more readable format
address = Web3.toChecksumAddress(address)