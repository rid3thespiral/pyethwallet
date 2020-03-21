from Crypto.Cipher import AES
from Crypto.Protocol.KDF import scrypt
from Crypto.Util.Padding import pad, unpad
import json

with open(address + '.txt') as f:
	data = json.load(f)

salt = data['salt']
iv = data['initialization vector']
ct = data['encrypted private key']

salt = bytes.fromhex(salt)
iv = bytes.fromhex(iv)
ct = bytes.fromhex(ct)

key = scrypt(password, salt, 32, N = 2**20, r = 8, p = 1)

cipher = AES.new(key, AES.MODE_CBC, iv)
pt = unpad(cipher.decrypt(ct), AES.block_size)