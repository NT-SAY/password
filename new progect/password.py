import secrets
import hashlib
def Random_password(num):
    if num < 8:
        raise ValueError("you need more password")
    password = secrets.token_urlsafe(num)
    return password


def heshing_password_alg(password, name_alg):
    print(f"alogoritm heshing{hashlib.algorithms_available}")
    if name_alg not in hashlib.algorithms_available:
        raise ValueError(f"Algorithm {name_alg} not available")
    
    hash_obj = hashlib.new(name_alg)
    hash_obj.update(password.encode())
    return hash_obj.hexdigest()


password1 = Random_password(11)
print(f"your password: {Random_password(9)}")
print(f"alogoritm heshing{hashlib.algorithms_available}")
name_alg = input('enter your alg: ')
hashing_password = heshing_password_alg(password1, name_alg)
print(hashing_password)