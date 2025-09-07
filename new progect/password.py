import secrets
import hashlib
def Random_password(num):
    if num < 8:
        raise ValueError("you need more password")
    password = secrets.token_urlsafe(num)
    return password
def heshing_password(hm):
    num1 = secrets.token_bytes(hm)
    return num1
mage = Random_password(8)
print(mage)