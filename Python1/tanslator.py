import googletrans
from googletrans import Translator

translator = Translator()
textToTranslate = "Hello, World!"

result = translator.translate(textToTranslate, dest='es')
print(result.text)