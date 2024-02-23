###Program Name: digitalcert.py
###Programmer: Aaliyah Raderberg
###Project: Python Design a program that generates digital certificates using cryptographic techniques such as public-key encryption
###Credit: Idea taken from Python Script for Digital Certificate Creation by Faraz @https://www.codewithfaraz.com/python/24/python-script-for-digital-certificate-creation

# importing packages & modules
from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os

# Implementation to generate certificate
df = pd.read_csv('list.csv')
font = ImageFont.truetype('arial.ttf', 50)
for index, j in df.iterrows():
    img = Image.open('certificate.png')
    draw = ImageDraw.Draw(img)
    draw.text(xy=(125, 325),
              text='{}'.format(j['name']),
              fill=(0, 0, 0),
              font=font)  # customization
    draw.text(xy=(400, 425),
              text='{}'.format(j['instructor']),
              fill=(0, 0, 0),
              font=font)  # customization
    img.save('{}.png'.format(j['name']))
