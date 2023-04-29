from MissingTranslations import find_missing_translations


def test_translation_exists():
    files = [
        {"lang": "de", "path": "./fixtures/de.yml"},
        {"lang": "fr", "path": "./fixtures/fr.yml"},
        {"lang": "it", "path": "./fixtures/it.yml"},
        {"lang": "en", "path": "./fixtures/en.yml"}
    ]

    missing = find_missing_translations(files)

    assert same_arrays(missing["./fixtures/fr.yml"], [
        {
            "key": "fr.general.visibilities.private",
            "translation": "Privat",
            "target_lang": "fr",
            "source_lang": "de"
        },
        {
            "key": "fr.general.title",
            "translation": "RailsTranslator",
            "target_lang": "fr",
            "source_lang": "en"
        }
    ])

    assert same_arrays(missing["./fixtures/de.yml"], [
        {
            "key": "de.general.title",
            "translation": "RailsTranslator",
            "target_lang": "de",
            "source_lang": "en"
        }
    ])

    assert len(missing["./fixtures/it.yml"]) == 38


def same_arrays(array1, array2):
    for item in array1:
        if item not in array2:
            return False
    return True


