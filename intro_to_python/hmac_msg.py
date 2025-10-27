import hmac #hash-based msg authentification code
import hashlib

def calc_hash(key: str, msg: str):
    b_key = key.encode()
    b_msg = msg.encode()
    hash_value = hmac.new(b_key, b_msg, hashlib.sha256) #generates hash based on key
    return hash_value.hexdigest()

key = "123456789"
hash1 = calc_hash(key, "Pay me $100")
hash2 = calc_hash(key, "Pay me $1000")
hash3 = calc_hash(key, "Pay me $100")

print(hash1 == hash2)
print(hash1 == hash3)