import hashlib


KEY = "bgvyzdsv"
FIVE_FLAG = True

for i in range(10000000):
    enc_str = (KEY + f"{i:06}").encode()
    md5 = hashlib.md5()
    md5.update(enc_str)

    st = md5.hexdigest()

    if st.startswith("00000") and FIVE_FLAG:
        print(f"5-zeroes hash: {i}")
        FIVE_FLAG = False

    if st.startswith("000000"):
        print(f"6-zeroes hash: {i}")
        break
