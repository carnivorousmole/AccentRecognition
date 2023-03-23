from build_model import run
from itertools import combinations
import datetime
import matplotlib.pyplot as plt


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
FEATURES_ALL = ['mfcc','fbe','hil' ] 

def today():
    return datetime.datetime.now().strftime("%d_%b")

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
        try:
            run(lang_set_config=lang + "_en_64mel_", expt_name_config=lang+"_en", project_name_config=today()+"_duolingo", audio_input_path_config="/Users/dylanwalsh/Code/input/audio_files/audios_word_split/please_call_Stella_ask_")
        except Exception as e:
            print(e)


def features_and_layers_test():
    results = {}
    for f in FEATURES_ALL:
        for l in ["ar_en_64mel", "mn_en_64mel", "ar_mn_en_64mel"]:
            for num_layers in [2,4]:
                try:
                    metrics = run(lang_set_config=l, features_config=f, expt_name_config=l+"_"+f +"_"+str(num_layers)+"_layers", 
                                project_name_config=today()+"_lang_features_layers", 
                                audio_input_path_config="/Users/dylanwalsh/Code/input/audio_files/audios_word_split/please_call_Stella_ask_",
                                cnn_layers_config=num_layers)
                    acc = metrics["accuracy"]
                    results[(l, f)] = acc
                except Exception as e:
                    print(e)

def individual_features_test():
    results = {}
    # for l in ["ar_mn_sp_en_64mel_", "ar_en_64mel_","mn_en_64mel_","sp_en_64mel_"]:
    for l in ["ar_mn_en_64mel"]:

        for f in FEATURES_ALL:
            try:
                metrics = run(lang_set_config=l, features_config=f, expt_name_config=l+"_"+f, project_name_config=today()+"_if_4", audio_input_path_config="/Users/dylanwalsh/Code/input/audio_files/audios_word_split/please_call_Stella_ask_")
                acc = metrics["accuracy"]
                results[(l, f)] = acc
            except Exception as e:
                print(e)
    
    fig, ax = plt.subplots()
    for i, (lang_set, feature) in enumerate(results.keys()):
        ax.bar(i, results[(lang_set, feature)], label=f"{lang_set} - {feature}")
    ax.set_xticks(range(len(results)))
    ax.set_xticklabels([f"{lang_set}\n{feature}" for (lang_set, feature) in results.keys()], rotation=45, ha="right")
    ax.set_xlabel("Language Set and Feature")
    ax.set_ylabel("Accuracy")
    ax.legend()
    #save plt
    plt.savefig("individual_features_test.png")


def mutliclass_features_test():
    for f in FEATURES:
        run("sp_ru_mn_fr_ko_ar_en_64mel_",f + "_hil")

def clip_length_test():
    for seconds in range(1,10):
        run(lang_set_config= "ar_ko_mn_en_64mel_", num_seconds_config = seconds, expt_name_config="CL_test_"+str(seconds),project_name_config="26_feb_CL")

def word_segment_tests():
    word_segments = ["please_", "please_call_", "please_call_Stella_", "please_call_Stella_ask_", "please_call_Stella_ask_her_"]
    # word_segments = ["please_call_Stella_"]
    langs = "ar_ko_mn_en_64mel_"

    for word_segment in word_segments:
        try:
            run(lang_set_config=langs, expt_name_config=word_segment+langs, project_name_config="19_mar_word_segment_2", audio_input_path_config="/Users/dylanwalsh/Code/input/audio_files/audios_word_split/"+word_segment)
        except Exception as e:
            print(e)





if __name__ == '__main__':
    # english_test()
    # mutliclass_features_test()
    # individual_features_test()
    # clip_length_test()
    # word_segment_tests()
    # english_test()
    features_and_layers_test()


# iterate over the set of strings
# for string in strings:
    # run the run method of the build_model module, passing in the current string as an argument
    # run(string)
