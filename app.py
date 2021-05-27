from datetime import datetime
import googletrans
from googletrans import Translator
import json
# print(len(datetime.now()))
translator = Translator()
language_list = googletrans.LANGUAGES



def open_file(file_name):
    my_file = open(file_name, 'r')
    data = my_file.read()
    data = json.loads(data)
    
    my_file.close()
    return data

def save_file(file_name, dict_to_save):
    my_file = open(file_name, 'w')
    data_to_json = json.dumps(dict_to_save)
    my_file.write(data_to_json)
    my_file.close()
    print("nowa baza danych: ", json.dumps(dict_to_save, sort_keys=True, indent=4))

def trans(trans_lib, available_languages, translation_memory):
    target_language = "en"

    while True:
        today_date = datetime.today().strftime('%Y-%m-%d')
        text_to_translate = input("Co chcesz przetłumaczyć? ")
        if text_to_translate == 'ch':
            target_language = input("Na jaki jezych chcesz prztlumaczyć? ")
            while target_language not in available_languages:
                print("Nie mam takiego jezyka w bazie")
                target_language = input("Na jaki jezych chcesz prztlumaczyć? ")

        translation = trans_lib.translate(text_to_translate, dest=target_language)
        src = translation.src
        dest = translation.dest
        source_text = translation.origin
        target_text = translation.text
        print(f"source text({src}): ", source_text)
        print(f"target text({dest}): ", target_text)
        print("Jak chcesz wyjsc wpisz - 'q' ")
        if text_to_translate == 'q':
            break
        # print("tm memory: ", json.dumps(translation_memory, sort_keys=True, indent=4))
        # if source_text in translation_memory['2021-02-22']:
        #     print("jest takie slowo w bazie")

        print("Jak chcesz zmienic jezyk docelowy wpisz - 'ch' ")
        if target_text not in translation_memory:
            # print(f"slowa {source_text} nie ma w bazie", translation_memory)
            print(f"slowa {source_text} nie ma w bazie")
        if target_text not in translation_memory.values():
            file_to_save = input("Czy chcesz zapisać tłumaczenie?. Wybierz - 'tak' jeśli chesz to zapisać ")
            if file_to_save == 'tak':
                print("Plik zapisany")
                translation_memory = open_file('data')
                # print('before save: ', translation_memory)
                # translation_memory[today_date] = []
                translated_content = {
                    src:source_text,
                    dest: target_text
                }

                if today_date not in translation_memory:
                    translation_memory[today_date] = [translated_content]
                else:
                    translation_memory[today_date].append(translated_content)

                print('to save: ', translation_memory)
                save_file('data', translation_memory)
            

# def save_translation_to_base(text, data_base):
#     translation_memory = data_base.open()
# print(json.dumps(language_list, sort_keys=True, indent=4))
tm_memory = open_file('data')
trans(translator, language_list, tm_memory)

print("Dzięki za użycie")
print(datetime.now().date())
            # file_name = 'data'
            # old_file = open(file_name, 'r')
            # content = old_file.read()
            # json_to_dict_source = json.loads(content)

            
            # new_file = json_to_dict_source.
            # old_file = open(file_name, 'w')
            # data_to_json = json.dumps(json_to_dict_source)
            # old_file.write(data_to_json)
            # old_file.close()


# def save_file(file_name, dict_to_save):
#     my_file = open(file_name, 'w')
#     data_to_json = json.dumps(dict_to_save)
#     my_file.write(data_to_json)
#     my_file.close()
#     print("nowa baza danych: ", json.dumps(dict_to_save, sort_keys=True, indent=4))