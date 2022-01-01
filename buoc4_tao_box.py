from PIL import Image
import pytesseract
import cv2
import os

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
f = open('data_train/list.lst', 'rt')
lines = f.readlines()
f.close()
for line in lines:
    line = line.replace('\n', '')
    print(line)
    pos = line.rfind(".")
    os.system('tesseract '+'data_train/' + line + ' ' + 'data_train/'+ line[0:pos] + ' -l vie wordstrbox')