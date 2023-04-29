from MissingTranslations import find_missing_translations
from yaml.loader import BaseLoader
from shadowbar import ProgressBar
from deepl import Translator
import codecs
import yaml
import os


def catch_up(translation_files):
    missing = []

    for _, (_, files) in enumerate(translation_files.items()):
        missing.append(find_missing_translations(files))

    count = 0
    for miss in missing:
        for _, (_, array) in enumerate(miss.items()):
            count += len(array)

    if count == 0:
        print("Nothing to translate")
        return

    print("Translating files")
    pbar_counter, pbar = ProgressBar.new(50, count)

    for missing_translations in missing:
        for _, (file, missing) in enumerate(missing_translations.items()):
            with open(file, "r") as translation_file:
                data = yaml.load(translation_file, Loader=BaseLoader) or {}

                for miss in missing:
                    translated = translate(miss["translation"], miss["source_lang"], miss["target_lang"])
                    add_flat_path_to_dict(data, miss["key"], translated)

                    pbar_counter.value += 1

            with codecs.open(file, "w", "utf-8") as translation_file:
                write_dict(data, translation_file)

    pbar.wait_complete()


def write_dict(data, file, indentation_level=0):
    indent = " " * indentation_level
    for key, value in data.items():
        if isinstance(value, str):
            file.write(f"{indent}{key}: {wrap_string(value)}\n")
        else:
            file.write(f"{indent}{key}:\n")
            write_dict(value, file, indentation_level + 2)


def wrap_string(string):
    if string.startswith("%"):
        return f"\"{string}\""
    return string


def add_flat_path_to_dict(dictionary, flat_path, value):
    splits = flat_path.split(".")
    current = splits.pop(0)

    if current not in dictionary:
        dictionary[current] = {}

    if len(splits) == 0:
        dictionary[current] = value
        return

    add_flat_path_to_dict(dictionary[current], ".".join(splits), value)


def translate(text, source_lang, target_lang):
    translator = Translator(os.getenv("AUTH_KEY"))
    return translator.translate_text(text, source_lang=lang_key(source_lang), target_lang=lang_key(target_lang)).text


def lang_key(lang):
    if lang == "en":
        return "en-GB"
    return lang
