import time
from build_model import run
from itertools import combinations
import datetime
import matplotlib.pyplot as plt


FOREIGN_LANGUAGES = {
    # only considering those with >80 samples
    'ar': 'arabic',
    # 'ch': 'chinese',
    # 'da': 'dari',
    # 'en': 'english',
    'fr': 'french',
    # 'hi': 'hindi',
    # 'ko': 'korean',
    # 'mn': 'mandarin',
    # 'ru': 'russian',
    # 'sp': 'spanish',
}

standard_set = "ar_mn_en_64mel_"

FEATURES = [ 'f0' , 'cen'] 
FEATURES_ALL = ['mfcc','mhfcc','fbe','hil' ] 

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


def duolingo_test():
    test_name = "duolingo" + "_" + today()
    num_average = 2
    # create dictionary to store results
    results = {}
    for i in range(num_average):
        # loop over something
        for lang in FOREIGN_LANGUAGES.keys():
                # loop over something else               
                try:
                    metric =  run(lang_set_config=lang + "_en_64mel_",
                                   expt_name_config=lang+"_en", 
                                    project_name_config= test_name,
                                    audio_input_path_config="/Users/dylanwalsh/Code/input/audio_files/audios_word_split/please_call_Stella_ask_")
                    # store results in dictionary indexed by loop variables
                    if (lang) in results:
                        results[(lang)].append(metric["accuracy"])
                    else:
                        results[(lang)] = [metric["accuracy"]]
                except Exception as e:
                    print(e)
    # average results
    averages = {k: sum(v)/len(v) for k, v in results.items()}
    # save results to file
    with open(test_name +".txt", "w") as f:
        f.write(str(averages))



def multi_word_test():
    test_name = "multi_word_fbe" + "_" + today()
    num_average = 3
    # create dictionary to store results
    results = {}
     # loop over something
    full_string = 'please'
    for word in ['_', 'call_', 'Stella_', 'ask_', 'her_']:
        full_string = full_string + word
        for i in range(num_average):
            try:
                metric = run(lang_set_config=standard_set, 
                            features_config= "fbe", 
                            expt_name_config=word, 
                            project_name_config= test_name,
                            audio_input_path_config="/Users/dylanwalsh/Code/input/audio_files/audios_word_split/" + full_string)

                # store results in dictionary indexed by loop variables
                if (word) in results:
                    results[(word)].append(metric["accuracy"])
                else:
                    results[(word)] = [metric["accuracy"]]
                    
            except Exception as e:
                print(e)
    # average results
    averages = {k: sum(v)/len(v) for k, v in results.items()}
    # save results to file
    with open("results/"+ test_name +".txt", "w") as f:
        f.write(str(averages))


def multi_word_test_numbers():
    test_name = "multi_word_fbe_number" + "_" + today()
    num_average = 3
    # create dictionary to store results
    results = {}
     # loop over something
    full_string = 'please'
    for num in [1,2,3,4,5]:
        for i in range(num_average):
            try:
                metric = run(lang_set_config=standard_set, 
                            features_config= "fbe", 
                            expt_name_config=str(num), 
                            project_name_config= test_name,
                            audio_input_path_config="/Users/dylanwalsh/Code/input/audio_files/audios_word_split_by_numbers2/" + str(num))

                # store results in dictionary indexed by loop variables
                if (num) in results:
                    results[(num)].append(metric["accuracy"])
                else:
                    results[(num)] = [metric["accuracy"]]
                    
            except Exception as e:
                print(e)
    # average results
    averages = {k: sum(v)/len(v) for k, v in results.items()}
    # save results to file
    with open("results/"+ test_name +".txt", "w") as f:
        f.write(str(averages))


def single_word_test():
    test_name = "single_word_fbe" + "_" + today()
    num_average = 3
    # create dictionary to store results
    results = {}
     # loop over something
    for word in ['please', 'call', 'Stella', 'ask', 'her']:
        for i in range(num_average):
            try:
                metric = run(lang_set_config=standard_set, 
                            features_config= "fbe", 
                            expt_name_config=word, 
                            project_name_config= test_name,
                            audio_input_path_config="/Users/dylanwalsh/Code/input/audio_files/audios_word_split/" + word)

                # store results in dictionary indexed by loop variables
                if (word) in results:
                    results[(word)].append(metric["accuracy"])
                else:
                    results[(word)] = [metric["accuracy"]]
                    
            except Exception as e:
                print(e)
    # average results
    averages = {k: sum(v)/len(v) for k, v in results.items()}
    # save results to file
    with open("results/"+ test_name +".txt", "w") as f:
        f.write(str(averages))

def fixed_trim_test():
    test_name = "fixed_trim_fbe" + "_" + today()
    num_average = 3
    # create dictionary to store results
    results = {}
     # loop over something
    for num_seconds in ['5', '10', '15']:
        for i in range(num_average):
            try:
                metric = run(lang_set_config=standard_set, 
                            features_config= "fbe", 
                            expt_name_config=num_seconds, 
                            project_name_config= test_name,
                            audio_input_path_config="/Users/dylanwalsh/Code/input/audio_files/audios_manual",
                            num_seconds_config=num_seconds)

                # store results in dictionary indexed by loop variables
                if (num_seconds) in results:
                    results[(num_seconds)].append(metric["accuracy"])
                else:
                    results[(num_seconds)] = [metric["accuracy"]]
                    
            except Exception as e:
                print(e)
    # average results
    averages = {k: sum(v)/len(v) for k, v in results.items()}
    # save results to file
    with open("results/"+ test_name +".txt", "w") as f:
        f.write(str(averages))




