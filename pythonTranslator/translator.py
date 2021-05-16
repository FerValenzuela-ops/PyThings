from translate import Translator

translator = Translator(to_lang="es")

try:
    with open('./toTranslate.txt', mode='r') as my_file:
        to_translate = my_file.read()
except FileNotFoundError as e:
    print('check if your file path is silly')

    

translation = translator.translate(to_translate)

print(translation)

