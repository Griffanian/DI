french_words= ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]
eng_word=[] 
from googletrans import Translator, constants
from pprint import pprint

translator = Translator()
for item in french_words:
    translation = translator.translate(item)
    eng_word.append(translation.text)
print(eng_word)