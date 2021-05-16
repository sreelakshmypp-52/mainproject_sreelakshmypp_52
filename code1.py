# -*- coding: utf-8 -*-

import pytesseract
from PTL  import Image
import pyttsx3
from googletrans import translator
img=Image.open("text5.png")
print(img)
pytesseract.pytesseract.tesseract_cmd=r'c:\programfiles(x86)\Tesseract-0CR\tesseract.exee'
result=pytesseact.tesseract.image_to_tring(img)
with open('abc.txt',mode='w')as file:
    file.write(result)
    print(result)
    
    
    
from google_trans_new import google_translator
translator=google_translator()
translate_text=translator.transalte(result,lang_tgt='bs')
print(translate_text)
engine=pyttsx3.init()
p=google_translator()
k=p.transalte(result,iang_tgt='bs')
engine.say(k)
engine.runAndWait()
