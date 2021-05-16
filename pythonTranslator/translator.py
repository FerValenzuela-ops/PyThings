from translate import Translator

translator = Translator(to_lang="es")

try:
    with open('./toTranslate.txt', mode='r') as my_file:
        to_translate = my_file.read()
        translation = translator.translate(to_translate)
        with open('./translated-to-es.txt', mode='w') as my_file2:
            my_file2.write(translation)
except FileNotFoundError as e:
    print('check if your file path is silly')
