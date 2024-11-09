import img2pdf
from PIL import Image
import os

#--> use raw string prefix eg- r"file path" or use double backslashes \\ to avoid unicode syntax error
img_path = "paste image file folder path"   
pdf_path = "paste pdf folder path you want for converted pdf file "

image = Image.open(img_path)
pdf_bytes =img2pdf.convert(image.filename)

file = open(pdf_path, "wb")
file.write(pdf_bytes)

image.close()
file.close()

print("sucessfully converted to pdf :)")
