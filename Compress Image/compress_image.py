###Program Name: compress_image.py
###Programmer: Aaliyah Raderberg
###Project:  Python-based photo compressor

##Description: This script prompts the user to enter the input image file path
##and the output image file path. It then compresses the image at the input path
##and saves the compressed image at the output path.
##
##You can adjust the quality parameter in the compress_image function to control the level
##of compression. Higher quality values result in better image quality but larger file sizes,
##while lower quality values result in more compression and smaller file sizes with potential loss
##of image quality. Adjust this value according to your preferences and requirements.

from PIL import Image
import os

def compress_image(input_path, output_path, quality=85):
    try:
        # Open the image file
        with Image.open(input_path) as img:
            # Compress and save the image with the specified quality
            img.save(output_path, optimize=True, quality=quality)
        return True
    except Exception as e:
        print(f"An error occurred while compressing the image: {e}")
        return False

def main():
    # Input image file path
    input_path = input("Enter the input image file path: ")

    # Check if the input file exists
    if not os.path.exists(input_path):
        print("Input file does not exist.")
        return

    # Output image file path
    output_path = input("Enter the output image file path: ")

    # Compress the image
    if compress_image(input_path, output_path):
        print("Image compressed successfully.")
    else:
        print("Failed to compress image.")

if __name__ == "__main__":
    main()
