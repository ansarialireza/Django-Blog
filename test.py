import hmac
import hashlib

key = b'my-secret-key'
message = b'my-message'

h = hmac.new(key, message, hashlib.sha256)
result = h.hexdigest()

print(result)
