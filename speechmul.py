import pytesseract


from PIL import Image


import pyttsx3


from googletrans import Translator


img = Image.open('r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'')


print(img)

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

result = pytesseract.image_to_string(img)

with open('abc.txt', mode='w') as file:
    file.write(result)
    print(result)
from google_trans_new import google_translator  
translator = google_translator()  
translate_text = translator.translate(result,lang_tgt='bs')
print(translate_text)
engine = pyttsx3.init()

k = p.translate(result, lang_tgt='bs')

data="UTF-8 data"
udata=data.decode("utf-8")
data=udata.encode("latin-1","ignore")

from google_trans_new import google_translator  
translator = google_translator()  
translate_text = translator.translate(result,lang_tgt='tu')
print(translate_text)
engine = pyttsx3.init()

k = p.translate(result, lang_
                
 from google_trans_new import google_translator  
translator = google_translator()  
translate_text = translator.translate(result,lang_tgt='my')
print(translate_text)
engine = pyttsx3.init()

k = p.translate(result, lang_
                
from google_trans_new import google_translator  
translator = google_translator()  
translate_text = translator.translate(result,lang_tgt='fr')
print(translate_text)
engine = pyttsx3.init()

k = p.translate(result, lang_

engine.say(k)
engine.runAndWait() 
