from translate import Translator
translator = Translator(to_lang="es")

with open('./toTranslate.txt', mode='r') as my_file:
    to_translate = my_file.read()
    

translation = translator.translate(to_translate)

print(translation)

