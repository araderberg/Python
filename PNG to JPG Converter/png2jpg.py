###Program Name: png2jpg.py                            
###Programmer: Aaliyah Raderberg
###Project: Python PNG to JPG converter

from PIL import Image
import os

def convert_png_to_jpg(input_png_path, output_jpg_path):
  """Converts a PNG image to JPG format and saves it.

  Args:
      input_png_path: Path to the input PNG file.
      output_jpg_path: Path to the output JPG file.
  """
  try:
    image = Image.open(input_png_path).convert("RGB")  # Convert to RGB if necessary
    image.save(output_jpg_path, "JPEG")
    print(f"PNG image converted to JPG successfully: {output_jpg_path}")
  except FileNotFoundError:
    print(f"Error: Input PNG file not found: {input_png_path}")
  except Exception as e:
    print(f"Error converting PNG to JPG: {e}")

### Example usage:
##input_png = "D:/Python/Codes/compress_cool.png"
##output_jpg = "cool_converted_image.jpg"
##convert_png_to_jpg(input_png, output_jpg)

def main():
    input_png = input("Enter the path to the PNG file: ")
    output_jpg = input("Enter the output file name to save: ")

    # Check if the output directory exists, if not create it
    if not os.path.exists(input_png):
        os.makedirs(input_png)

    convert_png_to_jpg(input_png, output_jpg)

if __name__ == "__main__":
    main()

