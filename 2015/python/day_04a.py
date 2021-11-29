import hashlib


KEY = "bgvyzdsv"

for i in range(10000000):
    enc_str = (KEY + f"{i:06}").encode()
    md5 = hashlib.md5()
    md5.update(enc_str)
    if md5.hexdigest().startswith("00000"):
        print(i)
        break
