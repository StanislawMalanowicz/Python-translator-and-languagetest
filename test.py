import json
import random
# stuff = ['spam', 'eggs', 'lumberjack', 'knights', 'ni']

day_one = [
        {
            "en": "some new word",
            "pl": "jakies nowe slowo"
        },
        {
            "en": "another new word",
            "pl": "kolejne nowe slowo"
        },
        {
            "en": "some nice words",
            "pl": "jakies ladne slowa"
        },
        {
            "en": "birds",
            "pl": "ptaki"
        },
        {
            "cz": "kocka",
            "pl": "kot"
        },
        
    ]

def open_file(file_name):
    my_file = open(file_name, 'r')
    data = my_file.read()
    data = json.loads(data)
    
    my_file.close()
    return data



def get_words(tm_memory):
    words_to_test = tm_memory
    filter_words = list()
    for day, value in words_to_test.items():
        # counter = 0
        # print("day: ", value)
        for tm in value:
            if all(key in tm for key in ("pl", "en")):
                filter_words.append(tm)
                # print("tm: ",tm)
            # print("tm is:", tm)
    return filter_words
    

def words_to_test(words, num):
    num_of_words = len(words)-1
    choosed_words = []
    for i in range(num):
        get_word = random.choice(words)
        choosed_words.append(get_word)
    
    return choosed_words

def exam(words_list):
    # print(len(words_list))
    task_num = len(words_list)

    print("Witam w teście")
    good_answ_counter = 0
    for el in words_list:
        word_to_translate = el.get('en')
        secret_word = el.get('pl')
        student_word = input(f"Co oznacza '{word_to_translate}'? ")
        if student_word == secret_word:
            good_answ_counter += 1
    print(f"Odpowiedziales dobrze {good_answ_counter} na {task_num} pytań")

data_base = open_file('data')
words_to_exam = get_words(data_base)
exam_words = words_to_test(words_to_exam, 5)
# print(words_to_test(words_to_exam))
exam(exam_words)

# json.dumps(words_to_test(words_to_exam), sort_keys=True, indent=4)