def features_and_layers_test():
    results = {}
    for f in FEATURES_ALL:
        for l in ["ar_mn_en_64mel"]:
            for num_layers in [4,2]:
                try:
                    metrics = run(lang_set_config=l, features_config=f, expt_name_config=l+"_"+f +"_"+str(num_layers)+"_layers", 
                                project_name_config=today()+"_lang_features_layers_2", 
                                audio_input_path_config="/Users/dylanwalsh/Code/input/audio_files/audios_word_split/please_call_Stella_ask_",
                                cnn_layers_config=num_layers)
                    acc = metrics["accuracy"]
                    results[(l, f)] = acc
                except Exception as e:
                    print(e)
                    # wait for 5 sconds
                    time.sleep(5)

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


def multiclass_features_test():
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
        for f in FEATURES_ALL:
            try:
                run(lang_set_config=langs,
                    expt_name_config=word_segment+langs,
                    project_name_config= today()+"_word_seg_"+f, 
                    audio_input_path_config="/Users/dylanwalsh/Code/input/audio_files/audios_word_split/"+word_segment, 
                    features_config=f) 
            except Exception as e:
                print(e)


# def lang_features_test():
#     # create dictionary to store results
#     results = {}
#     for lang in ["ar", "mn" ,"sp" , "fr", "ar_mn_sp_fr"]:
#     # for lang in ["ar_mn","fr_sp"]:
#             lang = lang + "_en_64mel_"
#             for f in FEATURES_ALL:
#                 try:
#                     metric = run(lang_set_config=lang, features_config=f, expt_name_config=lang+"_"+f, project_name_config=today()+"_lang_features_test_3")
#                     # add resullts to dictionary
#                     results[(lang, f)] = metric["accuracy"]
#                 except Exception as e:
#                     print(e)
#     # save results to file
#     with open("lang_features_test.txt", "w") as f:
#         f.write(str(results))
#     # plot results as grouped bar
#     fig, ax = plt.subplots()
#     for i, (lang_set, feature) in enumerate(results.keys()):
#         ax.bar(i, results[(lang_set, feature)], label=f"{lang_set} - {feature}")
#     ax.set_xticks(range(len(results)))
#     ax.set_xticklabels([f"{lang_set}\n{feature}" for (lang_set, feature) in results.keys()], rotation=45, ha="right")
#     ax.set_xlabel("Language Set and Feature")
#     ax.set_ylabel("Accuracy")



def centroid_added_test():
    # create dictionary to store results
    results = {}
    for lang in ["ar", "mn" ,"sp" , "fr", "ar_mn","sp_fr","ar_mn_sp_fr"]:
            lang = lang + "_en_64mel_"
            for f in FEATURES_ALL:
                for cen in ['','_f0']:
                    f = f + cen
                    try:
                        metric = run(lang_set_config=lang, features_config=f, 
                                     expt_name_config=lang+"_"+f,
                                      project_name_config=today()+"_f0_test")
                        # add resullts to dictionary
                        results[(lang, f)] = metric["accuracy"]
                    except Exception as e:
                        print(e)
    # save results to file
    with open("centroid_test.txt", "w") as f:
        f.write(str(results))


                

def max_pool_4_test():
    for lang in ["ar", "mn" ,"ar_mn"]:
            for f in ['fbe', 'hil']:
                for mp in [True,False]:
                    try:
                        run(lang_set_config=lang + "_en_64mel_", features_config=f, 
                            expt_name_config=lang+"_"+f+"_"+str(mp)+"_max_pool", 
                            project_name_config=today()+"_max_pool_test", max_pool_4_config=mp)
                    except Exception as e:
                        print(e)



def lang_features_test():
    test_name = "lang_features" + "_" + today()
    num_average = 3

    # create dictionary to store results
    results = {}

    # loop over something
    for lang in ["ar", "mn" ,"sp" , "fr", "ar_mn_sp_fr"]:
        lang = lang + "_en_64mel_"
        # loop over something else            
        for f in FEATURES_ALL:
             for i in range(num_average):
                try:
                    metric = run(lang_set_config=lang, 
                                features_config=f, 
                                expt_name_config=lang+"_"+f, 
                                project_name_config= test_name,
                                    audio_input_path_config="/Users/dylanwalsh/Code/input/audio_files/audios_word_split_by_numbers2/4")

                    # store results in dictionary indexed by loop variables
                    if (lang, f) in results:
                        results[(lang, f)].append(metric["accuracy"])
                    else:
                        results[(lang, f)] = [metric["accuracy"]]
                        
                except Exception as e:
                    print(e)

    # average results
    averages = {k: sum(v)/len(v) for k, v in results.items()}


    # save results to file
    with open("results/"+ test_name +".txt", "w") as f:
        f.write(str(averages))




def test_template():
    test_name = "test_template" + "_" + today()
    num_average = 3

    # create dictionary to store results
    results = {}

    # loop over something
    for lang in []:
        # loop over something else            
        for f in FEATURES_ALL:
             for i in range(num_average):
                try:
                    metric = run(lang_set_config=lang, 
                                features_config=f, 
                                expt_name_config=lang+"_"+f, 
                                project_name_config= test_name,
                                    audio_input_path_config="/Users/dylanwalsh/Code/input/audio_files/audios_word_split_by_numbers2/4")

                    # store results in dictionary indexed by loop variables
                    if (lang, f) in results:
                        results[(lang, f)].append(metric["accuracy"])
                    else:
                        results[(lang, f)] = [metric["accuracy"]]
                        
                except Exception as e:
                    print(e)

    # average results
    averages = {k: sum(v)/len(v) for k, v in results.items()}


    # save results to file
    with open("results/"+ test_name +".txt", "w") as f:
        f.write(str(averages))



if __name__ == '__main__':
    # fixed_trim_test()
    # single_word_test()
    # multi_word_test()
    # multi_word_test_numbers()
    lang_features_test()
  
