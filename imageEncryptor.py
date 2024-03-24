from PIL import Image

def encrypt_image(image_path, key):
    # Open the image
    img = Image.open(image_path)
    
    # Get the width and height of the image
    width, height = img.size
    
    # Convert the image to RGB mode
    img = img.convert("RGB")
    
    # Create a new image for encryption
    encrypted_img = Image.new("RGB", (width, height))
    
    # Iterate through each pixel of the image
    for x in range(width):
        for y in range(height):
            # Get the RGB values of the pixel
            r, g, b = img.getpixel((x, y))
            
            # Manipulate the pixel values based on the key
            r = (r + key) % 256
            g = (g + key) % 256
            b = (b + key) % 256
            
            # Set the manipulated pixel values in the encrypted image
            encrypted_img.putpixel((x, y), (r, g, b))
    
    # Save the encrypted image
    encrypted_img.save("encrypted_image.png")

def decrypt_image(image_path, key):
    # Open the encrypted image
    encrypted_img = Image.open(image_path)
    
    # Get the width and height of the image
    width, height = encrypted_img.size
    
    # Create a new image for decryption
    decrypted_img = Image.new("RGB", (width, height))
    
    # Iterate through each pixel of the image
    for x in range(width):
        for y in range(height):
            # Get the RGB values of the pixel
            r, g, b = encrypted_img.getpixel((x, y))
            
            # Reverse the manipulation of the pixel values based on the key
            r = (r - key) % 256
            g = (g - key) % 256
            b = (b - key) % 256
            
            # Set the decrypted pixel values in the new image
            decrypted_img.putpixel((x, y), (r, g, b))
    
    # Save the decrypted image
    decrypted_img.save("decrypted_image.png")

# Example usage
image_path = "D:\Internship\Prodigy Infotech\Tasks/2. Image Encryptor/backlash.jpeg"
key = 50

# Encrypt the image
encrypt_image(image_path, key)

# Decrypt the image
decrypt_image("encrypted_image.png", key)
