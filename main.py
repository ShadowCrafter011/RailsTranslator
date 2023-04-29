from IndexTranslations import find_translation_files
from RailsTranslatorException import *
from dotenv import load_dotenv
from CatchUp import catch_up
import os


def main():
    load_dotenv()

    root_path = input("What is the Rails root path? ")
    locales_path = os.path.join(root_path, "config/locales")

    if not os.path.exists(locales_path):
        raise NotARailsProject("Path doesn't seem to contain a Rails project")

    translation_files = find_translation_files(locales_path)
    catch_up(translation_files)


if __name__ == '__main__':
    main()
