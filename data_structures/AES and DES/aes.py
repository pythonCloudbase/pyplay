from Crypto.Cipher import AES

def pad(text):
    while(len(text)%16 != 0):
        text += " "
    print(text)
    return text

get = input("input key (64 bits):")

aes = AES.new(pad(get),AES.MODE_ECB)



padded_text = pad("Hello")
encrypt = aes.encrypt(padded_text)

print(encrypt)

