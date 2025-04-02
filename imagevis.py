import numpy as np
import cv2
import matplotlib.pyplot as plt

def message_to_bin(message):
    binary = ''.join(format(ord(char), '08b') for char in message)
    print(binary)
    return binary

def encode_lsb(image, message):
    binary_message = message_to_bin(message)  # Null terminator
    img_copy = image.copy()
    index = 0
    
    for i in range(image.shape[1]):
        for c in range(3):  # Modify all color channels
            if index < len(binary_message):
                img_copy[0, i, c] = (img_copy[0, i, c] & 0xFE) | int(binary_message[index])  # Modify LSB
                index += 1

    # for i in range(image.shape[1]):
    #     for c in range(3):  # Modify all color channels
    #         if index < len(binary_message):
    #             if int(binary_message[index]) == 1:
    #                 img_copy[0, i, c] = min(img_copy[0, i, c] + diff, 255)  # Increase value by `diff`, but not above 255
    #             else:
    #                 img_copy[0, i, c] = max(img_copy[0, i, c] - diff, 0)  # Decrease value by `diff`, but not below 0
    #             index += 1    
    
    return img_copy

# Create an all-white image (10x2 pixels, 3 channels)
width = 15
height = 1
white_image = np.full((height, width, 3), 255, dtype=np.uint8)
print(white_image)

# Encode message in LSB of first row
encoded_image = encode_lsb(white_image, "Hello")
print(encoded_image)

border = np.zeros((1, width, 3), dtype=np.uint8)

# Properly stack the modified first row, border, and original second row
comparison_image = np.vstack((border, encoded_image, white_image, border))

plt.figure(figsize=(8, 2))
plt.imshow(comparison_image)
plt.axis('off')
plt.title("Top: Encoded | Middle: Border | Bottom: Original")
plt.show()