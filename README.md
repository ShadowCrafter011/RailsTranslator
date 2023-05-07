# Rails translator
![Rails Translator build status](https://github.com/ShadowCrafter011/RailsTranslator/actions/workflows/python-app.yml/badge.svg)

Translate your whole Rails app with only this script.

This script looks at all the locale files in your Rails app and identifies keys that are missing in other files in the same directory.
Using the DeepL API the script automatically translates the text and puts it into the right file.

Make sure that there is a file for every language you want to translate to. So if you want to translate `config/locales/de.yml` to english, make sure that `config/locales/en.yml` exists. Because if it doesn't the script wont translate it. The file can be empty

# Getting started
- Download or clone this Github repository
- (Optional) Create a virtual environment
- Install dependencies `pip install -r requirements.txt`
- Run main.py and specify the root of your Rails project
