from PIL import Image
import random
import os
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import words

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
    #print(binary_message)
    
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


meme_path = r"E:/Shaarav/gifs and images/Memes templates -HD-/png/"
images = os.listdir(meme_path)

test_image1 = random.choice(images)
input_image1 = meme_path + test_image1

print(input_image1)
#os.startfile(input_image)

output_image1 = "output1.png"
secret_message1 = r"Hello"

encode_lsb(input_image1, output_image1, secret_message1)

decoded_message = decode_lsb(output_image1)
print("Decoded Message1:", decoded_message)
print("Validity 1 is:",is_valid_text(decoded_message))

# test_image2 = random.choice(images)
# input_image2 = meme_path + test_image1

# #print(input_image)
# #os.startfile(input_image)

# output_image2 = "output2.png"
# secret_message2 = r"Uijt jt b dpifsfou tfoufodf"

# encode_lsb(input_image2, output_image2, secret_message2)

# decoded_message = decode_lsb(output_image2)
# print("Decoded Message2:", decoded_message)
# print("Validity 2 is:",is_valid_text(decoded_message))

