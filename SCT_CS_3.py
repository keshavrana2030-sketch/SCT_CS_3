from PIL import Image


def encrypt_image(image_path, key):

    img = Image.open(image_path)

    pixels = img.load()

    width, height = img.size


    for i in range(width):

        for j in range(height):

            r, g, b = pixels[i, j]

            r = (r + key) % 256
            g = (g + key) % 256
            b = (b + key) % 256

            pixels[i, j] = (r, g, b)


    img.save("encrypted.png")

    print("Encrypted image saved as encrypted.png")



def decrypt_image(image_path, key):

    img = Image.open(image_path)

    pixels = img.load()

    width, height = img.size


    for i in range(width):

        for j in range(height):

            r, g, b = pixels[i, j]

            r = (r - key) % 256
            g = (g - key) % 256
            b = (b - key) % 256

            pixels[i, j] = (r, g, b)


    img.save("decrypted.png")

    print("Decrypted image saved as decrypted.png")



while True:

    print("\nImage Encryption Tool")

    print("1. Encrypt Image")

    print("2. Decrypt Image")

    print("3. Exit")


    choice = input("Enter choice: ")


    if choice == "1":

        path = input("Enter image path: ")

        key = int(input("Enter key: "))

        encrypt_image(path, key)


    elif choice == "2":

        path = input("Enter encrypted image path: ")

        key = int(input("Enter key: "))

        decrypt_image(path, key)


    elif choice == "3":

        break


    else:

        print("Invalid Choice")