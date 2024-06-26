from IndexTranslations import add_array
from yaml.loader import BaseLoader
from flatdict import FlatDict
import yaml


def find_missing_translations(files):
    translations = {}
    lang_to_file = {}

    for data in files:
        with open(data["path"], "r") as file:
            json = yaml.load(file, Loader=BaseLoader) or {}
            translations[data["lang"]] = FlatDict(json, delimiter=".")
            lang_to_file[data["lang"]] = data["path"]

    missing_data = {}

    for _, (lang, data) in enumerate(translations.items()):
        for _, (key, translation) in enumerate(data.items()):
            missing = translation_exists(translations, key)

            for missing_lang in missing:
                item_key = key.replace(lang, missing_lang, 1)
                filename = lang_to_file[missing_lang]

                if array_contains_dict_key(missing_data, filename, item_key):
                    continue

                add_array(missing_data, filename, {
                    "key": item_key,
                    "translation": translation,
                    "target_lang": missing_lang,
                    "source_lang": lang
                })

                print(f"Missing translation: {item_key}. Translating {translation} from {lang} to {missing_lang}")

    return missing_data


def array_contains_dict_key(dictionary, key, item):
    if key not in dictionary:
        return False

    for i in dictionary[key]:
        if i["key"] == item:
            return True
    return False


def translation_exists(translations, key):
    missing = []
    split_key = key.split(".")
    split_key.pop(0)
    key = ".".join(split_key)
    for _, (lang, data) in enumerate(translations.items()):
        if f"{lang}.{key}" not in data:
            missing.append(lang)
    return missing
