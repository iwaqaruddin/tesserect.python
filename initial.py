from pandas.core import indexing
import pytesseract
from PIL import Image
import csv
import re
import pandas as pd


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# for x in range(1,24):
#     img1= Image.open('images/'+str(x)+'.jpg')
#     text=pytesseract.image_to_string(img1)
#     m = re.findall(r"foF2 [\d.-]+", text)
#     if m:
#         print(str(x)+m[0])

    # with open('abc.csv', 'w') as f:
    #     writer = csv.writer(f)


    #     writer.writerow(m)

# file_name='abc.jpg'
# link='images/'
img1= Image.open('images/3.jpg')
text=pytesseract.image_to_data(img1)
m = re.findall(r"foF2 [\d.-]+", text)
print(text)