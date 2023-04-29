from CatchUp import wrap_string, lang_key, add_flat_path_to_dict
from IndexTranslations import add_array, merge_dicts


def test_merge_dicts():
    dict1 = {"array1": [1, 2, 3], "array2": [1, 2]}
    dict2 = {"array1": [4], "array3": [1, 2, 3]}
    dict3 = {"array3": [4]}
    merged = merge_dicts(dict1, dict2, dict3)
    assert merged == {
        "array1": [1, 2, 3, 4],
        "array2": [1, 2],
        "array3": [1, 2, 3, 4]
    }


def test_add_array():
    dictionary = {
        "test": []
    }
    add_array(dictionary, "test", 1)
    add_array(dictionary, "test2", 1)

    assert dictionary["test"] == [1]
    assert  dictionary["test2"] == [1]


def test_wrap_string():
    assert wrap_string("test") == "test"
    assert wrap_string("%wrap") == "\"%wrap\""


def test_lang_key():
    assert lang_key("de") == "de"
    assert lang_key("en") != "en"


def test_flat_path():
    dictionary = {
        "one": {
            "two": {
                "three": {
                    "four": 1
                }
            },
            "1+1": {
                "1+2": {}
            }
        }
    }

    add_flat_path_to_dict(dictionary, "one.two.test", 1)
    add_flat_path_to_dict(dictionary, "test", 1)
    add_flat_path_to_dict(dictionary, "one.1+1.1+2", 1)

    assert dictionary["one"]["two"]["test"] == 1
    assert dictionary["test"] == 1
    assert dictionary["one"]["1+1"]["1+2"] == 1
