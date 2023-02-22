from build_model import run
from itertools import combinations



LANGUAGES = {
    # only considering those with >80 samples
    'ar': 'arabic',
    # 'ch': 'chinese',
    # 'da': 'dari',
    # 'en': 'english',
    'fr': 'french',
    # 'hi': 'hindi',
    'ko': 'korean',
    'mn': 'mandarin',
    'ru': 'russian',
    'sp': 'spanish',
}

FEATURES = [ 'f0' , 'cen'] 
FEATURES_ALL = [ 'mfcc' , 'fbe','hil' ] 

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
        run(lang + "_en_64mel_", "hil")

def individual_features_test():
    for l in ["ar_ko_mn_en_64mel_","sp_ru_fr_en_64mel_","sp_ru_mn_fr_ko_ar_en_64mel_"]:
        for f in FEATURES_ALL:
            run(l,f)

def mutliclass_features_test():
    for f in FEATURES:
        run("sp_ru_mn_fr_ko_ar_en_64mel_",f + "_hil")

def clip_length_test():
    for seconds in range(1,10):
        run(lang_set_config= "ar_ko_mn_en_64mel_", num_seconds_config = seconds, expt_name_config="CL_test_"+str(seconds),project_name_config="20_feb_CL_B")





if __name__ == '__main__':
    # english_test()
    # mutliclass_features_test()
    # individual_features_test()
    clip_length_test()

# iterate over the set of strings
# for string in strings:
    # run the run method of the build_model module, passing in the current string as an argument
    # run(string)
