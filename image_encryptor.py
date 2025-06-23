# image_encryptor.py
# Task 2 - Simple Image Encryption Tool using Pixel Manipulation
# By Tarun Mehra

from PIL import Image

def encrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            pixels[i, j] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)

    img.save(output_path)
    print("✅ Encrypted image saved as:", output_path)


def decrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            pixels[i, j] = ((r - key) % 256, (g - key) % 256, (b - key) % 256)

    img.save(output_path)
    print("✅ Decrypted image saved as:", output_path)


# 🟢 MAIN MENU
print("🔐 Image Encryption Tool by Tarun Mehra")
print("1. Encrypt an Image")
print("2. Decrypt an Image")
print("-----------------------------------------")

choice = input("Enter your choice (1/2): ")
key = int(input("Enter your secret key (any number): "))

if choice == '1':
    encrypt_image("original.png", "encrypted.png", key)
elif choice == '2':
    decrypt_image("encrypted.png", "decrypted.png", key)
else:
    print("❌ Invalid choice. Please enter 1 or 2.")
