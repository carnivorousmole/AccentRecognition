from build_model import run
from itertools import combinations


LANGUAGES = {
    'ar': 'arabic',
    'bn': 'bengali',
    'bu': 'bulgarian',
    'ch': 'chinese',
    'da': 'dari',
    'du': 'dutch',
    'en': 'english',
    'fr': 'french',
    'ge': 'german',
    'gu': 'gujarati',
    'hi': 'hindi',
    'it': 'italian',
    'ko': 'korean',
    'ku': 'kurdish',
    'ma': 'macedonian',
    'mn': 'mandarin',
    'ne': 'nepali',
    'pa': 'pashto',
    'po': 'polish',
    'pt': 'portuguese',
    'ro': 'romanian',
    'ru': 'russian',
    'sp': 'spanish',
    'sw': 'swedish',
    'ta': 'tajiki',
    'ur': 'urdu',
    'vi': 'vietnamese'
}

def get_combinations(strings):
    combs = []
    for i in range(2, len(strings)+1):
        comb = combinations(strings, i)
        combs.extend(comb)
    return combs

def tuple_to_string(combinations):
    return ['_'.join(comb) for comb in combinations]

# define a set of strings
strings = ['en_ge_sw_du_ru_po_fr_it_sp_64mel_','ru_po_64mel_']

def english_test():
    for lang in LANGUAGES.keys():
        run(lang + "_en_64mel_")


if __name__ == '__main__':
    english_test()


# iterate over the set of strings
# for string in strings:
    # run the run method of the build_model module, passing in the current string as an argument
    # run(string)
