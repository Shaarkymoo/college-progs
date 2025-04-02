from PIL import Image
import random
import os
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import words

import base64
import binascii
import codecs
import urllib.parse
from Crypto.Cipher import AES
import base64
import hashlib
from stegano import lsb

text = "Password1234"
message = "Password1234"

# Hide message in image
# lsb.hide("input.jpg", "Hello, CyberChef!").save("output.png")

# # Extract hidden message
# hidden_text = lsb.reveal("output.png")
# print(f"Hidden Text: {hidden_text}")

# text = message.encode()
# md5_hash = hashlib.md5(text).hexdigest()
# sha256_hash = hashlib.sha256(text).hexdigest()

# print(f"MD5 Hash: {md5_hash}")
# print(f"SHA256 Hash: {sha256_hash}")

# def pad(s): return s + (16 - len(s) % 16) * chr(16 - len(s) % 16)
# def unpad(s): return s[:-ord(s[-1])]

# key = b"thisisakey123456"  # 16-byte key
# cipher = AES.new(key, AES.MODE_ECB)

# text = message
# encrypted = base64.b64encode(cipher.encrypt(pad(text).encode())).decode()
# # decrypted = unpad(cipher.decrypt(base64.b64decode(encrypted)).decode())

# print(f"AES Encrypted: {encrypted}")
# # print(f"AES Decrypted: {decrypted}")

# # text = "Hello, CyberChef!"
# # encoded = urllib.parse.quote(text)
# # decoded = urllib.parse.unquote(encoded)

# # print(f"URL Encoded: {encoded}")
# # print(f"URL Decoded: {decoded}")

# encoded = codecs.encode(text, "rot_13")
# # decoded = codecs.decode(encoded, "rot_13")

# print(f"ROT13 Encoded: {encoded}")
# # print(f"ROT13 Decoded: {decoded}")

# def xor_encrypt_decrypt(text, key):
#     return ''.join(chr(ord(c) ^ key) for c in text)

# key = 42  # XOR key (can be any number)
# encrypted = xor_encrypt_decrypt(text, key)
# # decrypted = xor_encrypt_decrypt(encrypted, key)

# print(f"XOR Encrypted: {encrypted.encode()}")
# # print(f"XOR Decrypted: {decrypted}")

# encoded = binascii.hexlify(text.encode()).decode()
# # decoded = binascii.unhexlify(encoded).decode()

# print(f"Hex Encoded: {encoded}")
# # print(f"Hex Decoded: {decoded}")

encoded = base64.b64encode(text.encode()).decode()
# # decoded = base64.b64decode(encoded).decode()

print(f"Base64 Encoded: {encoded}")
# # print(f"Base64 Decoded: {decoded}")

#nltk.download("words")
#nltk.download("punkt")
#nltk.download("punkt_tab")

def is_valid_text(text):
    word_list = set(words.words())  # English dictionary
    tokens = word_tokenize(text)
    valid_words = [word for word in tokens if word.lower() in word_list]
    return len(valid_words) / max(1, len(tokens)), valid_words  # Ratio of valid words

# text1 = "The quick brown fox jumps over the lazy dog."
# text2 = "Xhwor glkdz uor."

# print(is_valid_text(text1))  # Should be close to 1
# print(is_valid_text(text2))  # Should be close to 0

def encode_lsb(image_path, output_path, secret_message):
    
    img = Image.open(image_path)
    pixels = list(img.getdata())
    #print("pixels are: ",pixels[25:30])

    secret_message += "EOF" 
    print(secret_message)
    binary_message = ''.join(format(ord(char), '08b') for char in secret_message)
    print(binary_message)
    
    if len(binary_message) > len(pixels) * 3:
        raise ValueError("Message larger than image")

    new_pixels = []
    binary_index = 0
    a=0
    for pixel in pixels:
        new_pixel = list(pixel) 
        for i in range(3): 
            if binary_index < len(binary_message):
                new_pixel[i] = (new_pixel[i] & ~1) | int(binary_message[binary_index])
                #print(a:=a+1,binary_message[binary_index],pixel,new_pixel)
                binary_index += 1

        new_pixels.append(tuple(new_pixel))

    img.putdata(new_pixels)
    img.save(output_path)

    print(f"Message encoded into {output_path}")


def decode_lsb(image_path):
    
    img = Image.open(image_path)
    pixels = list(img.getdata())

    binary_message = ""

    for pixel in pixels:
        for i in range(3):
            binary_message += str(pixel[i] & 1)


    message = ""
    for i in range(0, len(binary_message), 8):
        char = chr(int(binary_message[i:i+8], 2))
        if message[-3:] == "EOF":  
            break
        message += char

    return message[:-3]  








meme_path = r"D:/college/Sem8/csd4002 ethical hacking/img5.png"
#images = os.listdir(meme_path)
#test_image1 = random.choice(images)

input_image1 = meme_path #+ test_image1

print(input_image1)
#os.startfile(input_image)

output_image1 = "output1.png"
secret_message1 = r"start reverse_shell 192.168.1.100:4444"

encode_lsb(input_image1, output_image1, secret_message1)

decoded_message = decode_lsb(output_image1)
print("Decoded Message1:", decoded_message)
print("Validity 1 is:",is_valid_text(decoded_message))

# # test_image2 = random.choice(images)
# # input_image2 = meme_path + test_image1

# #print(input_image)
# #os.startfile(input_image)

# output_image2 = "output2.png"
# secret_message2 = r"Uijt jt b dpifsfou tfoufodf"

# encode_lsb(input_image2, output_image2, secret_message2)

# decoded_message = decode_lsb(output_image2)
# print("Decoded Message2:", decoded_message)
# print("Validity 2 is:",is_valid_text(decoded_message))



