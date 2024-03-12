from PIL import Image

def encrypt_image(image_path, key):
    img = Image.open(image_path)
    pixels = img.load()
    width, height = img.size
    
    encrypted_pixels = []
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            r = (r + key) % 256
            g = (g + key) % 256
            b = (b + key) % 256
            encrypted_pixels.append((r, g, b))
    
    encrypted_img = Image.new(img.mode, img.size)
    encrypted_img.putdata(encrypted_pixels)
    encrypted_img.save("encrypted_image.png")
    print("Image encrypted successfully.")

def decrypt_image(encrypted_image_path, key):
    encrypted_img = Image.open(encrypted_image_path)
    pixels = encrypted_img.load()
    width, height = encrypted_img.size
    
    decrypted_pixels = []
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            r = (r - key) % 256
            g = (g - key) % 256
            b = (b - key) % 256
            decrypted_pixels.append((r, g, b))
    
    decrypted_img = Image.new(encrypted_img.mode, encrypted_img.size)
    decrypted_img.putdata(decrypted_pixels)
    decrypted_img.save("decrypted_image.png")
    print("Image decrypted successfully.")

def main():
    while True:
        choice = input("Choose an option:\n1. Encrypt Image\n2. Decrypt Image\n3. Exit\n")
        if choice == '1':
            image_path = input("Enter the path to the image to encrypt: ")
            key = int(input("Enter the encryption key: "))
            encrypt_image(image_path, key)
        elif choice == '2':
            encrypted_image_path = input("Enter the path to the encrypted image: ")
            key = int(input("Enter the decryption key: "))
            decrypt_image(encrypted_image_path, key)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
