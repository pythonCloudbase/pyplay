from Crypto.Cipher import DES

get = input("Enter the key (64 bit): ")

def pad(text):
    while(text%64 !=  0):
        text += " "
    return text

des =  DES.new(get,DES.MODE_ECB)

padded_text = pad("Hello")

encrypted = des.encrypt(padded_text)
print("encrypted: ", encrypted)

decrypted = des.decrpypt(encrypted)
print("decrypted: ", decrypted.decode())
