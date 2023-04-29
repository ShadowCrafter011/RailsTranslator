import os


def find_translation_files(base_path):
    files = {}

    pathes = [path for path in os.listdir(base_path)]
    full_pathes = [os.path.join(base_path, path) for path in pathes]
    directories = filter(lambda p: os.path.isdir(p), full_pathes)

    for path in pathes:
        full_path = os.path.join(base_path, path)

        if os.path.isfile(full_path) and path.endswith(".yml"):
            add_array(files, base_path, {
                "lang": path.replace(".yml", ""),
                "path": full_path
            })

    for directory in directories:
        files = merge_dicts(files, find_translation_files(directory))

    return files


def add_array(dictionary, key, item):
    if key in dictionary:
        dictionary[key].append(item)
    else:
        dictionary[key] = [item]


def merge_dicts(*dicts):
    output = {}
    for d in dicts:
        for _, (key, array) in enumerate(d.items()):
            if key in output:
                output[key] += array
            else:
                output[key] = array
    return output
