###Program Name: qrcode.py
###Programmer: Aaliyah Raderberg
###Project: Python QR Code generator

##Description: This code takes user input for the data to encode and the filename to save the QR code.
##It then generates the QR code with black fill color and red background color using the qrcode library
##and saves it as the specified filename.

import qrcode

def generate_qr_code(data, filename, fill_color="black", back_color="red"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    img.save(filename)

if __name__ == "__main__":
    data = input("Enter the data to encode: ")
    filename = input("Enter the filename to save the QR code (with extension): ")
    generate_qr_code(data, filename, fill_color="black", back_color="red")
    print(f"QR code generated and saved as '{filename}'")
